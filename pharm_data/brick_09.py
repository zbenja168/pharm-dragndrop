BRICK = {
    "brick_num": 9,
    "brick_title": "Pharmacokinetics-3: Loading and Maintenance Dose",
    "games": [
        {
            "slug": "pk_variables",
            "title": "Dosing Equation Variables",
            "subtitle": "Match each pharmacokinetic variable to what it represents, the formula it drives, and an example fact",
            "categories": ["What it represents", "Formula it drives", "Illustrative fact"],
            "data": {
                "Cp": {
                    "What it represents": "Target plasma concentration at steady state",
                    "Formula it drives": "Both the loading and maintenance dose",
                    "Illustrative fact": "Target of 1.5 mcg/L in the digoxin example"
                },
                "Vd": {
                    "What it represents": "Volume of distribution (apparent)",
                    "Formula it drives": "Loading dose = Cp x Vd / F",
                    "Illustrative fact": "Amiodarone's is very large (~66 L/kg)"
                },
                "F": {
                    "What it represents": "Bioavailability, fraction of unchanged drug reaching circulation",
                    "Formula it drives": "Denominator of both dosing formulas",
                    "Illustrative fact": "1.0 for IV; estimated ~0.7 for oral drugs"
                },
                "CL": {
                    "What it represents": "Clearance, volume cleared of drug per unit time",
                    "Formula it drives": "Maintenance dose = Cp x CL x tau / F",
                    "Illustrative fact": "120 L/day in the oral digoxin case"
                },
                "tau": {
                    "What it represents": "Dosage interval, the time between doses",
                    "Formula it drives": "Maintenance dose only (if not continuous)",
                    "Illustrative fact": "12 h when a drug is dosed twice daily"
                }
            }
        },
        {
            "slug": "loading_vs_maintenance",
            "title": "Loading Dose vs Maintenance Dose",
            "subtitle": "Sort each feature under the dose it describes",
            "categories": ["Loading Dose", "Maintenance Dose"],
            "data": {
                "Primary determinant": {
                    "Loading Dose": "Volume of distribution (Vd)",
                    "Maintenance Dose": "Clearance (CL)"
                },
                "Which drugs need it": {
                    "Loading Dose": "Only a few, lipophilic drugs (amiodarone, digoxin)",
                    "Maintenance Dose": "Most drugs need one"
                },
                "Need for modification": {
                    "Loading Dose": "Rarely needs modification",
                    "Maintenance Dose": "Modified per patient or drug characteristics"
                },
                "Purpose": {
                    "Loading Dose": "Rapidly reach the target steady-state level",
                    "Maintenance Dose": "Sustain steady state and prevent toxicity"
                },
                "Formula": {
                    "Loading Dose": "Cp x Vd / F",
                    "Maintenance Dose": "Cp x CL x tau / F"
                }
            }
        },
        {
            "slug": "dose_calculations",
            "title": "Worked Dose Calculations",
            "subtitle": "Match each dosing scenario to its given values and its calculated dose",
            "categories": ["Given values", "Calculated dose"],
            "data": {
                "Fauxspirin IV loading dose": {
                    "Given values": "Cp 50 mg/mL, Vd 5 mL, IV bolus (F = 1)",
                    "Calculated dose": "250 mg"
                },
                "Fauxspirin oral loading dose": {
                    "Given values": "Cp 100 mg/mL, Vd 5 mL, oral (F = 0.5)",
                    "Calculated dose": "1000 mg"
                },
                "Fauxspirin IV maintenance dose": {
                    "Given values": "Cp 50 mg/mL, CL 2 mL/h, continuous IV (F = 1)",
                    "Calculated dose": "100 mg/h"
                },
                "Fauxspirin oral maintenance dose": {
                    "Given values": "Cp 100 mg/mL, CL 2 mL/h, every 12 h, oral (F = 0.5)",
                    "Calculated dose": "4800 mg"
                },
                "Digoxin oral loading dose": {
                    "Given values": "Cp 1.5 mcg/L, Vd 500 L, oral (F = 0.6)",
                    "Calculated dose": "1.25 mg"
                }
            }
        },
        {
            "slug": "clinical_applications",
            "title": "Clinical Applications and Concepts",
            "subtitle": "Match each concept to a key detail from the brick and its clinical result",
            "categories": ["Underlying concept", "Key detail from the brick", "Result or consequence"],
            "data": {
                "Amiodarone dosing": {
                    "Underlying concept": "Highly lipophilic drug with a very large Vd",
                    "Key detail from the brick": "Vd ~66 L/kg; oral absorption incomplete and variable (30-70%)",
                    "Result or consequence": "800 mg loading dose, then 200 mg maintenance dose"
                },
                "Phenytoin toxicity case": {
                    "Underlying concept": "Loading dose never switched to a maintenance dose",
                    "Key detail from the brick": "Serum phenytoin rose to 3x the maximum therapeutic level",
                    "Result or consequence": "Somnolence, severe ataxia, and dysarthria"
                },
                "Loading dose purpose": {
                    "Underlying concept": "Large single initial dose",
                    "Key detail from the brick": "Target level reached with one administration",
                    "Result or consequence": "Rapid achievement of steady-state concentration"
                },
                "Dosing without a loading dose": {
                    "Underlying concept": "Regular maintenance dosing only",
                    "Key detail from the brick": "Needs about 4-5 half-lives to accumulate",
                    "Result or consequence": "Delayed time to reach steady state"
                },
                "Doubling the infusion rate": {
                    "Underlying concept": "Css is proportional to infusion rate",
                    "Key detail from the brick": "Infusion time is left unchanged",
                    "Result or consequence": "Steady-state concentration doubles"
                }
            }
        }
    ]
}
