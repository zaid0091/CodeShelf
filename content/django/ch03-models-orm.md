---
title: Models and ORM
description: Model fields, relationships, QuerySets, lookups, and managers
order: 3
tags: [django, orm, models]
---

# Chapter 3: Models and ORM

> **Models are the heart of Django — they define your data and how you query it.**

---

## Table of Contents

1. [What is the ORM?](#what-is-the-orm?)
2. [Defining Your First Model](#defining-your-first-model)
3. [Common Field Types](#common-field-types)
4. [Field Options: null, blank, default](#field-options:-null,-blank,-default)
5. [Relationships: ForeignKey, M2M, OneToOne](#relationships:-foreignkey,-m2m,-onetoone)
6. [CRUD with the ORM](#crud-with-the-orm)
7. [QuerySets and Laziness](#querysets-and-laziness)
8. [Field Lookups](#field-lookups)
9. [Q Objects and F Expressions](#q-objects-and-f-expressions)
10. [Aggregation and Annotation](#aggregation-and-annotation)
11. [Custom Managers](#custom-managers)
12. [select_related and prefetch_related](#select_related-and-prefetch_related)
13. [Model Meta Options](#model-meta-options)
14. [Best Practices](#best-practices)
15. [Common Mistakes](#common-mistakes)
16. [Interview Points](#interview-points)
17. [Exercises](#exercises)
18. [Chapter Summary](#chapter-summary)

---
## What is the ORM?

> **Definition:** The **Object-Relational Mapper (ORM)** maps Python classes to database tables and instances to rows. You query with Python instead of writing SQL for most operations.

```python
Post.objects.filter(published=True)
```

Translates roughly to:

```sql
SELECT * FROM blog_post WHERE published = true;
```

Benefits:
- Database-agnostic code (switch SQLite to PostgreSQL with settings change)
- Protection against SQL injection when using ORM APIs
- Migrations keep schema in sync with models

Raw SQL is still available when needed: `Post.objects.raw("SELECT ...")`.

### Why this matters

Understanding **What is the ORM?** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **What is the ORM?** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Defining Your First Model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title
```

| Piece | Purpose |
|-------|---------|
| `class Post(models.Model)` | Defines table `blog_post` |
| `__str__` | Human-readable in admin/shell |
| `Meta.ordering` | Default sort for QuerySets |
| `auto_now_add` | Set once on create |
| `auto_now` | Updated every save |

### Why this matters

Understanding **Defining Your First Model** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Defining Your First Model** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Common Field Types

| Field | Database | Use case |
|-------|----------|----------|
| `CharField` | VARCHAR | Titles, names (requires `max_length`) |
| `TextField` | TEXT | Long content |
| `IntegerField` | INTEGER | Counts |
| `PositiveIntegerField` | INTEGER | Views, ratings (>=0) |
| `BooleanField` | BOOLEAN | Flags |
| `DateField` | DATE | Birth dates |
| `DateTimeField` | TIMESTAMP | Created/updated |
| `EmailField` | VARCHAR | Emails (validation) |
| `URLField` | VARCHAR | URLs |
| `SlugField` | VARCHAR | URL segments |
| `DecimalField` | DECIMAL | Money (`max_digits`, `decimal_places`) |
| `JSONField` | JSON | Flexible metadata |
| `FileField` / `ImageField` | path | Uploads (needs Pillow for images) |

```python
price = models.DecimalField(max_digits=10, decimal_places=2)
metadata = models.JSONField(default=dict, blank=True)
```

### Why this matters

Understanding **Common Field Types** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Common Field Types** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Field Options: null, blank, default

| Option | Layer | Meaning |
|--------|-------|---------|
| `null=True` | Database | Column allows NULL |
| `blank=True` | Validation | Forms may leave empty |
| `default` | Both | Value when not provided |
| `unique=True` | Database | Unique constraint |
| `db_index=True` | Database | Index for faster lookups |
| `choices` | Validation | Limited allowed values |

```python
STATUS = [("draft", "Draft"), ("published", "Published")]

status = models.CharField(max_length=20, choices=STATUS, default="draft")
```

**String fields:** prefer `blank=True` without `null=True` (Django convention: empty string, not NULL).

**Non-string optional fields:** use both `null=True, blank=True`.

### Why this matters

Understanding **Field Options: null, blank, default** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Field Options: null, blank, default** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Relationships: ForeignKey, M2M, OneToOne

```python
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    tags = models.ManyToManyField(Tag, blank=True)
```

| Type | Cardinality | Reverse accessor |
|------|-------------|------------------|
| `ForeignKey` | many-to-one | `author.posts.all()` |
| `ManyToManyField` | many-to-many | `tag.post_set.all()` |
| `OneToOneField` | one-to-one | `user.profile` |

### on_delete (required on ForeignKey)

| Value | Behavior |
|-------|----------|
| `CASCADE` | Delete children when parent deleted |
| `PROTECT` | Raise error if children exist |
| `SET_NULL` | Set FK null (needs `null=True`) |
| `SET_DEFAULT` | Set to default value |

### Why this matters

Understanding **Relationships: ForeignKey, M2M, OneToOne** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Relationships: ForeignKey, M2M, OneToOne** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## CRUD with the ORM

### Create

```python
post = Post.objects.create(title="Hello", body="World", slug="hello")
# or
post = Post(title="Hi", body="...")
post.save()
```

### Read

```python
Post.objects.all()
Post.objects.get(pk=1)
Post.objects.filter(published=True)
Post.objects.filter(title__icontains="django")
Post.objects.exclude(published=False)
Post.objects.order_by("-created_at")[:10]
```

### Update

```python
post.title = "Updated"
post.save()
Post.objects.filter(pk=1).update(published=True)
```

### Delete

```python
post.delete()
Post.objects.filter(published=False).delete()
```

> `get()` raises `DoesNotExist` if 0 rows and `MultipleObjectsReturned` if >1. Use `filter().first()` when unsure.

### Why this matters

Understanding **CRUD with the ORM** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **CRUD with the ORM** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## QuerySets and Laziness

> **Definition:** A **QuerySet** is a lazy collection of model instances. The database query runs when you **evaluate** the QuerySet.

Evaluation triggers:
- Iteration: `for post in posts`
- `list(posts)`, `len(posts)`
- `bool(posts)` in `if posts`
- slicing with step (sometimes)
- `print(posts.query)` after evaluation

```python
qs = Post.objects.filter(published=True)  # no SQL yet
for p in qs:  # SQL runs here
    print(p.title)
```

Chaining returns new QuerySets:

```python
Post.objects.filter(published=True).order_by("-created_at").select_related("author")
```

### Why this matters

Understanding **QuerySets and Laziness** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **QuerySets and Laziness** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Field Lookups

Double underscore: `field__lookup=value`

```python
Post.objects.filter(views__gte=100)
Post.objects.filter(title__startswith="Django")
Post.objects.filter(created_at__year=2024)
Post.objects.filter(email__isnull=True)
Post.objects.filter(status__in=["draft", "review"])
```

| Lookup | Meaning |
|--------|---------|
| `exact`, `iexact` | Equal (case sensitive / insensitive) |
| `contains`, `icontains` | Substring |
| `startswith`, `endswith` | Prefix/suffix |
| `gt`, `gte`, `lt`, `lte` | Comparisons |
| `in` | In list |
| `range` | Between |
| `isnull` | NULL check |
| `date`, `year`, `month` | Date parts |

### Why this matters

Understanding **Field Lookups** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Field Lookups** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Q Objects and F Expressions

```python
from django.db.models import Q, F

Post.objects.filter(Q(published=True) | Q(author__username="admin"))
Post.objects.filter(Q(title__icontains="django") & Q(published=True))

Post.objects.update(views=F("views") + 1)
```

| Tool | Use |
|------|-----|
| `Q` | Complex OR/AND/NOT in filters |
| `F` | Reference column values in queries (atomic updates) |

`F` avoids race conditions:

```python
# BAD: read-modify-write race
post.views += 1
post.save()

# GOOD: database-level increment
Post.objects.filter(pk=post.pk).update(views=F("views") + 1)
```

### Why this matters

Understanding **Q Objects and F Expressions** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Q Objects and F Expressions** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Aggregation and Annotation

```python
from django.db.models import Count, Avg, Max, Min, Sum

Post.objects.aggregate(avg_views=Avg("views"), total=Count("id"))
# {'avg_views': 42.5, 'total': 100}

from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.annotate(post_count=Count("posts")).filter(post_count__gt=5)
```

| Method | Returns |
|--------|---------|
| `aggregate()` | Dict of aggregates over entire queryset |
| `annotate()` | Adds aggregate per row to each instance |

### Why this matters

Understanding **Aggregation and Annotation** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Aggregation and Annotation** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Custom Managers

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    # fields...
    objects = models.Manager()
    published = PublishedManager()

Post.published.all()
```

Use managers for default filtering (published only, soft-delete exclusion).

### Why this matters

Understanding **Custom Managers** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Custom Managers** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## select_related and prefetch_related

```python
# N+1 problem
for post in Post.objects.all():
    print(post.author.username)  # extra query per post!

# Fix FK with select_related
for post in Post.objects.select_related("author"):
    print(post.author.username)

# Fix M2M with prefetch_related
for post in Post.objects.prefetch_related("tags"):
    for tag in post.tags.all():
        print(tag.name)
```

| Method | SQL strategy | For |
|--------|--------------|-----|
| `select_related` | SQL JOIN | ForeignKey, OneToOne |
| `prefetch_related` | Separate query + join in Python | ManyToMany, reverse FK |

### Why this matters

Understanding **select_related and prefetch_related** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **select_related and prefetch_related** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Model Meta Options

```python
class Meta:
    ordering = ["-created_at"]
    verbose_name = "blog post"
    verbose_name_plural = "blog posts"
    indexes = [models.Index(fields=["slug"])]
    constraints = [
        models.UniqueConstraint(fields=["author", "slug"], name="unique_author_slug")
    ]
```

| Option | Effect |
|--------|--------|
| `ordering` | Default ORDER BY |
| `indexes` | Database indexes |
| `constraints` | DB-level rules |
| `db_table` | Custom table name |

### Why this matters

Understanding **Model Meta Options** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Model Meta Options** in one sentence?
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
| null=True on CharField | Two empties: NULL and '' | Use blank=True, empty string |
| Forgetting migrations | DB out of sync | makemigrations + migrate |
| Using get() carelessly | Unhandled exceptions | filter().first() or try/except |
| N+1 queries | Slow pages | select_related / prefetch_related |
| Missing __str__ | Unreadable admin | Define __str__ on every model |

---

## Interview Points

**Q: What is a QuerySet?** — Lazy collection of model rows; SQL on evaluation.

**Q: null vs blank?** — null=DB; blank=validation. Strings: blank only usually.

**Q: select_related vs prefetch_related?** — JOIN for FK; separate query for M2M/reverse FK.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 3.1: Build Post model

Create Post with title, slug, body, published, timestamps.

<details>
<summary>Click to reveal solution for Exercise 3.1</summary>

Define model, makemigrations, migrate, create rows in shell.

</details>

---

### Exercise 3.2: Practice CRUD

Create 5 posts in shell; filter published; update one.

<details>
<summary>Click to reveal solution for Exercise 3.2</summary>

Use create(), filter(), save(), update().

</details>

---

### Exercise 3.3: Lookups

Filter posts with title containing 'django' case-insensitive.

<details>
<summary>Click to reveal solution for Exercise 3.3</summary>

`Post.objects.filter(title__icontains='django')`

</details>

---

### Exercise 3.4: Add author FK

Add ForeignKey to User; migrate; use select_related in loop.

<details>
<summary>Click to reveal solution for Exercise 3.4</summary>

Add field, migrate, `Post.objects.select_related('author')`.

</details>

---
## Chapter Summary

Excellent work completing Chapter 3. Here is what you learned:

- Completed Chapter 3: Models and ORM
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

**➡️ [Next Chapter →](./ch04-views-urls.md)**

---

*Chapter 3 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Models and ORM

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

## Extended Study Guide: Chapter 3

> Use this section for review, interviews, and spaced repetition after completing **Models and ORM**.

### Frequently Asked Questions

**Q: What table name does Post create?**

By default app_label + model name lowercase: blog_post.

**Q: Can I rename the database table?**

Yes: Meta.db_table = 'custom_name'.

**Q: What is related_name?**

Name for reverse relation from ForeignKey target back to source.

**Q: Difference between save() and update()?**

save() per instance, runs signals, calls full_clean optionally. update() single SQL, no save() on each instance.

**Q: When does DoesNotExist happen?**

Model.objects.get() with zero matching rows.

**Q: Can QuerySets be chained?**

Yes. Each filter returns a new QuerySet.

**Q: What is pk?**

Shortcut for primary key field name, usually id.

**Q: How to do OR queries?**

Use Q objects: filter(Q(a=1) | Q(b=2)).

**Q: How to avoid N+1?**

select_related for FK, prefetch_related for M2M.

**Q: Should I use raw SQL?**

When ORM is awkward (complex reports). Always parameterize.


### Step-by-Step Walkthrough

1. Define Post model with fields from chapter.
2. makemigrations and migrate.
3. Open shell: create 3 posts.
4. Filter published=True.
5. Practice __icontains lookup.
6. Add author ForeignKey; migrate again.
7. Loop posts with select_related('author').
8. Try get() vs filter().first() behavior.

### Additional Code Patterns

#### Pattern 3.1

```python
Post.objects.filter(published=True).order_by('-created_at')
```

#### Pattern 3.2

```python
Post.objects.select_related('author').all()
```

### Review checklist

```text
[ ] I can explain the main concepts without notes
[ ] I typed the code examples myself
[ ] I completed all exercises
[ ] I fixed at least one error using the traceback
[ ] I read the linked official Django documentation
```
