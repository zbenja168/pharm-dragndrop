BRICK = {
    "brick_num": 36,
    "brick_title": "β-lactam Antibiotics (Penicillins & Carbapenems)",
    "games": [
        {
            "slug": "penicillin_subgroups",
            "title": "Penicillin Subgroups",
            "subtitle": "Match each penicillin subgroup to its example drugs, key property, and clinical pearl",
            "categories": ["Example Drugs", "Key Property", "Clinical Pearl"],
            "data": {
                "Natural penicillins": {
                    "Example Drugs": "Penicillin G and penicillin V",
                    "Key Property": "Relatively narrow spectrum of activity",
                    "Clinical Pearl": "Penicillin G is acid labile and poorly absorbed orally"
                },
                "Antistaphylococcal penicillins": {
                    "Example Drugs": "Nafcillin",
                    "Key Property": "Stable against staphylococcal penicillinase",
                    "Clinical Pearl": "Hepatic and biliary elimination contribute substantially to clearance"
                },
                "Aminopenicillins": {
                    "Example Drugs": "Ampicillin and amoxicillin",
                    "Key Property": "Acid stable, so useful by the oral route",
                    "Clinical Pearl": "Maculopapular rash in Epstein-Barr virus mononucleosis"
                },
                "Antipseudomonal penicillins": {
                    "Example Drugs": "Piperacillin",
                    "Key Property": "Broad spectrum when paired with tazobactam",
                    "Clinical Pearl": "Renally eliminated; adjust dose in renal impairment"
                }
            }
        },
        {
            "slug": "beta_lactam_resistance",
            "title": "How Bacteria Resist β-lactams",
            "subtitle": "Match each resistance mechanism to what changes, a classic example, and whether a β-lactamase inhibitor helps",
            "categories": ["What Changes", "Classic Example", "Does an Inhibitor Help?"],
            "data": {
                "β-lactamase production": {
                    "What Changes": "Enzyme hydrolyzes the β-lactam ring",
                    "Classic Example": "Organism that inactivates amoxicillin given alone",
                    "Does an Inhibitor Help?": "Yes, if clavulanate, sulbactam, or tazobactam inhibits it"
                },
                "Altered PBPs": {
                    "What Changes": "Target PBPs have reduced drug affinity",
                    "Classic Example": "Penicillin-nonsusceptible S. pneumoniae; methicillin-resistant staphylococci",
                    "Does an Inhibitor Help?": "No; inhibitors do not restore PBP binding"
                },
                "Decreased penetration": {
                    "What Changes": "Outer-membrane porin changes limit drug access",
                    "Classic Example": "Gram-negative bacteria with altered porins",
                    "Does an Inhibitor Help?": "No; drug still cannot reach its PBP targets"
                },
                "Carbapenemase production": {
                    "What Changes": "Enzyme hydrolyzes and inactivates carbapenems",
                    "Classic Example": "Isolate resistant despite carbapenem β-lactamase stability",
                    "Does an Inhibitor Help?": "Selected combinations such as meropenem/vaborbactam may"
                }
            }
        },
        {
            "slug": "companions_and_interactions",
            "title": "Partner Drugs and Interactions",
            "subtitle": "Match each agent to the β-lactam it is paired with, how it acts, and the result",
            "categories": ["Paired With", "How It Acts", "Result"],
            "data": {
                "Cilastatin": {
                    "Paired With": "Imipenem",
                    "How It Acts": "Inhibits dehydropeptidase I in the proximal tubular brush border",
                    "Result": "Adequate imipenem concentrations reach the urine"
                },
                "Tazobactam": {
                    "Paired With": "Piperacillin",
                    "How It Acts": "Inhibits certain bacterial β-lactamases",
                    "Result": "Partner penicillin is protected from enzymatic hydrolysis"
                },
                "Probenecid": {
                    "Paired With": "Penicillins",
                    "How It Acts": "Inhibits renal tubular secretion",
                    "Result": "Higher serum penicillin concentrations"
                },
                "Valproic acid": {
                    "Paired With": "Carbapenems (an interaction, not a planned pairing)",
                    "How It Acts": "Carbapenem markedly lowers serum valproate concentration",
                    "Result": "Breakthrough seizures; combination generally avoided"
                }
            }
        },
        {
            "slug": "beta_lactam_reactions",
            "title": "β-lactam Reactions",
            "subtitle": "Match each reaction to its mechanism, setting or timing, and manifestations",
            "categories": ["Mechanism", "Setting or Timing", "Manifestations"],
            "data": {
                "Type I hypersensitivity": {
                    "Mechanism": "IgE-mediated mast-cell degranulation",
                    "Setting or Timing": "Within minutes to hours of exposure",
                    "Manifestations": "Urticaria, angioedema, bronchospasm, hypotension, anaphylaxis"
                },
                "Type II hypersensitivity": {
                    "Mechanism": "IgG against penicillin bound to red blood cells",
                    "Setting or Timing": "Especially after prolonged high-dose therapy",
                    "Manifestations": "Coombs-positive hemolytic anemia"
                },
                "Type III hypersensitivity": {
                    "Mechanism": "Immune-complex reaction",
                    "Setting or Timing": "One to three weeks after exposure",
                    "Manifestations": "Serum sickness-like fever, urticaria, arthralgias, lymphadenopathy"
                },
                "Type IV hypersensitivity": {
                    "Mechanism": "T-cell-mediated delayed reaction",
                    "Setting or Timing": "Delayed onset during therapy",
                    "Manifestations": "Delayed skin eruptions or acute interstitial nephritis"
                },
                "Aminopenicillin rash": {
                    "Mechanism": "Not necessarily IgE-mediated",
                    "Setting or Timing": "Ampicillin or amoxicillin during EBV mononucleosis",
                    "Manifestations": "Generalized maculopapular rash"
                },
                "Jarisch-Herxheimer reaction": {
                    "Mechanism": "Response to products of dying microbes, not allergy",
                    "Setting or Timing": "First 24 hours after treating a spirochetal infection",
                    "Manifestations": "Fever, chills, headache, myalgias"
                }
            }
        }
    ]
}
