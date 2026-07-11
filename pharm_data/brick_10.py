BRICK = {
    "brick_num": 10,
    "brick_title": "Pharmacodynamics 3 - Pharmacogenomics",
    "games": [
        {
            "slug": "metabolizer_phenotypes",
            "title": "CYP Metabolizer Phenotypes",
            "subtitle": "Match each metabolizer group to its enzyme activity, effect on drug levels, and clinical consequence",
            "categories": ["Enzyme Activity", "Effect on Active-Drug Levels", "Clinical Consequence"],
            "data": {
                "Ultra-rapid metabolizer (UM)": {
                    "Enzyme Activity": "Greatly increased enzyme activity",
                    "Effect on Active-Drug Levels": "Drug metabolized too quickly, subtherapeutic levels",
                    "Clinical Consequence": "Reduced therapeutic effect (or toxicity from prodrugs)"
                },
                "Extensive metabolizer (EM)": {
                    "Enzyme Activity": "Normal enzyme activity",
                    "Effect on Active-Drug Levels": "Expected, normal drug levels",
                    "Clinical Consequence": "Expected drug response"
                },
                "Intermediate metabolizer (IM)": {
                    "Enzyme Activity": "Reduced activity, fewer functional enzymes",
                    "Effect on Active-Drug Levels": "Higher than normal drug levels",
                    "Clinical Consequence": "Increased risk of side effects and toxicity"
                },
                "Poor metabolizer (PM)": {
                    "Enzyme Activity": "Little to no enzyme activity",
                    "Effect on Active-Drug Levels": "Drug metabolized slowly, highest levels",
                    "Clinical Consequence": "Highest risk of toxicity (or prodrug stays inactive)"
                }
            }
        },
        {
            "slug": "drug_gene_tests",
            "title": "Drug-Gene Pairs and Pharmacogenomic Testing",
            "subtitle": "Match each drug to its associated gene/test, its use, and whether testing is required before therapy",
            "categories": ["Associated Gene / Test", "Drug Class or Use", "Testing Required Before Therapy?"],
            "data": {
                "Abacavir": {
                    "Associated Gene / Test": "HLA-B*5701",
                    "Drug Class or Use": "NRTI antiretroviral for HIV",
                    "Testing Required Before Therapy?": "Yes"
                },
                "Allopurinol": {
                    "Associated Gene / Test": "HLA-B*5801",
                    "Drug Class or Use": "Urate-lowering therapy for gout",
                    "Testing Required Before Therapy?": "No"
                },
                "Clopidogrel": {
                    "Associated Gene / Test": "CYP2C19",
                    "Drug Class or Use": "Antiplatelet agent",
                    "Testing Required Before Therapy?": "No"
                },
                "Warfarin": {
                    "Associated Gene / Test": "CYP2C9 (and VKORC1)",
                    "Drug Class or Use": "Oral anticoagulant / blood thinner",
                    "Testing Required Before Therapy?": "No"
                },
                "Trastuzumab": {
                    "Associated Gene / Test": "HER2 gene expression",
                    "Drug Class or Use": "Anti-HER2 monoclonal antibody",
                    "Testing Required Before Therapy?": "Yes"
                },
                "Cetuximab": {
                    "Associated Gene / Test": "KRAS mutation",
                    "Drug Class or Use": "EGFR-inhibitor monoclonal antibody",
                    "Testing Required Before Therapy?": "Yes"
                }
            }
        },
        {
            "slug": "cyp_enzyme_associations",
            "title": "Key CYP Enzyme Drug Associations",
            "subtitle": "Match each CYP enzyme to a classic substrate, a notable inhibitor, and a notable inducer",
            "categories": ["Classic Substrate", "Notable Inhibitor", "Notable Inducer"],
            "data": {
                "CYP3A4": {
                    "Classic Substrate": "Metabolizes the largest share of common drugs",
                    "Notable Inhibitor": "Fluconazole, erythromycin, diltiazem, grapefruit juice",
                    "Notable Inducer": "Rifampin, carbamazepine, St. John's wort"
                },
                "CYP1A2": {
                    "Classic Substrate": "Caffeine",
                    "Notable Inhibitor": "Ciprofloxacin",
                    "Notable Inducer": "Smoking, rifampin, phenytoin"
                },
                "CYP2C9": {
                    "Classic Substrate": "Warfarin",
                    "Notable Inhibitor": "Trimethoprim-sulfamethoxazole, metronidazole, fluconazole",
                    "Notable Inducer": "Rifampin, carbamazepine, phenytoin"
                },
                "CYP2C19": {
                    "Classic Substrate": "Clopidogrel",
                    "Notable Inhibitor": "Omeprazole, esomeprazole (PPIs)",
                    "Notable Inducer": "Rifampin, carbamazepine, phenytoin"
                },
                "CYP2D6": {
                    "Classic Substrate": "Codeine",
                    "Notable Inhibitor": "Fluoxetine, paroxetine, duloxetine (SSRIs), amiodarone",
                    "Notable Inducer": "None listed (dash in the source table)"
                }
            }
        },
        {
            "slug": "inducers_inhibitors",
            "title": "CYP Inducers vs Inhibitors",
            "subtitle": "Match each agent to the enzyme it affects, whether it induces or inhibits, and the clinical result",
            "categories": ["Enzyme(s) Affected", "Effect on Substrate Metabolism", "Clinical Example / Result"],
            "data": {
                "Rifampin": {
                    "Enzyme(s) Affected": "CYP3A4, 2C9, 2C19, 1A2 (broad)",
                    "Effect on Substrate Metabolism": "Induces - speeds up metabolism",
                    "Clinical Example / Result": "Co-administered drugs become less effective"
                },
                "St. John's wort": {
                    "Enzyme(s) Affected": "CYP3A4, 2C9, 1A2",
                    "Effect on Substrate Metabolism": "Induces - speeds up metabolism",
                    "Clinical Example / Result": "Herbal product causes drug failure"
                },
                "Grapefruit juice": {
                    "Enzyme(s) Affected": "CYP3A4",
                    "Effect on Substrate Metabolism": "Inhibits - slows metabolism",
                    "Clinical Example / Result": "Raised levels of CYP3A4 substrates"
                },
                "Trimethoprim-sulfamethoxazole": {
                    "Enzyme(s) Affected": "CYP2C9",
                    "Effect on Substrate Metabolism": "Inhibits - slows metabolism",
                    "Clinical Example / Result": "Raises warfarin levels, bleeding risk"
                },
                "Ciprofloxacin": {
                    "Enzyme(s) Affected": "CYP1A2",
                    "Effect on Substrate Metabolism": "Inhibits - slows metabolism",
                    "Clinical Example / Result": "Raised levels of CYP1A2 substrates"
                },
                "Omeprazole": {
                    "Enzyme(s) Affected": "CYP2C19",
                    "Effect on Substrate Metabolism": "Inhibits - slows metabolism",
                    "Clinical Example / Result": "Raised levels of CYP2C19 substrates"
                }
            }
        }
    ]
}
