BRICK = {
    "brick_num": 35,
    "brick_title": "Principles of Antibacterial Drugs",
    "games": [
        {
            "slug": "pkpd_index_by_drug",
            "title": "PK/PD Indices by Drug Class",
            "subtitle": "Match each antibacterial drug to its PK/PD index, what predicts efficacy, and its dosing implication",
            "categories": ["PK/PD Index", "What Predicts Efficacy", "Dosing Implication"],
            "data": {
                "β-Lactams": {
                    "PK/PD Index": "%T>MIC (time-dependent activity)",
                    "What Predicts Efficacy": "Percent of dosing interval spent above the MIC",
                    "Dosing Implication": "More frequent dosing or prolonged infusion"
                },
                "Aminoglycosides": {
                    "PK/PD Index": "Cmax/MIC (concentration-dependent activity)",
                    "What Predicts Efficacy": "Peak drug concentration relative to the MIC",
                    "Dosing Implication": "Larger, less frequent doses; post-antibiotic effect"
                },
                "Vancomycin": {
                    "PK/PD Index": "AUC/MIC (exposure-dependent activity)",
                    "What Predicts Efficacy": "Total drug exposure over time relative to MIC",
                    "Dosing Implication": "Both dose and dosing interval shape total exposure"
                },
                "Fluoroquinolones": {
                    "PK/PD Index": "AUC/MIC, shared with vancomycin",
                    "What Predicts Efficacy": "Overall exposure across time divided by the MIC",
                    "Dosing Implication": "Adjust dose or interval to change total exposure"
                }
            }
        },
        {
            "slug": "susceptibility_measures",
            "title": "Susceptibility Measures and Reports",
            "subtitle": "Match each measure or report to its definition, how it is obtained, and its clinical role",
            "categories": ["Definition", "How Obtained", "Clinical Role"],
            "data": {
                "MIC": {
                    "Definition": "Lowest drug concentration with no visible bacterial growth",
                    "How Obtained": "Dilution series read for cloudiness after about a day",
                    "Clinical Role": "Main measurement used to determine susceptibility"
                },
                "MBC": {
                    "Definition": "Concentration giving a 99.9% fall in original colony count",
                    "How Obtained": "Subculture from the same dilution testing as the MIC",
                    "Clinical Role": "Rarely used; shows if an agent is more bactericidal"
                },
                "Breakpoint": {
                    "Definition": "Cutoff MIC considered susceptible for an organism-drug pair",
                    "How Obtained": "Monitored and published by a national organization",
                    "Clinical Role": "Lets the lab classify an isolate's MIC result"
                },
                "Antibiogram": {
                    "Definition": "Cumulative percent of local isolates susceptible to each drug",
                    "How Obtained": "Facility or community data over a defined period",
                    "Clinical Role": "Guides empiric therapy before patient results return"
                },
                "Culture and sensitivity report": {
                    "Definition": "Susceptibility results for one patient's own isolate",
                    "How Obtained": "Laboratory testing of the patient's sample",
                    "Clinical Role": "Allows a switch from empiric to definitive therapy"
                }
            }
        },
        {
            "slug": "static_vs_cidal",
            "title": "Bacteriostatic vs Bactericidal",
            "subtitle": "Match each finding or setting to its interpretation, the role of host immunity, and the clinical implication",
            "categories": ["Interpretation", "Role of Host Immunity", "Clinical Implication"],
            "data": {
                "MBC/MIC ratio less than 4": {
                    "Interpretation": "Bactericidal: kills bacteria as its primary action",
                    "Role of Host Immunity": "Killing does not depend on host clearance",
                    "Clinical Implication": "Preferred when host defenses may be inadequate"
                },
                "MBC/MIC ratio greater than 4": {
                    "Interpretation": "Bacteriostatic: halts bacterial growth and replication",
                    "Role of Host Immunity": "Immunocompetent host clears the halted organism",
                    "Clinical Implication": "Outcomes similar to cidal drugs for most infections"
                },
                "Endocarditis or meningitis": {
                    "Interpretation": "Setting in which bactericidal drugs are preferred",
                    "Role of Host Immunity": "Anatomic location limits immune effectiveness",
                    "Clinical Implication": "Choose an agent with a low MBC/MIC ratio"
                },
                "Immunosuppressed patient": {
                    "Interpretation": "Host less able to clear a growth-halted organism",
                    "Role of Host Immunity": "Weakened by immunosuppressive therapy",
                    "Clinical Implication": "Weigh bactericidal activity in drug choice"
                }
            }
        },
        {
            "slug": "reading_the_report",
            "title": "Reading the Results Wisely",
            "subtitle": "Match each result or pitfall to what it means, a common misreading, and the right response",
            "categories": ["What It Means", "Common Misreading", "Right Response"],
            "data": {
                "Intermediate result": {
                    "What It Means": "MIC approaches ordinarily achievable drug levels",
                    "Common Misreading": "Treating it as synonymous with resistance",
                    "Right Response": "Reassess exposure, penetration, and susceptible alternatives"
                },
                "Lowest MIC among several drugs": {
                    "What It Means": "Most potent in vitro against this one organism",
                    "Common Misreading": "Assuming it is automatically the best choice",
                    "Right Response": "Weigh drug distribution to the infection site"
                },
                "High local antibiogram susceptibility": {
                    "What It Means": "Most local isolates were susceptible last period",
                    "Common Misreading": "Assuming this patient's isolate must be susceptible",
                    "Right Response": "Use for empiric choice, then follow patient results"
                },
                "Clear tube in a dilution series": {
                    "What It Means": "No visible growth at that drug concentration",
                    "Common Misreading": "Assuming the bacteria in the tube were killed",
                    "Right Response": "Subculture for 99.9% killing to find the MBC"
                }
            }
        }
    ]
}
