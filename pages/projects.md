---
layout: page
title: Projects
parent: Research
nav: Projects
nav_order: 1
---

<div class="container custom-container">

  <div class="row">
    {% for post in site.posts %}
      {% if post.categories contains 'projects' %}

  <div class="col-sm-4 top-buffer">
   <div class="card pt-1" style="width: 305px">
   <a href="{{post.url}}">
    <img class="card-img-top" src="{{ post.thumbnail }}" style="height: 300px; width: 300px; display: block;" class="img-fluid">
   </a>
    <div class="card-body pt-1">
      <h5 class="card-title">{{ post.title }}</h5>
      <a href="{{post.url}}" class="btn btn-primary">See details</a>
    </div>
   </div> 
  </div>
        {% endif %}
    {% endfor %}
   </div> 
</div>