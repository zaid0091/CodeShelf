---
title: Deployment Basics
description: Production settings, Gunicorn, WSGI, environment variables, and hosting overview
order: 12
tags: [django, deployment, production]
---

# Chapter 12: Deployment Basics

> **Development ends where production begins — DEBUG off, real database, real server.**

---

## Table of Contents

1. [Dev vs Prod](#dev-vs-prod)
2. [prod settings](#prod-settings)
3. [Gunicorn](#gunicorn)
4. [nginx stack](#nginx-stack)
5. [deploy checklist](#deploy-checklist)
6. [environ](#environ)
7. [logging](#logging)
8. [hosting](#hosting)
9. [health check](#health-check)
10. [docker](#docker)
11. [postgres](#postgres)
12. [HTTPS cookies](#https-cookies)
13. [ALLOWED_HOSTS](#allowed_hosts)
14. [Database connection pooling](#database-connection-pooling)
15. [Static on CDN](#static-on-cdn)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---
## Dev vs Prod

DEBUG, server, DB, static differ.

### Why this matters

Understanding **Dev vs Prod** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Dev vs Prod** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## prod settings

DEBUG=False, ALLOWED_HOSTS, env secrets.

### Why this matters

Understanding **prod settings** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **prod settings** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Gunicorn

gunicorn mysite.wsgi:application

### Why this matters

Understanding **Gunicorn** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Gunicorn** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## nginx stack

SSL, static, proxy to Gunicorn.

### Why this matters

Understanding **nginx stack** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **nginx stack** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## deploy checklist

install migrate collectstatic run.

### Why this matters

Understanding **deploy checklist** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **deploy checklist** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## environ

django-environ for env vars.

### Why this matters

Understanding **environ** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **environ** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## logging

LOGGING to stdout for containers.

### Why this matters

Understanding **logging** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **logging** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## hosting

Railway Render Fly AWS VPS.

### Why this matters

Understanding **hosting** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **hosting** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## health check

Simple 200 OK endpoint.

### Why this matters

Understanding **health check** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **health check** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## docker

Optional Dockerfile CMD gunicorn.

### Why this matters

Understanding **docker** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **docker** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## postgres

Production database choice.

### Why this matters

Understanding **postgres** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **postgres** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## HTTPS cookies

SECURE_SSL_REDIRECT, secure cookies.

### Why this matters

Understanding **HTTPS cookies** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **HTTPS cookies** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## ALLOWED_HOSTS

Required when DEBUG=False — list domain names.

### Why this matters

Understanding **ALLOWED_HOSTS** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **ALLOWED_HOSTS** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Database connection pooling

CONN_MAX_AGE in DATABASES for persistent connections.

### Why this matters

Understanding **Database connection pooling** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Database connection pooling** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Static on CDN

Point STATIC_URL to CDN after collectstatic upload.

### Why this matters

Understanding **Static on CDN** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Static on CDN** in one sentence?
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

**Q: Summarize chapter 12 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 12.1: Hands-on practice

Implement one feature from Chapter 12 in a local project.

<details>
<summary>Click to reveal solution for Exercise 12.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 12.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 12.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 12.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 12.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 12.4: Explain aloud

Explain Chapter 12 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 12.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 12. Here is what you learned:

- Completed Chapter 12: Deployment Basics
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

**➡️ [Next Chapter →](./ch13-best-practices.md)**

---

*Chapter 12 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Deployment Basics

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

## Extended Study Guide: Chapter 12

> Use this section for review, interviews, and spaced repetition after completing **Deployment Basics**.

### Frequently Asked Questions

**Q: What is the main goal of the deployment chapter?**

Master deployment patterns used in every Django project.

**Q: How does this fit MTV?**

Identify which layer (model, view, template) each example touches.

**Q: What is the most common beginner mistake here?**

See Common Mistakes section in the main chapter body.

**Q: What official docs page should I read?**

Search docs.djangoproject.com for deployment.

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

#### Pattern 12.1

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
