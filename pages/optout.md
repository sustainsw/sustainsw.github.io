---
layout: page
title: Opt-out
nav: Opt-out
parent: Research
nav_order: 2
layout: page
---

To opt-out, please [email
plh-tr.researchdataoptout@nhs.net](mailto:plh-tr.researchdataoptout@nhs.net?subject=Opt-out),
including the following:

- I want to opt-out of (choose one or more of the following studies): 
{% for post in site.posts %}
    - {{ post.title }}
{% endfor %}
    - All of the above

- Name

- Date of birth

- Address

- NHS number (if known)

- Hospital Number (if known)

- Contact email (optional)

- Contact phone number (optional)

