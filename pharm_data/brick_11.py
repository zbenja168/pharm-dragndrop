BRICK = {
    "brick_num": 11,
    "brick_title": "Nonopioid Analgesics - Acetaminophen",
    "games": [
        {
            "slug": "metabolic_pathways",
            "title": "Acetaminophen Metabolic Pathways",
            "subtitle": "Match each metabolic route to its share of metabolism, product, and toxicity significance",
            "categories": ["Share / When Active", "Product Formed", "Toxicity Significance"],
            "data": {
                "Glucuronidation": {
                    "Share / When Active": "~45-55% of normal metabolism (Phase II)",
                    "Product Formed": "Nontoxic acetaminophen glucuronide conjugate",
                    "Toxicity Significance": "Reduced in malnutrition, shifting drug toward the NAPQI route"
                },
                "Sulfation": {
                    "Share / When Active": "~30-40% of normal metabolism (Phase II)",
                    "Product Formed": "Nontoxic acetaminophen sulfate conjugate",
                    "Toxicity Significance": "Saturates in overdose, diverting drug to the CYP450 route"
                },
                "CYP450 oxidation (CYP2E1)": {
                    "Share / When Active": "~10% at normal doses; rises sharply in overdose",
                    "Product Formed": "Toxic N-acetyl-p-benzoquinone imine (NAPQI)",
                    "Toxicity Significance": "Induced by chronic alcohol and isoniazid, raising NAPQI output"
                },
                "Glutathione conjugation": {
                    "Share / When Active": "Detoxifies NAPQI as it is formed",
                    "Product Formed": "Nontoxic conjugated (mercapturate) NAPQI",
                    "Toxicity Significance": "Depleted in overdose, allowing NAPQI to bind hepatocytes"
                }
            }
        },
        {
            "slug": "acetaminophen_vs_nsaids",
            "title": "Acetaminophen vs. NSAIDs",
            "subtitle": "Sort each pharmacologic feature into the acetaminophen column and the NSAID column",
            "categories": ["Acetaminophen", "NSAIDs"],
            "data": {
                "Anti-inflammatory action": {
                    "Acetaminophen": "Weak; only limited peripheral COX inhibition",
                    "NSAIDs": "Strong; robust peripheral COX inhibition"
                },
                "Main site of COX inhibition": {
                    "Acetaminophen": "Central (CNS); oxidized by brain CYP450 to inhibit COX",
                    "NSAIDs": "Peripheral tissues, with central effects as well"
                },
                "Effect on platelets / clotting": {
                    "Acetaminophen": "None; high platelet peroxidase blocks its COX effect",
                    "NSAIDs": "Aspirin is antithrombotic by blocking platelet thromboxane"
                },
                "Classified as an NSAID": {
                    "Acetaminophen": "No; not classified as an NSAID",
                    "NSAIDs": "Yes, by definition"
                },
                "Analgesic / antipyretic use": {
                    "Acetaminophen": "Yes; raises pain threshold via central COX inhibition",
                    "NSAIDs": "Yes; achieved through COX inhibition"
                }
            }
        },
        {
            "slug": "overdose_management",
            "title": "Managing Acetaminophen Overdose",
            "subtitle": "Match each element to its role in overdose and its key detail",
            "categories": ["Role in Overdose", "Key Detail"],
            "data": {
                "N-acetylcysteine (NAC)": {
                    "Role in Overdose": "Antidote",
                    "Key Detail": "Supplies cysteine to restore glutathione; give preferably within 16 hours"
                },
                "Glutathione": {
                    "Role in Overdose": "Endogenous detoxifier",
                    "Key Detail": "Conjugates NAPQI, but is depleted in overdose so NAPQI injures hepatocytes"
                },
                "NAPQI": {
                    "Role in Overdose": "Toxic metabolite",
                    "Key Detail": "Binds hepatic proteins, causing oxidative stress and centrilobular necrosis"
                },
                "Rumack-Matthew nomogram": {
                    "Role in Overdose": "Risk-prediction tool",
                    "Key Detail": "Plots serum acetaminophen versus time since ingestion to predict hepatotoxicity"
                },
                "Serum transaminases (AST)": {
                    "Role in Overdose": "Marker of hepatic injury",
                    "Key Detail": "Rise rapidly in overdose; AST over 1000 IU/L signals severe hepatotoxicity"
                }
            }
        },
        {
            "slug": "inflammatory_pathway",
            "title": "The Inflammatory (Prostaglandin) Pathway",
            "subtitle": "Match each pathway component to its role and a defining note",
            "categories": ["Role in the Pathway", "Defining Note"],
            "data": {
                "Phospholipase A2": {
                    "Role in the Pathway": "Releases arachidonic acid from membrane phospholipids",
                    "Defining Note": "First step, triggered by physical, chemical, inflammatory, and mitogenic stimuli"
                },
                "Arachidonic acid": {
                    "Role in the Pathway": "Fatty-acid substrate for the COX enzymes",
                    "Defining Note": "Converted by COX-1 and COX-2 into prostaglandin intermediates"
                },
                "COX-1 and COX-2": {
                    "Role in the Pathway": "Convert arachidonic acid into PGH2",
                    "Defining Note": "Inhibited by NSAIDs; only weakly and centrally inhibited by acetaminophen"
                },
                "PGH2": {
                    "Role in the Pathway": "Prostaglandin intermediate",
                    "Defining Note": "Converted into the tissue-specific prostaglandins"
                },
                "Thromboxane A2": {
                    "Role in the Pathway": "Tissue-specific prostanoid end product",
                    "Defining Note": "Acts on platelets, blood vessels, macrophages, and kidney"
                }
            }
        }
    ]
}
