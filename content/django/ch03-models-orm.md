---
title: Models and ORM
description: Design models, use field types and relationships, run CRUD with QuerySets, write powerful lookups, and avoid N+1 queries with select_related and prefetch_related
order: 3
tags: [django, orm, models, querysets, database]
---

# Chapter 3 — Models and ORM

> Define your database with Python classes, then read, write, and query data without writing SQL.
>
> **Difficulty:** Beginner → Intermediate &nbsp;·&nbsp; **Estimated time:** 45 – 60 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 2 — Setup and Project Structure](./ch02-setup-project-structure.md), basic SQL helps but is not required

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Explain what an **ORM** is and why Django uses one
- ✔ Define models with the right **field types** and **field options** (`null`, `blank`, `default`, `unique`)
- ✔ Connect models with **ForeignKey**, **ManyToManyField**, and **OneToOneField**
- ✔ Run full **CRUD** (Create, Read, Update, Delete) operations using the ORM
- ✔ Use **field lookups** (`__icontains`, `__gte`, `__year`, …) for expressive queries
- ✔ Combine conditions with **Q objects** and atomic updates with **F expressions**
- ✔ Optimize queries with **`select_related`** and **`prefetch_related`** to avoid N+1 issues
- ✔ Generate and apply **migrations** safely

---

## Visual Preview

Here is the model you will build in this lesson, the database table it produces, and the kind of query that will read from it:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

Generated SQL (PostgreSQL syntax, simplified):

```sql
CREATE TABLE blog_post (
    id           BIGSERIAL PRIMARY KEY,
    title        VARCHAR(200) NOT NULL,
    body         TEXT NOT NULL,
    published    BOOLEAN NOT NULL DEFAULT FALSE,
    created_at   TIMESTAMPTZ NOT NULL
);
```

Querying it from Python:

```python
>>> Post.objects.filter(published=True, title__icontains="django").count()
3
```

That's the magic of the ORM — one Python class becomes a SQL table, and one Python call becomes a parameterized SQL query.

---

## Core Concept

### What the ORM does

> **Definition — ORM (Object-Relational Mapper):** A layer that maps Python classes to database tables and Python objects to table rows, so you can query and update the database with method calls (`Post.objects.filter(...)`) instead of raw SQL.

Django's ORM gives you four benefits at once: **safety** (parameterized queries kill SQL injection), **portability** (the same code targets SQLite, PostgreSQL, MySQL), **schema versioning** (via migrations), and **expressiveness** (Python is more readable than SQL for most app logic).

### Models = tables, instances = rows

Every subclass of `models.Model` becomes a database table. Every instance of that class becomes a row. Class **attributes** become **columns**.

### QuerySets are lazy

> **Definition — QuerySet:** A lazy, chainable representation of a database query. Nothing hits the database until the QuerySet is iterated, sliced, or otherwise evaluated.

This is the single most important thing to remember about the ORM. You can stack `.filter().exclude().order_by()` indefinitely with zero database cost — and then trigger exactly one SQL query when you finally iterate or call `list()`.

### Relationships are first-class

Django provides three relationship fields — `ForeignKey` (many-to-one), `ManyToManyField` (many-to-many), and `OneToOneField` (one-to-one). Each one creates the right SQL constraint **and** gives you forward and reverse accessors in Python.

### Migrations keep schema in sync

> **Definition — Migration:** A versioned, code-generated description of a schema change. `makemigrations` writes the file; `migrate` applies it.

Never edit your database manually — let migrations be the single source of truth.

---

## Syntax

The minimum a model needs:

```python
from django.db import models

class ModelName(models.Model):
    field_name = models.FieldType(<options>)

    def __str__(self):
        return self.field_name
```

The minimum query pattern:

```python
ModelName.objects.<manager-method>(<lookups>)
```

Where `<manager-method>` is one of `all`, `get`, `filter`, `exclude`, `create`, `update`, `delete`, `aggregate`, `annotate`, and so on.

