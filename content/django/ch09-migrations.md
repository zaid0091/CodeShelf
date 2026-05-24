---
title: Migrations
description: makemigrations, migrate, migration files, squashing, and data migrations
order: 9
tags: [django, migrations, database]
---

# Chapter 9: Migrations

> **Migrations version-control your database schema — never edit production DB by hand.**

---

## Table of Contents

1. [Migrations Intro](#migrations-intro)
2. [makemigrations migrate](#makemigrations-migrate)
3. [showmigrations sqlmigrate](#showmigrations-sqlmigrate)
4. [Migration structure](#migration-structure)
5. [AddField nullable](#addfield-nullable)
6. [RunPython](#runpython)
7. [squashmigrations](#squashmigrations)
8. [fake rollback](#fake-rollback)
9. [best practices](#best-practices)
10. [conflicts](#conflicts)
11. [zero downtime](#zero-downtime)
12. [testing migrations](#testing-migrations)
13. [RenameField RenameModel](#renamefield-renamemodel)
14. [RunSQL](#runsql)
15. [Migration plan command](#migration-plan-command)
16. [Best Practices](#best-practices)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---
## Migrations Intro

Python files tracking schema versions.

### Why this matters

Understanding **Migrations Intro** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Migrations Intro** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## makemigrations migrate

Create files then apply to database.

### Why this matters

Understanding **makemigrations migrate** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **makemigrations migrate** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## showmigrations sqlmigrate

Status and SQL preview.

### Why this matters

Understanding **showmigrations sqlmigrate** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **showmigrations sqlmigrate** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Migration structure

dependencies and operations list.

### Why this matters

Understanding **Migration structure** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Migration structure** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## AddField nullable

Multi-step for non-null on existing data.

### Why this matters

Understanding **AddField nullable** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **AddField nullable** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## RunPython

Data migrations with apps.get_model.

### Why this matters

Understanding **RunPython** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **RunPython** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## squashmigrations

Combine migration history.

### Why this matters

Understanding **squashmigrations** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **squashmigrations** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## fake rollback

--fake and migrate to older number.

### Why this matters

Understanding **fake rollback** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **fake rollback** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## best practices

Commit migrations; never edit applied.

### Why this matters

Understanding **best practices** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **best practices** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## conflicts

Merge migration files when teams diverge.

### Why this matters

Understanding **conflicts** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **conflicts** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## zero downtime

Nullable first, backfill, enforce constraint.

### Why this matters

Understanding **zero downtime** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **zero downtime** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## testing migrations

Test on copy of production data.

### Why this matters

Understanding **testing migrations** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **testing migrations** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## RenameField RenameModel

Use migration operations instead of manual SQL when renaming.

### Why this matters

Understanding **RenameField RenameModel** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **RenameField RenameModel** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## RunSQL

Escape hatch for raw SQL in migrations — use rarely with reviewed SQL.

### Why this matters

Understanding **RunSQL** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **RunSQL** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Migration plan command

`sqlmigrate app 0001` previews SQL before applying.

### Why this matters

Understanding **Migration plan command** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Migration plan command** in one sentence?
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

**Q: Summarize chapter 9 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 9.1: Hands-on practice

Implement one feature from Chapter 9 in a local project.

<details>
<summary>Click to reveal solution for Exercise 9.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 9.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 9.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 9.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 9.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 9.4: Explain aloud

Explain Chapter 9 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 9.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 9. Here is what you learned:

- Completed Chapter 9: Migrations
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

**➡️ [Next Chapter →](./ch10-static-media-files.md)**

---

*Chapter 9 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Migrations

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

## Extended Study Guide: Chapter 9

> Use this section for review, interviews, and spaced repetition after completing **Migrations**.

### Frequently Asked Questions

**Q: What is the main goal of the migrations chapter?**

Master migrations patterns used in every Django project.

**Q: How does this fit MTV?**

Identify which layer (model, view, template) each example touches.

**Q: What is the most common beginner mistake here?**

See Common Mistakes section in the main chapter body.

**Q: What official docs page should I read?**

Search docs.djangoproject.com for migrations.

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

#### Pattern 9.1

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
