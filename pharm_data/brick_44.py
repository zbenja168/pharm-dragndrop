BRICK = {
    "brick_num": 44,
    "brick_title": "Renin-Angiotensin-Aldosterone System Inhibitors",
    "games": [
        {
            "slug": "raas_pathway_steps",
            "title": "Walking the RAAS Pathway",
            "subtitle": "Match each RAAS component to where it comes from, what it does, and the drug link",
            "categories": ["Origin", "Role in the Pathway", "Drug Link"],
            "data": {
                "Renin": {
                    "Origin": "Juxtaglomerular cells of the renal afferent arteriole",
                    "Role in the Pathway": "Protease that cleaves angiotensinogen into angiotensin I",
                    "Drug Link": "Blocked by aliskiren, the only US renin inhibitor"
                },
                "Angiotensin I": {
                    "Origin": "Cut from liver-made angiotensinogen",
                    "Role in the Pathway": "Precursor hormone carried to the lungs",
                    "Drug Link": "Its conversion is blocked by the -pril drugs"
                },
                "ACE": {
                    "Origin": "Expressed primarily in the lungs",
                    "Role in the Pathway": "Converts angiotensin I to Ang II and degrades bradykinin",
                    "Drug Link": "Inhibited by captopril, enalapril, lisinopril"
                },
                "Angiotensin II": {
                    "Origin": "Peptide hormone produced from angiotensin I",
                    "Role in the Pathway": "Vasoconstricts, constricts efferent arteriole, releases aldosterone",
                    "Drug Link": "Its receptors are blocked by the -sartan drugs"
                },
                "Aldosterone": {
                    "Origin": "Adrenal gland, stimulated by Ang II",
                    "Role in the Pathway": "Expands blood volume and drives renal K+ secretion",
                    "Drug Link": "Secretion falls with both ACE-Is and ARBs"
                }
            }
        },
        {
            "slug": "raas_inhibitor_adverse_effects",
            "title": "Adverse Effects of ACE-Is and ARBs",
            "subtitle": "Match each adverse effect to its mechanism, who is at risk, and how it is handled",
            "categories": ["Mechanism", "Higher-Risk Setting", "Prevention or Management"],
            "data": {
                "Hyperkalemia": {
                    "Mechanism": "Less aldosterone, so less renal tubular K+ secretion",
                    "Higher-Risk Setting": "CKD or diabetic kidney disease (low renin secretion)",
                    "Prevention or Management": "Avoid potassium-sparing diuretics and K+ supplements"
                },
                "Prerenal acute kidney injury": {
                    "Mechanism": "Efferent arteriole dilation acutely lowers GFR",
                    "Higher-Risk Setting": "Low-flow states such as dehydration or heart failure",
                    "Prevention or Management": "Usually recovers in 7-10 days; reduce or stop if GFR keeps falling"
                },
                "Dry cough": {
                    "Mechanism": "Bradykinin buildup causes bronchoconstriction",
                    "Higher-Risk Setting": "ACE-I use; can start even years into therapy",
                    "Prevention or Management": "Tolerate it, or switch to another ACE-I or an ARB"
                },
                "Angioedema": {
                    "Mechanism": "Bradykinin on endothelium triggers substance P release",
                    "Higher-Risk Setting": "African American patients (4.5 times greater risk)",
                    "Prevention or Management": "Prefer a DHP CCB such as amlodipine for hypertension alone"
                }
            }
        },
        {
            "slug": "raas_interactions_contraindications",
            "title": "Interactions and Contraindications",
            "subtitle": "Match each combination or condition to the verdict and the reason behind it",
            "categories": ["Verdict", "Main Concern"],
            "data": {
                "ACE-I plus ARB together": {
                    "Verdict": "Never combine; no added clinical benefit",
                    "Main Concern": "Additive hyperkalemia, AKI, and angioedema risk"
                },
                "Potassium-sparing diuretic or K+ supplement": {
                    "Verdict": "Avoid alongside an ACE-I or ARB",
                    "Main Concern": "Further potassium retention causing hyperkalemia"
                },
                "Chronic NSAID use": {
                    "Verdict": "Avoid long-term co-use",
                    "Main Concern": "Afferent constriction plus efferent dilation causes prerenal AKI"
                },
                "Beta-blocker, CCB, or loop diuretic": {
                    "Verdict": "Commonly co-prescribed",
                    "Main Concern": "No notable drug interaction"
                },
                "Pregnancy or bilateral renal artery stenosis": {
                    "Verdict": "Contraindicated",
                    "Main Concern": "Listed contraindications to both ACE-Is and ARBs"
                }
            }
        },
        {
            "slug": "choosing_the_right_agent",
            "title": "Choosing the Right Agent",
            "subtitle": "Match each patient scenario to the best choice and the reasoning",
            "categories": ["Best Choice", "Reasoning"],
            "data": {
                "Hypertension alone, African American patient": {
                    "Best Choice": "DHP calcium channel blocker such as amlodipine",
                    "Reasoning": "4.5 times greater risk of ACE-I-induced angioedema"
                },
                "Hypertension plus heart failure, African American patient": {
                    "Best Choice": "Trial of an ARB with close monitoring",
                    "Reasoning": "Comorbidity justifies RAAS blockade with lower angioedema risk"
                },
                "Bothersome dry cough on lisinopril": {
                    "Best Choice": "Switch to a different ACE-I or an ARB",
                    "Reasoning": "ARBs leave bradykinin breakdown by ACE intact"
                },
                "CKD with proteinuria": {
                    "Best Choice": "ACE-I or ARB as first-line therapy",
                    "Reasoning": "Lowers glomerular pressure and slows kidney disease"
                },
                "Patient recovering from a myocardial infarction": {
                    "Best Choice": "ACE-I or ARB (post-MI indication)",
                    "Reasoning": "Post-MI is one of the four first-line indications"
                }
            }
        }
    ]
}
