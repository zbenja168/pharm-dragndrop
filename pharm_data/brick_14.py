BRICK = {
    "brick_num": 14,
    "brick_title": "Autonomic Nervous System - Vasopressors and Inotropes",
    "games": [
        {
            "slug": "vasopressor_inotrope_profiles",
            "title": "Vasopressors and Inotropes - Drug Profiles",
            "subtitle": "Match each sympathomimetic agent to its receptor activity, hemodynamic effect, and clinical class",
            "categories": ["Receptor Activity", "Hemodynamic Effect", "Clinical Classification"],
            "data": {
                "Epinephrine": {
                    "Receptor Activity": "Equal affinity for alpha and beta receptors",
                    "Hemodynamic Effect": "Raises systolic BP, cardiac output, and bronchodilation",
                    "Clinical Classification": "Vasopressor; cornerstone ACLS drug in cardiac arrest"
                },
                "Norepinephrine": {
                    "Receptor Activity": "Alpha-1 greater than alpha-2, non-selective for beta",
                    "Hemodynamic Effect": "Constricts all vascular beds, raises systolic and diastolic BP and SVR",
                    "Clinical Classification": "Vasopressor for hemodynamically unstable patients"
                },
                "Dopamine": {
                    "Receptor Activity": "Beta-1 plus D1/D2 dopaminergic (alpha-1 at higher doses)",
                    "Hemodynamic Effect": "Increases contractility with renal vascular vasodilation",
                    "Clinical Classification": "Vasopressor with dopaminergic renal effects"
                },
                "Dobutamine": {
                    "Receptor Activity": "Beta-1 selective (higher affinity for beta-1 than beta-2)",
                    "Hemodynamic Effect": "Raises contractility, heart rate, stroke volume and cardiac output",
                    "Clinical Classification": "Positive inotropic agent (inotrope)"
                },
                "Isoproterenol": {
                    "Receptor Activity": "Potent activator of both beta-1 and beta-2 (beta-1 equals beta-2)",
                    "Hemodynamic Effect": "Increases heart rate and contractility with bronchodilation",
                    "Clinical Classification": "Non-selective beta agonist"
                }
            }
        },
        {
            "slug": "autonomic_receptors",
            "title": "Autonomic Receptors and Their Signaling",
            "subtitle": "Match each receptor to its G-protein coupling, second messenger change, and representative effect",
            "categories": ["G-Protein Coupling", "Second Messenger Change", "Representative Effect"],
            "data": {
                "Alpha-1": {
                    "G-Protein Coupling": "Gq",
                    "Second Messenger Change": "Increased IP3, DAG and intracellular Ca2+",
                    "Representative Effect": "Vasoconstriction that raises blood pressure"
                },
                "Beta-1": {
                    "G-Protein Coupling": "Gs",
                    "Second Messenger Change": "Increased cAMP",
                    "Representative Effect": "Increased heart rate and cardiac contractility"
                },
                "Beta-2": {
                    "G-Protein Coupling": "Gs",
                    "Second Messenger Change": "Increased cAMP",
                    "Representative Effect": "Bronchodilation (relaxes bronchial smooth muscle)"
                },
                "M2 (muscarinic)": {
                    "G-Protein Coupling": "Gi",
                    "Second Messenger Change": "Decreased cAMP",
                    "Representative Effect": "Decreased heart rate"
                },
                "M3 (muscarinic)": {
                    "G-Protein Coupling": "Gq",
                    "Second Messenger Change": "Increased IP3, DAG and intracellular Ca2+",
                    "Representative Effect": "Bronchial and smooth muscle contraction"
                }
            }
        },
        {
            "slug": "gpcr_signaling_pathways",
            "title": "G-Protein and Receptor Signaling Pathways",
            "subtitle": "Match each signaling class to its action on the effector, second messenger change, and example receptors",
            "categories": ["Action on Effector", "Second Messenger Change", "Example Receptors"],
            "data": {
                "Gs pathway": {
                    "Action on Effector": "Stimulates adenylyl cyclase (activates protein kinase A)",
                    "Second Messenger Change": "Increased cAMP",
                    "Example Receptors": "Beta-1, beta-2, beta-3 adrenergic"
                },
                "Gi pathway": {
                    "Action on Effector": "Inhibits adenylyl cyclase",
                    "Second Messenger Change": "Decreased cAMP",
                    "Example Receptors": "Alpha-2, M2 and M4 muscarinic"
                },
                "Gq pathway": {
                    "Action on Effector": "Activates phospholipase C (splits PIP2 into IP3 and DAG)",
                    "Second Messenger Change": "Increased intracellular Ca2+",
                    "Example Receptors": "Alpha-1, M1, M3 and M5 muscarinic"
                },
                "Nicotinic channel": {
                    "Action on Effector": "Ligand-gated cation channel opened directly by ACh",
                    "Second Messenger Change": "Direct depolarization (no second messenger)",
                    "Example Receptors": "Nicotinic muscle (nM) and neuronal (nN)"
                }
            }
        },
        {
            "slug": "organ_autonomic_effects",
            "title": "Organ Effects of Autonomic Activation",
            "subtitle": "Match each organ to its sympathetic effect, parasympathetic effect, and key sympathetic receptor",
            "categories": ["Sympathetic Effect", "Parasympathetic Effect", "Key Sympathetic Receptor"],
            "data": {
                "Heart": {
                    "Sympathetic Effect": "Increased heart rate and contractility",
                    "Parasympathetic Effect": "Decreased heart rate",
                    "Key Sympathetic Receptor": "Beta-1 (Gs)"
                },
                "Bronchial smooth muscle": {
                    "Sympathetic Effect": "Bronchodilation",
                    "Parasympathetic Effect": "Bronchoconstriction (increased bronchial contraction)",
                    "Key Sympathetic Receptor": "Beta-2 (Gs)"
                },
                "Iris / pupil": {
                    "Sympathetic Effect": "Pupillary dilation (mydriasis)",
                    "Parasympathetic Effect": "Pupillary constriction (miosis, pin-point pupils)",
                    "Key Sympathetic Receptor": "Alpha-1 (Gq)"
                },
                "Stomach (gastric secretion)": {
                    "Sympathetic Effect": "Decreased gastric secretions",
                    "Parasympathetic Effect": "Increased gastric acid secretion",
                    "Key Sympathetic Receptor": "Alpha / beta adrenergic"
                }
            }
        }
    ]
}
