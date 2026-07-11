BRICK = {
    "brick_num": 17,
    "brick_title": "α1-Adrenergic Blockers",
    "games": [
        {
            "slug": "classify_alpha_blockers",
            "title": "Classify the α-Blockers",
            "subtitle": "Match each drug to its receptor target, primary clinical use, and signature feature",
            "categories": ["Receptor Target", "Primary Clinical Use", "Signature Feature"],
            "data": {
                "Tamsulosin": {
                    "Receptor Target": "α1A-selective (uroselective) blocker",
                    "Primary Clinical Use": "Benign prostatic hyperplasia",
                    "Signature Feature": "Highest risk of intraoperative floppy iris syndrome"
                },
                "Alfuzosin": {
                    "Receptor Target": "Nonselective α1-blocker used uroselectively",
                    "Primary Clinical Use": "Benign prostatic hyperplasia",
                    "Signature Feature": "'-osin' suffix like all α1-blockers"
                },
                "Prazosin": {
                    "Receptor Target": "Nonselective α1-blocker, rapid onset",
                    "Primary Clinical Use": "Hypertension (not first-line)",
                    "Signature Feature": "First-dose orthostatic hypotension"
                },
                "Doxazosin": {
                    "Receptor Target": "Nonselective α1-blocker, long-acting",
                    "Primary Clinical Use": "Hypertension, also approved for BPH",
                    "Signature Feature": "Non-uroselective α1-blocker"
                },
                "Phenoxybenzamine": {
                    "Receptor Target": "Nonselective α1 and α2 antagonist",
                    "Primary Clinical Use": "Pheochromocytoma before surgery",
                    "Signature Feature": "Irreversible, long and pronounced blockade"
                },
                "Phentolamine": {
                    "Receptor Target": "Nonselective α1 and α2 antagonist",
                    "Primary Clinical Use": "Pheochromocytoma, short-term BP control",
                    "Signature Feature": "Reversible antagonist"
                }
            }
        },
        {
            "slug": "alpha1_receptor_sites",
            "title": "α1-Receptor Locations & Effects",
            "subtitle": "Match each α1-receptor location to the effect of activation and the result of blockade",
            "categories": ["Effect of α1 Activation", "Result of α1-Blockade"],
            "data": {
                "Prostate and bladder neck": {
                    "Effect of α1 Activation": "Smooth muscle contraction, urethral obstruction",
                    "Result of α1-Blockade": "Relaxation, dilated urethra, better urine flow"
                },
                "Arteriolar smooth muscle": {
                    "Effect of α1 Activation": "Vasoconstriction, raised vascular resistance",
                    "Result of α1-Blockade": "Vasodilation, lower blood pressure"
                },
                "Dilator pupillae (radial iris) muscle": {
                    "Effect of α1 Activation": "Pupil dilation (mydriasis)",
                    "Result of α1-Blockade": "Iris atrophy, floppy iris in cataract surgery"
                },
                "GI and urinary sphincters": {
                    "Effect of α1 Activation": "Sphincter contraction",
                    "Result of α1-Blockade": "Sphincter relaxation"
                },
                "Vascular tone / baroreflex": {
                    "Effect of α1 Activation": "Sympathetic outflow maintains standing BP",
                    "Result of α1-Blockade": "Impaired baroreflex, orthostatic hypotension"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "Adverse Effects of α1-Blockers",
            "subtitle": "Match each adverse effect to its mechanism and its key drug or setting",
            "categories": ["Underlying Mechanism", "Key Drug / Setting Association"],
            "data": {
                "Orthostatic hypotension": {
                    "Underlying Mechanism": "Vasodilation; baroreflex can't raise sympathetic outflow",
                    "Key Drug / Setting Association": "Highest with prazosin (first-dose); falls in elderly"
                },
                "Intraoperative floppy iris syndrome": {
                    "Underlying Mechanism": "Iris dilator muscle inhibition and atrophy",
                    "Key Drug / Setting Association": "Tamsulosin, during cataract surgery"
                },
                "Retrograde ejaculation": {
                    "Underlying Mechanism": "Bladder relaxation, semen propelled into bladder",
                    "Key Drug / Setting Association": "Tamsulosin and silodosin"
                },
                "Priapism / prolonged erection": {
                    "Underlying Mechanism": "Excess penile smooth muscle relaxation",
                    "Key Drug / Setting Association": "Nonselective α1-blockers"
                },
                "Dangerous hypotension": {
                    "Underlying Mechanism": "Additive vasodilation with other agents",
                    "Key Drug / Setting Association": "With PDE-5 inhibitors (sildenafil)"
                }
            }
        },
        {
            "slug": "pheochromocytoma_pharm",
            "title": "Pheochromocytoma Pharmacology",
            "subtitle": "Match each agent or step to its role and key property in pheochromocytoma management",
            "categories": ["Role in Management", "Key Property"],
            "data": {
                "Phenoxybenzamine": {
                    "Role in Management": "Initial blockade before surgery; long-term if inoperable",
                    "Key Property": "Irreversible nonselective α-antagonist"
                },
                "Phentolamine": {
                    "Role in Management": "Short-term control of hypertension",
                    "Key Property": "Reversible nonselective α-antagonist"
                },
                "α-Blockade (given first)": {
                    "Role in Management": "Controls catecholamine-driven vasoconstriction",
                    "Key Property": "Must precede beta-blockade in the regimen"
                },
                "β-Blockade (given second)": {
                    "Role in Management": "Controls tachycardia after α-blockade",
                    "Key Property": "β-first risks unopposed α vasoconstriction crisis"
                },
                "Adrenal medulla tumor": {
                    "Role in Management": "Source of excess endogenous catecholamines",
                    "Key Property": "Presents with hypertensive crisis, flushing, tachycardia"
                }
            }
        }
    ]
}
