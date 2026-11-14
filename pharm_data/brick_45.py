BRICK = {
    "brick_num": 45,
    "brick_title": "Metformin, GLP-1 RA, and SGLT2 Inhibitors",
    "games": [
        {
            "slug": "three_classes_vs_secretagogues",
            "title": "Three Classes vs. Insulin Secretagogues",
            "subtitle": "Match each drug group to its glucose-lowering action, hypoglycemia risk, and weight effect",
            "categories": ["Glucose-Lowering Action", "Hypoglycemia Risk Alone", "Weight Effect"],
            "data": {
                "Metformin": {
                    "Glucose-Lowering Action": "Increases cellular sensitivity to insulin",
                    "Hypoglycemia Risk Alone": "Low; does not force insulin release",
                    "Weight Effect": "Weight neutral or small weight loss"
                },
                "GLP-1 receptor agonists": {
                    "Glucose-Lowering Action": "Mimic incretin to raise glucose-dependent insulin secretion",
                    "Hypoglycemia Risk Alone": "Low; insulin release is glucose-dependent",
                    "Weight Effect": "Weight loss through increased satiety"
                },
                "SGLT2 inhibitors": {
                    "Glucose-Lowering Action": "Increase renal excretion of glucose",
                    "Hypoglycemia Risk Alone": "Low; action is insulin-independent",
                    "Weight Effect": "Modest loss from glucose calories lost in urine"
                },
                "Sulfonylureas and meglitinides": {
                    "Glucose-Lowering Action": "Insulin secretagogues that drive insulin release",
                    "Hypoglycemia Risk Alone": "Can cause hypoglycemia",
                    "Weight Effect": "Weight gain"
                }
            }
        },
        {
            "slug": "metformin_by_tissue",
            "title": "Metformin, Tissue by Tissue",
            "subtitle": "Match each site to what metformin does there and the result",
            "categories": ["What Metformin Does Here", "Result"],
            "data": {
                "Liver": {
                    "What Metformin Does Here": "Decreases gluconeogenesis and glycogenolysis",
                    "Result": "Lower hepatic glucose production"
                },
                "Skeletal muscle": {
                    "What Metformin Does Here": "Stimulates AMPK, driving GLUT-4 to the cell membrane",
                    "Result": "More glucose uptake and less lipogenesis"
                },
                "Intestine": {
                    "What Metformin Does Here": "Inhibits mitochondrial electron transport; cuts glucose absorption",
                    "Result": "Anaerobic glucose metabolism generates lactate"
                },
                "Kidney": {
                    "What Metformin Does Here": "Clears the lactate produced during therapy",
                    "Result": "Reduced function predisposes to lactic acidosis"
                },
                "Terminal ileum": {
                    "What Metformin Does Here": "Interferes with vitamin B12 absorption",
                    "Result": "Reversible anemia and neuropathy with long-term use"
                }
            }
        },
        {
            "slug": "metformin_adverse_effects",
            "title": "Metformin Adverse Effects and Fixes",
            "subtitle": "Match each metformin adverse effect to its cause or risk factor and how to prevent or manage it",
            "categories": ["Cause or Risk Factor", "Prevention or Management"],
            "data": {
                "GI upset and diarrhea": {
                    "Cause or Risk Factor": "Common when first starting therapy",
                    "Prevention or Management": "Start low, titrate every 1-2 weeks, take with food, use extended-release"
                },
                "Metallic taste": {
                    "Cause or Risk Factor": "Drug is secreted in the saliva on starting or restarting",
                    "Prevention or Management": "Self-resolves within a few weeks of consistent use"
                },
                "Vitamin B12 deficiency": {
                    "Cause or Risk Factor": "Long-term use; affects about 7% of patients",
                    "Prevention or Management": "Monitor B12 and supplement when appropriate"
                },
                "Lactic acidosis": {
                    "Cause or Risk Factor": "High dose, poor renal function, severe CHF, progressive liver disease",
                    "Prevention or Management": "Do not start at eGFR 30-45; contraindicated below eGFR 30"
                }
            }
        },
        {
            "slug": "glp1_sglt2_adverse_effects",
            "title": "GLP-1 RA and SGLT2 Inhibitor Adverse Effects",
            "subtitle": "Match each adverse effect to its drug class, trigger, and counseling point",
            "categories": ["Drug Class", "Trigger or Mechanism", "Counseling Point"],
            "data": {
                "Nausea and early satiety": {
                    "Drug Class": "GLP-1 receptor agonist",
                    "Trigger or Mechanism": "Most noticeable at initiation or a dose increase",
                    "Counseling Point": "Eat smaller meals, stop when full, avoid large high-fat meals"
                },
                "Acute pancreatitis": {
                    "Drug Class": "GLP-1 RA (rare effect)",
                    "Trigger or Mechanism": "Rare but important class adverse effect",
                    "Counseling Point": "Seek care for severe abdominal pain radiating to the back"
                },
                "Hypoglycemia in combination": {
                    "Drug Class": "GLP-1 RA added to insulin or a sulfonylurea",
                    "Trigger or Mechanism": "Partner drug lowers glucose independent of glucose level",
                    "Counseling Point": "Reduce the insulin or sulfonylurea dose"
                },
                "Genital mycotic infection": {
                    "Drug Class": "SGLT2 inhibitor",
                    "Trigger or Mechanism": "Glucosuria",
                    "Counseling Point": "Good genital hygiene; treat itching or discharge early"
                },
                "Volume depletion and dizziness": {
                    "Drug Class": "SGLT2 inhibitor (diuretic effect)",
                    "Trigger or Mechanism": "Osmotic diuresis increases urination",
                    "Counseling Point": "Maintain fluid intake; take care with vomiting or diarrhea"
                },
                "Euglycemic diabetic ketoacidosis": {
                    "Drug Class": "SGLT2 inhibitor (rare effect)",
                    "Trigger or Mechanism": "Fasting, acute illness, major surgery, very low-carb intake",
                    "Counseling Point": "Hold the drug during serious illness or before procedures"
                }
            }
        }
    ]
}
