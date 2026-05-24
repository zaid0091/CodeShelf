---
title: Static and Media Files
description: STATIC_URL, MEDIA_URL, collectstatic, serving files in dev and production
order: 10
tags: [django, static, media]
---

# Chapter 10: Static and Media Files

> **Static files ship with your code; media files are uploaded by users — configure both correctly.**

---

## Table of Contents

1. [Static vs Media](#static-vs-media)
2. [STATIC settings](#static-settings)
3. [static tag](#static-tag)
4. [collectstatic](#collectstatic)
5. [MEDIA settings](#media-settings)
6. [FileField](#filefield)
7. [dev serving](#dev-serving)
8. [production](#production)
9. [Whitenoise](#whitenoise)
10. [storages S3](#storages-s3)
11. [findstatic](#findstatic)
12. [cache busting](#cache-busting)
13. [STATICFILES_FINDERS](#staticfiles_finders)
14. [ImageField Pillow](#imagefield-pillow)
15. [Private media](#private-media)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---
## Static vs Media

Static from repo; media from users.

### Why this matters

Understanding **Static vs Media** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Static vs Media** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## STATIC settings

STATIC_URL, STATICFILES_DIRS, STATIC_ROOT.

### Why this matters

Understanding **STATIC settings** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **STATIC settings** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## static tag

{% load static %}{% static 'path' %}

### Why this matters

Understanding **static tag** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **static tag** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## collectstatic

Gather files for production.

### Why this matters

Understanding **collectstatic** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **collectstatic** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## MEDIA settings

MEDIA_URL, MEDIA_ROOT.

### Why this matters

Understanding **MEDIA settings** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **MEDIA settings** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## FileField

upload_to path on model.

### Why this matters

Understanding **FileField** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **FileField** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## dev serving

static() in urls when DEBUG.

### Why this matters

Understanding **dev serving** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **dev serving** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## production

nginx or S3, not Django for scale.

### Why this matters

Understanding **production** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **production** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Whitenoise

Middleware for static on PaaS.

### Why this matters

Understanding **Whitenoise** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Whitenoise** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## storages S3

django-storages backend.

### Why this matters

Understanding **storages S3** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **storages S3** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## findstatic

Debug path resolution.

### Why this matters

Understanding **findstatic** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **findstatic** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## cache busting

ManifestStaticFilesStorage hashed names.

### Why this matters

Understanding **cache busting** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **cache busting** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## STATICFILES_FINDERS

FileSystemFinder + AppDirectoriesFinder locate static files.

### Why this matters

Understanding **STATICFILES_FINDERS** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **STATICFILES_FINDERS** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## ImageField Pillow

pip install Pillow for ImageField support.

### Why this matters

Understanding **ImageField Pillow** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **ImageField Pillow** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Private media

Do not expose private uploads under public MEDIA_URL; use signed URLs.

### Why this matters

Understanding **Private media** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Private media** in one sentence?
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

**Q: Summarize chapter 10 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 10.1: Hands-on practice

Implement one feature from Chapter 10 in a local project.

<details>
<summary>Click to reveal solution for Exercise 10.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 10.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 10.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 10.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 10.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 10.4: Explain aloud

Explain Chapter 10 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 10.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 10. Here is what you learned:

- Completed Chapter 10: Static and Media Files
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

**➡️ [Next Chapter →](./ch11-class-based-views.md)**

---

*Chapter 10 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Static and Media Files

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

## Extended Study Guide: Chapter 10

> Use this section for review, interviews, and spaced repetition after completing **Static and Media Files**.

### Frequently Asked Questions

**Q: What is the main goal of the static files chapter?**

Master static files patterns used in every Django project.

**Q: How does this fit MTV?**

Identify which layer (model, view, template) each example touches.

**Q: What is the most common beginner mistake here?**

See Common Mistakes section in the main chapter body.

**Q: What official docs page should I read?**

Search docs.djangoproject.com for static files.

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

#### Pattern 10.1

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
