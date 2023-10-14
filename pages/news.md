---
layout: page
title: News
nav: News
nav_order: 1
---

<div class="container">
    {% for post in site.posts %}
    <div class="blog-row">
        <div class="col-md-4">
            <div class="blog-block">
                <img src="{{ post.thumbnail }}" style="height: 225px; width: 100%; display: block;" class="img-fluid">
            </div>
        </div>
        <div class="col-md-8">
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
                <small class="text-muted">{{post.reading_time}}</small>
            </div>
        </div>
    </div>
    {% endfor %}
</div>