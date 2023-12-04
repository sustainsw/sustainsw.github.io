---
layout: page
title: Opt Out
nav: Opt Out
parent: Research
nav_order: 2
layout: page
---



To opt out please email **plh-tr.researchdataoptout@nhs.net**
and include the following information:
- I want to opt out of (choose one or some of the following studies): 
{% for post in site.posts %}
    - {{ post.title }}
{% endfor %}

    - All of the above
- Forename:

- Surname:

- Date of birth:

- Address:

- NHS number(if known):

- Hospital Number (if known):

- Contact email (optional):

- Contact phone number (optional):



<button onclick="location.href='mailto:plh-tr.researchdataoptout@nhs.net?subject=Subject&body=I want to opt out of xxx';">
    Draft Email
</button>