---

## Live Code Playground

A complete, runnable example you can paste into your project. We'll define two related models, register them with the admin, and run a few queries in the Django shell.

### `blog/models.py`

```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["slug"])]

    def __str__(self):
        return self.title
```

### `blog/admin.py`

```python
from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
```

### Apply the schema

```bash
python manage.py makemigrations
python manage.py migrate
```

### Try the ORM in the Django shell

```bash
python manage.py shell
```

```python
from blog.models import Author, Post

# CREATE
ada = Author.objects.create(name="Ada Lovelace", email="ada@example.com")
Post.objects.create(
    title="Hello Django",
    slug="hello-django",
    body="My first post.",
    published=True,
    author=ada,
)

# READ
Post.objects.all()
Post.objects.filter(published=True)
Post.objects.get(slug="hello-django")
Post.objects.filter(title__icontains="django").count()

# UPDATE (a single field on a single row)
post = Post.objects.get(slug="hello-django")
post.views += 1
post.save(update_fields=["views"])

# DELETE
Post.objects.filter(published=False).delete()
```

> 💡 **Tip:** Re-run `python manage.py makemigrations` every time you change a model — Django won't notice the change otherwise.

---

## Step-by-Step Example

Let's walk through building the `Post` model end-to-end so every step is testable.

### Step 1 — Define the model

In `blog/models.py`:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Step 2 — Generate the migration

```bash
python manage.py makemigrations
```

Django prints something like:

```text
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

### Step 3 — Inspect the SQL (optional but eye-opening)

```bash
python manage.py sqlmigrate blog 0001
```

Django shows the exact `CREATE TABLE` statement it will run.

### Step 4 — Apply the migration

```bash
python manage.py migrate
```

The `blog_post` table now exists in `db.sqlite3`.

### Step 5 — Create and query in the shell

```python
>>> from blog.models import Post
>>> Post.objects.create(title="First post", body="Hi!", published=True)
<Post: First post>
>>> Post.objects.count()
1
>>> Post.objects.filter(published=True)
<QuerySet [<Post: First post>]>
```

### Step 6 — Add a `__str__`

Without it, the admin and the shell will show `<Post: Post object (1)>`. With it:

```python
def __str__(self):
    return self.title
```

Now the admin and shell display **First post** instead.

### Step 7 — Register the model with the admin

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Visit `/admin/` and you can now create, edit, and delete `Post` rows visually.

---

## Try It Yourself

> **Task:** Extend the blog so each post can have **multiple tags**, and tags can belong to **multiple posts** (many-to-many).
>
> 1. Create a `Tag` model with a `name` field (max length 30, unique).
> 2. Add a `tags = models.ManyToManyField(Tag, related_name="posts", blank=True)` to `Post`.
> 3. Run `makemigrations` and `migrate`.
> 4. In the Django shell, create a few tags, attach two of them to an existing post, and query for "all posts that have the `django` tag".

Hints:

- Use `tag.posts.all()` for the reverse accessor (because of `related_name="posts"`).
- Attach tags with `post.tags.add(tag1, tag2)`.
- Filter by related field: `Post.objects.filter(tags__name="django")`.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `blog/models.py`

```python
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title
```

### Generate and apply the migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Use it in the shell

```python
>>> from blog.models import Post, Tag
>>> django_tag = Tag.objects.create(name="django")
>>> python_tag = Tag.objects.create(name="python")
>>> post = Post.objects.first()
>>> post.tags.add(django_tag, python_tag)

# Forward: tags on a post
>>> post.tags.all()
<QuerySet [<Tag: django>, <Tag: python>]>

# Reverse: posts with a given tag
>>> django_tag.posts.all()
<QuerySet [<Post: First post>]>

