---
layout: page
title: Event SDK

---

Download the SDKs [here](/developers/downloads/).

{% for platform in site.data.platforms %}
{% capture thecycle %}{% cycle 'odd', 'even' %}{% endcapture %}
{% if thecycle == 'odd' %}
<div class="row">
{% endif %}
<div class="card col-xm-12 col-sm-12 col-md-12 col-lg-6">
    <div class="header">
        <h2>
            <a href="{{platform.path}}" title="{{platform.title}} overview">{{platform.title}}</a>
        </h2>
    </div>
    <div class="toc">
        <ul>
            {% if platform.tutorial %}<li><a href="{{platform.tutorial}}" title="Get started for {{platform.title}}">Get started{% if platform.tutorial == "#" %} (Coming soon){% endif %}</a></li>{% endif %}
            {% if platform.path %}<li><a href="{{platform.path}}" title="API Reference for {{platform.title}}">API Reference{% if platform.path == "#" %} (Coming soon){% endif %}</a></li>{% endif %}
        </ul>
    </div>
</div>
{% if thecycle == 'even' %}
</div>
{% endif %}
{% endfor %}
