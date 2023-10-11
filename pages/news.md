---
layout: page
title: News
nav: News
nav_order: 1
---


<div class="container">
    <div class="row">
        {% for post in site.posts %}
        <div class="col-md-12">
            <div class="card mb-12 box-shadow">
                <img class="card-img-top"
                    data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail"
                    alt="Thumbnail [100%x225]" style="height: 225px; width: 100%; display: block;"
                    src="{{ post.thumbnail }}" data-holder-rendered="true">
                <div class="card-body">
                    <p class="card-text">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <button type="button" class="btn btn-sm btn-outline-secondary">Read More</button>
                        </div>
                        <small class="text-muted">9 mins</small>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
