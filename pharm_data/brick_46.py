BRICK = {
    "brick_num": 46,
    "brick_title": "Sulfonamides (Folic acid synthesis inhibitors)",
    "games": [
        {
            "slug": "meet_the_folate_drugs",
            "title": "Meet the Folate-Pathway Drugs",
            "subtitle": "Match each drug to its role, distinguishing feature, and use or partner",
            "categories": ["Role", "Distinguishing Feature", "Use or Partner"],
            "data": {
                "Sulfadiazine": {
                    "Role": "Sulfonamide that competitively blocks DHPS",
                    "Distinguishing Feature": "Short-acting, half-life about 10 hours",
                    "Use or Partner": "Systemic infections; paired with pyrimethamine"
                },
                "Sulfamethoxazole (SMX)": {
                    "Role": "Sulfonamide partly metabolized by CYP2C9",
                    "Distinguishing Feature": "Intermediate-acting, half-life 9-12 hours",
                    "Use or Partner": "UTI, gut and skin infections; paired with TMP"
                },
                "Trimethoprim (TMP)": {
                    "Role": "Folate antagonist that blocks dihydrofolate reductase",
                    "Distinguishing Feature": "Stronger affinity for bacterial than human enzyme",
                    "Use or Partner": "Combined with SMX for synergistic killing"
                },
                "Pyrimethamine": {
                    "Role": "Folate antagonist paired with a short-acting sulfonamide",
                    "Distinguishing Feature": "Bacteriostatic when used on its own",
                    "Use or Partner": "Combined with sulfadiazine"
                }
            }
        },
        {
            "slug": "folate_synthesis_pathway",
            "title": "The Bacterial Folate Pathway",
            "subtitle": "Match each pathway component to its role and how the drugs affect it",
            "categories": ["Role in Pathway", "Drug Connection"],
            "data": {
                "PABA": {
                    "Role in Pathway": "Substrate bacteria take in or produce",
                    "Drug Connection": "Structurally mimicked by sulfonamides"
                },
                "Dihydropteroate synthase (DHPS)": {
                    "Role in Pathway": "Joins PABA with pteridine",
                    "Drug Connection": "Competitively inhibited by sulfonamides"
                },
                "Dihydropteroic acid": {
                    "Role in Pathway": "DHPS product that is converted to DHF",
                    "Drug Connection": "Not formed when sulfonamides block step 2"
                },
                "Dihydrofolate reductase": {
                    "Role in Pathway": "Converts DHF to tetrahydrofolic acid",
                    "Drug Connection": "Inhibited by trimethoprim and pyrimethamine"
                },
                "Tetrahydrofolic acid (THF)": {
                    "Role in Pathway": "Required to make DNA, RNA and proteins",
                    "Drug Connection": "Depleted most when both enzymes are blocked"
                }
            }
        },
        {
            "slug": "sulfonamide_pharmacokinetics",
            "title": "Sulfonamide Pharmacokinetics",
            "subtitle": "Match each pharmacokinetic phase to its key fact and clinical significance",
            "categories": ["Key Fact", "Clinical Significance"],
            "data": {
                "Absorption": {
                    "Key Fact": "Very good oral and good topical absorption",
                    "Clinical Significance": "Given orally, topically or parenterally"
                },
                "Metabolism": {
                    "Key Fact": "Hepatic; SMX partly via CYP2C9",
                    "Clinical Significance": "Basis of the warfarin interaction and raised INR"
                },
                "Distribution": {
                    "Key Fact": "Reaches urine, vaginal and middle ear fluids",
                    "Clinical Significance": "Good cerebrospinal fluid penetration as well"
                },
                "Excretion": {
                    "Key Fact": "Mainly urinary, much of it unmetabolized",
                    "Clinical Significance": "Gives good efficacy for urinary tract infections"
                }
            }
        },
        {
            "slug": "sulfonamide_adverse_effects",
            "title": "Adverse Effects, Interactions and Pregnancy",
            "subtitle": "Match each clinical setting to the problem it causes and the mechanism or note",
            "categories": ["Problem", "Mechanism or Note"],
            "data": {
                "Warfarin co-therapy": {
                    "Problem": "Raised INR and bleeding risk",
                    "Mechanism or Note": "SMX/TMP inhibits CYP2C9, slowing warfarin metabolism"
                },
                "ACEi/ARB or NSAID co-therapy": {
                    "Problem": "Hyperkalemia",
                    "Mechanism or Note": "Potentially life-threatening in elderly and HIV patients"
                },
                "G6PD deficiency": {
                    "Problem": "Rapid acute hemolytic anemia",
                    "Mechanism or Note": "Rare reaction triggered by sulfonamide exposure"
                },
                "First trimester of pregnancy": {
                    "Problem": "Neural tube defects",
                    "Mechanism or Note": "TMP interferes with folate metabolism"
                },
                "Last month of pregnancy": {
                    "Problem": "Kernicterus in the neonate",
                    "Mechanism or Note": "Sulfonamide displaces bilirubin from serum albumin"
                },
                "Taking the tablet with little fluid": {
                    "Problem": "Crystalluria",
                    "Mechanism or Note": "Prevented by drinking at least 8 oz of water per dose"
                }
            }
        }
    ]
}
