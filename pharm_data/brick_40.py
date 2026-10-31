BRICK = {
    "brick_num": 40,
    "brick_title": "Protein Synthesis Inhibitors-2 of 2: Adverse Drug Reaction",
    "games": [
        {
            "slug": "psi_interaction_partners",
            "title": "PSI Drug Interaction Partners",
            "subtitle": "Match each antibiotic to its interacting drugs, the mechanism, and the consequence or management",
            "categories": ["Interacting Drugs", "Mechanism", "Consequence or Management"],
            "data": {
                "Linezolid": {
                    "Interacting Drugs": "SSRIs and SNRIs",
                    "Mechanism": "Reversible MAO inhibition raises serotonin levels",
                    "Consequence or Management": "Serotonin syndrome: shivering up to rigidity, fever, seizures"
                },
                "Clarithromycin": {
                    "Interacting Drugs": "Simvastatin and lovastatin; also warfarin",
                    "Mechanism": "CYP3A4 substrate and inhibitor",
                    "Consequence or Management": "Avoid the statins; use warfarin with caution"
                },
                "Tetracycline": {
                    "Interacting Drugs": "Antacids, polyvalent cations, bismuth, dairy",
                    "Mechanism": "Chelation of the drug by cations in the gut",
                    "Consequence or Management": "Give cations 1-2 h before or 4 h after the dose"
                },
                "Amikacin": {
                    "Interacting Drugs": "Amphotericin B, vancomycin, NSAIDs, contrast dye",
                    "Mechanism": "Additive toxicity to renal tubular cells",
                    "Consequence or Management": "Higher risk of acute tubular necrosis"
                },
                "Erythromycin": {
                    "Interacting Drugs": "Other agents that lengthen the QT interval",
                    "Mechanism": "Additive QT interval prolongation",
                    "Consequence or Management": "Higher arrhythmia risk; avoid the combination"
                }
            }
        },
        {
            "slug": "signature_psi_toxicities",
            "title": "Signature Toxicities of the PSIs",
            "subtitle": "Match each protein synthesis inhibitor to its signature adverse effect, other adverse effects, and key clinical note",
            "categories": ["Signature Adverse Effect", "Other Adverse Effects", "Clinical Note"],
            "data": {
                "Chloramphenicol": {
                    "Signature Adverse Effect": "Gray baby syndrome: hypotension and cyanosis",
                    "Other Adverse Effects": "Aplastic anemia, thrombocytopenia, granulocytopenia",
                    "Clinical Note": "Reserved for when alternatives are ineffective"
                },
                "Quinupristin/dalfopristin": {
                    "Signature Adverse Effect": "Arthralgia and myalgia in over 45% of patients",
                    "Other Adverse Effects": "Raised creatinine and hyperbilirubinemia in over 33%",
                    "Clinical Note": "Given IV only; can be used in pregnancy"
                },
                "Clindamycin": {
                    "Signature Adverse Effect": "C. difficile pseudomembranous colitis",
                    "Other Adverse Effects": "Diarrhea, allergic reaction, neuromuscular blockade",
                    "Clinical Note": "Oral form can be used in pregnancy"
                },
                "Macrolides": {
                    "Signature Adverse Effect": "QT prolongation with arrhythmia risk",
                    "Other Adverse Effects": "GI upset: nausea, vomiting, diarrhea",
                    "Clinical Note": "Contraindicated in cholestatic jaundice or hepatic dysfunction"
                },
                "Linezolid": {
                    "Signature Adverse Effect": "Serotonin syndrome with serotonergic antidepressants",
                    "Other Adverse Effects": "Bone marrow suppression, peripheral neuropathy",
                    "Clinical Note": "Marrow and nerve toxicity from mitochondrial PSI"
                }
            }
        },
        {
            "slug": "aminoglycoside_toxicities",
            "title": "Aminoglycoside Toxicities",
            "subtitle": "Match each aminoglycoside toxicity to its mechanism, reversibility or risk, and clinical caution",
            "categories": ["Mechanism", "Reversibility or Risk", "Clinical Caution"],
            "data": {
                "Nephrotoxicity": {
                    "Mechanism": "Accumulation in proximal tubular epithelial cells",
                    "Reversibility or Risk": "Risk rises with renal impairment and old age",
                    "Clinical Caution": "Avoid co-use with other nephrotoxins such as vancomycin"
                },
                "Cochlear toxicity": {
                    "Mechanism": "Mitochondrial ribosome inhibition kills cochlear cells",
                    "Reversibility or Risk": "Irreversible: cochlear cells cannot regenerate",
                    "Clinical Caution": "Hearing loss is permanent"
                },
                "Vestibular toxicity": {
                    "Mechanism": "Mitochondrial ribosome inhibition kills vestibular cells",
                    "Reversibility or Risk": "Sometimes reversible: these cells can regenerate",
                    "Clinical Caution": "Balance deficits may improve over time"
                },
                "Neuromuscular blockade": {
                    "Mechanism": "Antagonism of acetylcholine receptors",
                    "Reversibility or Risk": "Rare adverse effect",
                    "Clinical Caution": "Use caution in myasthenia gravis"
                },
                "Fetal harm": {
                    "Mechanism": "Toxicity to the developing fetus",
                    "Reversibility or Risk": "Limited topical use is acceptable",
                    "Clinical Caution": "Systemic use contraindicated in pregnancy"
                }
            }
        },
        {
            "slug": "tetracycline_counseling",
            "title": "Counseling a Patient on Tetracyclines",
            "subtitle": "Match each tetracycline concern to the problem it causes, its cause, and the advice to give",
            "categories": ["Problem", "Cause", "Advice"],
            "data": {
                "Dairy products": {
                    "Problem": "Drug is not absorbed and fails to work",
                    "Cause": "Calcium in milk and yogurt chelates the drug",
                    "Advice": "Avoid dairy 1 h before and 2 h after a dose"
                },
                "Antacids and polyvalent cations": {
                    "Problem": "Loss of drug effect from binding in the gut",
                    "Cause": "Ca, Mg, Fe, Al, Zn, multivitamins, bismuth subsalicylate",
                    "Advice": "Dose them 1-2 h before or 4 h after the drug"
                },
                "Sunlight": {
                    "Problem": "Photosensitivity reaction",
                    "Cause": "UV exposure while taking the drug",
                    "Advice": "Avoid excessive sunlight"
                },
                "Children under 8": {
                    "Problem": "Yellow teeth and impaired bone growth",
                    "Cause": "Deposition in calcifying teeth and bone",
                    "Advice": "Avoid, except short-course doxycycline (<21 days)"
                },
                "Pregnancy and nursing": {
                    "Problem": "Potential fetal harm",
                    "Cause": "Chelation affecting developing fetal tissue",
                    "Advice": "Contraindicated; check a pregnancy test first"
                }
            }
        }
    ]
}
