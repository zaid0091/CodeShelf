---
title: Templates
description: Django template language, inheritance, context, filters, and tags
order: 5
tags: [django, templates, dtl]
---

# Chapter 5: Templates

> **Templates turn data into HTML — learn the Django Template Language (DTL) properly.**

---

## Table of Contents

1. [Template System Overview](#template-system-overview)
2. [Template Layout and Namespaces](#template-layout-and-namespaces)
3. [Syntax: Variables Tags Comments](#syntax:-variables-tags-comments)
4. [Inheritance and Blocks](#inheritance-and-blocks)
5. [Loops and Conditionals](#loops-and-conditionals)
6. [url and static Tags](#url-and-static-tags)
7. [Filters Reference](#filters-reference)
8. [Context and Processors](#context-and-processors)
9. [Custom Tags and Filters](#custom-tags-and-filters)
10. [CSRF in Forms](#csrf-in-forms)
11. [XSS and Escaping](#xss-and-escaping)
12. [Debugging Templates](#debugging-templates)
13. [Including Partials](#including-partials)
14. [Template Loaders](#template-loaders)
15. [Built-in Template Reference](#built-in-template-reference)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---
## Template System Overview

> **Definition:** Templates separate presentation from Python logic.

Django Template Language avoids arbitrary Python in HTML for security. Views call `render(request, template, context)`.

### Why this matters

Understanding **Template System Overview** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Template System Overview** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Template Layout and Namespaces

```text
blog/templates/blog/post_list.html
```

App name subfolder prevents template name collisions.

### Why this matters

Understanding **Template Layout and Namespaces** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Template Layout and Namespaces** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Syntax: Variables Tags Comments

```django
{{ post.title }}
{% if user.is_authenticated %}{% endif %}
{# comment #}
```

### Why this matters

Understanding **Syntax: Variables Tags Comments** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Syntax: Variables Tags Comments** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Inheritance and Blocks

```django
{% extends "blog/base.html" %}
{% block content %}...{% endblock %}
```

### Why this matters

Understanding **Inheritance and Blocks** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Inheritance and Blocks** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Loops and Conditionals

```django
{% for post in posts %}{{ forloop.counter }}{% empty %}No posts{% endfor %}
```

### Why this matters

Understanding **Loops and Conditionals** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Loops and Conditionals** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## url and static Tags

```django
{% url 'post-detail' pk=post.pk %}
{% load static %}
<link href="{% static 'css/style.css' %}">
```

### Why this matters

Understanding **url and static Tags** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **url and static Tags** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Filters Reference

| Filter | Use |
|--------|-----|
| date | Format datetime |
| default | Fallback |
| truncatewords | Shorten text |

### Why this matters

Understanding **Filters Reference** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Filters Reference** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Context and Processors

Context processors inject `user`, `request`, `messages` globally.

### Why this matters

Understanding **Context and Processors** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Context and Processors** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Custom Tags and Filters

Create `templatetags/` module with `@register.filter`.

### Why this matters

Understanding **Custom Tags and Filters** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Custom Tags and Filters** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## CSRF in Forms

`{% csrf_token %}` required on POST forms.

### Why this matters

Understanding **CSRF in Forms** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **CSRF in Forms** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## XSS and Escaping

Auto-escape in `{{ }}`. Never `|safe` on user content.

### Why this matters

Understanding **XSS and Escaping** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **XSS and Escaping** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Debugging Templates

Read TemplateDoesNotExist searched paths list.

### Why this matters

Understanding **Debugging Templates** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Debugging Templates** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Including Partials

```django
{% include "blog/partials/pagination.html" %}
```

Pass context with `with`:`{% include "x" with foo=bar %}`.

### Why this matters

Understanding **Including Partials** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Including Partials** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Template Loaders

Filesystem and app_directories loaders search DIRS then each app's templates/.

### Why this matters

Understanding **Template Loaders** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Template Loaders** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Built-in Template Reference

Bookmark Django docs: Built-in template tags and filters. Learn `widthratio`, `yesno`, `pluralize` when needed.

### Why this matters

Understanding **Built-in Template Reference** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Built-in Template Reference** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Best Practices

Apply conventions from this chapter consistently.

See also [Best Practices](./ch13-best-practices.md) for project-wide standards.

- Read official docs for your Django version
- Keep views thin and models focused
- Use named URLs everywhere
- Run `python manage.py check` before commits

---

## Common Mistakes

Many beginners hit the same walls. Learn from these early.

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
| Skipping docs | Reinvent wrong patterns | Read django docs for this topic |
| Copy-paste without understanding | Mystery bugs | Type code yourself |
| No tests | Regressions ship | Write tests for critical paths |
| Ignoring security defaults | Vulnerabilities | Keep CSRF and auth middleware enabled |
| Hard-coded URLs | Breaks on URL change | Use reverse and {% url %} |

---

## Interview Points

**Q: Summarize chapter 5 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 5.1: Hands-on practice

Implement one feature from Chapter 5 in a local project.

<details>
<summary>Click to reveal solution for Exercise 5.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 5.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 5.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 5.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 5.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 5.4: Explain aloud

Explain Chapter 5 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 5.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 5. Here is what you learned:

- Completed Chapter 5: Templates
- Reviewed core patterns and examples
- Practiced with exercises

### Key rules to remember

```
✅ Practice in a real project
✅ Use official docs
❌ Skip migrations
❌ Disable security middleware in production
```

---

## Next Chapter

Continue to the next chapter.

**➡️ [Next Chapter →](./ch06-forms.md)**

---

*Chapter 5 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Templates

### Glossary

| Term | Definition |
|------|------------|
| Django | High-level Python web framework |
| MTV | Model-Template-View architecture |
| ORM | Object-Relational Mapper for database access |
| QuerySet | Lazy database query representation |
| Migration | Version-controlled schema change file |

### Self-check questions

1. Can you explain this chapter's main idea in two sentences?
2. Can you write the key code patterns from memory?
3. Can you debug one common error mentioned in Common Mistakes?

### Command reference

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py test
```
---

## Extended Study Guide: Chapter 5

> Use this section for review, interviews, and spaced repetition after completing **Templates**.

### Frequently Asked Questions

**Q: What is the main goal of the DTL chapter?**

Master DTL patterns used in every Django project.

**Q: How does this fit MTV?**

Identify which layer (model, view, template) each example touches.

**Q: What is the most common beginner mistake here?**

See Common Mistakes section in the main chapter body.

**Q: What official docs page should I read?**

Search docs.djangoproject.com for DTL.

**Q: How do I practice effectively?**

Build a small blog feature using only this chapter's patterns.

**Q: What breaks in production vs development?**

Settings like DEBUG, static/media serving, and security flags.

**Q: How is this tested?**

Use Django TestCase and Client to assert responses.

**Q: What interview questions appear?**

See Interview Points in the main chapter.

**Q: How does this connect to the next chapter?**

Read the Next Chapter link at the bottom.

**Q: What command validates my project?**

python manage.py check


### Step-by-Step Walkthrough

1. Re-read the chapter Table of Contents.
2. For each section, write a one-sentence summary in your notes.
3. Complete all four exercises without peeking at solutions first.
4. Break something on purpose and fix it using error messages.
5. Cross-link concepts to prior chapters (models, views, templates).
6. Optional: teach the chapter outline to someone else in 5 minutes.

### Additional Code Patterns

#### Pattern 5.1

```python
# Practice pattern
# See main chapter for full examples
```

### Review checklist

```text
[ ] I can explain the main concepts without notes
[ ] I typed the code examples myself
[ ] I completed all exercises
[ ] I fixed at least one error using the traceback
[ ] I read the linked official Django documentation
```
