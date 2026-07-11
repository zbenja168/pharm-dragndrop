BRICK = {
    "brick_num": 1,
    "brick_title": "Pharmacokinetics 1 of 3 - Drug Absorption and Distribution",
    "games": [
        {
            "slug": "routes_of_administration",
            "title": "Routes of Drug Administration",
            "subtitle": "Match each route to its class, primary site, and distinguishing feature",
            "categories": ["Route Class", "Primary Site", "Distinguishing Feature"],
            "data": {
                "Oral": {
                    "Route Class": "Enteral",
                    "Primary Site": "Small intestine",
                    "Distinguishing Feature": "Convenient and cost-effective but reduced by first-pass metabolism"
                },
                "Sublingual": {
                    "Route Class": "Enteral",
                    "Primary Site": "Venous blood under the tongue",
                    "Distinguishing Feature": "Bypasses the hepatic portal vein and the liver"
                },
                "Intravenous": {
                    "Route Class": "Parenteral",
                    "Primary Site": "Systemic circulation directly",
                    "Distinguishing Feature": "Rapid effect with 100 percent bioavailability"
                },
                "Intramuscular": {
                    "Route Class": "Parenteral",
                    "Primary Site": "Skeletal muscle such as the deltoid or vastus lateralis",
                    "Distinguishing Feature": "Depot preparation dissolves slowly for a sustained dose"
                },
                "Subcutaneous": {
                    "Route Class": "Parenteral",
                    "Primary Site": "Cutis just below the dermis and epidermis",
                    "Distinguishing Feature": "Slow sustained uptake used for insulin and heparin"
                },
                "Inhalation": {
                    "Route Class": "Other",
                    "Primary Site": "Alveolar epithelium of the lungs",
                    "Distinguishing Feature": "About 100 square meters of surface area speeds absorption"
                }
            }
        },
        {
            "slug": "adme_stages",
            "title": "The ADME Stages of Pharmacokinetics",
            "subtitle": "Match each pharmacokinetic stage to its order, primary organ, and key process",
            "categories": ["Order in ADME", "Primary Organ or Site", "Key Process"],
            "data": {
                "Absorption": {
                    "Order in ADME": "First stage",
                    "Primary Organ or Site": "Small intestine",
                    "Key Process": "Drug enters the body and travels to the circulation"
                },
                "Distribution": {
                    "Order in ADME": "Second stage",
                    "Primary Organ or Site": "Blood and tissues",
                    "Key Process": "Drug is spread throughout the body"
                },
                "Metabolism": {
                    "Order in ADME": "Third stage",
                    "Primary Organ or Site": "Liver",
                    "Key Process": "Drug molecule is broken down"
                },
                "Excretion": {
                    "Order in ADME": "Fourth stage",
                    "Primary Organ or Site": "Kidneys",
                    "Key Process": "Waste drug is eliminated from the body"
                }
            }
        },
        {
            "slug": "special_populations_distribution",
            "title": "Distribution in Special Populations",
            "subtitle": "Match each patient group to its body composition change, drug effect, and dosing implication",
            "categories": ["Body Composition Change", "Effect on the Drug", "Dosing Implication"],
            "data": {
                "Neonates and children": {
                    "Body Composition Change": "Higher total body water and lower body fat",
                    "Effect on the Drug": "Decreased protein binding and an immature blood-brain barrier let drugs into the CNS",
                    "Dosing Implication": "Dosing must account for greater CNS exposure"
                },
                "Older adults": {
                    "Body Composition Change": "Increased body fat and decreased serum albumin",
                    "Effect on the Drug": "More free active drug and accumulation in fatty tissue",
                    "Dosing Implication": "Often require lower doses"
                },
                "Obese patient": {
                    "Body Composition Change": "Large adipose tissue mass",
                    "Effect on the Drug": "Lipophilic drugs accumulate in fat",
                    "Dosing Implication": "Prolonged duration of action"
                },
                "Liver disease or malnutrition": {
                    "Body Composition Change": "Reduced albumin production",
                    "Effect on the Drug": "Higher free (active) drug fraction",
                    "Dosing Implication": "Risk of an exaggerated drug effect"
                }
            }
        },
        {
            "slug": "bioavailability_first_pass",
            "title": "Bioavailability and the First-Pass Effect",
            "subtitle": "Match each route to its bioavailability, first-pass exposure, and consequence",
            "categories": ["Bioavailability (F)", "First-Pass Exposure", "Consequence"],
            "data": {
                "Intravenous injection": {
                    "Bioavailability (F)": "100 percent (F = 1.0)",
                    "First-Pass Exposure": "None, enters the circulation directly",
                    "Consequence": "Precise and immediate serum levels"
                },
                "Oral tablet": {
                    "Bioavailability (F)": "About 70 percent on average (F near 0.7)",
                    "First-Pass Exposure": "Full, travels through the portal vein to the liver first",
                    "Consequence": "Up to 90 percent of active drug lost before circulation"
                },
                "Sublingual tablet": {
                    "Bioavailability (F)": "High",
                    "First-Pass Exposure": "Avoided, drains into oral cavity veins",
                    "Consequence": "Rapid onset while bypassing the liver"
                },
                "Rectal suppository": {
                    "Bioavailability (F)": "Partial first-pass",
                    "First-Pass Exposure": "Reduced, some drug bypasses the liver",
                    "Consequence": "Useful when the oral route is not possible"
                }
            }
        }
    ]
}
