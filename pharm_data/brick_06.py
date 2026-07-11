BRICK = {
    "brick_num": 6,
    "brick_title": "Pharmacodynamics 2: Quantal Dose Response and Therapeutic Index",
    "games": [
        {
            "slug": "dose_response_metrics",
            "title": "Dose-Response Metrics",
            "subtitle": "Match each drug metric to its definition, the curve it comes from, and its use",
            "categories": ["Definition", "Curve Type", "Use"],
            "data": {
                "ED50 (median effective dose)": {
                    "Definition": "dose at which 50% of a population shows the effect",
                    "Curve Type": "quantal effect curve",
                    "Use": "recommend a prescribing dose range"
                },
                "TD50 (median toxic dose)": {
                    "Definition": "dose producing a toxic effect in 50% of a population",
                    "Curve Type": "quantal toxicity curve",
                    "Use": "serves as the numerator of the therapeutic index"
                },
                "LD50 (median lethal dose)": {
                    "Definition": "dose that is lethal to 50% of a population",
                    "Curve Type": "quantal lethality curve",
                    "Use": "shows how safely toxic and therapeutic doses separate"
                },
                "EC50": {
                    "Definition": "concentration giving 50% of the maximal effect",
                    "Curve Type": "graded concentration-effect curve",
                    "Use": "compare potency between drugs"
                },
                "Emax": {
                    "Definition": "the maximum effect a drug can produce",
                    "Curve Type": "graded response plateau",
                    "Use": "compare efficacy between drugs"
                }
            }
        },
        {
            "slug": "curve_types",
            "title": "Dose-Response Curve Types",
            "subtitle": "Match each curve to what it represents, its response type, and its key output",
            "categories": ["What It Represents", "Response Type", "Key Output"],
            "data": {
                "Graded dose-response curve": {
                    "What It Represents": "drug effect versus concentration in a single patient",
                    "Response Type": "continuous, graded effect",
                    "Key Output": "Emax and EC50"
                },
                "Quantal dose-response curve": {
                    "What It Represents": "proportion of a population showing a defined outcome",
                    "Response Type": "all-or-none (present or absent)",
                    "Key Output": "median effective dose (ED50)"
                },
                "Frequency distribution curve": {
                    "What It Represents": "number of patients responding at each dose",
                    "Response Type": "Gaussian, bell-shaped spread",
                    "Key Output": "the peak median responding dose"
                },
                "Cumulative frequency curve": {
                    "What It Represents": "running total of subjects responding as dose rises",
                    "Response Type": "sigmoidal, S-shaped rise",
                    "Key Output": "an ED50, TD50, or LD50 value"
                }
            }
        },
        {
            "slug": "safety_and_dosing",
            "title": "Safety and Dosing Concepts",
            "subtitle": "Match each safety concept to its definition, its formula, and its clinical use",
            "categories": ["Definition", "Formula or Boundary", "Clinical Use"],
            "data": {
                "Therapeutic index (TI)": {
                    "Definition": "relative safety margin of a drug",
                    "Formula or Boundary": "TD50 divided by ED50",
                    "Clinical Use": "guides how closely a drug must be monitored"
                },
                "Margin of safety": {
                    "Definition": "safety measure derived from preclinical animal studies",
                    "Formula or Boundary": "LD1 divided by ED99",
                    "Clinical Use": "helps set starting doses for first human trials"
                },
                "Therapeutic window": {
                    "Definition": "concentration range between benefit and toxicity",
                    "Formula or Boundary": "minimum toxic minus minimum effective concentration",
                    "Clinical Use": "keep plasma level here for safe, effective therapy"
                },
                "Minimum effective concentration": {
                    "Definition": "lowest plasma level that gives clinical benefit",
                    "Formula or Boundary": "lower bound of the therapeutic window",
                    "Clinical Use": "target to begin achieving the desired effect"
                },
                "Minimum toxic concentration": {
                    "Definition": "plasma level above which toxic effects appear",
                    "Formula or Boundary": "upper bound of the therapeutic window",
                    "Clinical Use": "stay below it to avoid adverse effects"
                }
            }
        },
        {
            "slug": "antagonism_interactions",
            "title": "Drug Antagonism and Interactions",
            "subtitle": "Match each interaction to its mechanism, a brick example, and its key feature",
            "categories": ["Mechanism", "Example", "Key Feature"],
            "data": {
                "Physiologic antagonism": {
                    "Mechanism": "two agents produce opposite physiologic effects",
                    "Example": "glucagon opposing insulin on blood glucose",
                    "Key Feature": "acts via different pathways to maintain homeostasis"
                },
                "Chemical antagonism": {
                    "Mechanism": "one drug directly inactivates another drug",
                    "Example": "antacids neutralizing stomach acid",
                    "Key Feature": "a chemical reaction, separate from enzyme inhibition"
                },
                "Chelation": {
                    "Mechanism": "a chelator binds and inactivates a metal ion",
                    "Example": "deferoxamine binding excess iron",
                    "Key Feature": "sequesters the ion for elimination by the kidneys"
                },
                "DNA intercalation": {
                    "Mechanism": "a drug inserts into and damages DNA",
                    "Example": "cisplatin intercalating into DNA",
                    "Key Feature": "cytotoxic action used against cancer"
                }
            }
        }
    ]
}