# Query by related field
>>> Post.objects.filter(tags__name="django")
<QuerySet [<Post: First post>]>
```

**Why this works:** A `ManyToManyField` creates a **hidden join table** (`blog_post_tags`) that links `post_id` to `tag_id`. Django gives you forward accessors (`post.tags`) and reverse accessors (`tag.posts`) for free, and the join table is fully managed by migrations.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** `Post.objects.filter(...)` always returns a **QuerySet** — possibly empty. `Post.objects.get(...)` returns a single object or raises `DoesNotExist`. Use `filter().first()` when you're not sure the row exists.

> 💡 **Tip:** `select_related("author")` does a SQL `JOIN` — perfect for `ForeignKey` and `OneToOneField`. `prefetch_related("tags")` does a separate query and joins in Python — required for `ManyToManyField` and reverse foreign keys.

> 💡 **Tip:** Use `update_fields=["title"]` on `save()` to write only the columns you changed. It's faster and avoids race conditions on other fields.

> ⚠️ **Warning:** `null=True` on a `CharField` or `TextField` creates **two** "empty" states — `NULL` and `""`. Always prefer `blank=True` for strings and leave `null` unset.

> ⚠️ **Warning:** A model change **without** `makemigrations` won't break runtime — until you try to query the new field and Django blows up because the column doesn't exist in the database.

> ⚠️ **Warning:** Avoid `Model.objects.update(...)` when you need `save()` signals (like `auto_now`, `pre_save`, `post_save`). `update()` bypasses `save()` entirely.

---

## Common Mistakes

- ❌ **N+1 queries.** Looping over `Post.objects.all()` and accessing `post.author.name` runs one query for the list and one for **every** post. Fix it with `select_related("author")`.
- ❌ **Using `.get()` when you should use `.filter().first()`.** `.get()` raises `DoesNotExist` if the row is missing — fine for must-exist lookups, dangerous for optional ones.
- ❌ **Forgetting `__str__`.** The admin, the shell, and most debugging output become unreadable (`<Post: Post object (3)>`).
- ❌ **Setting `null=True` on a `CharField`.** Now you have to check for both `""` and `None` everywhere.
- ❌ **Editing migrations by hand.** Always regenerate them with `makemigrations` and review them with `sqlmigrate`.
- ❌ **Forgetting `on_delete` on a `ForeignKey`.** Django 2.0+ refuses to migrate without it — pick `CASCADE`, `PROTECT`, `SET_NULL`, or `SET_DEFAULT` deliberately.
- ❌ **Calling `.count()` on a list.** `len(qs)` evaluates the QuerySet. `qs.count()` issues a `SELECT COUNT(*)` — much cheaper for large tables.

---

## Mini Quiz

**Q1.** What does `Post.objects.filter(published=True)` return?

- A) A list of posts
- B) A lazy **QuerySet** that hasn't queried the database yet ✔
- C) A single post object
- D) A SQL string

**Q2.** Which method should you use to follow a **`ForeignKey`** efficiently and avoid N+1 queries?

- A) `prefetch_related("author")`
- B) `select_related("author")` ✔
- C) `only("author")`
- D) `defer("author")`

**Q3.** What's the difference between `null=True` and `blank=True`?

- A) They are synonyms
- B) `null=True` is database-level (allows `NULL`); `blank=True` is form/validation-level (allows empty input) ✔
- C) `null=True` only works on integers; `blank=True` only works on strings
- D) `blank=True` is deprecated in Django 5

**Q4.** Which expression atomically increments a counter to avoid race conditions?

- A) `post.views = post.views + 1; post.save()`
- B) `Post.objects.update(views=views + 1)`
- C) `Post.objects.update(views=F("views") + 1)` ✔
- D) `Post.objects.increment("views")`

**Q5.** What does `related_name="posts"` on `author = ForeignKey(Author, ...)` give you?

- A) A property `author.posts` that returns all posts by that author ✔
- B) A new field on `Post` called `posts`
- C) A new database column
- D) A read-only alias for `author.post_set`

---

## Real World Example

A typical e-commerce schema in Django uses every relationship type you just learned:

```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )
    tags = models.ManyToManyField("Tag", related_name="products", blank=True)


