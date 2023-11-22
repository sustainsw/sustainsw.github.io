---
layout: project
title: Aneuysm clip detection
thumbnail: /assets/img/projects_thumbnail_aneurysm_cxr.png
brief: a brief intro to the project
status: completed
---


{% include project_head.html 
disease_area = "Neuroscience; subarachnoid haemorrhage"
data_sources = "University Hospitals Plymouth NHS Trust (UHPNT)"
project_stage = " Dissemination of results"
ethical_approval = "granted"
principal_investigator = "Mark Thurston"
lead_researcher = "Megan Courtman"
funders = "n/a"
paper_reference = "https://pearl.plymouth.ac.uk/handle/10026.1/21636"
%}


### Summary


![project_img_ces](/assets/img/project_img_ces.png){:width="800px"}

Flagging the presence of metal devices before a head MRI scan is essential to allow appropriate safety checks. There is an unmet need for an automated system which can flag aneurysm clips prior to MRI appointments. We assessed the accuracy with which a machine learning model could detect the presence of an aneurysm clip on CT images, as the vast majority of patients with aneurysm clips have had CT head imaging previously performed as part of their treatment. We trained deep learning models on a dataset of 246 CT head localizers. These are poorer quality scans which precede full CT scans, but in which aneurysm clips can often be clearly seen (see Figure). When tested on an unseen dataset of 24 CT localizers, the trained models classified the presence of aneurysm clips with an average sensitivity of 100% and an average accuracy of 82%. There were no dangerous false negative results; any errors were false positives. We used an explainable AI technique called SHapley Additive exPlanations (SHAP) to calculate and visualise the contribution of individual pixels to the predictions. This highlighted that appropriate regions of interest were informing the models (see Figure). This application could be a useful addition to current processes, enabling automatic safety screening for devices to improve MRI patient safety.


<a href="{% link pages/optout.md%}">
 <button type="button" class="btn btn-primary btn-lg btn-block">Click to Opt Out</button> 
</a>

