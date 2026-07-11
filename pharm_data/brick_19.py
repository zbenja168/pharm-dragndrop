BRICK = {
    "brick_num": 19,
    "brick_title": "Acid Suppression Drugs: PPIs and H2 Receptor Antagonists",
    "games": [
        {
            "slug": "signals_of_gastric_acid",
            "title": "Signals That Control Gastric Acid",
            "subtitle": "Match each substance to its parietal-cell receptor, signaling pathway, and net effect on acid",
            "categories": ["Receptor Target", "Signaling Pathway", "Net Effect on Acid"],
            "data": {
                "Acetylcholine": {
                    "Receptor Target": "M3 muscarinic receptor on parietal cells",
                    "Signaling Pathway": "Gq pathway raising intracellular calcium",
                    "Net Effect on Acid": "Stimulates H+ secretion via the proton pump"
                },
                "Histamine": {
                    "Receptor Target": "H2 receptor on parietal cells",
                    "Signaling Pathway": "Gs pathway raising cAMP and activating PKA",
                    "Net Effect on Acid": "Strongest stimulus for acid secretion"
                },
                "Gastrin": {
                    "Receptor Target": "Gastrin (CCK) receptor on parietal and ECL cells",
                    "Signaling Pathway": "Gq pathway that also drives ECL histamine release",
                    "Net Effect on Acid": "Stimulates acid directly and via released histamine"
                },
                "Somatostatin": {
                    "Receptor Target": "Somatostatin receptor on parietal cells",
                    "Signaling Pathway": "Gi pathway that lowers cAMP",
                    "Net Effect on Acid": "Inhibits gastric acid secretion"
                }
            }
        },
        {
            "slug": "meet_the_acid_suppressors",
            "title": "Meet the Acid-Suppressing Drugs",
            "subtitle": "Match each drug to its class, naming clue, and distinguishing feature",
            "categories": ["Drug Class", "Naming Clue", "Distinguishing Feature"],
            "data": {
                "Omeprazole": {
                    "Drug Class": "Proton pump inhibitor",
                    "Naming Clue": "-prazole suffix",
                    "Distinguishing Feature": "Available both by prescription and over the counter"
                },
                "Pantoprazole": {
                    "Drug Class": "Proton pump inhibitor",
                    "Naming Clue": "-prazole suffix",
                    "Distinguishing Feature": "Only PPI available IV and orally; popular in inpatients"
                },
                "Esomeprazole": {
                    "Drug Class": "Proton pump inhibitor",
                    "Naming Clue": "-prazole suffix",
                    "Distinguishing Feature": "Available both by prescription and over the counter"
                },
                "Cimetidine": {
                    "Drug Class": "H2 receptor antagonist",
                    "Naming Clue": "-tidine suffix",
                    "Distinguishing Feature": "Anti-androgenic effects and inhibits many CYP enzymes"
                },
                "Famotidine": {
                    "Drug Class": "H2 receptor antagonist",
                    "Naming Clue": "-tidine suffix",
                    "Distinguishing Feature": "Preferred H2 blocker; main side effect is headache"
                }
            }
        },
        {
            "slug": "long_term_ppi_effects",
            "title": "Long-Term PPI Adverse Effects",
            "subtitle": "Match each effect group to its examples, mechanism, and clinical note",
            "categories": ["Examples", "Underlying Mechanism", "Clinical Note"],
            "data": {
                "Short-term effects": {
                    "Examples": "Headache, nausea, vomiting, and diarrhea",
                    "Underlying Mechanism": "Common, mild reactions that resolve with brief use",
                    "Clinical Note": "PPIs are generally safe when used short-term"
                },
                "Malabsorption": {
                    "Examples": "Low Ca2+, Mg2+, Fe2+, and vitamin B12 deficiency",
                    "Underlying Mechanism": "Higher gastric pH reduces absorption of minerals",
                    "Clinical Note": "Fractures, osteoporosis, and hypomagnesemia in the elderly"
                },
                "Infection": {
                    "Examples": "Clostridioides difficile colitis and pneumonia",
                    "Underlying Mechanism": "Altered gut microbiota lets opportunists overgrow",
                    "Clinical Note": "Normal flora can become pathogenic with long-term use"
                },
                "Renal and neurologic": {
                    "Examples": "Chronic kidney disease and dementia",
                    "Underlying Mechanism": "Unclear; only a correlation with long-term use",
                    "Clinical Note": "May favor switching to an H2RA for long-term therapy"
                }
            }
        },
        {
            "slug": "acid_suppressor_interactions",
            "title": "Drug Interactions of Acid Suppressors",
            "subtitle": "Match each factor to its interaction mechanism and clinical consequence",
            "categories": ["Interaction Mechanism", "Clinical Consequence"],
            "data": {
                "Cimetidine": {
                    "Interaction Mechanism": "Inhibits multiple CYP enzymes (3A4, 1A2, 2C19, 2D6)",
                    "Clinical Consequence": "Supratherapeutic or toxic levels of other drugs"
                },
                "PPI metabolism": {
                    "Interaction Mechanism": "PPIs are substrates of CYP3A4",
                    "Clinical Consequence": "Altered metabolism of other CYP3A4 drugs"
                },
                "PPI effect on gastric pH": {
                    "Interaction Mechanism": "PPIs raise gastric pH (less acidic)",
                    "Clinical Consequence": "Decreased iron and B12 absorption leading to anemia"
                },
                "Levothyroxine": {
                    "Interaction Mechanism": "Absorption depends on an acidic stomach",
                    "Clinical Consequence": "Reduced effect when combined with a PPI"
                }
            }
        }
    ]
}
