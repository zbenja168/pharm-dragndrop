BRICK = {
    "brick_num": 43,
    "brick_title": "Fluoroquinolones (DNA Gyrase inhibitors)",
    "games": [
        {
            "slug": "meet_the_fluoroquinolones",
            "title": "Meet the Fluoroquinolones",
            "subtitle": "Match each agent to its group, where it is used, and its distinguishing feature",
            "categories": ["Group", "Main Use", "Distinguishing Feature"],
            "data": {
                "Levofloxacin": {
                    "Group": "Respiratory fluoroquinolone",
                    "Main Use": "Respiratory infections above the diaphragm",
                    "Distinguishing Feature": "Better Pseudomonas coverage and milder side effects"
                },
                "Moxifloxacin": {
                    "Group": "Respiratory fluoroquinolone with S. pneumoniae coverage",
                    "Main Use": "Key systemic agent for respiratory infections",
                    "Distinguishing Feature": "Greatest risk of QTc prolongation in the class"
                },
                "Gatifloxacin": {
                    "Group": "Respiratory fluoroquinolone (eye use only)",
                    "Main Use": "Topical ophthalmic therapy",
                    "Distinguishing Feature": "Only available in ophthalmic form in the US"
                },
                "Ciprofloxacin": {
                    "Group": "Non-respiratory systemic fluoroquinolone",
                    "Main Use": "Systemic infections below the diaphragm, e.g. pyelonephritis",
                    "Distinguishing Feature": "Notable CYP1A2 inhibitor; most effective systemically"
                },
                "Norfloxacin": {
                    "Group": "Non-respiratory fluoroquinolone grouped with ciprofloxacin",
                    "Main Use": "Still used outside the United States",
                    "Distinguishing Feature": "Withdrawn from the US market"
                },
                "Nalidixic acid": {
                    "Group": "Original nonfluorinated quinolone",
                    "Main Use": "None today; core structure of the class",
                    "Distinguishing Feature": "No longer on the market"
                }
            }
        },
        {
            "slug": "topoisomerases_and_resistance",
            "title": "Targets, Killing, and Resistance",
            "subtitle": "Match each player to its normal role, what fluoroquinolones do to it, and the consequence",
            "categories": ["Normal Role", "Fluoroquinolone Interaction", "Consequence"],
            "data": {
                "DNA gyrase": {
                    "Normal Role": "Uniquely creates negative supercoils ahead of replication",
                    "Fluoroquinolone Interaction": "Primary type II topoisomerase target of the class",
                    "Consequence": "Cannot relieve supercoiling tension for replication"
                },
                "Topoisomerase IV": {
                    "Normal Role": "Relaxes negative supercoils and decatenates chromosomes",
                    "Fluoroquinolone Interaction": "Sister enzyme inhibited with variable specificity",
                    "Consequence": "Completed daughter chromosomes are not separated"
                },
                "Ligase domain": {
                    "Normal Role": "Reseals the nick made in the DNA strand",
                    "Fluoroquinolone Interaction": "Directly inhibited by the drug",
                    "Consequence": "Nicks go unrepaired; the enzyme becomes a DNA shredder"
                },
                "Nuclease domain": {
                    "Normal Role": "Nicks a DNA strand so it can uncoil",
                    "Fluoroquinolone Interaction": "Left active and keeps cutting",
                    "Consequence": "Replication halts and the cell dies (bactericidal)"
                },
                "Efflux pumps": {
                    "Normal Role": "Actively transport substances out of the bacterium",
                    "Fluoroquinolone Interaction": "Modified to export more drug",
                    "Consequence": "Resistance via lower intracellular drug levels"
                },
                "Plasmids": {
                    "Normal Role": "Small loops of DNA shared between nearby bacteria",
                    "Fluoroquinolone Interaction": "Carry altered target-site resistance genes",
                    "Consequence": "Rapid spread of resistance through a population"
                }
            }
        },
        {
            "slug": "pk_and_interactions",
            "title": "Pharmacokinetics and Drug Interactions",
            "subtitle": "Match each factor to its effect on fluoroquinolone therapy and how to manage it",
            "categories": ["Effect", "Mechanism", "Management"],
            "data": {
                "Antacids (Al, Mg, Ca)": {
                    "Effect": "Decreased fluoroquinolone absorption",
                    "Mechanism": "Di- and trivalent cations chelate the drug",
                    "Management": "Give the fluoroquinolone 4-6 hours afterward"
                },
                "Iron, minerals, multivitamins": {
                    "Effect": "Reduced oral uptake of the antibiotic",
                    "Mechanism": "Multivalent cations bind the drug in the gut",
                    "Management": "Separate doses; fluoroquinolone given 4-6 hours later"
                },
                "Theophylline": {
                    "Effect": "Rising levels and toxicity on ciprofloxacin",
                    "Mechanism": "Ciprofloxacin inhibits CYP1A2, slowing its elimination",
                    "Management": "Significantly decrease the theophylline dose"
                },
                "Beta-lactam antibiotics": {
                    "Effect": "Synergy with fluoroquinolones",
                    "Mechanism": "Cell wall inhibition eases drug entry to targets",
                    "Management": "Can be combined to increase efficiency"
                },
                "Food": {
                    "Effect": "Little effect on absorption",
                    "Mechanism": "Absorption is quick through the gut wall",
                    "Management": "No special timing around meals needed"
                }
            }
        },
        {
            "slug": "fluoroquinolone_adverse_effects",
            "title": "Fluoroquinolone Adverse Effects",
            "subtitle": "Match each organ system to its adverse effect, key detail, and who is at risk",
            "categories": ["Adverse Effect", "Key Detail", "Risk Group or Action"],
            "data": {
                "Gastrointestinal": {
                    "Adverse Effect": "Nausea, vomiting, diarrhea; C. difficile colitis",
                    "Key Detail": "Most common adverse effect, from gut dysbiosis",
                    "Risk Group or Action": "Loss of competing normal flora allows overgrowth"
                },
                "Cardiac": {
                    "Adverse Effect": "QTc prolongation and torsades de pointes",
                    "Key Detail": "Inhibition of specific potassium channels",
                    "Risk Group or Action": "Highest with moxifloxacin; EKG monitoring"
                },
                "Neurologic": {
                    "Adverse Effect": "Delirium, agitation, memory impairment, neuropathy",
                    "Key Detail": "Very good CNS penetration, even after one dose",
                    "Risk Group or Action": "Neuropathy can last years or be permanent"
                },
                "Musculoskeletal": {
                    "Adverse Effect": "Tendinopathy, tendon rupture, cartilage erosion",
                    "Key Detail": "Achilles tendon most often affected",
                    "Risk Group or Action": "Children: arthropathy in weight-bearing joints"
                },
                "Dermatologic": {
                    "Adverse Effect": "Rash, phototoxicity, rarely SJS/TEN",
                    "Key Detail": "Rash in 1-2%, worsens with prolonged treatment",
                    "Risk Group or Action": "Sunscreen; avoid the class for life after SJS"
                },
                "Metabolic and vascular": {
                    "Adverse Effect": "Hypoglycemia; aortic aneurysm or dissection",
                    "Key Detail": "Both hyper- and hypoglycemia reported",
                    "Risk Group or Action": "Elderly diabetics; avoid if aneurysm risk"
                }
            }
        }
    ]
}
