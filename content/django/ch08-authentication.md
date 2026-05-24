---
title: Authentication
description: User model, login, logout, permissions, decorators, and custom user models
order: 8
tags: [django, auth, users]
---

# Chapter 8: Authentication

> **Authentication answers who is this user — authorization answers what can they do.**

---

## Table of Contents

1. [Auth Overview](#auth-overview)
2. [User model](#user-model)
3. [Login Logout](#login-logout)
4. [Decorators](#decorators)
5. [Templates user](#templates-user)
6. [Groups](#groups)
7. [AUTH_USER_MODEL](#auth_user_model)
8. [Custom User](#custom-user)
9. [Password validators](#password-validators)
10. [Sessions](#sessions)
11. [Permissions on models](#permissions-on-models)
12. [Object-level permissions](#object-level-permissions)
13. [Password hashing](#password-hashing)
14. [Login required redirect](#login-required-redirect)
15. [UserPassesTestMixin](#userpassestestmixin)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---
## Auth Overview

django.contrib.auth: users, groups, permissions.

### Why this matters

Understanding **Auth Overview** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Auth Overview** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## User model

create_user, create_superuser, set_password.

### Why this matters

Understanding **User model** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **User model** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Login Logout

LoginView, LogoutView, LOGIN_URL settings.

### Why this matters

Understanding **Login Logout** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Login Logout** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Decorators

@login_required, @permission_required.

### Why this matters

Understanding **Decorators** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Decorators** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Templates user

{% if user.is_authenticated %}

### Why this matters

Understanding **Templates user** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Templates user** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Groups

Group permissions assigned to users.

### Why this matters

Understanding **Groups** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Groups** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## AUTH_USER_MODEL

FK to settings.AUTH_USER_MODEL always.

### Why this matters

Understanding **AUTH_USER_MODEL** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **AUTH_USER_MODEL** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Custom User

AbstractUser before first migrate.

### Why this matters

Understanding **Custom User** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Custom User** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Password validators

AUTH_PASSWORD_VALIDATORS list.

### Why this matters

Understanding **Password validators** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Password validators** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Sessions

SESSION_COOKIE_SECURE in production.

### Why this matters

Understanding **Sessions** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Sessions** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Permissions on models

add, change, delete, view per model.

### Why this matters

Understanding **Permissions on models** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Permissions on models** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Object-level permissions

Third-party or custom checks in views.

### Why this matters

Understanding **Object-level permissions** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Object-level permissions** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Password hashing

Django stores hashed passwords — never plain text. `user.check_password('x')`.

### Why this matters

Understanding **Password hashing** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Password hashing** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Login required redirect

`LOGIN_URL` setting where anonymous users go for @login_required.

### Why this matters

Understanding **Login required redirect** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Login required redirect** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## UserPassesTestMixin

CBV: override `test_func()` for custom authorization logic.

### Why this matters

Understanding **UserPassesTestMixin** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **UserPassesTestMixin** in one sentence?
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

**Q: Summarize chapter 8 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 8.1: Hands-on practice

Implement one feature from Chapter 8 in a local project.

<details>
<summary>Click to reveal solution for Exercise 8.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 8.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 8.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 8.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 8.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 8.4: Explain aloud

Explain Chapter 8 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 8.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 8. Here is what you learned:

- Completed Chapter 8: Authentication
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

**➡️ [Next Chapter →](./ch09-migrations.md)**

---

*Chapter 8 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Authentication

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

## Extended Study Guide: Chapter 8

> Use this section for review, interviews, and spaced repetition after completing **Authentication**.

### Frequently Asked Questions

**Q: What is the main goal of the auth chapter?**

Master auth patterns used in every Django project.

**Q: How does this fit MTV?**

Identify which layer (model, view, template) each example touches.

**Q: What is the most common beginner mistake here?**

See Common Mistakes section in the main chapter body.

**Q: What official docs page should I read?**

Search docs.djangoproject.com for auth.

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

#### Pattern 8.1

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
