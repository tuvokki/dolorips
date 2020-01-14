Title: {{ title }}
Date: {{ date }}
Category: {{ category }}
Tags: {{ tags }}
source_path: {{ category.lower() }}/{{ name }}.md
{% if draft %}status: draft{% endif %}

# {{ title }}

{% for item in contents %}{{ item }}

{% endfor %}
