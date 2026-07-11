BRICK = {
    "brick_num": 31,
    "brick_title": "Renin-Angiotensin-Aldosterone System Inhibitors",
    "games": [
        {
            "slug": "raas_pathway",
            "title": "Steps of the RAAS Pathway",
            "subtitle": "Match each component of the renin-angiotensin-aldosterone system to its source, trigger, and result",
            "categories": ["Source / Origin", "Substrate or Trigger", "Result / Product"],
            "data": {
                "Renin": {
                    "Source / Origin": "Juxtaglomerular cells of the kidney",
                    "Substrate or Trigger": "Low blood pressure, low blood volume, or low renal blood flow",
                    "Result / Product": "Cleaves angiotensinogen into angiotensin I"
                },
                "Angiotensinogen": {
                    "Source / Origin": "Liver",
                    "Substrate or Trigger": "Inactive protein cleaved by renin",
                    "Result / Product": "Serves as the precursor to angiotensin I"
                },
                "ACE": {
                    "Source / Origin": "Lungs (pulmonary endothelium)",
                    "Substrate or Trigger": "Acts on angiotensin I",
                    "Result / Product": "Converts angiotensin I into angiotensin II"
                },
                "Angiotensin II": {
                    "Source / Origin": "Formed from angiotensin I by ACE",
                    "Substrate or Trigger": "Binds angiotensin II type 1 receptors",
                    "Result / Product": "Causes vasoconstriction and raises blood pressure"
                },
                "Aldosterone": {
                    "Source / Origin": "Adrenal gland (adrenal cortex)",
                    "Substrate or Trigger": "Released in response to angiotensin II",
                    "Result / Product": "Promotes sodium and water retention, raising blood volume"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "Adverse Effects of RAAS Inhibitors",
            "subtitle": "Match each adverse effect to its mechanism, clinical feature, and key association",
            "categories": ["Underlying Mechanism", "Key Clinical Feature", "Notable Association"],
            "data": {
                "Hyperkalemia": {
                    "Underlying Mechanism": "Reduced aldosterone lowers renal tubular potassium secretion",
                    "Key Clinical Feature": "Elevated serum potassium and potassium retention",
                    "Notable Association": "Worse with potassium-sparing diuretics or chronic kidney disease"
                },
                "Acute Kidney Injury": {
                    "Underlying Mechanism": "Efferent arteriole dilation lowers glomerular filtration rate",
                    "Key Clinical Feature": "Prerenal drop in GFR within the first days of therapy",
                    "Notable Association": "Precipitated by dehydration, heart failure, or NSAIDs"
                },
                "Dry Cough": {
                    "Underlying Mechanism": "Bradykinin accumulation from ACE inhibition",
                    "Key Clinical Feature": "Persistent dry, hacking cough",
                    "Notable Association": "Switching to an ARB has a lower incidence"
                },
                "Angioedema": {
                    "Underlying Mechanism": "Bradykinin drives substance P release and tissue swelling",
                    "Key Clinical Feature": "Swelling of the face, lips, tongue, and airway",
                    "Notable Association": "About 4.5 times higher risk in African American patients"
                }
            }
        },
        {
            "slug": "indications",
            "title": "Clinical Indications for RAAS Inhibitors",
            "subtitle": "Match each indication to the benefit provided, typical co-therapy, and mechanistic rationale",
            "categories": ["Primary Benefit", "Typical Co-therapy", "Mechanistic Rationale"],
            "data": {
                "Hypertension": {
                    "Primary Benefit": "Lowers blood pressure (most common indication)",
                    "Typical Co-therapy": "Used alone or with a diuretic",
                    "Mechanistic Rationale": "Blocks angiotensin II-driven vasoconstriction"
                },
                "Heart Failure": {
                    "Primary Benefit": "Prevents ventricular fibrosis and abnormal cardiac remodeling",
                    "Typical Co-therapy": "Beta-blockers and loop diuretics",
                    "Mechanistic Rationale": "Reduces the harmful cardiac effects of angiotensin II"
                },
                "Ischemic Heart Disease (post-MI)": {
                    "Primary Benefit": "Prevents post-MI fibrosis and remodeling",
                    "Typical Co-therapy": "Aspirin, statins, and beta-blockers",
                    "Mechanistic Rationale": "Limits maladaptive remodeling after myocardial infarction"
                },
                "Chronic Kidney Disease with Proteinuria": {
                    "Primary Benefit": "Reduces proteinuria and microalbuminuria",
                    "Typical Co-therapy": "Part of an overall blood-pressure control plan",
                    "Mechanistic Rationale": "Lowers glomerular hydrostatic pressure by dilating the efferent arteriole"
                }
            }
        },
        {
            "slug": "contra_interactions",
            "title": "Contraindications and Drug Interactions",
            "subtitle": "Match each factor to its type, the reason behind it, and the resulting risk",
            "categories": ["Type", "Reason", "Resulting Risk"],
            "data": {
                "Pregnancy": {
                    "Type": "Contraindication",
                    "Reason": "The drugs are teratogenic to the fetus",
                    "Resulting Risk": "Fetal kidney injury"
                },
                "Bilateral Renal Artery Stenosis": {
                    "Type": "Contraindication",
                    "Reason": "Kidneys depend on efferent constriction due to low renal blood flow",
                    "Resulting Risk": "Declining renal function"
                },
                "NSAIDs": {
                    "Type": "Drug interaction",
                    "Reason": "Block prostaglandin-driven dilation of the afferent arteriole",
                    "Resulting Risk": "Acute kidney injury"
                },
                "Potassium-Sparing Diuretics": {
                    "Type": "Drug interaction",
                    "Reason": "Additive reduction in renal potassium excretion",
                    "Resulting Risk": "Hyperkalemia"
                },
                "Combining an ACE Inhibitor with an ARB": {
                    "Type": "Should be avoided",
                    "Reason": "Provides no additional clinical benefit",
                    "Resulting Risk": "Additive hyperkalemia, acute kidney injury, and angioedema"
                }
            }
        }
    ]
}
