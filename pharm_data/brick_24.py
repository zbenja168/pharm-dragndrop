BRICK = {
    "brick_num": 24,
    "brick_title": "Calcium Channel Blockers",
    "games": [
        {
            "slug": "meet_the_ccbs",
            "title": "Meet the Calcium Channel Blockers",
            "subtitle": "Match each drug to its chemical class, signature property, and characteristic adverse effect",
            "categories": ["Chemical Class", "Signature Property", "Characteristic Adverse Effect"],
            "data": {
                "Amlodipine": {
                    "Chemical Class": "Dihydropyridine (DHP)",
                    "Signature Property": "Slow absorption, prolonged and steady effect",
                    "Characteristic Adverse Effect": "Peripheral edema with little reflex tachycardia"
                },
                "Nifedipine (immediate-release)": {
                    "Chemical Class": "Dihydropyridine (DHP)",
                    "Signature Property": "Rapid absorption, short half-life (~1.8 h)",
                    "Characteristic Adverse Effect": "Reflex tachycardia, flushing, and headache"
                },
                "Verapamil": {
                    "Chemical Class": "Non-dihydropyridine (non-DHP)",
                    "Signature Property": "Strongest suppression of SA nodal firing and contractility",
                    "Characteristic Adverse Effect": "Constipation"
                },
                "Diltiazem": {
                    "Chemical Class": "Non-dihydropyridine (non-DHP)",
                    "Signature Property": "Combined vascular and nodal effects; used for rate control",
                    "Characteristic Adverse Effect": "Bradycardia; avoid in high-grade heart block"
                }
            }
        },
        {
            "slug": "tissue_actions",
            "title": "Tissue-Level Actions of CCBs",
            "subtitle": "Match each target tissue to the molecular step CCBs interrupt and the therapeutic effect",
            "categories": ["Target Tissue", "Molecular Step Interrupted", "Therapeutic Effect"],
            "data": {
                "Arteriolar smooth muscle": {
                    "Target Tissue": "Vascular (arteriolar) smooth muscle",
                    "Molecular Step Interrupted": "Ca-calmodulin activation of myosin light-chain kinase",
                    "Therapeutic Effect": "Vasodilation and lower blood pressure (antihypertensive)"
                },
                "Contractile myocardium": {
                    "Target Tissue": "Cardiac contractile muscle",
                    "Molecular Step Interrupted": "Ca binding to troponin C for actin-myosin cross-bridging",
                    "Therapeutic Effect": "Negative inotropy that lowers O2 demand (antianginal)"
                },
                "SA node": {
                    "Target Tissue": "Sinoatrial (SA) node pacemaker cells",
                    "Molecular Step Interrupted": "Ca-dependent slow depolarization and firing rate",
                    "Therapeutic Effect": "Negative chronotropy that slows heart rate"
                },
                "AV node": {
                    "Target Tissue": "Atrioventricular (AV) node conduction tissue",
                    "Molecular Step Interrupted": "Ca-dependent conduction through slow-response cells",
                    "Therapeutic Effect": "Slowed AV conduction for rate control in SVT and atrial fibrillation"
                }
            }
        },
        {
            "slug": "ccb_pharmacokinetics",
            "title": "Pharmacokinetics and Drug Interactions",
            "subtitle": "Match each pharmacokinetic feature to its mechanism and clinical consequence",
            "categories": ["PK Feature", "Mechanism / Detail", "Clinical Consequence"],
            "data": {
                "Immediate-release nifedipine": {
                    "PK Feature": "Rapid absorption, short half-life",
                    "Mechanism / Detail": "Quick onset causes a sudden drop in blood pressure",
                    "Clinical Consequence": "Reflex sympathetic activation with tachycardia and flushing"
                },
                "Amlodipine": {
                    "PK Feature": "Slow absorption, prolonged effect",
                    "Mechanism / Detail": "Steady-state reached over roughly 7-10 days of dosing",
                    "Clinical Consequence": "Body adapts, so there is less reflex tachycardia"
                },
                "CYP3A4 metabolism": {
                    "PK Feature": "Extensive first-pass metabolism (all CCBs are CYP3A4 substrates)",
                    "Mechanism / Detail": "Levels rise with strong CYP3A4 inhibitors",
                    "Clinical Consequence": "Macrolides, antiretrovirals, and grapefruit juice raise CCB levels"
                },
                "Verapamil as CYP3A4 inhibitor": {
                    "PK Feature": "Verapamil strongly inhibits CYP3A4",
                    "Mechanism / Detail": "Impairs clearance of other CYP3A4 substrates",
                    "Clinical Consequence": "Raises statin levels (simvastatin, atorvastatin) and toxicity risk"
                }
            }
        },
        {
            "slug": "ccb_adverse_effects",
            "title": "Adverse Effects and Contraindications",
            "subtitle": "Match each adverse effect to its mechanism and the drug(s) most associated with it",
            "categories": ["Adverse Effect / Issue", "Underlying Mechanism", "Most Associated Drug(s)"],
            "data": {
                "Peripheral (pedal) edema": {
                    "Adverse Effect / Issue": "Peripheral (pedal) edema",
                    "Underlying Mechanism": "Precapillary arteriolar dilation raises hydrostatic pressure while venules stay constricted",
                    "Most Associated Drug(s)": "Dihydropyridines (amlodipine, nifedipine)"
                },
                "Reflex tachycardia": {
                    "Adverse Effect / Issue": "Reflex tachycardia",
                    "Underlying Mechanism": "Rapid vasodilation triggers a sympathetic reflex",
                    "Most Associated Drug(s)": "Immediate-release nifedipine"
                },
                "Constipation": {
                    "Adverse Effect / Issue": "Constipation",
                    "Underlying Mechanism": "Calcium blockade relaxes gastrointestinal smooth muscle",
                    "Most Associated Drug(s)": "Verapamil"
                },
                "Worsened heart block": {
                    "Adverse Effect / Issue": "Bradycardia and worsened heart block",
                    "Underlying Mechanism": "Excess suppression of SA and AV nodal activity",
                    "Most Associated Drug(s)": "Non-DHPs (verapamil, diltiazem), contraindicated in 2nd/3rd degree block"
                }
            }
        }
    ]
}
