import pandas as pd

UNI_MERIT_DATA = {
    "University of the Punjab (PU / PUCIT)": {
        "BS Computer Science": {"last_merit": 86.5, "fsc_weight": 0.50, "matric_weight": 0.25, "entry_test_weight": 0.25},
        "BS Software Engineering": {"last_merit": 85.5, "fsc_weight": 0.50, "matric_weight": 0.25, "entry_test_weight": 0.25},
        "BS Data Science": {"last_merit": 84.0, "fsc_weight": 0.50, "matric_weight": 0.25, "entry_test_weight": 0.25},
        "BS Information Technology (BS IT)": {"last_merit": 83.2, "fsc_weight": 0.50, "matric_weight": 0.25, "entry_test_weight": 0.25},
        "BS Artificial Intelligence": {"last_merit": 85.0, "fsc_weight": 0.50, "matric_weight": 0.25, "entry_test_weight": 0.25},
        "BBIT (Business & IT)": {"last_merit": 78.5, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "BS International Relations (BS IR)": {"last_merit": 75.0, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "Pharm-D (Pharmacy)": {"last_merit": 89.2, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
    },
    "UET Lahore": {
        "BS Computer Science": {"last_merit": 81.2, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BS Software Engineering": {"last_merit": 80.0, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BS Cyber Security": {"last_merit": 78.5, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BSc Electrical Engineering": {"last_merit": 76.5, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BSc Mechanical Engineering": {"last_merit": 74.0, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BS Business Information Technology": {"last_merit": 72.0, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
    },
    "GCU Lahore (Government College University)": {
        "BS Computer Science": {"last_merit": 84.5, "fsc_weight": 0.40, "matric_weight": 0.10, "entry_test_weight": 0.50},
        "BS Software Engineering": {"last_merit": 82.0, "fsc_weight": 0.40, "matric_weight": 0.10, "entry_test_weight": 0.50},
        "BS Data Science": {"last_merit": 80.5, "fsc_weight": 0.40, "matric_weight": 0.10, "entry_test_weight": 0.50},
        "BS Biotechnology": {"last_merit": 80.0, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
        "BS International Relations": {"last_merit": 76.2, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
        "BS Business Administration (BBA)": {"last_merit": 78.0, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
    },
    "King Edward Medical University / SIMS": {
        "MBBS (Medicine)": {"last_merit": 91.5, "fsc_weight": 0.40, "matric_weight": 0.10, "entry_test_weight": 0.50},
        "BDS (Dentistry)": {"last_merit": 90.0, "fsc_weight": 0.40, "matric_weight": 0.10, "entry_test_weight": 0.50},
        "Doctor of Physical Therapy (DPT)": {"last_merit": 86.0, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
    },
    "LCWU (Lahore College for Women University)": {
        "BS Computer Science": {"last_merit": 81.0, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BS Software Engineering": {"last_merit": 79.5, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "BS Information Technology": {"last_merit": 77.0, "fsc_weight": 0.50, "matric_weight": 0.17, "entry_test_weight": 0.33},
        "Pharm-D": {"last_merit": 87.0, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "BS International Relations": {"last_merit": 71.0, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
    },
    "Kinnaird College for Women": {
        "BS Computer Science": {"last_merit": 83.0, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
        "BS Business Administration": {"last_merit": 79.0, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
        "BS International Relations": {"last_merit": 76.5, "fsc_weight": 0.80, "matric_weight": 0.20, "entry_test_weight": 0.00},
    },
    "UVAS Lahore": {
        "Pharm-D": {"last_merit": 88.5, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "BS Biotechnology": {"last_merit": 85.0, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "BS Biochemistry": {"last_merit": 82.5, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
        "BS Applied Microbiology": {"last_merit": 81.0, "fsc_weight": 0.70, "matric_weight": 0.30, "entry_test_weight": 0.00},
    }
}

def calculate_required_test_marks(matric_marks: float, fsc_marks: float, target_uni: str, target_field: str) -> dict:
    if target_uni not in UNI_MERIT_DATA or target_field not in UNI_MERIT_DATA[target_uni]:
        return {"error": "University or Field data not found."}
    
    data = UNI_MERIT_DATA[target_uni][target_field]
    last_cutoff = data["last_merit"]
    
    matric_pct = (matric_marks / 1100) * 100
    fsc_pct = (fsc_marks / 1100) * 100
    
    current_contrib = (matric_pct * data["matric_weight"]) + (fsc_pct * data["fsc_weight"])
    needed_contrib = last_cutoff - current_contrib
    
    if data["entry_test_weight"] > 0:
        required_test_pct = (needed_contrib / data["entry_test_weight"])
        return {
            "target_uni": target_uni,
            "target_field": target_field,
            "last_year_cutoff_percent": last_cutoff,
            "your_academic_contribution": round(current_contrib, 2),
            "required_entry_test_percent": round(required_test_pct, 2),
            "status": "Achievable" if required_test_pct <= 100 else "High Risk (Need near full marks)"
        }
    else:
        achieved_aggregate = current_contrib
        return {
            "target_uni": target_uni,
            "target_field": target_field,
            "last_year_cutoff_percent": last_cutoff,
            "achieved_aggregate": round(achieved_aggregate, 2),
            "status": "Eligible" if achieved_aggregate >= last_cutoff else "Below Cutoff"
        }

def find_eligible_universities(matric_marks: float, fsc_marks: float, assumed_test_score: float = 70.0) -> list:
    eligible_list = []
    matric_pct = (matric_marks / 1100) * 100
    fsc_pct = (fsc_marks / 1100) * 100
    
    for uni, fields in UNI_MERIT_DATA.items():
        for field, criteria in fields.items():
            aggregate = (matric_pct * criteria["matric_weight"]) + \
                        (fsc_pct * criteria["fsc_weight"]) + \
                        (assumed_test_score * criteria["entry_test_weight"])
            
            diff = aggregate - criteria["last_merit"]
            
            if diff >= 0:
                status = "Safe / High Chance"
            elif diff >= -3.0:
                status = "Borderline / Possible"
            else:
                status = "Low Chance"
                
            eligible_list.append({
                "University": uni,
                "Field": field,
                "Last Year Cutoff (%)": criteria["last_merit"],
                "Your Est. Aggregate (%)": round(aggregate, 2),
                "Admission Probability": status
            })
            
    return eligible_list

SOURCES = {
    "Merit Calculator": calculate_required_test_marks,
    "Eligibility Finder": find_eligible_universities
}