BRICK = {
    "brick_num": 5,
    "brick_title": "Pharmacodynamics 1: Receptor Agonists and Antagonists",
    "games": [
        {
            "slug": "dose_response_parameters",
            "title": "Dose-Response Parameters",
            "subtitle": "Match each parameter to its definition, where it is read on the curve, and what a higher value means",
            "categories": ["Definition", "Where It Is Read", "A Higher Value Means"],
            "data": {
                "Emax": {
                    "Definition": "the maximum effect a drug can produce",
                    "Where It Is Read": "the plateau (top) of the dose-response curve",
                    "A Higher Value Means": "a greater maximal response, i.e. more efficacy"
                },
                "EC50": {
                    "Definition": "concentration that produces 50% of the maximal effect",
                    "Where It Is Read": "the midpoint along the drug-concentration (x) axis",
                    "A Higher Value Means": "lower potency, since more drug is needed"
                },
                "Efficacy": {
                    "Definition": "the maximal response a drug is capable of producing",
                    "Where It Is Read": "compared by the height of the Emax plateau",
                    "A Higher Value Means": "a taller curve reaching a higher maximal effect"
                },
                "Potency": {
                    "Definition": "amount of drug needed to reach an established effect",
                    "Where It Is Read": "determined from the EC50 of the curve",
                    "A Higher Value Means": "the curve is shifted left, needing less drug"
                },
                "Affinity": {
                    "Definition": "extent or tightness with which a drug binds its receptor",
                    "Where It Is Read": "inversely related to Kd (affinity = 1/Kd)",
                    "A Higher Value Means": "more receptors occupied, lowering EC50 and raising potency"
                }
            }
        },
        {
            "slug": "drugs_in_the_brick",
            "title": "Drugs in the Brick",
            "subtitle": "Match each drug to its class, its mechanism or selectivity, and its clinical use",
            "categories": ["Class", "Mechanism or Selectivity", "Clinical Use"],
            "data": {
                "Albuterol": {
                    "Class": "beta-2 receptor agonist",
                    "Mechanism or Selectivity": "activates beta-2 receptors in the lungs (Kd ~100 nM)",
                    "Clinical Use": "bronchodilation for asthma via a rescue inhaler"
                },
                "Propranolol": {
                    "Class": "non-selective beta-blocker",
                    "Mechanism or Selectivity": "blocks both beta-1 and beta-2 receptors",
                    "Clinical Use": "limits increases in heart rate in cardiovascular disease"
                },
                "Metoprolol": {
                    "Class": "selective beta-1 blocker",
                    "Mechanism or Selectivity": "blocks beta-1 receptors while sparing beta-2",
                    "Clinical Use": "controls an elevated heart rate or tachycardia"
                },
                "Lisinopril": {
                    "Class": "antihypertensive medication",
                    "Mechanism or Selectivity": "lowers blood pressure",
                    "Clinical Use": "treatment of hypertension"
                },
                "Aspirin": {
                    "Class": "antiplatelet agent",
                    "Mechanism or Selectivity": "reduces clotting but increases bleeding risk",
                    "Clinical Use": "held about 7 days before surgery to limit bleeding"
                }
            }
        },
        {
            "slug": "receptors_and_drug_action",
            "title": "Receptors, Ligands, and Drug Action",
            "subtitle": "Match each term to its definition, its role in signaling, and a matching example or type",
            "categories": ["Definition", "Role in Signaling", "Example or Type"],
            "data": {
                "Receptor": {
                    "Definition": "cell component, usually a protein, that a drug binds",
                    "Role in Signaling": "recognizes a signal and translates it into a cellular event",
                    "Example or Type": "GPCR, tyrosine kinase, or nuclear receptor"
                },
                "Ligand": {
                    "Definition": "a molecule that binds to a receptor",
                    "Role in Signaling": "can either activate or inhibit the receptor",
                    "Example or Type": "may be endogenous or exogenous to the body"
                },
                "Agonist": {
                    "Definition": "binds a receptor and activates or induces it",
                    "Role in Signaling": "turns on the associated cellular action",
                    "Example or Type": "albuterol at the beta-2 receptor"
                },
                "Antagonist": {
                    "Definition": "blocks a receptor's function",
                    "Role in Signaling": "binds or competes for binding, giving no effect",
                    "Example or Type": "beta-blockers such as propranolol"
                },
                "G-protein-coupled receptor": {
                    "Definition": "a cell-membrane-bound receptor type",
                    "Role in Signaling": "links a bound signal to G-protein activity",
                    "Example or Type": "one of several membrane receptor classes"
                }
            }
        },
        {
            "slug": "selectivity_and_affinity",
            "title": "Selectivity, Specificity, and Affinity",
            "subtitle": "Match each concept to its definition, its key point, and a brick example or formula",
            "categories": ["Definition", "Key Point", "Example or Formula"],
            "data": {
                "Specificity": {
                    "Definition": "having only one effect across all biological systems",
                    "Key Point": "the strict property, rarely achieved by real drugs",
                    "Example or Formula": "the vast majority of drugs are NOT specific"
                },
                "Selectivity": {
                    "Definition": "one main effect at an appropriately high concentration",
                    "Key Point": "most drugs are selective rather than specific",
                    "Example or Formula": "metoprolol acts as a selective beta-1 blocker"
                },
                "Affinity": {
                    "Definition": "extent or fraction to which a drug binds its receptor",
                    "Key Point": "one of the factors that determines potency",
                    "Example or Formula": "albuterol has a Kd of ~100 nM for the beta-2 receptor"
                },
                "Kd (dissociation constant)": {
                    "Definition": "value reflecting the strength of drug-receptor binding",
                    "Key Point": "a higher Kd means weaker binding and lower affinity",
                    "Example or Formula": "affinity is inversely proportional to Kd (1/Kd)"
                }
            }
        }
    ]
}
