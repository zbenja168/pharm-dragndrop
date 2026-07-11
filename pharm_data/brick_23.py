BRICK = {
    "brick_num": 23,
    "brick_title": "β-Blockers",
    "games": [
        {
            "slug": "organ_effects",
            "title": "Where β-Blockade Acts",
            "subtitle": "Match each tissue to the normal β-effect it uses and what happens when that receptor is blocked",
            "categories": ["Tissue / Cell", "Normal β-Effect (agonist)", "Result of β-Blockade"],
            "data": {
                "Heart (SA/AV node & myocardium)": {
                    "Tissue / Cell": "Cardiac pacemaker and contractile tissue",
                    "Normal β-Effect (agonist)": "β1 raises heart rate and contractility",
                    "Result of β-Blockade": "Lower heart rate and contractility (negative chrono/inotropy)"
                },
                "Kidney (juxtaglomerular cells)": {
                    "Tissue / Cell": "Renin-secreting cells of the nephron",
                    "Normal β-Effect (agonist)": "β1 stimulates renin release, driving RAAS",
                    "Result of β-Blockade": "Less renin, lowering angiotensin II and blood pressure"
                },
                "Bronchiolar smooth muscle": {
                    "Tissue / Cell": "Airway smooth muscle of the lungs",
                    "Normal β-Effect (agonist)": "β2 causes bronchodilation",
                    "Result of β-Blockade": "Bronchoconstriction, dangerous in asthma/COPD"
                },
                "Hepatocytes (liver)": {
                    "Tissue / Cell": "Glucose-releasing cells of the liver",
                    "Normal β-Effect (agonist)": "β2 promotes glycogenolysis and glucose release",
                    "Result of β-Blockade": "Hypoglycemia and masked warning symptoms"
                },
                "Skeletal muscle arterioles": {
                    "Tissue / Cell": "Resistance vessels of skeletal muscle",
                    "Normal β-Effect (agonist)": "β2 causes vasodilation",
                    "Result of β-Blockade": "Vasoconstriction from unopposed α1 tone"
                }
            }
        },
        {
            "slug": "clinical_uses",
            "title": "Why We Prescribe β-Blockers",
            "subtitle": "Match each indication to the underlying problem, the rationale, and a representative agent",
            "categories": ["Clinical Problem", "Rationale for β-Blockade", "Example Agent"],
            "data": {
                "Post-MI / acute coronary syndrome": {
                    "Clinical Problem": "Oxygen supply-demand mismatch in cardiac muscle",
                    "Rationale for β-Blockade": "Cuts myocardial oxygen demand via negative inotropy/chronotropy",
                    "Example Agent": "Metoprolol (β1-selective)"
                },
                "Chronic heart failure (HFrEF)": {
                    "Clinical Problem": "Falling cardiac output triggers sympathetic overdrive",
                    "Rationale for β-Blockade": "Blunts harmful chronic sympathetic activation, improving survival",
                    "Example Agent": "Carvedilol"
                },
                "Hyperthyroidism": {
                    "Clinical Problem": "Excess thyroid hormone amplifies sympathetic tone",
                    "Rationale for β-Blockade": "Controls tremor, tachycardia, and anxiety",
                    "Example Agent": "Propranolol (nonselective)"
                },
                "Situational (performance) anxiety": {
                    "Clinical Problem": "Adrenergic surge before public performance",
                    "Rationale for β-Blockade": "Suppresses tremor and palpitations prophylactically",
                    "Example Agent": "Propranolol"
                },
                "Open-angle glaucoma": {
                    "Clinical Problem": "Elevated intraocular pressure",
                    "Rationale for β-Blockade": "Decreases aqueous humor production in the eye",
                    "Example Agent": "Timolol (topical eye drops)"
                },
                "Migraine prophylaxis": {
                    "Clinical Problem": "Recurrent disabling headaches",
                    "Rationale for β-Blockade": "Prevents attacks by an unknown mechanism",
                    "Example Agent": "Metoprolol"
                }
            }
        },
        {
            "slug": "pk_profiles",
            "title": "Pharmacokinetic Personalities",
            "subtitle": "Match each β-blocker to its solubility/elimination, a distinctive PK feature, and its selectivity",
            "categories": ["Solubility / Elimination", "Distinctive PK Feature", "Selectivity"],
            "data": {
                "Propranolol": {
                    "Solubility / Elimination": "Highly lipophilic; hepatic metabolism",
                    "Distinctive PK Feature": "Most lipophilic agent; crosses the blood-brain barrier, short half-life",
                    "Selectivity": "Nonselective β-blocker"
                },
                "Atenolol": {
                    "Solubility / Elimination": "Hydrophilic; renal excretion",
                    "Distinctive PK Feature": "Eliminated largely unchanged by the kidneys, longer half-life",
                    "Selectivity": "β1-selective (cardioselective)"
                },
                "Esmolol": {
                    "Solubility / Elimination": "Rapidly hydrolyzed by blood esterases",
                    "Distinctive PK Feature": "IV-only agent with onset within 5-10 minutes",
                    "Selectivity": "β1-selective, ultra-short-acting"
                },
                "Labetalol": {
                    "Solubility / Elimination": "Extensively metabolized by the liver; oral and IV",
                    "Distinctive PK Feature": "IV onset within 5 minutes for hypertensive emergencies",
                    "Selectivity": "Nonselective β plus α1-blockade"
                },
                "Pindolol": {
                    "Solubility / Elimination": "Partial β-agonist with intrinsic sympathomimetic activity",
                    "Distinctive PK Feature": "Gives low-grade β-stimulation at rest; avoid in angina",
                    "Selectivity": "Nonselective β-blocker with ISA"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "β-Blocker Adverse Effects",
            "subtitle": "Match each adverse effect to its mechanism, the group at highest risk, and how to manage it",
            "categories": ["Mechanism", "Highest-Risk Group", "Management / Prevention"],
            "data": {
                "Bronchoconstriction": {
                    "Mechanism": "β2-blockade in bronchiolar smooth muscle",
                    "Highest-Risk Group": "Patients with asthma or COPD",
                    "Management / Prevention": "Prefer a β1-selective agent"
                },
                "Bradycardia / heart block": {
                    "Mechanism": "Negative chronotropy slows SA and AV node conduction",
                    "Highest-Risk Group": "Patients with AV conduction defects",
                    "Management / Prevention": "Avoid and monitor heart rate"
                },
                "Masked hypoglycemia": {
                    "Mechanism": "β2-blockade blunts adrenergic warning signs",
                    "Highest-Risk Group": "Insulin-treated diabetics",
                    "Management / Prevention": "Use β1-selective agents with caution"
                },
                "Rebound angina on withdrawal": {
                    "Mechanism": "β1-receptor upregulation and hypersensitivity",
                    "Highest-Risk Group": "Patients who stop therapy abruptly",
                    "Management / Prevention": "Taper the dose gradually"
                },
                "Depression, fatigue, sexual dysfunction": {
                    "Mechanism": "Blockade of central and autonomic β-receptors",
                    "Highest-Risk Group": "Patients on lipophilic CNS-penetrating agents",
                    "Management / Prevention": "Consider a hydrophilic agent"
                },
                "Hyperkalemia": {
                    "Mechanism": "Reduced β-mediated cellular potassium uptake",
                    "Highest-Risk Group": "Patients with chronic kidney disease",
                    "Management / Prevention": "Monitor serum potassium"
                }
            }
        }
    ]
}
