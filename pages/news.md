---
layout: page
title: News
nav: News
nav_order: 1
---
<div class="container custom-container">
    {% for post in site.posts %}
      {% if post.categories contains 'news' %}
    <div class="blog-row">
        <div class="col-md-3">
            <div class="blog-block">
                <img src="{{ post.thumbnail }}" style="height: 250px; width: 250px; display: block;" class="img-fluid">
            </div>
        </div>
        <div class="col-md-9">
            <div class="blog-block">
                <h2>{{ post.title }}</h2>
                <p>
                    {{ post.excerpt | strip_html | truncatewords: 50 }}
                </p>
            </div>
            <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <a class="btn btn-sm btn-outline-secondary" href="{{post.url}}" role="button">Read More</a>
                </div>
                <small class="text-muted">{{ post.date | date: "%b %d, %Y" }}</small>
            </div>
        </div>
    </div>
      {% endif %}
    {% endfor %}
</div>