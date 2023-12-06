---
layout: page
title: Announcements
parent: News
nav: Announcements
nav_order: 10
---

<!-- <a href="https://twitter.com/plymUni?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-lang="en" data-dnt="true"
    data-show-count="false">Follow @plymUni</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> -->

<!-- <a class="twitter-timeline" href="https://twitter.com/PlymUni?ref_src=twsrc%5Etfw">Tweets by PlymUni</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> -->

### News
<div class="container custom-container">
    {% for post in site.posts %}
      {% if post.categories contains 'news' %}
    <div class="blog-row">
        <div class="col-md-3 d-flex align-items-center">
            <div class="blog-block">
                <img src="{{ post.thumbnail }}" style="width: 250px; display: block;" class="img-fluid">
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
