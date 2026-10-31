BRICK = {
    "brick_num": 38,
    "brick_title": "Vancomycin and Bacitracin",
    "games": [
        {
            "slug": "building_the_wall",
            "title": "Building the Peptidoglycan Wall",
            "subtitle": "Match each step of cell wall synthesis to where it happens and which drug blocks it",
            "categories": ["What Happens", "Location", "Drug That Blocks It"],
            "data": {
                "Glycan synthesis": {
                    "What Happens": "NAG and NAM glycans are made",
                    "Location": "Cytoplasm of the bacterial cell",
                    "Drug That Blocks It": "Not the target of either drug"
                },
                "Step 1": {
                    "What Happens": "NAM is joined to the lipid bactoprenol",
                    "Location": "Membrane surface",
                    "Drug That Blocks It": "Bacitracin, which halts all new unit synthesis"
                },
                "Step 2": {
                    "What Happens": "NAG is joined to the bactoprenol-NAM group",
                    "Location": "On the lipid carrier at the membrane",
                    "Drug That Blocks It": "Proceeds normally under both drugs"
                },
                "Step 3": {
                    "What Happens": "NAM-NAG unit crosses membrane and joins the growing chain",
                    "Location": "Outer cell wall",
                    "Drug That Blocks It": "Vancomycin, by binding the D-Ala-D-Ala terminus"
                },
                "Cross-linking": {
                    "What Happens": "Transpeptidases link chains through peptide chains",
                    "Location": "Between chains in the multilayered wall",
                    "Drug That Blocks It": "Beta-lactams inhibit transpeptidase"
                }
            }
        },
        {
            "slug": "vancomycin_adverse_effects",
            "title": "Vancomycin Adverse Effects",
            "subtitle": "Match each adverse effect to its mechanism or feature, what raises the risk, and its frequency or prevention",
            "categories": ["Mechanism or Feature", "Raises the Risk", "Frequency or Prevention"],
            "data": {
                "Nephrotoxicity": {
                    "Mechanism or Feature": "Drug accumulates in proximal tubular cells, inducing apoptosis",
                    "Raises the Risk": "Aminoglycosides, amphotericin B, IV contrast, vasopressors, high dose",
                    "Frequency or Prevention": "Common; reduced by AUC/MIC-guided PK dosing"
                },
                "Ototoxicity": {
                    "Mechanism or Feature": "Drug accumulates in the inner ear",
                    "Raises the Risk": "Aminoglycosides and loop diuretics such as furosemide",
                    "Frequency or Prevention": "Rare"
                },
                "Infusion syndrome (red man)": {
                    "Mechanism or Feature": "Mast cells release histamine, causing diffuse flushing",
                    "Raises the Risk": "Rapid infusion of the drug",
                    "Frequency or Prevention": "Prevented by antihistamine and 1-4 hour infusion"
                },
                "Thrombophlebitis and infusion pain": {
                    "Mechanism or Feature": "Local reaction at the intravenous infusion site",
                    "Raises the Risk": "Intravenous administration itself",
                    "Frequency or Prevention": "Far more common than the organ toxicities"
                }
            }
        },
        {
            "slug": "two_peptidoglycan_inhibitors",
            "title": "Vancomycin vs Bacitracin",
            "subtitle": "Match each drug or formulation to its use, its action, and its key adverse effect",
            "categories": ["Typical Use", "Cell Wall Action", "Key Adverse Effect"],
            "data": {
                "Intravenous vancomycin": {
                    "Typical Use": "Serious gram-positive infections, especially MRSA",
                    "Cell Wall Action": "Binds D-Ala-D-Ala, blocking polymerization",
                    "Key Adverse Effect": "Nephrotoxicity, cleared 90% by glomerular filtration"
                },
                "Topical bacitracin": {
                    "Typical Use": "Ointment for superficial skin infections",
                    "Cell Wall Action": "Prevents NAM from joining bactoprenol",
                    "Key Adverse Effect": "Contact dermatitis"
                },
                "Ophthalmic bacitracin": {
                    "Typical Use": "Applied to the eye",
                    "Cell Wall Action": "Same first-step block of new wall units",
                    "Key Adverse Effect": "Blurred vision"
                },
                "Beta-lactams (for contrast)": {
                    "Typical Use": "Cell wall agents such as cephalosporins",
                    "Cell Wall Action": "Inhibit transpeptidase cross-linking",
                    "Key Adverse Effect": "Hypersensitivity and cross-reactivity"
                }
            }
        },
        {
            "slug": "clinical_decisions",
            "title": "Clinical Decisions",
            "subtitle": "Match each clinical scenario to the best agent or action and the reason for it",
            "categories": ["Best Agent or Action", "Rationale"],
            "data": {
                "Cellulitis with MRSA and group A strep bacteremia": {
                    "Best Agent or Action": "Intravenous vancomycin",
                    "Rationale": "Covers both organisms; few drugs cover MRSA"
                },
                "Minor superficial skin infection": {
                    "Best Agent or Action": "Bacitracin ointment",
                    "Rationale": "Topical agent suited to superficial infections"
                },
                "Flushing during a fast vancomycin infusion": {
                    "Best Agent or Action": "Diphenhydramine first and slow the infusion",
                    "Rationale": "Blocks and limits mast-cell histamine release"
                },
                "Vancomycin plus an aminoglycoside and furosemide": {
                    "Best Agent or Action": "Monitor kidney function and hearing",
                    "Rationale": "Combination adds nephrotoxic and ototoxic risk"
                },
                "Vancomycin in obesity or critical illness": {
                    "Best Agent or Action": "AUC/MIC-guided individualized dosing",
                    "Rationale": "Host factors raise nephrotoxicity risk"
                }
            }
        }
    ]
}
