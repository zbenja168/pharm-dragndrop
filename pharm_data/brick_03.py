BRICK = {
    "brick_num": 3,
    "brick_title": "Pharmacokinetics: pH and pKa",
    "games": [
        {
            "slug": "ion_environments",
            "title": "Drug Ionization Across pH Environments",
            "subtitle": "Match each drug-in-environment scenario to its predominant form, its charge, and whether it crosses the membrane",
            "categories": ["Predominant Form", "Charge", "Membrane Crossing"],
            "data": {
                "Weak acid in acidic environment (pH < pKa)": {
                    "Predominant Form": "HA, the unionized form",
                    "Charge": "Neutral (uncharged)",
                    "Membrane Crossing": "Crosses the lipid bilayer and is absorbed"
                },
                "Weak acid in alkaline environment (pH > pKa)": {
                    "Predominant Form": "A-, the ionized form",
                    "Charge": "Negatively charged",
                    "Membrane Crossing": "Trapped in solution; poorly absorbed"
                },
                "Weak base in acidic environment (pH < pKa)": {
                    "Predominant Form": "BH+, the ionized form",
                    "Charge": "Positively charged",
                    "Membrane Crossing": "Trapped in solution; poorly absorbed"
                },
                "Weak base in alkaline environment (pH > pKa)": {
                    "Predominant Form": "B, the unionized form",
                    "Charge": "Neutral (uncharged)",
                    "Membrane Crossing": "Crosses the lipid bilayer and is absorbed"
                }
            }
        },
        {
            "slug": "gi_absorption_sites",
            "title": "Absorption Sites Along the GI Tract",
            "subtitle": "Match each region of the gut to its luminal pH, its absorption role, and the key feature that explains it",
            "categories": ["Luminal pH", "Absorption Role", "Key Structural / Chemical Feature"],
            "data": {
                "Proximal duodenum": {
                    "Luminal pH": "Relatively acidic (near the stomach)",
                    "Absorption Role": "Best site for weakly acidic drugs",
                    "Key Structural / Chemical Feature": "Acidity keeps weak acids unionized so they cross"
                },
                "Distal ileum": {
                    "Luminal pH": "Alkaline",
                    "Absorption Role": "Best site for weakly basic drugs",
                    "Key Structural / Chemical Feature": "Alkalinity keeps weak bases unionized so they cross"
                },
                "Stomach": {
                    "Luminal pH": "Strongly acidic",
                    "Absorption Role": "Poor site for drug absorption overall",
                    "Key Structural / Chemical Feature": "Thick mucus layer and limited surface area"
                },
                "Small intestine (overall)": {
                    "Luminal pH": "Mildly alkaline lumen",
                    "Absorption Role": "Primary site of drug absorption",
                    "Key Structural / Chemical Feature": "Villi and microvilli give a large surface area"
                }
            }
        },
        {
            "slug": "ionization_terms",
            "title": "Key Terms in Drug Ionization",
            "subtitle": "Match each term to its meaning, its consequence for membrane crossing, and its associated property",
            "categories": ["Meaning", "Membrane Consequence", "Associated Property"],
            "data": {
                "pKa": {
                    "Meaning": "pH at which 50% is ionized and 50% is unionized",
                    "Membrane Consequence": "Predicts how readily a drug ionizes at a given pH",
                    "Associated Property": "Compared against the local surrounding pH"
                },
                "Ionized form": {
                    "Meaning": "Charged species (A- or BH+)",
                    "Membrane Consequence": "Cannot cross the lipid bilayer easily",
                    "Associated Property": "Hydrophilic and polar"
                },
                "Unionized form": {
                    "Meaning": "Neutral species (HA or B)",
                    "Membrane Consequence": "Crosses the lipid bilayer easily",
                    "Associated Property": "Lipophilic and nonpolar"
                },
                "Low pH (acidic solution)": {
                    "Meaning": "High H+ concentration",
                    "Membrane Consequence": "Weak acids stay unionized and are absorbed",
                    "Associated Property": "Weak bases gain H+ and become ionized"
                },
                "High pH (alkaline solution)": {
                    "Meaning": "Low H+ concentration",
                    "Membrane Consequence": "Weak acids give up H+ and are not absorbed",
                    "Associated Property": "Weak bases lose H+ and become unionized"
                }
            }
        },
        {
            "slug": "methotrexate_case",
            "title": "Case: Alkalinizing Urine for Methotrexate",
            "subtitle": "Match each factor in the chemotherapy case to what it is, its effect on charge/pH, and the clinical result",
            "categories": ["What It Is", "Effect on pH / Charge", "Clinical Result"],
            "data": {
                "Methotrexate": {
                    "What It Is": "Weakly acidic chemotherapy drug",
                    "Effect on pH / Charge": "Becomes ionized (charged) in alkaline urine",
                    "Clinical Result": "Rapidly excreted, reducing toxicity"
                },
                "Sodium bicarbonate": {
                    "What It Is": "A base (alkaline in nature)",
                    "Effect on pH / Charge": "Raises urine pH above the drug's pKa",
                    "Clinical Result": "Drives methotrexate toward its ionized form"
                },
                "Ionized methotrexate": {
                    "What It Is": "Charged, water-soluble form of the drug",
                    "Effect on pH / Charge": "Hydrophilic; stays dissolved in water",
                    "Clinical Result": "Not reabsorbed, so the kidney clears it quickly"
                },
                "Acidic (untreated) urine": {
                    "What It Is": "Low urine pH with high H+",
                    "Effect on pH / Charge": "Keeps methotrexate more unionized",
                    "Clinical Result": "Greater reabsorption and risk of adverse effects"
                }
            }
        }
    ]
}
