BRICK = {
    "brick_num": 7,
    "brick_title": "Nonopioid Analgesics - Aspirin",
    "games": [
        {
            "slug": "cox_mechanism",
            "title": "Aspirin's Actions on COX Enzymes and Platelets",
            "subtitle": "Match each molecular target to how aspirin acetylation affects it and the clinical result",
            "categories": ["Molecular Action", "Dose / Condition", "Clinical Result"],
            "data": {
                "COX-1": {
                    "Molecular Action": "Completely inactivated once acetylated",
                    "Dose / Condition": "Inhibited across effective doses",
                    "Clinical Result": "Loss of gastric mucosal protection (GI ulcers)"
                },
                "COX-2 (inhibition)": {
                    "Molecular Action": "Irreversibly inhibited, blocking prostacyclin (PGI2) production",
                    "Dose / Condition": "Higher doses (>75 mg)",
                    "Clinical Result": "Analgesic and antipyretic effect"
                },
                "COX-2 (acetylated)": {
                    "Molecular Action": "Catalytic activity switched from cyclooxygenase to lipoxygenase",
                    "Dose / Condition": "After acetylation of the enzyme",
                    "Clinical Result": "Generates lipoxygenase (LOX) products instead of prostaglandins"
                },
                "Thromboxane A2 (platelets)": {
                    "Molecular Action": "Synthesis irreversibly blocked via COX inhibition",
                    "Dose / Condition": "Low dose (e.g., 81 mg)",
                    "Clinical Result": "Prevents platelet aggregation (antithrombotic)"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "Adverse Effects of Aspirin",
            "subtitle": "Match each adverse effect to its mechanism and its key feature or at-risk population",
            "categories": ["Adverse Effect", "Underlying Mechanism", "Key Feature / Population"],
            "data": {
                "GI toxicity": {
                    "Adverse Effect": "Ulcers, erosive gastritis, upper GI bleeding",
                    "Underlying Mechanism": "Inhibition of prostaglandin function damages gastric mucosa",
                    "Key Feature / Population": "Most common ADR; avoid in active peptic ulcer disease"
                },
                "Reye's syndrome": {
                    "Adverse Effect": "Fatty liver degeneration with hepatic encephalopathy",
                    "Underlying Mechanism": "Salicylate-triggered mitochondrial/hepatic injury",
                    "Key Feature / Population": "Febrile children <18 recovering from viral infection"
                },
                "AERD (hypersensitivity)": {
                    "Adverse Effect": "Bronchoconstriction, rhinitis, respiratory distress",
                    "Underlying Mechanism": "COX-1 inhibition shunts arachidonate to pro-inflammatory leukotrienes",
                    "Key Feature / Population": "Asthma, rhinitis, nasal polyps; median onset around age 34"
                },
                "Tinnitus": {
                    "Adverse Effect": "Ringing in the ears",
                    "Underlying Mechanism": "High-dose salicylate effect on the cochlea",
                    "Key Feature / Population": "Occurs at high doses"
                },
                "Salicylate toxicity": {
                    "Adverse Effect": "Metabolic acidosis in overdose",
                    "Underlying Mechanism": "Saturated hepatic enzymes shift metabolism to zero-order kinetics",
                    "Key Feature / Population": "Seen with aspirin overdose; elimination decreases"
                }
            }
        },
        {
            "slug": "pharmacokinetics",
            "title": "Aspirin Pharmacokinetics and Dosing",
            "subtitle": "Match each pharmacokinetic parameter to its value and its clinical significance",
            "categories": ["Parameter", "Value / Description", "Clinical Significance"],
            "data": {
                "pKa": {
                    "Parameter": "Acid dissociation constant",
                    "Value / Description": "pKa of 3.5 (weak acid)",
                    "Clinical Significance": "Mostly absorbed in the stomach"
                },
                "Metabolism": {
                    "Parameter": "Biotransformation",
                    "Value / Description": "Hydrolyzed to salicylic acid",
                    "Clinical Significance": "First-order kinetics; shifts to zero-order in overdose"
                },
                "Elimination": {
                    "Parameter": "Route of clearance",
                    "Value / Description": "Cleared renally",
                    "Clinical Significance": "Raising urinary pH increases clearance"
                },
                "Antiplatelet duration": {
                    "Parameter": "Duration of platelet effect",
                    "Value / Description": "Lasts the platelet lifespan (~7-10 days)",
                    "Clinical Significance": "Platelets are non-nucleated and cannot resynthesize COX"
                },
                "Cardiovascular dose": {
                    "Parameter": "Protective daily dose range",
                    "Value / Description": "75 to 325 mg daily",
                    "Clinical Significance": "Equal CV benefit to 1300 mg with far fewer side effects"
                }
            }
        },
        {
            "slug": "contraindications",
            "title": "When to Avoid Aspirin",
            "subtitle": "Match each contraindication to the reason and the recommended action",
            "categories": ["Contraindication", "Reason", "Recommended Action"],
            "data": {
                "Febrile child / viral illness": {
                    "Contraindication": "Infants and children under 18",
                    "Reason": "Risk of Reye's syndrome",
                    "Recommended Action": "Substitute acetaminophen or a pediatric NSAID"
                },
                "Active peptic ulcer disease": {
                    "Contraindication": "Existing gastric or duodenal ulcer",
                    "Reason": "Increased risk of GI bleeding",
                    "Recommended Action": "Choose a non-ulcerogenic analgesic"
                },
                "Asthma with nasal polyps": {
                    "Contraindication": "Asthma, rhinitis, nasal polyps (AERD)",
                    "Reason": "Hypersensitivity with leukotriene-driven bronchospasm",
                    "Recommended Action": "Avoid all COX-1 inhibitors"
                },
                "NSAID hypersensitivity": {
                    "Contraindication": "Prior hypersensitivity to NSAIDs",
                    "Reason": "Cross-reactivity and anaphylactic reactions",
                    "Recommended Action": "Withhold aspirin entirely"
                },
                "Severe organ failure / bleeding": {
                    "Contraindication": "Severe liver or renal failure, active bleeding",
                    "Reason": "Bleeding risk and impaired drug clearance",
                    "Recommended Action": "Hold aspirin due to bleeding and clearance risk"
                }
            }
        }
    ]
}
