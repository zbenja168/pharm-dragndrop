BRICK = {
    "brick_num": 4,
    "brick_title": "Nonopioid Analgesics - NSAIDs",
    "games": [
        {
            "slug": "prostaglandins",
            "title": "Prostaglandins and Their Roles",
            "subtitle": "Match each prostaglandin to its main source, key action, and the effect of blocking it with NSAIDs",
            "categories": ["Main Source / Tissue", "Key Physiologic Action", "Effect of NSAID Blockade"],
            "data": {
                "PGE2": {
                    "Main Source / Tissue": "Kidney, brain, blood vessels, stomach",
                    "Key Physiologic Action": "Stimulates pain receptors, resets hypothalamic set point, reduces gastric acid, dilates vessels",
                    "Effect of NSAID Blockade": "Analgesia and antipyresis, but loss of gastric and renal protection"
                },
                "PGI2 (prostacyclin)": {
                    "Main Source / Tissue": "Vascular endothelium",
                    "Key Physiologic Action": "Dilates blood vessels and inhibits platelet aggregation",
                    "Effect of NSAID Blockade": "Reduced PGI2 raises thrombotic and cardiovascular risk"
                },
                "Thromboxane A2 (TxA2)": {
                    "Main Source / Tissue": "Platelets",
                    "Key Physiologic Action": "Promotes platelet aggregation and vasoconstriction",
                    "Effect of NSAID Blockade": "Aspirin blockade prevents clot formation (antithrombotic)"
                },
                "PGF2-alpha": {
                    "Main Source / Tissue": "Uterus, airways, eyes",
                    "Key Physiologic Action": "Stimulates pain receptors",
                    "Effect of NSAID Blockade": "Contributes to the analgesic effect"
                },
                "PGD2": {
                    "Main Source / Tissue": "Mast cells, brain, airways",
                    "Key Physiologic Action": "Mediates the inflammatory response",
                    "Effect of NSAID Blockade": "Reduced inflammation, swelling, and redness"
                }
            }
        },
        {
            "slug": "nsaid_classes",
            "title": "Classifying NSAIDs",
            "subtitle": "Match each NSAID to its chemical class, COX selectivity, and signature clinical feature",
            "categories": ["Chemical Class", "COX Selectivity", "Signature Clinical Feature"],
            "data": {
                "Aspirin": {
                    "Chemical Class": "Salicylate",
                    "COX Selectivity": "Nonselective, irreversible",
                    "Signature Clinical Feature": "Antiplatelet drug for MI and stroke prevention"
                },
                "Ibuprofen": {
                    "Chemical Class": "Nonsalicylate carboxylic acid",
                    "COX Selectivity": "Nonselective, reversible",
                    "Signature Clinical Feature": "OTC analgesic; IV form closes the ductus arteriosus"
                },
                "Indomethacin": {
                    "Chemical Class": "Nonsalicylate carboxylic acid",
                    "COX Selectivity": "Nonselective, reversible",
                    "Signature Clinical Feature": "Closes patent ductus arteriosus in premature neonates"
                },
                "Celecoxib": {
                    "Chemical Class": "Coxib",
                    "COX Selectivity": "Selective COX-2",
                    "Signature Clinical Feature": "Better GI safety but higher cardiovascular risk"
                },
                "Naproxen": {
                    "Chemical Class": "Nonsalicylate carboxylic acid",
                    "COX Selectivity": "Nonselective, reversible",
                    "Signature Clinical Feature": "Lowest cardiovascular risk among the NSAIDs"
                },
                "Diclofenac": {
                    "Chemical Class": "Older nonsalicylate NSAID",
                    "COX Selectivity": "COX-2 selective",
                    "Signature Clinical Feature": "Topical gel used for osteoarthritis; high CV risk"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "NSAID Adverse Effects by Organ System",
            "subtitle": "Match each adverse effect to its organ system, underlying mechanism, and management note",
            "categories": ["Organ System", "Mechanism", "Management / At-Risk Note"],
            "data": {
                "Peptic ulcers and GI bleeding": {
                    "Organ System": "Gastrointestinal",
                    "Mechanism": "Loss of COX-1 PGE2/PGI2 that protect the gastric lining",
                    "Management / At-Risk Note": "Prefer selective COX-2 in patients with ulcer history"
                },
                "Thrombosis and myocardial infarction": {
                    "Organ System": "Cardiovascular",
                    "Mechanism": "Reduced PGI2 leaves platelet prothrombotic activity unopposed",
                    "Management / At-Risk Note": "Avoid long-term use in established coronary disease"
                },
                "Acute kidney injury": {
                    "Organ System": "Renal",
                    "Mechanism": "Loss of PGE2/PGI2 afferent arteriole dilation lowers GFR",
                    "Management / At-Risk Note": "Contraindicated in significant renal impairment; risk if >65"
                },
                "Elevated blood pressure": {
                    "Organ System": "Vascular / hypertension",
                    "Mechanism": "Blunts the effect of antihypertensive drugs",
                    "Management / At-Risk Note": "Use cautiously in uncontrolled hypertension"
                },
                "Premature ductus closure": {
                    "Organ System": "Fetal circulation",
                    "Mechanism": "Blocks PGE2 that maintains ductus arteriosus patency",
                    "Management / At-Risk Note": "Avoid in the 3rd trimester (>30 weeks)"
                }
            }
        },
        {
            "slug": "drug_interactions",
            "title": "NSAID Drug Interactions",
            "subtitle": "Match each co-administered drug to the risk it adds with NSAIDs and the mechanism",
            "categories": ["Added Risk", "Mechanism", "Clinical Note"],
            "data": {
                "Warfarin": {
                    "Added Risk": "Bleeding",
                    "Mechanism": "Nonsalicylate NSAIDs displace protein-bound warfarin and inhibit platelets",
                    "Clinical Note": "Avoid the combination"
                },
                "Glucocorticoids": {
                    "Added Risk": "GI bleeding and ulcer",
                    "Mechanism": "Additive gastroduodenal mucosal toxicity",
                    "Clinical Note": "Increases risk of GI bleeding"
                },
                "SSRIs": {
                    "Added Risk": "GI bleeding",
                    "Mechanism": "Impaired platelet serotonin worsens GI toxicity",
                    "Clinical Note": "Monitor for gastrointestinal bleeding"
                },
                "ACE inhibitors": {
                    "Added Risk": "Acute kidney injury and hyperkalemia",
                    "Mechanism": "Combined loss of renal perfusion and afferent dilation",
                    "Clinical Note": "Monitor renal function and potassium"
                },
                "Lithium": {
                    "Added Risk": "Lithium toxicity",
                    "Mechanism": "Reduced renal excretion raises lithium levels",
                    "Clinical Note": "Monitor serum lithium concentration"
                },
                "Methotrexate": {
                    "Added Risk": "Methotrexate toxicity",
                    "Mechanism": "Reduced renal excretion raises methotrexate levels",
                    "Clinical Note": "Caution with high-dose methotrexate therapy"
                }
            }
        }
    ]
}
