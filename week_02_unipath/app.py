import streamlit as st
import pandas as pd
from groq import Groq
from utils import SOURCES, UNI_MERIT_DATA

st.set_page_config(page_title="UniPath AI Lahore", page_icon="🎓", layout="wide")
st.title("🎓 UniPath AI: Lahore Public Sector Merit & Admission Advisor")

# Auto-fetch secret key from Streamlit Secrets or sidebar fallback
groq_api_key = st.secrets.get("GROQ_API_KEY", "")

if not groq_api_key:
    with st.sidebar:
        st.header("🔑 Groq API Setup")
        groq_api_key = st.text_input("Enter Groq API Key", type="password")

st.subheader("1. Academic Marks")
c1, c2 = st.columns(2)
with c1:
    matric_marks = st.number_input("Matric Marks (Out of 1100)", 300, 1100, 1061)
with c2:
    fsc_marks = st.number_input("Intermediate / FSC Marks (Out of 1100)", 300, 1100, 918)

mode = st.radio("Choose Mode:", ["Target Specific University", "Auto-Match All Eligible Universities"])

if mode == "Target Specific University":
    st.subheader("2. Target Selection")
    selected_uni = st.selectbox("Select Target University", list(UNI_MERIT_DATA.keys()))
    available_fields = list(UNI_MERIT_DATA[selected_uni].keys())
    selected_field = st.selectbox("Select Target Field", available_fields)

    if st.button("Calculate & Get Groq AI Strategy", type="primary"):
        if not groq_api_key:
            st.error("Groq API Key missing. Add it in sidebar or Streamlit Secrets.")
        else:
            calc_func = SOURCES["Merit Calculator"]
            result = calc_func(matric_marks, fsc_marks, selected_uni, selected_field)
            
            st.divider()
            st.subheader("📊 Merit Calculation Output")
            st.json(result)
            
            try:
                client = Groq(api_key=groq_api_key)
                prompt = f"""
                You are an expert Pakistani Career Counselor for Lahore Public Sector Universities.
                Student Profile: Matric: {matric_marks}/1100, FSC: {fsc_marks}/1100.
                Target: {selected_uni} - {selected_field}.
                Calculated Data: {result}.
                
                Provide:
                1. Clear feasibility assessment.
                2. Entry Test Strategy (e.g., ECAT / MDCAT / PU Test guidance).
                3. Two alternative Lahore public universities or programs as backup.
                """
                
                # Instructor's model: llama-3.1-8b-instant
                try:
                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.1-8b-instant",
                    )
                except Exception:
                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.3-70b-versatile",
                    )
                
                st.subheader("🧠 Groq AI Career Roadmap")
                st.info(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Groq API Error: {e}")

else:
    st.subheader("2. Auto-Match Eligibility")
    assumed_test = st.slider("Assumed Entry Test Score (%)", 30, 100, 70)
    
    if st.button("Find All Matching Universities", type="primary"):
        finder_func = SOURCES["Eligibility Finder"]
        results = finder_func(matric_marks, fsc_marks, assumed_test)
        
        df = pd.DataFrame(results)
        st.divider()
        st.subheader("📋 Matched Universities & Programs")
        st.dataframe(df, use_container_width=True)