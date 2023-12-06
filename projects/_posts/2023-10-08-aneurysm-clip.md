---
layout: project
title: Aneurysm clip detection
thumbnail: /assets/img/projects_thumbnail_aneurysm_cxr.png
brief: automated aneurysm clip detection
status: completed
---


{% include project_head.html 
disease_area = "MRI safety; neuroscience; subarachnoid haemorrhage"
data_sources = '<a href="https://www.plymouthhospitals.nhs.uk/">University Hospitals Plymouth</a>; 
<a href="https://www.royalcornwall.nhs.uk/">Royal Cornwall Hospitals</a>'
project_stage = "Results accepted for publication"
ethical_approval = "Granted"
principal_investigator = "Mark Thurston"
lead_researcher = "Megan Courtman"
funders = '<a href="https://royalcornwallhospitals.nhs.uk/">Royal Cornwall Hospitals NHS Trust</a>'
%}


### Summary

Flagging the presence of intracranial surgical clips for aneurysms before an MRI
scan is essential to allow appropriate safety checks to take place.

This project assessed the accuracy with which a machine learning model could
classify the presence or absence of intracranial aneurysm clips on pre-existing
imaging data.

![CT localiser image with a aneurysm clip
highlighted](/assets/img/project_img_ces.png){:width="600px"}

This project analysed a total of 246 CT head studies, half of which 
had aneurysm clips present. An explainable AI technique called SHapley Additive 
exPlanations (SHAP) was used to calculate and visualise the contribution of 
individual pixels to the predictions. This highlighted that appropriate regions 
of interest were informing the output of the models.

The model could be used to screen for patients requiring additional safety
input before MRI scan appointments.

The focus of many healthcare applications of computer vision techniques has
been for diagnosis and guiding management. This work illustrates an application
of computer vision image classification to enhance current processes and
improve patient safety.

The results have been accepted for publication in the [Journal for Digital
Imaging](https://link.springer.com/journal/10278).

