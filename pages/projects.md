---
title: Projects
nav: Projects
nav_order: 1
---

### Parkinson's disease
Prospective neuroprotective treatments for PD are highlighting the need for early diagnostic tests. MRI is not currently considered a robust imaging test for PD, but exploratory techniques have suggested that dedicated experimental sequences may be able to detect early pathological brain changes. We explored whether such changes might be detectable in routine MRI scans by employing deep learning (DL) methods. This subset of machine learning has recently shown great promise in diagnostic medical imaging, with its potential to detect patterns invisible to the human eye. Emerging explainability methods are allowing DL predictions to be better interpreted.
{% raw %}
   <a href="/pages/test.html">
      <img alt="Parkinson's disease" src="/assets/img/project_pd.png" width="1050" height="300">
   </a>
{% endraw %}

<br/>

### Aneurysm Clip in a CT head
Flagging the presence of metal devices before a head MRI scan is essential to allow
appropriate safety checks. There is an unmet need for an automated system which can
flag aneurysm clips prior to MRI appointments. We assess the accuracy with which a
machine learning model can classify the presence or absence of an aneurysm clip on
CT images. A total of 262 CT head scans were collected, 140 with aneurysm clips
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

{% raw %}
   <a href="/pages/test.html">
      <img alt="Aneurysm Clip in a CT head" src="/assets/img/project_aneurysm_cxr.png" width="700" height="300">
   </a>
{% endraw %}