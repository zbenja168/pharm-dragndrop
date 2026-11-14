BRICK = {
    "brick_num": 32,
    "brick_title": "Metformin, GLP-1 RA, and SGLT2 Inhibitors",
    "games": [
        {
            "slug": "antidiabetic_classes_overview",
            "title": "Antidiabetic Classes at a Glance",
            "subtitle": "Match each medication class to its mechanistic category, example drugs, and primary mechanism",
            "categories": ["Mechanistic Category", "Example Drugs", "Primary Mechanism"],
            "data": {
                "Biguanides": {
                    "Mechanistic Category": "Increase cellular sensitivity to insulin",
                    "Example Drugs": "Metformin",
                    "Primary Mechanism": "Decrease hepatic glucose production and improve peripheral insulin sensitivity"
                },
                "GLP-1 receptor agonists": {
                    "Mechanistic Category": "Stimulate glucose-dependent insulin release",
                    "Example Drugs": "Semaglutide, liraglutide, dulaglutide, exenatide",
                    "Primary Mechanism": "Mimic incretin signaling to raise glucose-dependent insulin and lower glucagon"
                },
                "SGLT2 inhibitors": {
                    "Mechanistic Category": "Increase renal excretion of glucose",
                    "Example Drugs": "Empagliflozin, dapagliflozin, canagliflozin",
                    "Primary Mechanism": "Block glucose reabsorption in the proximal tubule, increasing glucosuria"
                },
                "Insulin secretagogues": {
                    "Mechanistic Category": "Force insulin release regardless of glucose level",
                    "Example Drugs": "Sulfonylureas and meglitinides",
                    "Primary Mechanism": "Trigger glucose-independent insulin release, causing hypoglycemia and weight gain"
                }
            }
        },
        {
            "slug": "metformin_sites_of_action",
            "title": "Metformin: Where It Works",
            "subtitle": "Match each tissue to metformin's local action and the cellular event behind it",
            "categories": ["Tissue", "Local Action", "Cellular Event"],
            "data": {
                "Liver": {
                    "Tissue": "Hepatocytes of the liver",
                    "Local Action": "Decreased hepatic glucose production",
                    "Cellular Event": "Reduced gluconeogenesis and glycogenolysis"
                },
                "Intestine": {
                    "Tissue": "Intestinal wall and lumen",
                    "Local Action": "Decreased intestinal absorption of glucose",
                    "Cellular Event": "Inhibition of mitochondrial electron transport favoring anaerobic metabolism"
                },
                "Skeletal muscle": {
                    "Tissue": "Peripheral skeletal muscle cells",
                    "Local Action": "Increased glucose uptake and utilization",
                    "Cellular Event": "AMPK stimulation drives GLUT-4 translocation to the cell membrane"
                },
                "Adipose tissue": {
                    "Tissue": "Fat cells",
                    "Local Action": "Decreased lipogenesis",
                    "Cellular Event": "AMPK activation lowers triglyceride and LDL cholesterol levels"
                }
            }
        },
        {
            "slug": "glp1_receptor_agonist_effects",
            "title": "GLP-1 Receptor Agonist Effects",
            "subtitle": "Match each site of GLP-1 action to its immediate effect and the net benefit it provides",
            "categories": ["Site or Target", "Immediate Effect", "Net Benefit"],
            "data": {
                "Pancreatic beta cells": {
                    "Site or Target": "Insulin-secreting pancreatic beta cells",
                    "Immediate Effect": "Increased glucose-dependent insulin secretion",
                    "Net Benefit": "Lowers glucose with low hypoglycemia risk when used alone"
                },
                "Pancreatic alpha cells": {
                    "Site or Target": "Glucagon-secreting pancreatic alpha cells",
                    "Immediate Effect": "Decreased glucagon secretion",
                    "Net Benefit": "Reduces hepatic glucose output"
                },
                "Stomach": {
                    "Site or Target": "Gastric emptying pathway",
                    "Immediate Effect": "Slowed gastric emptying",
                    "Net Benefit": "Blunts postprandial glucose spikes"
                },
                "Satiety center": {
                    "Site or Target": "Central appetite and satiety signaling",
                    "Immediate Effect": "Increased satiety",
                    "Net Benefit": "Decreases food intake and promotes weight loss"
                }
            }
        },
        {
            "slug": "metformin_adverse_effects_mitigation",
            "title": "Metformin Adverse Effects and Mitigation",
            "subtitle": "Match each metformin adverse effect to its cause and the strategy that reduces it",
            "categories": ["Adverse Effect", "Cause", "Mitigation or Note"],
            "data": {
                "GI upset": {
                    "Adverse Effect": "Nausea, diarrhea, flatulence, abdominal pain",
                    "Cause": "Common effect just after starting therapy",
                    "Mitigation or Note": "Start at lowest dose, take with food, titrate slowly, or use extended-release"
                },
                "Metallic taste": {
                    "Adverse Effect": "Persistent metallic taste in the mouth",
                    "Cause": "Metformin is secreted in the saliva",
                    "Mitigation or Note": "Self-resolves within a few weeks of consistent use"
                },
                "Vitamin B12 deficiency": {
                    "Adverse Effect": "Anemia and neuropathy from B12 deficiency",
                    "Cause": "Impaired B12 absorption in the terminal ileum with long-term use",
                    "Mitigation or Note": "Incidence about 7 percent; mitigate with B12 supplementation"
                },
                "Lactic acidosis": {
                    "Adverse Effect": "Rare but potentially fatal lactic acidosis",
                    "Cause": "Inhibition of mitochondrial electron transport with impaired lactate clearance",
                    "Mitigation or Note": "Dose-adjust for renal function; contraindicated when eGFR is below 30"
                }
            }
        }
    ]
}
