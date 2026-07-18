BRICK = {
    "brick_num": 18,
    "brick_title": "Autonomic Nervous System - Vasopressors and Inotropes",
    "games": [
        {
            "slug": "sympathomimetic_agents",
            "title": "Vasopressors and Inotropes",
            "subtitle": "Match each sympathomimetic agent to its main receptor targets, hemodynamic effect, and clinical class",
            "categories": ["Main Receptor Targets", "Key Hemodynamic Effect", "Clinical Classification"],
            "data": {
                "Epinephrine": {
                    "Main Receptor Targets": "Equal affinity for alpha and beta receptors",
                    "Key Hemodynamic Effect": "Raises systolic BP, contractility, heart rate; bronchodilation",
                    "Clinical Classification": "Vasopressor; cornerstone ACLS cardiac-arrest drug"
                },
                "Norepinephrine": {
                    "Main Receptor Targets": "Alpha1 much greater than alpha2, non-selective beta",
                    "Key Hemodynamic Effect": "Constricts all vascular beds; raises systolic and diastolic BP and SVR",
                    "Clinical Classification": "Vasopressor for hemodynamic instability"
                },
                "Dopamine": {
                    "Main Receptor Targets": "Beta1 at therapeutic dose, alpha1 at higher dose, renal D1/D2",
                    "Key Hemodynamic Effect": "Increases contractility; renal vascular vasodilation",
                    "Clinical Classification": "Vasopressor with dopaminergic renal effect"
                },
                "Dobutamine": {
                    "Main Receptor Targets": "Beta1 much greater than beta2 selectivity",
                    "Key Hemodynamic Effect": "Increases contractility, stroke volume, and cardiac output",
                    "Clinical Classification": "Positive inotrope"
                },
                "Isoproterenol": {
                    "Main Receptor Targets": "Potent non-selective beta1 equals beta2",
                    "Key Hemodynamic Effect": "Raises heart rate and contractility; bronchodilation",
                    "Clinical Classification": "Non-selective beta agonist"
                }
            }
        },
        {
            "slug": "receptor_gpcr_coupling",
            "title": "Autonomic Receptor GPCR Coupling",
            "subtitle": "Match each autonomic receptor to its G-protein class, second-messenger action, and a representative tissue effect",
            "categories": ["G-Protein Class", "Second-Messenger Action", "Representative Tissue Effect"],
            "data": {
                "Alpha1": {
                    "G-Protein Class": "Gq",
                    "Second-Messenger Action": "PLC raises IP3/DAG and intracellular calcium",
                    "Representative Tissue Effect": "Vascular smooth muscle vasoconstriction"
                },
                "Alpha2": {
                    "G-Protein Class": "Gi",
                    "Second-Messenger Action": "Inhibits adenylyl cyclase, lowering cAMP",
                    "Representative Tissue Effect": "Reduced presynaptic norepinephrine release"
                },
                "Beta1": {
                    "G-Protein Class": "Gs",
                    "Second-Messenger Action": "Stimulates adenylyl cyclase, raising cAMP",
                    "Representative Tissue Effect": "Increased cardiac contractility and heart rate"
                },
                "Beta2": {
                    "G-Protein Class": "Gs",
                    "Second-Messenger Action": "Raises cAMP via adenylyl cyclase",
                    "Representative Tissue Effect": "Bronchial smooth muscle relaxation (bronchodilation)"
                },
                "M2 muscarinic": {
                    "G-Protein Class": "Gi",
                    "Second-Messenger Action": "Inhibits adenylyl cyclase, lowering cAMP",
                    "Representative Tissue Effect": "Slows heart rate in the myocardium"
                },
                "M3 muscarinic": {
                    "G-Protein Class": "Gq",
                    "Second-Messenger Action": "Activates PLC and calcium signaling",
                    "Representative Tissue Effect": "Bronchoconstriction and glandular secretion"
                }
            }
        },
        {
            "slug": "gpcr_signaling_pathways",
            "title": "Autonomic Signaling Pathways",
            "subtitle": "Match each signaling pathway to its coupled receptors, mechanism, and net second-messenger outcome",
            "categories": ["Coupled Receptors", "Signaling Mechanism", "Net Outcome"],
            "data": {
                "Gs pathway": {
                    "Coupled Receptors": "All beta receptors (beta1, beta2, beta3)",
                    "Signaling Mechanism": "Stimulates adenylyl cyclase and protein kinase A",
                    "Net Outcome": "Increased cAMP driving muscle contraction and secretion"
                },
                "Gi pathway": {
                    "Coupled Receptors": "Alpha2, M2, and M4 receptors",
                    "Signaling Mechanism": "Inhibits adenylyl cyclase (opposite of Gs)",
                    "Net Outcome": "Decreased cAMP production"
                },
                "Gq pathway": {
                    "Coupled Receptors": "All alpha1, M1, M3, and M5 receptors",
                    "Signaling Mechanism": "Activates phospholipase C to make IP3 and DAG",
                    "Net Outcome": "Calcium release and calcium-dependent signaling"
                },
                "Nicotinic receptor": {
                    "Coupled Receptors": "Muscle (nM) and neuronal (nN) subtypes",
                    "Signaling Mechanism": "Ligand-gated ion channel opened by acetylcholine",
                    "Net Outcome": "Cation influx and membrane depolarization"
                }
            }
        },
        {
            "slug": "receptor_tissue_effects",
            "title": "Receptor Tissue Effects and Agents",
            "subtitle": "Match each adrenergic or dopaminergic receptor to its primary tissue, activation effect, and a representative agent",
            "categories": ["Primary Tissue / Location", "Effect of Activation", "Representative Agent"],
            "data": {
                "Alpha1 receptor": {
                    "Primary Tissue / Location": "Vascular smooth muscle beds",
                    "Effect of Activation": "Vasoconstriction that raises systolic blood pressure",
                    "Representative Agent": "Norepinephrine"
                },
                "Beta1 receptor": {
                    "Primary Tissue / Location": "Heart (myocardium and SA node)",
                    "Effect of Activation": "Increased contractility and heart rate",
                    "Representative Agent": "Dobutamine"
                },
                "Beta2 receptor": {
                    "Primary Tissue / Location": "Bronchial and skeletal-muscle vasculature",
                    "Effect of Activation": "Bronchodilation and vasodilation",
                    "Representative Agent": "Isoproterenol"
                },
                "Dopaminergic D1/D2": {
                    "Primary Tissue / Location": "Renal vascular beds",
                    "Effect of Activation": "Vasodilation of renal vessels",
                    "Representative Agent": "Dopamine"
                }
            }
        }
    ]
}
