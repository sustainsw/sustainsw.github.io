---
layout: project
title: Aneurysm Clip
thumbnail: /assets/img/projects_thumbnail_aneurysm_cxr.png
brief: a brief intro to the project
---


Flagging the presence of metal devices before a head MRI scan is essential to allow
appropriate safety checks. There is an unmet need for an automated system which can
flag aneurysm clips prior to MRI appointments. We assess the accuracy with which a
machine learning model can classify the presence or absence of an aneurysm clip on
CT images. 
A total of 262 CT head scans were collected, 140 with aneurysm clips
visible and 122 without. The data were used to retrain a pre-trained image
classification neural network to classify CT localizer images. Models were developed
using five-fold cross-validation and then tested on a holdout test set. A mean sensitivity
of 100\% and a mean Receiver Operating Characteristic area-under-the-curve of 0.99
were achieved. Predictions were explained using SHapley Additive exPlanations
(SHAP), which highlighted that appropriate regions of interest were informing the
models. Models were also trained from scratch to classify three-dimensional CT head
scans. These did not exceed the accuracy of the localizer models. This work illustrates
an application of computer vision image classification to enhance current processes
and improve patient safety.


<a href="{% link pages/optout.md%}">
 <button type="button" class="btn btn-primary btn-lg btn-block">Click to Opt Out</button> 
</a>

