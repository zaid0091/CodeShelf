---
title: Templates
description: Django template language, inheritance, context, filters, and tags
order: 5
tags: [django, templates, dtl]
---

# Chapter 5: Templates

## 5.1 Template system overview

> **Definition:** Django **templates** are text files (usually HTML) with placeholders and logic tags. Views pass a **context** dict; the engine renders final HTML.

Configured in `settings.py` `TEMPLATES` — `APP_DIRS=True` loads `app/templates/`.

## 5.2 Template file layout

```text
blog/
└── templates/
    └── blog/
        ├── base.html
        ├── post_list.html
        └── post_detail.html
```

Namespace folders (`blog/`) avoid name collisions between apps.

## 5.3 Basic syntax

```django
{# comment #}
{{ variable }}
{{ post.title|truncatewords:10 }}
{% tag %}
```

| Syntax | Purpose |
|--------|---------|
| `{{ }}` | Output variable |
| `{% %}` | Logic tags |
| `{# #}` | Comments |
| `\|filter` | Transform value |

## 5.4 Template inheritance

```django
{# blog/templates/blog/base.html #}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}Blog{% endblock %}</title>
</head>
<body>
  <nav>...</nav>
  <main>{% block content %}{% endblock %}</main>
</body>
</html>
```

```django
{# post_list.html #}
{% extends "blog/base.html" %}

{% block title %}Posts{% endblock %}

{% block content %}
  <h1>Posts</h1>
  {% for post in posts %}
    <article>
      <h2><a href="{% url 'post-detail' pk=post.pk %}">{{ post.title }}</a></h2>
      <p>{{ post.body|truncatewords:30 }}</p>
    </article>
  {% empty %}
    <p>No posts yet.</p>
  {% endfor %}
{% endblock %}
```

## 5.5 Common tags

```django
{% if user.is_authenticated %}
  Hello, {{ user.username }}
{% else %}
  Please log in
{% endif %}

{% for item in items %}
  {{ forloop.counter }} — {{ item }}
{% endfor %}

{% include "blog/partials/pagination.html" %}
{% load static %}
<img src="{% static 'blog/logo.png' %}" alt="Logo">
```

| Tag | Purpose |
|-----|---------|
| `extends` | Inherit base template |
| `block` | Overridable region |
| `for` / `empty` | Loop with empty fallback |
| `if` / `elif` / `else` | Conditionals |
| `url` | Reverse named URL |
| `include` | Partial template |
| `static` | Static file URL |

## 5.6 Common filters

```django
{{ name|lower }}
{{ text|truncatewords:20 }}
{{ value|default:"N/A" }}
{{ created_at|date:"Y-m-d" }}
{{ html|safe }}  {# only trusted content! #}
{{ items|length }}
{{ price|floatformat:2 }}
```

## 5.7 Context from views

```python
return render(request, "blog/post_list.html", {
    "posts": posts,
    "page_title": "Latest Posts",
})
```

Context processors add global variables (`request`, `user`, `messages`).

## 5.8 Custom template tags (overview)

```python
# blog/templatetags/blog_extras.py
from django import template

register = template.Library()

@register.filter
def markdown(value):
    return render_markdown(value)
```

```django
{% load blog_extras %}
{{ post.body|markdown }}
```

## 5.9 CSRF in templates

Forms posting to Django must include:

```django
<form method="post">
  {% csrf_token %}
  ...
</form>
```

See [Forms](./ch06-forms.md).

## 5.10 Messages framework

```python
from django.contrib import messages

messages.success(request, "Post saved.")
```

```django
{% if messages %}
  {% for message in messages %}
    <div class="alert">{{ message }}</div>
  {% endfor %}
{% endif %}
```

## Exercises

1. Create `base.html` with blocks for title and content.
2. Build `post_list.html` and `post_detail.html` extending base.
3. Use `{% url %}`, `truncatewords`, and `{% empty %}`.
4. Add `{% load static %}` and reference an image.

## Summary

Templates separate presentation from views. Use inheritance, built-in tags/filters, and named URLs for maintainable HTML.

## Next chapter

Continue to [Forms](./ch06-forms.md).
