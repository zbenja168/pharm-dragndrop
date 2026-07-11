BRICK = {
    "brick_num": 8,
    "brick_title": "Pharmacokinetics-2: Volume of Distribution and Elimination Kinetics",
    "games": [
        {
            "slug": "pk_parameters",
            "title": "Pharmacokinetic Parameters",
            "subtitle": "Match each parameter to its definition, formula, and units",
            "categories": ["Definition", "Formula", "Units"],
            "data": {
                "Volume of Distribution (Vd)": {
                    "Definition": "Theoretical volume of blood needed to hold the drug in the body",
                    "Formula": "Dose administered divided by peak plasma concentration (Cmax)",
                    "Units": "Liters, or L/kg by weight"
                },
                "Clearance (CL)": {
                    "Definition": "Volume of blood completely cleared of drug per unit time",
                    "Formula": "Dose divided by the area under the curve (AUC)",
                    "Units": "mL/h or L/hr (volume per time)"
                },
                "Half-life (t1/2)": {
                    "Definition": "Time it takes to reduce the drug concentration by half",
                    "Formula": "(0.693 x Vd) divided by clearance",
                    "Units": "Hours (a measure of time)"
                },
                "Elimination rate constant (kel)": {
                    "Definition": "Fraction of drug eliminated per unit time",
                    "Formula": "0.693 divided by the half-life",
                    "Units": "Reciprocal time, per hour (h^-1)"
                },
                "Steady-state concentration (Css)": {
                    "Definition": "Concentration when the rate of drug in equals rate of drug out",
                    "Formula": "Dosing rate divided by clearance",
                    "Units": "Mass per volume, e.g. mg/mL"
                }
            }
        },
        {
            "slug": "vd_classes",
            "title": "Volume of Distribution Classes",
            "subtitle": "Match each Vd range to its compartment and molecule type",
            "categories": ["Approximate Vd", "Distribution Compartment", "Molecule Characteristics"],
            "data": {
                "Low Vd": {
                    "Approximate Vd": "Vd less than about 4 L (near blood volume, 4.5-5 L)",
                    "Distribution Compartment": "Intravascular: confined to plasma",
                    "Molecule Characteristics": "Large or charged molecules, plasma-protein bound"
                },
                "Intermediate Vd": {
                    "Approximate Vd": "Vd between about 4 and 7 L",
                    "Distribution Compartment": "Extracellular fluid: plasma plus interstitial fluid",
                    "Molecule Characteristics": "Small hydrophilic molecules"
                },
                "High Vd": {
                    "Approximate Vd": "Vd greater than about 40 L",
                    "Distribution Compartment": "Everywhere: all tissues, including fat",
                    "Molecule Characteristics": "Small lipophilic molecules"
                },
                "Amiodarone / chloroquine": {
                    "Approximate Vd": "Very large Vd (hundreds of liters)",
                    "Distribution Compartment": "Sequestered in tissue such as adipose or bone",
                    "Molecule Characteristics": "Lipophilic drugs that accumulate in tissue"
                }
            }
        },
        {
            "slug": "physiologic_factors",
            "title": "Physiologic Factors Affecting Vd & Elimination",
            "subtitle": "Match each patient state to its effect and dosing implication",
            "categories": ["Effect on Vd", "Effect on Concentration / Elimination", "Clinical Implication"],
            "data": {
                "Neonate": {
                    "Effect on Vd": "Increased Vd for hydrophilic (water-soluble) drugs",
                    "Effect on Concentration / Elimination": "Drug diluted in extra body water, lowering plasma level",
                    "Clinical Implication": "May need a higher dose to reach the target plasma concentration"
                },
                "Pregnancy": {
                    "Effect on Vd": "Raises the volume of distribution of most drugs",
                    "Effect on Concentration / Elimination": "Lowers the peak serum concentration (Cmax)",
                    "Clinical Implication": "Monitor drug levels and adjust dose as needed"
                },
                "Older adult": {
                    "Effect on Vd": "Larger Vd for lipophilic drugs, smaller for hydrophilic drugs",
                    "Effect on Concentration / Elimination": "Reduced organ blood flow slows elimination",
                    "Clinical Implication": "Use Beers criteria; avoid or reduce dose of certain drugs"
                },
                "Heart failure": {
                    "Effect on Vd": "Reduced Vd because drug cannot distribute and stays in plasma",
                    "Effect on Concentration / Elimination": "Raises Cmax and reduces elimination",
                    "Clinical Implication": "Reduce drug dosage in severe heart failure"
                }
            }
        },
        {
            "slug": "steady_state",
            "title": "Steady State & Dosing Concepts",
            "subtitle": "Match each concept to its key fact and clinical consequence",
            "categories": ["Key Fact", "Determined By / Formula", "Clinical Consequence"],
            "data": {
                "Steady-state concentration (Css)": {
                    "Key Fact": "Rate of drug entering the body equals rate of drug leaving",
                    "Determined By / Formula": "Css equals dosing rate divided by clearance",
                    "Clinical Consequence": "Target level for a sustained therapeutic effect"
                },
                "Time to steady state": {
                    "Key Fact": "Steady state is reached after about 4-5 half-lives",
                    "Determined By / Formula": "Set by the elimination half-life, not dose or interval",
                    "Clinical Consequence": "Doubling the dose raises the level, not the speed to steady state"
                },
                "Peak concentration": {
                    "Key Fact": "Highest concentration, reached just after a dose",
                    "Determined By / Formula": "Rises with a larger dose or shorter dosing interval",
                    "Clinical Consequence": "High peaks increase the risk of toxicity"
                },
                "Trough concentration": {
                    "Key Fact": "Lowest concentration, reached just before the next dose",
                    "Determined By / Formula": "Falls with a longer dosing interval",
                    "Clinical Consequence": "Low troughs risk loss of therapeutic effect"
                },
                "Extended-release dosing": {
                    "Key Fact": "Formulation given at a long dosing interval",
                    "Determined By / Formula": "Longer interval widens the peak-to-trough difference",
                    "Clinical Consequence": "Large swings require careful attention to toxicity"
                }
            }
        }
    ]
}
