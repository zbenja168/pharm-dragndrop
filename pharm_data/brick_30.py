BRICK = {
    "brick_num": 30,
    "brick_title": "Opioid Agonists",
    "games": [
        {
            "slug": "opioid_medications",
            "title": "Opioid Medications at a Glance",
            "subtitle": "Match each opioid to its agonist type, relative potency, and a notable clinical feature",
            "categories": ["Agonist Type", "Relative Potency", "Notable Clinical Feature"],
            "data": {
                "Buprenorphine": {
                    "Agonist Type": "Partial mu-opioid agonist",
                    "Relative Potency": "N/A (partial activation only)",
                    "Notable Clinical Feature": "First-line for opioid use disorder; gives little 'high' at high doses"
                },
                "Codeine": {
                    "Agonist Type": "Full agonist",
                    "Relative Potency": "Weak",
                    "Notable Clinical Feature": "Antitussive prodrug converted to morphine; FDA black box in children under 12"
                },
                "Fentanyl": {
                    "Agonist Type": "Full agonist",
                    "Relative Potency": "Strong",
                    "Notable Clinical Feature": "Transdermal patch for chronic/cancer pain; drips used for analgosedation"
                },
                "Methadone": {
                    "Agonist Type": "Full agonist",
                    "Relative Potency": "Strong",
                    "Notable Clinical Feature": "Ultra-long duration; used for sustained control in opioid use disorder"
                },
                "Morphine": {
                    "Agonist Type": "Full agonist",
                    "Relative Potency": "Strong",
                    "Notable Clinical Feature": "Benchmark for potency via morphine milligram equivalents (MME)"
                },
                "Meperidine": {
                    "Agonist Type": "Full agonist",
                    "Relative Potency": "Weak",
                    "Notable Clinical Feature": "Short-acting full agonist for moderate-to-severe pain"
                }
            }
        },
        {
            "slug": "routes_of_administration",
            "title": "Routes of Opioid Administration",
            "subtitle": "Match each route to its first-pass metabolism, onset, and best clinical use",
            "categories": ["First-Pass Metabolism", "Onset of Action", "Best Use and Key Feature"],
            "data": {
                "Oral (PO)": {
                    "First-Pass Metabolism": "Subject to hepatic first-pass metabolism",
                    "Onset of Action": "Slower onset",
                    "Best Use and Key Feature": "Convenient, non-invasive for mild-moderate and chronic pain; lower bioavailability"
                },
                "Intravenous (IV)": {
                    "First-Pass Metabolism": "Avoids first-pass metabolism",
                    "Onset of Action": "Quickest onset",
                    "Best Use and Key Feature": "Preferred for acute severe pain; highest bioavailability"
                },
                "Intramuscular (IM)": {
                    "First-Pass Metabolism": "Avoids first-pass metabolism",
                    "Onset of Action": "Slower than IV",
                    "Best Use and Key Feature": "Least common; used when IV access is not yet available"
                },
                "Transdermal": {
                    "First-Pass Metabolism": "Avoids first-pass metabolism",
                    "Onset of Action": "Slow absorption through skin",
                    "Best Use and Key Feature": "Fentanyl patch for chronic/cancer pain with stable blood levels"
                }
            }
        },
        {
            "slug": "opioid_effects_mechanisms",
            "title": "Opioid Effects and Their Mechanisms",
            "subtitle": "Match each opioid effect to the receptor that mediates it, its mechanism or site, and a clinical note",
            "categories": ["Mediating Receptor", "Mechanism or Site", "Clinical Note"],
            "data": {
                "Analgesia": {
                    "Mediating Receptor": "Mu receptor",
                    "Mechanism or Site": "Activation in the periaqueductal gray blocks pain perception",
                    "Clinical Note": "Primary therapeutic use in moderate-to-severe pain"
                },
                "Respiratory depression": {
                    "Mediating Receptor": "Mu receptor",
                    "Mechanism or Site": "Reduces intrinsic rhythm generators in the ventrolateral medulla",
                    "Clinical Note": "Dangerous in COPD/asthma or overdose; a cause of death"
                },
                "Constipation": {
                    "Mediating Receptor": "Mu receptor",
                    "Mechanism or Site": "Decreases motility via enteric myenteric and submucosal neurons",
                    "Clinical Note": "Reliable, common side effect of opioid agonists"
                },
                "Diuresis": {
                    "Mediating Receptor": "Kappa receptor",
                    "Mechanism or Site": "Inhibits release of oxytocin and antidiuretic hormone",
                    "Clinical Note": "Kappa-mediated regulation of fluid balance"
                },
                "Dysphoria": {
                    "Mediating Receptor": "Kappa receptor",
                    "Mechanism or Site": "Produces depression and a sense of unease",
                    "Clinical Note": "Why kappa is not targeted for long-term analgesia"
                },
                "Antidepressant / anxiolytic effect": {
                    "Mediating Receptor": "Delta receptor",
                    "Mechanism or Site": "Related to dopamine modulation",
                    "Clinical Note": "Mood-related effects of delta receptor activation"
                }
            }
        },
        {
            "slug": "metabolism_polymorphism",
            "title": "Opioid Metabolism and Genetic Polymorphism",
            "subtitle": "Match each metabolic scenario to its effect, consequence, and key association",
            "categories": ["Effect on Metabolism", "Consequence", "Key Association"],
            "data": {
                "Ultrarapid (UR) metabolizer": {
                    "Effect on Metabolism": "Clears active drug very quickly",
                    "Consequence": "Significantly shorter duration of action",
                    "Key Association": "Up to 30% of Middle Eastern and North African descent"
                },
                "Poor metabolizer": {
                    "Effect on Metabolism": "Clears active drug slowly",
                    "Consequence": "Prolonged duration; a single dose can last 2-3x and risk overdose",
                    "Key Association": "Up to 35% of Asian descent"
                },
                "Codeine in a child under 12": {
                    "Effect on Metabolism": "Rapid CYP2D6 conversion of the prodrug to morphine",
                    "Consequence": "Toxic morphine levels causing respiratory depression and death",
                    "Key Association": "FDA black box warning"
                },
                "CYP450 inhibitor co-administration": {
                    "Effect on Metabolism": "Blocks metabolism of the opioid",
                    "Consequence": "Increased opioid blood levels",
                    "Key Association": "Enhanced respiratory depression, sedation, and constipation"
                }
            }
        }
    ]
}
