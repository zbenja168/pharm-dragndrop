BRICK = {
    "brick_num": 15,
    "brick_title": "Antihyperlipidemic Drugs - Statins",
    "games": [
        {
            "slug": "statin_pk_profiles",
            "title": "Statin PK/PD Profiles",
            "subtitle": "Match each statin to its metabolism, elimination half-life, and solubility",
            "categories": ["Metabolism", "Elimination Half-Life", "Solubility"],
            "data": {
                "Simvastatin": {
                    "Metabolism": "Hepatic, CYP3A4",
                    "Elimination Half-Life": "2 to 3 hours",
                    "Solubility": "Lipophilic"
                },
                "Fluvastatin": {
                    "Metabolism": "Hepatic, CYP2C9",
                    "Elimination Half-Life": "0.5 to 2.3 hours",
                    "Solubility": "Lipophilic"
                },
                "Pravastatin": {
                    "Metabolism": "Non-CYP450, hepatic OATP transporter",
                    "Elimination Half-Life": "1.3 to 2.8 hours",
                    "Solubility": "Hydrophilic"
                },
                "Rosuvastatin": {
                    "Metabolism": "Non-CYP450, hepatic OATP transporter",
                    "Elimination Half-Life": "19 hours",
                    "Solubility": "Hydrophilic"
                },
                "Pitavastatin": {
                    "Metabolism": "Minimal hepatic metabolism",
                    "Elimination Half-Life": "12 hours",
                    "Solubility": "Lipophilic"
                },
                "Atorvastatin": {
                    "Metabolism": "Hepatic, CYP3A4",
                    "Elimination Half-Life": "15 to 30 hours",
                    "Solubility": "Lipophilic"
                }
            }
        },
        {
            "slug": "statin_adverse_effects",
            "title": "Adverse Effects & Precautions",
            "subtitle": "Match each statin adverse effect to its key feature and clinical note",
            "categories": ["Adverse Effect", "Key Feature", "Clinical Note"],
            "data": {
                "Hepatic dysfunction": {
                    "Adverse Effect": "Hepatotoxicity",
                    "Key Feature": "Elevated liver aminotransferases (ALT)",
                    "Clinical Note": "Check LFTs before starting; consider alternate agent if ALT >3x upper limit"
                },
                "Rhabdomyolysis": {
                    "Adverse Effect": "Most severe muscle toxicity (SAMS)",
                    "Key Feature": "Markedly elevated CPK with myoglobinuria and acute kidney injury",
                    "Clinical Note": "Higher risk with CYP3A4-metabolized statins"
                },
                "New-onset diabetes": {
                    "Adverse Effect": "Impaired glycemic control",
                    "Key Feature": "Beta-cell lipotoxicity lowers insulin secretion",
                    "Clinical Note": "Increased LDL uptake in pancreatic beta-cells"
                },
                "Diarrhea": {
                    "Adverse Effect": "Gastrointestinal upset",
                    "Key Feature": "Loose, frequent stools",
                    "Clinical Note": "Common and generally mild adverse effect"
                },
                "Teratogenicity": {
                    "Adverse Effect": "Fetal risk",
                    "Key Feature": "Contraindicated in pregnancy",
                    "Clinical Note": "Discontinue statin; breastfeeding is not recommended"
                }
            }
        },
        {
            "slug": "statin_interactions",
            "title": "Statin Drug & Food Interactions",
            "subtitle": "Match each interacting agent to its class and its effect on statins",
            "categories": ["Interacting Agent", "Class", "Effect on Statin"],
            "data": {
                "Grapefruit juice": {
                    "Interacting Agent": "Grapefruit juice",
                    "Class": "Dietary / food",
                    "Effect on Statin": "Inhibits intestinal CYP3A4, raising simvastatin levels"
                },
                "Amiodarone": {
                    "Interacting Agent": "Amiodarone",
                    "Class": "Antiarrhythmic",
                    "Effect on Statin": "Inhibits CYP3A4; limit simvastatin to 20 mg/day or less"
                },
                "Diltiazem": {
                    "Interacting Agent": "Diltiazem",
                    "Class": "Calcium channel blocker",
                    "Effect on Statin": "Moderate CYP3A4 inhibitor, increases ADRs of CYP3A4 statins"
                },
                "Daptomycin": {
                    "Interacting Agent": "Daptomycin",
                    "Class": "Antibiotic",
                    "Effect on Statin": "Additive muscle toxicity, raises CPK and myopathy risk"
                },
                "Glucocorticoids": {
                    "Interacting Agent": "Glucocorticoids",
                    "Class": "Corticosteroid",
                    "Effect on Statin": "Additive myopathy risk with elevated CPK"
                }
            }
        },
        {
            "slug": "statin_mechanism_effects",
            "title": "Mechanism & Non-Lipid Effects",
            "subtitle": "Match each statin action to its mechanism and clinical benefit",
            "categories": ["Action", "Mechanism", "Clinical Benefit"],
            "data": {
                "LDL lowering": {
                    "Action": "Lower circulating LDL-C",
                    "Mechanism": "Inhibit HMG-CoA reductase; upregulate hepatic LDL receptors",
                    "Clinical Benefit": "Improved survival in primary and secondary prevention"
                },
                "Triglyceride lowering": {
                    "Action": "Reduce triglycerides",
                    "Mechanism": "Decrease circulating VLDL levels",
                    "Clinical Benefit": "Roughly 20 to 40% triglyceride reduction"
                },
                "Plaque stabilization": {
                    "Action": "Stabilize atherosclerotic plaque",
                    "Mechanism": "Maintain integrity of the fibrous cap",
                    "Clinical Benefit": "Protects plaque from rupture and acute coronary syndromes"
                },
                "Regression of atherosclerosis": {
                    "Action": "Regress atherosclerotic lesions",
                    "Mechanism": "Reduce atherosclerotic lesion burden over time",
                    "Clinical Benefit": "Slows disease progression"
                },
                "Reversal of endothelial dysfunction": {
                    "Action": "Improve endothelial function",
                    "Mechanism": "Reduce vasoconstriction linked to endothelial dysfunction",
                    "Clinical Benefit": "Better vascular reactivity"
                }
            }
        }
    ]
}