class Order(models.Model):
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderLine")
    created_at = models.DateTimeField(auto_now_add=True)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
```

**What this schema demonstrates:**

| Pattern | Where it appears |
|---------|------------------|
| `ForeignKey` with `PROTECT` | `Product.category` — block deletion of categories with products |
| `ForeignKey` with `CASCADE` | `OrderLine.order` — delete lines when the order is deleted |
| `ManyToManyField` with `through=` | `Order.products` via `OrderLine` — store extra fields per relationship |
| `DecimalField` for money | `price`, `unit_price` — never use `FloatField` for currency |
| `related_name` | `category.products`, `tag.products` — clean reverse accessors |

A typical "list all in-stock products in a category, including their tags" query becomes:

```python
Product.objects.filter(
    category__name="Books",
    in_stock=True,
).select_related("category").prefetch_related("tags")
```

One Python line → one optimized SQL query plan, no N+1 problems.

---

## Summary

Today you learned:

- ✔ Django's **ORM** maps Python classes to database tables and Python objects to rows.
- ✔ **Fields** describe columns; **field options** (`null`, `blank`, `default`, `unique`) control behavior at the DB and form level.
- ✔ Three relationship types — **`ForeignKey`**, **`ManyToManyField`**, **`OneToOneField`** — cover every real-world data shape.
- ✔ **QuerySets** are lazy — chain `.filter()`, `.exclude()`, `.order_by()` freely until you actually iterate.
- ✔ Use **`__lookup`** syntax (`__icontains`, `__gte`, `__year`, `__in`, `__isnull`) for expressive queries.
- ✔ **`Q`** combines conditions with `OR`/`AND`/`NOT`; **`F`** updates a column atomically based on its current value.
- ✔ Avoid **N+1 queries** with `select_related` (FK / OneToOne) and `prefetch_related` (M2M / reverse FK).
- ✔ **Migrations** are your schema's version control — `makemigrations`, then `migrate`.

### Key Takeaways

```text
✅ Models = tables, instances = rows, attributes = columns
✅ QuerySets are lazy until iterated, sliced, or list()-ed
✅ Use blank=True for strings, null=True only for non-strings
✅ Pick on_delete deliberately (CASCADE, PROTECT, SET_NULL)
✅ select_related for FKs, prefetch_related for M2Ms
✅ Q objects for complex conditions, F expressions for atomic updates
✅ Always run makemigrations + migrate after editing models
✅ DecimalField for money — never FloatField
```

### Command Reference

```bash
python manage.py makemigrations          # Generate migration files
python manage.py migrate                 # Apply migrations to the DB
python manage.py sqlmigrate blog 0001    # Show the raw SQL for a migration
python manage.py showmigrations          # List migrations and their state
python manage.py shell                   # Open the Django shell for the ORM
python manage.py createsuperuser         # Create an admin user
```

### Glossary

| Term | Definition |
|------|------------|
| ORM | Object-Relational Mapper — maps Python objects to DB rows |
| Model | Python class mapped to a database table |
| Field | Class attribute mapped to a column |
| QuerySet | Lazy, chainable representation of a database query |
| Manager | Object on a model (`objects`) that creates QuerySets |
| Lookup | `__name` filter syntax (e.g., `__icontains`, `__gte`) |
| `Q` object | Object that lets you combine filters with OR/AND/NOT |
| `F` expression | Reference to a database column inside an update |
| Migration | Versioned schema change file |
| N+1 problem | Running one query per related object in a loop |
| `select_related` | SQL JOIN to follow `ForeignKey` / `OneToOne` in one query |
| `prefetch_related` | Extra query + Python join for `ManyToMany` / reverse FK |
| `on_delete` | Required argument on `ForeignKey` controlling cascade behavior |
| `related_name` | Name of the reverse accessor on the other side of a relation |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Setup and Project Structure](./ch02-setup-project-structure.md) | [Views and URLs](./ch04-views-urls.md) |
