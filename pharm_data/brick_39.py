BRICK = {
    "brick_num": 39,
    "brick_title": "Protein Synthesis Inhibitor-1 of 2: Mechanisms of Action",
    "games": [
        {
            "slug": "sort_the_psi_classes",
            "title": "Sort the Protein Synthesis Inhibitor Classes",
            "subtitle": "Match each PSI class to its member drugs, ribosomal target, and key feature",
            "categories": ["Member Drug(s)", "Ribosomal Target", "Key Feature"],
            "data": {
                "Aminoglycosides": {
                    "Member Drug(s)": "Streptomycin, neomycin, gentamicin, tobramycin, amikacin",
                    "Ribosomal Target": "16S rRNA within the 30S subunit",
                    "Key Feature": "Amino sugars on an aminocyclitol nucleus; highly hydrophilic"
                },
                "Tetracyclines": {
                    "Member Drug(s)": "Doxycycline and minocycline (second generation)",
                    "Ribosomal Target": "30S subunit at the acceptor (A) site",
                    "Key Feature": "Names end in -cycline; broad-spectrum activity"
                },
                "Macrolides": {
                    "Member Drug(s)": "Azithromycin, clarithromycin, erythromycin",
                    "Ribosomal Target": "50S subunit at the shared MLS site",
                    "Key Feature": "Lose activity when erm genes alter 23S rRNA"
                },
                "Lincosamides": {
                    "Member Drug(s)": "Clindamycin",
                    "Ribosomal Target": "50S subunit, same site as macrolides",
                    "Key Feature": "About 90% oral bioavailability; reaches bone well"
                },
                "Streptogramins": {
                    "Member Drug(s)": "Dalfopristin and quinupristin",
                    "Ribosomal Target": "50S subunit during early and late phases",
                    "Key Feature": "Two agents acting synergistically to kill the cell"
                },
                "Oxazolidinones": {
                    "Member Drug(s)": "Linezolid",
                    "Ribosomal Target": "23S rRNA at the 30S-50S interface",
                    "Key Feature": "Unique binding site; free of cross-resistance"
                }
            }
        },
        {
            "slug": "which_step_is_blocked",
            "title": "Which Step Is Blocked?",
            "subtitle": "Match each agent to the translation step it disrupts and the result for the bacterium",
            "categories": ["Step Disrupted", "Result for the Bacterium"],
            "data": {
                "Tetracyclines": {
                    "Step Disrupted": "Aminoacyl-tRNA access to the acceptor site",
                    "Result for the Bacterium": "Growth halted only; bacteriostatic"
                },
                "Aminoglycosides": {
                    "Step Disrupted": "Translational proofreading of incoming amino acids",
                    "Result for the Bacterium": "Mistranslated membrane proteins cause lysis; bactericidal"
                },
                "Macrolides and clindamycin": {
                    "Step Disrupted": "Transpeptidation and translocation of tRNA",
                    "Result for the Bacterium": "Incomplete proteins released; mostly bacteriostatic"
                },
                "Linezolid": {
                    "Step Disrupted": "Initiation complex formation and first peptide bond",
                    "Result for the Bacterium": "Translation never gets started"
                },
                "Dalfopristin plus quinupristin": {
                    "Step Disrupted": "Early and late phases of protein synthesis",
                    "Result for the Bacterium": "Synergistic blockade leading to cell death"
                },
                "Chloramphenicol": {
                    "Step Disrupted": "Transpeptidation at the 50S subunit alone",
                    "Result for the Bacterium": "Bacteriostatic action"
                }
            }
        },
        {
            "slug": "psi_pharmacokinetics",
            "title": "PSI Pharmacokinetics",
            "subtitle": "Match each agent to its route or bioavailability, distribution or elimination, and CSF penetration",
            "categories": ["Route / Bioavailability", "Distribution or Elimination", "CSF Penetration"],
            "data": {
                "Aminoglycosides": {
                    "Route / Bioavailability": "IV or IM because of poor oral absorption",
                    "Distribution or Elimination": "Eliminated unchanged by the kidneys",
                    "CSF Penetration": "Minimal, like other 30S agents"
                },
                "Tetracyclines": {
                    "Route / Bioavailability": "Oral, IV, or IM",
                    "Distribution or Elimination": "Lipophilic; biliary excretion in urine and feces",
                    "CSF Penetration": "Minimal despite great tissue penetration"
                },
                "Macrolides": {
                    "Route / Bioavailability": "Oral bioavailability 30-50%, set by gastric pH stability",
                    "Distribution or Elimination": "Concentrated in tissues and phagocytic cells",
                    "CSF Penetration": "Poor unless the meninges are inflamed"
                },
                "Clindamycin": {
                    "Route / Bioavailability": "About 90% oral bioavailability",
                    "Distribution or Elimination": "Distributes especially well into bone",
                    "CSF Penetration": "Little CSF penetration"
                },
                "Linezolid": {
                    "Route / Bioavailability": "Excellent oral bioavailability",
                    "Distribution or Elimination": "Hepatically metabolized, like other 50S agents",
                    "CSF Penetration": "Readily enters the CSF"
                }
            }
        },
        {
            "slug": "how_bacteria_fight_back",
            "title": "How Bacteria Fight Back",
            "subtitle": "Match each resistance strategy to what it does, a classic example, and its consequence",
            "categories": ["What the Bacterium Does", "Classic Example", "Consequence"],
            "data": {
                "Enzymatic inactivation": {
                    "What the Bacterium Does": "Chemically modifies the antibiotic itself",
                    "Classic Example": "Gram-negative acetylation of aminoglycosides",
                    "Consequence": "Drug can no longer interact with 16S rRNA"
                },
                "Target site alteration": {
                    "What the Bacterium Does": "Lowers its own ribosome's affinity for the drug",
                    "Classic Example": "erm-mediated methylation of 23S rRNA",
                    "Consequence": "Cross-resistance across macrolides and clindamycin"
                },
                "Efflux pump": {
                    "What the Bacterium Does": "Actively transports the drug out of the cytoplasm",
                    "Classic Example": "TetA antiporter exchanging tetracycline for protons",
                    "Consequence": "Too little drug reaches the ribosome"
                },
                "Transmissible resistance": {
                    "What the Bacterium Does": "Passes resistance genes to other bacteria",
                    "Classic Example": "Horizontal transfer of plasmids",
                    "Consequence": "Resistance spreads through the bacterial population"
                }
            }
        }
    ]
}
