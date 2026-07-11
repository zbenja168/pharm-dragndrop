BRICK = {
    "brick_num": 2,
    "brick_title": "Pharmacokinetics 1 (2 of 3): Drug Metabolism and Excretion",
    "games": [
        {
            "slug": "cyp_inhibitors",
            "title": "Clinically Important CYP450 Inhibitors",
            "subtitle": "Match each CYP450 inhibitor to its drug class and clinical use (all inhibitors raise substrate serum drug levels)",
            "categories": ["Drug Class / Category", "Clinical Use", "Interaction Note"],
            "data": {
                "Ketoconazole": {
                    "Drug Class / Category": "Azole antifungal",
                    "Clinical Use": "Treats fungal infections",
                    "Interaction Note": "Raises plasma levels of CYP3A4 substrates"
                },
                "Ciprofloxacin": {
                    "Drug Class / Category": "Fluoroquinolone antibiotic",
                    "Clinical Use": "Treats bacterial infections",
                    "Interaction Note": "Slows metabolism of co-administered drugs"
                },
                "Omeprazole": {
                    "Drug Class / Category": "Proton pump inhibitor",
                    "Clinical Use": "Treats acid reflux",
                    "Interaction Note": "Also a prodrug activated at low gastric pH"
                },
                "Cyclosporine": {
                    "Drug Class / Category": "Immunosuppressant",
                    "Clinical Use": "Prevents organ transplant rejection",
                    "Interaction Note": "Both a CYP substrate and inhibitor"
                },
                "Amiodarone": {
                    "Drug Class / Category": "Antiarrhythmic",
                    "Clinical Use": "Controls cardiac rhythm disorders",
                    "Interaction Note": "Long half-life prolongs its inhibitory effect"
                },
                "Grapefruit juice": {
                    "Drug Class / Category": "Dietary CYP inhibitor",
                    "Clinical Use": "Consumed in large quantities as a food",
                    "Interaction Note": "Increases simvastatin and verapamil effects"
                }
            }
        },
        {
            "slug": "metabolism_concepts",
            "title": "Key Concepts in Drug Metabolism",
            "subtitle": "Match each metabolism concept to what it is, a key example, and its consequence",
            "categories": ["What It Is", "Key Example", "Consequence"],
            "data": {
                "Prodrug": {
                    "What It Is": "Inactive drug activated by metabolism",
                    "Key Example": "Codeine converted to morphine by a CYP enzyme",
                    "Consequence": "Requires metabolic activation to work"
                },
                "First-pass metabolism": {
                    "What It Is": "Oral drug metabolized by the liver before systemic circulation",
                    "Key Example": "Avoided by intravenous administration",
                    "Consequence": "Reduces oral bioavailability"
                },
                "Phase I reaction": {
                    "What It Is": "Modification by oxidation, reduction, or hydrolysis",
                    "Key Example": "Cytochrome P450 (CYP450) enzymes",
                    "Consequence": "Alters chemical structure into metabolites"
                },
                "Phase II reaction": {
                    "What It Is": "Conjugation that adds a functional group",
                    "Key Example": "Glucuronidation (the most common pathway)",
                    "Consequence": "Yields inactive, water-soluble metabolites"
                },
                "Enterohepatic circulation": {
                    "What It Is": "Drug recycled from liver to gut and back to liver",
                    "Key Example": "Glucuronidated drug freed by colonic bacteria",
                    "Consequence": "Prolongs the drug's presence in the body"
                },
                "Heme cofactor": {
                    "What It Is": "Molecule CYP450 uses to transfer electrons",
                    "Key Example": "Enables oxidation (Red-Ox) reactions",
                    "Consequence": "Drives Phase I biotransformation"
                }
            }
        },
        {
            "slug": "excretion_pathways",
            "title": "Drug Excretion Pathways",
            "subtitle": "Match each excretion route to the substances it handles and where the drug leaves the body",
            "categories": ["Substances Handled", "Excreted / Eliminated In", "Key Point"],
            "data": {
                "Renal filtration and secretion": {
                    "Substances Handled": "Unbound, water-soluble (hydrophilic) drugs",
                    "Excreted / Eliminated In": "Urine",
                    "Key Point": "Kidneys are the primary excretory organ"
                },
                "Hepatic biliary excretion": {
                    "Substances Handled": "Water-insoluble (lipophilic) metabolites",
                    "Excreted / Eliminated In": "Feces, via bile",
                    "Key Point": "Liver secretes lipophilic drugs into the gut"
                },
                "Enterohepatic recycling": {
                    "Substances Handled": "Glucuronidated drugs reabsorbed by the gut",
                    "Excreted / Eliminated In": "Recirculated, then renally excreted",
                    "Key Point": "Colonic bacteria remove the glucuronide group"
                },
                "Passive tubular reabsorption": {
                    "Substances Handled": "Lipophilic drug diffusing from the tubule",
                    "Excreted / Eliminated In": "Returned to the blood, escaping excretion",
                    "Key Point": "Partially defeats renal excretion"
                },
                "Minor excretory routes": {
                    "Substances Handled": "A small percentage of drugs",
                    "Excreted / Eliminated In": "Lungs, skin, tears, milk, and saliva",
                    "Key Point": "Accounts for only a small fraction of elimination"
                }
            }
        },
        {
            "slug": "factors_affecting_metabolism",
            "title": "Factors Affecting Drug Metabolism",
            "subtitle": "Match each factor to how it changes metabolism and its clinical consequence",
            "categories": ["Mechanism / Effect on Metabolism", "Clinical Consequence", "Example / Note"],
            "data": {
                "CYP inhibition": {
                    "Mechanism / Effect on Metabolism": "Decreases CYP enzyme activity",
                    "Clinical Consequence": "Higher serum drug levels and toxicity risk",
                    "Example / Note": "Caused by drugs like ketoconazole"
                },
                "CYP induction": {
                    "Mechanism / Effect on Metabolism": "Increases CYP enzyme synthesis or activity",
                    "Clinical Consequence": "Lower serum drug levels and reduced efficacy",
                    "Example / Note": "Caused by rifampin, phenytoin, or carbamazepine"
                },
                "Hepatic cirrhosis": {
                    "Mechanism / Effect on Metabolism": "Compromised Phase I pathways lower metabolism",
                    "Clinical Consequence": "Longer half-life; reduce dose to avoid toxicity",
                    "Example / Note": "Also reduces plasma proteins, raising free drug"
                },
                "Pharmacogenomics (CYP2D6)": {
                    "Mechanism / Effect on Metabolism": "Genetic variation in metabolizer status",
                    "Clinical Consequence": "Altered response to opioids such as codeine",
                    "Example / Note": "Patients range from poor to ultra-rapid metabolizers"
                },
                "Aging and reduced blood flow": {
                    "Mechanism / Effect on Metabolism": "Decreased hepatic and renal perfusion",
                    "Clinical Consequence": "Reduced metabolic capacity; needs dose monitoring",
                    "Example / Note": "Older adults have reduced circulation"
                },
                "Shock or hypotension": {
                    "Mechanism / Effect on Metabolism": "Decreased blood flow to the liver",
                    "Clinical Consequence": "Reduced metabolic rate",
                    "Example / Note": "Includes hypovolemia and low blood pressure"
                }
            }
        }
    ]
}
