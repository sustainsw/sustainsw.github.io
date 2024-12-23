---
layout: page
title: Projects
parent: Research
nav: Projects
nav_order: 5
---
### Active

<div class="container custom-container">

  <div class="row">
    {% for post in site.posts %}
      {% if post.categories contains 'projects' %}
        {% if post.status contains 'active' %}
          <div class="col-sm-4 top-buffer">
            <div class="card pt-1" style="width: 305px">
              <a href="{{post.url}}">
                <img class="card-img-top" src="{{ post.thumbnail }}" style="height: 300px; width: 300px; display: block;" class="img-fluid">
              </a>
              <div class="card-body pt-1">
                <h6 class="card-title">{{ post.title }}</h6>
                <div class="d-flex justify-content-between">
                  <a href="{{post.url}}" class="btn btn-primary"  target="_blank">Details</a>
                  {% if post.website %}
                    <a href="{{post.website}}" class="btn btn-primary"  target="_blank">Website</a>
                  {% endif %}
                </div>
              </div>
            </div>
          </div>
        {% endif %}
      {% endif %}
    {% endfor %}
  </div>
</div>



### Completed

<div class="container custom-container">

  <div class="row">
    {% for post in site.posts %}
      {% if post.categories contains 'projects' %}
      {% if post.status contains 'completed' %}
  <div class="col-sm-4 top-buffer">
   <div class="card pt-1" style="width: 305px">
   <a href="{{post.url}}">
    <img class="card-img-top" src="{{ post.thumbnail }}" style="height: 300px; width: 300px; display: block;" class="img-fluid">
   </a>
    <div class="card-body pt-1">
      <h6 class="card-title">{{ post.title }}</h6>
      <a href="{{post.url}}" class="btn btn-primary" target="_blank">Details</a>
    </div>
   </div>
  </div>
  {% endif %}
        {% endif %}
    {% endfor %}
   </div>
</div>
