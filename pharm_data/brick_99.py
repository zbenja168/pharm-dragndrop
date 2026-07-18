BRICK = {
    "brick_num": 99,
    "brick_title": "Cross-Brick Synthesis",
    "games": [
        {
            "slug": "pharmacokinetic_principles",
            "title": "Pharmacokinetic Principles Across Bricks",
            "subtitle": "Match each pharmacokinetic concept to its core idea, key determinant or formula, and clinical pearl.",
            "categories": ["Core Principle", "Key Determinant or Formula", "Clinical Pearl"],
            "data": {
                "Bioavailability (Brick 1)": {
                    "Core Principle": "Fraction of an administered dose that reaches the systemic circulation unchanged",
                    "Key Determinant or Formula": "F equals 1.0 for IV drugs and falls with poor absorption or first-pass loss",
                    "Clinical Pearl": "Oral drugs with high hepatic extraction have low F and need larger oral doses"
                },
                "Drug Metabolism (Brick 2)": {
                    "Core Principle": "Phase I CYP450 reactions add functional groups before phase II conjugation reactions",
                    "Key Determinant or Formula": "Hepatic clearance depends on liver blood flow, extraction ratio, and enzyme activity",
                    "Clinical Pearl": "CYP inducers speed metabolism while inhibitors raise levels and toxicity risk"
                },
                "Ion Trapping and pKa (Brick 3)": {
                    "Core Principle": "Only nonionized drug crosses membranes, so pH relative to pKa sets absorption",
                    "Key Determinant or Formula": "Henderson-Hasselbalch predicts ionized fraction from the pH minus pKa difference",
                    "Clinical Pearl": "Alkalinizing urine with bicarbonate traps and eliminates weak acids like aspirin"
                },
                "Volume of Distribution (Brick 8)": {
                    "Core Principle": "Apparent volume relating total drug in body to its measured plasma concentration",
                    "Key Determinant or Formula": "Vd equals amount of drug in body divided by plasma drug concentration",
                    "Clinical Pearl": "High Vd lipophilic or tissue-bound drugs resist removal by hemodialysis"
                },
                "Loading Dose (Brick 9)": {
                    "Core Principle": "Initial dose that rapidly fills the volume of distribution to target concentration",
                    "Key Determinant or Formula": "Loading dose equals target plasma concentration times Vd divided by bioavailability",
                    "Clinical Pearl": "Loading dose is unchanged in renal or hepatic failure since it depends on Vd"
                },
                "Pharmacogenomics (Brick 10)": {
                    "Core Principle": "Inherited genetic variation alters drug metabolism, transport, or receptor response",
                    "Key Determinant or Formula": "Poor versus ultrarapid metabolizer phenotypes shift effective drug exposure",
                    "Clinical Pearl": "Slow acetylators accumulate isoniazid and hydralazine, raising drug-induced lupus risk"
                }
            }
        },
        {
            "slug": "autonomic_drugs_by_receptor",
            "title": "Autonomic Drugs Across Bricks",
            "subtitle": "Match each autonomic drug to its receptor target, primary mechanism, and main clinical use.",
            "categories": ["Receptor Target", "Primary Mechanism", "Main Clinical Use"],
            "data": {
                "Norepinephrine (Brick 12)": {
                    "Receptor Target": "Potent alpha-1 with beta-1 activity and minimal beta-2 stimulation",
                    "Primary Mechanism": "Raises systemic vascular resistance and cardiac contractility as a vasopressor",
                    "Main Clinical Use": "First-line vasopressor for septic and other distributive shock states"
                },
                "Phenylephrine (Brick 16)": {
                    "Receptor Target": "Selective alpha-1 adrenergic receptor agonist with no beta activity",
                    "Primary Mechanism": "Causes vasoconstriction and reflex bradycardia through pure alpha-1 stimulation",
                    "Main Clinical Use": "Nasal decongestant, mydriatic, and pressor for hypotension with tachycardia"
                },
                "Prazosin (Brick 17)": {
                    "Receptor Target": "Selective alpha-1 adrenergic receptor antagonist blocking vascular tone",
                    "Primary Mechanism": "Relaxes arteriolar and venous smooth muscle plus bladder neck sphincter",
                    "Main Clinical Use": "Benign prostatic hyperplasia, resistant hypertension, and PTSD nightmares"
                },
                "Albuterol (Brick 20)": {
                    "Receptor Target": "Selective beta-2 adrenergic receptor agonist in bronchial smooth muscle",
                    "Primary Mechanism": "Raises cAMP to relax bronchioles and shift potassium into cells",
                    "Main Clinical Use": "Rescue bronchodilator in acute asthma and adjunct for hyperkalemia"
                },
                "Propranolol (Brick 23)": {
                    "Receptor Target": "Nonselective beta-1 and beta-2 adrenergic receptor antagonist",
                    "Primary Mechanism": "Lowers heart rate, contractility, and renin release by blocking beta receptors",
                    "Main Clinical Use": "Angina, arrhythmia, migraine prophylaxis, and performance anxiety tremor"
                },
                "Bethanechol (Brick 25)": {
                    "Receptor Target": "Direct muscarinic acetylcholine receptor agonist resistant to cholinesterase",
                    "Primary Mechanism": "Stimulates smooth muscle of the bladder detrusor and gastrointestinal tract",
                    "Main Clinical Use": "Postoperative and neurogenic urinary retention and postpartum atony"
                },
                "Atropine (Brick 26)": {
                    "Receptor Target": "Competitive muscarinic acetylcholine receptor antagonist across organs",
                    "Primary Mechanism": "Blocks parasympathetic tone to raise heart rate and dry secretions",
                    "Main Clinical Use": "Symptomatic bradycardia and antidote for organophosphate poisoning"
                }
            }
        },
        {
            "slug": "cardiovascular_vasodilators",
            "title": "Cardiovascular Vasodilators and Antihypertensives Across Bricks",
            "subtitle": "Match each cardiovascular drug to its class and mechanism, hemodynamic effect, and notable adverse effect.",
            "categories": ["Class and Mechanism", "Hemodynamic Effect", "Notable Adverse Effect"],
            "data": {
                "Doxazosin (Brick 17)": {
                    "Class and Mechanism": "Alpha-1 blocker relaxing arteriolar and venous smooth muscle",
                    "Hemodynamic Effect": "Lowers peripheral vascular resistance and bladder outlet resistance",
                    "Notable Adverse Effect": "First-dose orthostatic hypotension and reflex tachycardia"
                },
                "Nitroglycerin (Brick 21)": {
                    "Class and Mechanism": "Organic nitrate donating nitric oxide to raise smooth muscle cGMP",
                    "Hemodynamic Effect": "Predominant venodilation reduces preload and myocardial oxygen demand",
                    "Notable Adverse Effect": "Throbbing headache, flushing, hypotension, and tolerance with continuous use"
                },
                "Sildenafil (Brick 22)": {
                    "Class and Mechanism": "Phosphodiesterase-5 inhibitor preventing cGMP breakdown in vasculature",
                    "Hemodynamic Effect": "Prolongs cGMP vasodilation in corpus cavernosum and pulmonary vessels",
                    "Notable Adverse Effect": "Fatal hypotension when combined with nitrates and bluish vision tint"
                },
                "Metoprolol (Brick 23)": {
                    "Class and Mechanism": "Cardioselective beta-1 blocker reducing sympathetic drive to the heart",
                    "Hemodynamic Effect": "Lowers heart rate, contractility, and cardiac output over time",
                    "Notable Adverse Effect": "Bradycardia, fatigue, and masking of hypoglycemia in diabetics"
                },
                "Amlodipine (Brick 24)": {
                    "Class and Mechanism": "Dihydropyridine calcium channel blocker acting on vascular smooth muscle",
                    "Hemodynamic Effect": "Arteriolar dilation lowers afterload with little direct cardiac effect",
                    "Notable Adverse Effect": "Peripheral edema, flushing, and reflex tachycardia from vasodilation"
                },
                "Lisinopril (Brick 31)": {
                    "Class and Mechanism": "ACE inhibitor blocking conversion of angiotensin I to angiotensin II",
                    "Hemodynamic Effect": "Reduces afterload and preload and lowers glomerular efferent tone",
                    "Notable Adverse Effect": "Dry cough, hyperkalemia, angioedema, and fetal renal toxicity"
                }
            }
        },
        {
            "slug": "analgesics_and_antiinflammatories",
            "title": "Analgesics and Anti-Inflammatories Across Bricks",
            "subtitle": "Match each analgesic or anti-inflammatory drug to its mechanism, key toxicity, and antidote or management.",
            "categories": ["Mechanism", "Key Toxicity", "Antidote or Management"],
            "data": {
                "Ibuprofen (Brick 4)": {
                    "Mechanism": "Reversible nonselective inhibitor of COX-1 and COX-2 enzymes",
                    "Key Toxicity": "Gastric ulcers, acute kidney injury, and fluid retention",
                    "Antidote or Management": "Stop the NSAID, add a proton pump inhibitor, and support renal perfusion"
                },
                "Aspirin (Brick 7)": {
                    "Mechanism": "Irreversible covalent acetylation of COX-1 and COX-2 enzymes",
                    "Key Toxicity": "Tinnitus and mixed respiratory alkalosis with metabolic acidosis in overdose",
                    "Antidote or Management": "Alkalinize urine with sodium bicarbonate and give dialysis if severe"
                },
                "Acetaminophen (Brick 11)": {
                    "Mechanism": "Central COX inhibition giving analgesia and antipyresis without anti-inflammation",
                    "Key Toxicity": "Dose-dependent hepatic necrosis from the toxic NAPQI metabolite",
                    "Antidote or Management": "N-acetylcysteine replenishes glutathione to detoxify NAPQI"
                },
                "Prednisone (Brick 13)": {
                    "Mechanism": "Corticosteroid inhibiting phospholipase A2 and broad inflammatory gene transcription",
                    "Key Toxicity": "Cushingoid features, hyperglycemia, osteoporosis, and adrenal suppression",
                    "Antidote or Management": "Taper slowly to allow recovery of the hypothalamic-pituitary-adrenal axis"
                },
                "Morphine (Brick 30)": {
                    "Mechanism": "Full mu opioid receptor agonist reducing pain transmission and perception",
                    "Key Toxicity": "Respiratory depression, miosis, and constipation with overdose",
                    "Antidote or Management": "Naloxone reverses opioid effects and supportive ventilation as needed"
                },
                "Naloxone (Brick 29)": {
                    "Mechanism": "Competitive mu opioid receptor antagonist with rapid parenteral onset",
                    "Key Toxicity": "Precipitates acute withdrawal with agitation and pain in dependent patients",
                    "Antidote or Management": "Redose because short half-life may lapse before long opioid clears"
                }
            }
        },
        {
            "slug": "toxicities_and_antidotes",
            "title": "Drug Toxicities and Antidotes Across Bricks",
            "subtitle": "Match each drug or class to its culprit mechanism, characteristic toxicity, and antidote or management.",
            "categories": ["Culprit Mechanism", "Characteristic Toxicity", "Antidote or Management"],
            "data": {
                "Aspirin (Brick 7)": {
                    "Culprit Mechanism": "Salicylate uncouples oxidative phosphorylation and stimulates the respiratory center",
                    "Characteristic Toxicity": "Tinnitus with early respiratory alkalosis then anion-gap metabolic acidosis",
                    "Antidote or Management": "Sodium bicarbonate to alkalinize urine and hemodialysis in severe cases"
                },
                "Acetaminophen (Brick 11)": {
                    "Culprit Mechanism": "Excess NAPQI metabolite depletes hepatic glutathione stores",
                    "Characteristic Toxicity": "Centrilobular hepatic necrosis with rising transaminases after a delay",
                    "Antidote or Management": "N-acetylcysteine restores glutathione and is most effective given early"
                },
                "Corticosteroids (Brick 13)": {
                    "Culprit Mechanism": "Chronic exogenous glucocorticoid suppresses endogenous cortisol production",
                    "Characteristic Toxicity": "Iatrogenic Cushing syndrome and adrenal crisis if stopped abruptly",
                    "Antidote or Management": "Gradual dose taper and stress-dose steroids during acute illness"
                },
                "Statins (Brick 15)": {
                    "Culprit Mechanism": "HMG-CoA reductase inhibition can injure skeletal myocytes",
                    "Characteristic Toxicity": "Myopathy and rhabdomyolysis with elevated creatine kinase and myoglobinuria",
                    "Antidote or Management": "Discontinue the statin, hydrate aggressively, and avoid interacting CYP inhibitors"
                },
                "Organophosphates (Brick 28)": {
                    "Culprit Mechanism": "Irreversible acetylcholinesterase inhibition floods synapses with acetylcholine",
                    "Characteristic Toxicity": "Cholinergic crisis with salivation, lacrimation, urination, defecation, and bronchospasm",
                    "Antidote or Management": "Atropine blocks muscarinic effects and pralidoxime reactivates the enzyme before aging"
                },
                "Metformin (Brick 32)": {
                    "Culprit Mechanism": "Biguanide inhibits hepatic gluconeogenesis and promotes anaerobic metabolism",
                    "Characteristic Toxicity": "Rare life-threatening lactic acidosis, especially in renal impairment",
                    "Antidote or Management": "Hold the drug, give supportive care, and use hemodialysis for severe acidosis"
                }
            }
        },
        {
            "slug": "receptor_signaling_pathways",
            "title": "Receptor Signaling and Second Messengers Across Bricks",
            "subtitle": "Match each receptor or enzyme to its type, signaling pathway, and a representative drug and effect.",
            "categories": ["Receptor or Enzyme Type", "Signaling Pathway", "Representative Drug and Effect"],
            "data": {
                "Alpha-1 Adrenergic Receptor (Brick 16)": {
                    "Receptor or Enzyme Type": "Gq-coupled G-protein receptor on vascular smooth muscle",
                    "Signaling Pathway": "Phospholipase C generates IP3 and DAG, raising intracellular calcium",
                    "Representative Drug and Effect": "Phenylephrine stimulates it to cause vasoconstriction and pressor effect"
                },
                "Beta-2 Adrenergic Receptor (Brick 20)": {
                    "Receptor or Enzyme Type": "Gs-coupled G-protein receptor on bronchial smooth muscle",
                    "Signaling Pathway": "Adenylyl cyclase raises cAMP and activates protein kinase A",
                    "Representative Drug and Effect": "Albuterol activates it to relax bronchioles and relieve asthma"
                },
                "H2 Histamine Receptor (Brick 19)": {
                    "Receptor or Enzyme Type": "Gs-coupled G-protein receptor on gastric parietal cells",
                    "Signaling Pathway": "Raises cAMP to drive proton pump acid secretion into the stomach",
                    "Representative Drug and Effect": "Famotidine blocks it to reduce gastric acid and heal ulcers"
                },
                "H1 Histamine Receptor (Brick 27)": {
                    "Receptor or Enzyme Type": "Gq-coupled G-protein receptor on endothelium and nerves",
                    "Signaling Pathway": "Phospholipase C and IP3 mediate vasodilation, edema, and itch",
                    "Representative Drug and Effect": "Diphenhydramine blocks it to relieve allergy but causes sedation"
                },
                "Nitric Oxide and Guanylyl Cyclase (Brick 21)": {
                    "Receptor or Enzyme Type": "Soluble cytoplasmic enzyme activated by nitric oxide",
                    "Signaling Pathway": "Converts GTP to cGMP, dephosphorylating myosin to relax smooth muscle",
                    "Representative Drug and Effect": "Nitroglycerin donates nitric oxide to venodilate and reduce preload"
                },
                "Phosphodiesterase-5 (Brick 22)": {
                    "Receptor or Enzyme Type": "Intracellular enzyme that degrades cGMP in smooth muscle",
                    "Signaling Pathway": "Inhibition preserves cGMP to sustain vasodilation downstream of nitric oxide",
                    "Representative Drug and Effect": "Sildenafil inhibits it to enhance erection and lower pulmonary pressure"
                },
                "GLP-1 Receptor (Brick 32)": {
                    "Receptor or Enzyme Type": "Gs-coupled G-protein receptor on pancreatic beta cells",
                    "Signaling Pathway": "Raises cAMP to promote glucose-dependent insulin release and satiety",
                    "Representative Drug and Effect": "Semaglutide activates it to lower glucose and promote weight loss"
                }
            }
        }
    ]
}
