---
title: Migrations
description: Version-control your database schema — makemigrations, migrate, data migrations with RunPython, squashing, conflicts, and zero-downtime strategies
order: 9
tags: [django, migrations, database, schema]
---

# Chapter 9 — Migrations

> Migrations are git for your database schema — never edit production tables by hand again.
>
> **Difficulty:** Intermediate &nbsp;·&nbsp; **Estimated time:** 45 – 60 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 3 — Models and ORM](./ch03-models-orm.md)

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Explain what a **migration** is and why every Django project depends on them
- ✔ Run **`makemigrations`** and **`migrate`** confidently in any environment
- ✔ Inspect a migration's **`dependencies`** and **`operations`** before applying it
- ✔ Preview the SQL with **`sqlmigrate`** and the state with **`showmigrations`**
- ✔ Add a non-null column to a populated table without crashing — the **3-step pattern**
- ✔ Write **data migrations** with **`RunPython`** using historical models
- ✔ **Squash** long migration histories and **rename** fields/models safely
- ✔ Resolve **migration conflicts** when teammates' branches diverge
- ✔ Recover from broken state with **`migrate --fake`** and roll forward/back
- ✔ Plan **zero-downtime** schema changes for production deployments

---

## Visual Preview

What migrations actually do — turn a Python class change into a versioned SQL change:

```text
You change blog/models.py:

   class Post(models.Model):
       title    = models.CharField(max_length=200)
+      summary  = models.CharField(max_length=300, blank=True)

         │
         ▼
   $ python manage.py makemigrations blog
   → blog/migrations/0003_post_summary.py
         │
         ▼
   $ python manage.py sqlmigrate blog 0003
     ALTER TABLE "blog_post"
       ADD COLUMN "summary" varchar(300) NOT NULL DEFAULT '';
         │
         ▼
   $ python manage.py migrate
     Applying blog.0003_post_summary... OK
         │
         ▼
   django_migrations table:
   ┌────┬──────┬──────────────────────┬─────────────────────┐
   │ id │ app  │ name                 │ applied             │
   ├────┼──────┼──────────────────────┼─────────────────────┤
   │ 14 │ blog │ 0003_post_summary    │ 2026-05-26 07:55:13 │
   └────┴──────┴──────────────────────┴─────────────────────┘
```

By the end of this lesson, every schema change in your project will follow this pattern — reviewable, reversible, and identical across dev, CI, and production.

---

## Core Concept

### What a migration is

> **Definition — Migration:** A versioned, code-generated description of a schema change. Each migration is a Python file in `<app>/migrations/` containing a list of **operations** (`AddField`, `RemoveField`, `RunPython`, …) and a list of **dependencies** on prior migrations.

Django records every applied migration in a `django_migrations` table. When you run `migrate`, Django compares that table to the files on disk and applies whatever's missing — once.

### `makemigrations` ≠ `migrate`

Two completely different commands:

| | **`makemigrations`** | **`migrate`** |
|---|----------------------|---------------|
| Reads | Your `models.py` files | Your migration files |
| Writes | New migration files | Rows in `django_migrations` + DDL on the DB |
| Touches the database? | **No** | **Yes** |
| Run on every dev machine? | Yes | Yes |
| Commit the result? | **Yes** (commit the migration file) | No |

**Always `makemigrations` locally, commit the file, then `migrate` runs in every environment** — including CI, staging, and production.

### Dependencies and operations

Every migration is just:

```python
class Migration(migrations.Migration):
    dependencies = [("blog", "0002_initial")]
    operations = [
        migrations.AddField(
            model_name="post",
            name="summary",
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
```

`dependencies` is the migration graph — Django walks it to figure out the order. `operations` is the list of changes to apply.

### Schema migrations vs. data migrations

> **Schema migration:** Changes the **shape** of the database — `AddField`, `RemoveField`, `AlterField`, `CreateModel`, `RemoveModel`, indexes.
>
> **Data migration:** Changes the **contents** of the database — written with `RunPython(forwards, backwards)`. Used to backfill columns, normalize values, or seed data.

You usually combine them: add a nullable column → backfill it with `RunPython` → make it non-null in a follow-up migration.

### Migrations are immutable once shared

> Once a migration has been pushed to git or applied in any environment, **never edit it**. Generate a new migration to make further changes. Editing applied migrations leads to inconsistent state across machines and broken CI.

---

## Syntax

A typical migration file Django generates for you:

```python
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_published"),     # the migration this one extends
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="summary",
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
```

The four commands you'll run on every project:

```bash
python manage.py makemigrations [app]        # generate from models.py
python manage.py migrate [app] [name]        # apply (or rollback to) a migration
python manage.py showmigrations              # list every migration + applied flag
python manage.py sqlmigrate <app> <name>     # preview the SQL without running it
```

---

## Live Code Playground

A complete worked example: add a `summary` column to `Post`, backfill it from `body`, then enforce a non-null constraint — three migrations, zero downtime.

### Step 1 — model change (`blog/models.py`)

```python
class Post(models.Model):
    title   = models.CharField(max_length=200)
    body    = models.TextField()
    summary = models.CharField(max_length=300, blank=True)   # NEW
```

### Step 2 — generate the schema migration

```bash
python manage.py makemigrations blog
# blog/migrations/0003_post_summary.py
```

```python
# 0003_post_summary.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("blog", "0002_initial")]
    operations = [
        migrations.AddField(
            model_name="post",
            name="summary",
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
```

### Step 3 — write the data migration (manually)

Create `blog/migrations/0004_backfill_summary.py`:

```python
from django.db import migrations


def backfill_summary(apps, schema_editor):
    Post = apps.get_model("blog", "Post")     # historical model
    for post in Post.objects.filter(summary=""):
        post.summary = (post.body or "")[:300]
        post.save(update_fields=["summary"])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("blog", "0003_post_summary")]
    operations = [migrations.RunPython(backfill_summary, noop)]
```

### Step 4 — tighten the constraint

Edit `blog/models.py`:

```python
summary = models.CharField(max_length=300)   # blank=True removed
```

```bash
python manage.py makemigrations blog
# blog/migrations/0005_alter_post_summary.py — sets the column to NOT NULL
```

### Step 5 — preview and apply

```bash
python manage.py sqlmigrate blog 0003
python manage.py sqlmigrate blog 0004        # → "RunPython" (no SQL preview)
python manage.py sqlmigrate blog 0005

python manage.py migrate blog
```

```text
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0003_post_summary... OK
  Applying blog.0004_backfill_summary... OK
  Applying blog.0005_alter_post_summary... OK
```

### Step 6 — inspect the state

```bash
python manage.py showmigrations blog

# blog
#  [X] 0001_initial
#  [X] 0002_post_published
#  [X] 0003_post_summary
#  [X] 0004_backfill_summary
#  [X] 0005_alter_post_summary
```

> 💡 **Tip:** Always use `apps.get_model("blog", "Post")` inside `RunPython` — never `from .models import Post`. The historical model matches the schema as it was *at that point in history*; the imported model matches today's code and may have fields that don't exist yet.

---

## Step-by-Step Example

Walk through the **3-step "add a non-null column" pattern** from zero. This is the single most useful migration skill you can have.

### Step 1 — Add the column as **nullable** (or with a blank default)

```python
# blog/models.py
class Post(models.Model):
    ...
    author_email = models.EmailField(blank=True, default="")
```

```bash
python manage.py makemigrations blog
python manage.py migrate blog
```

The column exists, but old rows have an empty string and new rows can be created without an email. **No downtime.**

### Step 2 — Backfill with a data migration

```bash
python manage.py makemigrations blog --empty -n backfill_author_email
```

Edit the generated file:

```python
def backfill(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.filter(author_email="").update(author_email="unknown@example.com")


def noop(apps, schema_editor): pass


operations = [migrations.RunPython(backfill, noop)]
```

Run it:

```bash
python manage.py migrate blog
```

Every existing row now has a value.

### Step 3 — Tighten the constraint

```python
author_email = models.EmailField()   # blank=True / default removed
```

```bash
python manage.py makemigrations blog
python manage.py migrate blog
```

The column is now `NOT NULL`. **Still no downtime**, because every row already had data before the constraint was applied.

### Why this 3-step dance matters

A single-step `AddField(NOT NULL)` would either fail (no default) or block for a long table-level lock while the database fills the default into millions of rows. The three-step pattern keeps each step **fast** (a metadata change, an idempotent backfill, another metadata change).

### Bonus — running the backfill in chunks for huge tables

```python
def backfill(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    qs = Post.objects.filter(author_email="").only("id")
    while True:
        batch = list(qs[:1000])
        if not batch:
            break
        Post.objects.filter(pk__in=[p.pk for p in batch]).update(
            author_email="unknown@example.com"
        )
```

Chunked updates avoid holding a transaction open over the whole table.

---

## Try It Yourself

> **Task:** Add a **`status`** column to `Post` with the choices `("draft", "Draft")`, `("published", "Published")`, `("archived", "Archived")`, defaulting old rows correctly and **never** allowing `NULL`:
>
> 1. Old rows where `published=True` should become `status="published"`.
> 2. Old rows where `published=False` should become `status="draft"`.
> 3. The final column must be **non-null** with a default of `"draft"`.
>
> Use the **3-step pattern** — schema (nullable) → data backfill → tighten constraint.

Hints:

- For step 1, the migration's field should be `CharField(max_length=20, blank=True, default="")` so old rows can fall through.
- For step 2, generate an empty migration with `makemigrations blog --empty -n backfill_status` and write the `RunPython` body.
- For step 3, change the model to `CharField(max_length=20, choices=STATUS_CHOICES, default="draft")` and let `makemigrations` produce the `AlterField`.
- Provide a `noop` reverse function — `RunPython(forwards, noop)` — so unapplying the migration doesn't crash.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### Step 1 — `blog/models.py` (nullable schema)

```python
class Post(models.Model):
    ...
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=20, blank=True, default="")
```

```bash
python manage.py makemigrations blog
# 0006_post_status.py — AddField with blank=True default=""
python manage.py migrate blog
```

### Step 2 — `blog/migrations/0007_backfill_status.py`

```bash
python manage.py makemigrations blog --empty -n backfill_status
```

```python
from django.db import migrations


def forwards(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.filter(published=True,  status="").update(status="published")
    Post.objects.filter(published=False, status="").update(status="draft")


def backwards(apps, schema_editor):
    # the column will be dropped if we go further back; nothing to undo
    pass


class Migration(migrations.Migration):
    dependencies = [("blog", "0006_post_status")]
    operations = [migrations.RunPython(forwards, backwards)]
```

```bash
python manage.py migrate blog
```

### Step 3 — `blog/models.py` (tighten)

```python
STATUS_CHOICES = [
    ("draft",     "Draft"),
    ("published", "Published"),
    ("archived",  "Archived"),
]

class Post(models.Model):
    ...
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
```

```bash
python manage.py makemigrations blog
# 0008_alter_post_status.py — AlterField removing blank=True
python manage.py migrate blog
```

### What's happening

1. **Step 1** is a fast, online schema change. Old rows get `""`, new rows can omit the column.
2. **Step 2** backfills every row idempotently — re-running the migration would do nothing because the `WHERE status=""` filter is already false.
3. **Step 3** flips the column from "blank allowed" to a real choices field with a default. Because every row already has a value, the migration is again a fast metadata change.
4. The `noop` `backwards` function lets `migrate --backwards` succeed — Django can move past this migration in either direction without crashing.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** **Always** preview migrations on production-class data before deploying. `python manage.py sqlmigrate <app> <name>` prints the exact SQL without running it.

> 💡 **Tip:** Use `makemigrations --name <descriptive>` so files end up named `0007_post_summary.py` instead of `0007_auto_20260526_0755.py`.

> 💡 **Tip:** Generate a stub for a data-only migration with `makemigrations --empty <app> -n <name>`. This is the right way to bootstrap a `RunPython` migration.

> 💡 **Tip:** Inside `RunPython`, **always** call `apps.get_model("app", "Model")`. The "historical model" reflects the schema as it was at that migration — your imported model may already have new fields.

> 💡 **Tip:** Squash long histories with `python manage.py squashmigrations <app> <last_migration>` once a project is stable. New developers `migrate` once instead of replaying 250 migrations.

> ⚠️ **Warning:** Migration files are **part of your code base**. Commit them. Tell your team to commit them. CI must run `migrate` against a real database — not skip it.

> ⚠️ **Warning:** Never edit a migration that has been **pushed to git** or **applied in any environment**. Generate a new migration instead.

> ⚠️ **Warning:** **Never** `from .models import Post` inside `RunPython`. Use `apps.get_model(...)`. Forgetting this rule produces migrations that work on your machine and crash on a teammate's.

> ⚠️ **Warning:** A non-null column added to a populated table without a default will fail on PostgreSQL with `column "x" of relation "y" contains null values`. Use the **3-step pattern** for any non-trivial column.

> ⚠️ **Warning:** `migrate --fake` marks a migration as applied **without running it**. Use only when you genuinely have already-existing schema (e.g., legacy DB). Otherwise, you'll desync code and database.

---

## Common Mistakes

- ❌ **Forgetting to commit migration files.** Other developers re-run `makemigrations` and end up with duplicate, conflicting numbers.
- ❌ **Editing applied migrations.** Once a migration has been applied anywhere, treat it as immutable. Make a new one instead.
- ❌ **Importing models directly in `RunPython`.** The model's current code may have fields that didn't exist when the migration was supposed to run.
- ❌ **Adding a non-null column with no default to a populated table.** Always make the column nullable / blank-default first, backfill, then tighten.
- ❌ **`makemigrations` on production.** Never. Run it locally, commit the file, run `migrate` in production.
- ❌ **Skipping `sqlmigrate` previews on big migrations.** Surprises are expensive when they hit production.
- ❌ **Using `--fake` to bypass real migration errors.** That hides the bug, not fixes it. Investigate first.
- ❌ **Renaming a field by deleting + adding.** `RemoveField` + `AddField` drops the data. Use `RenameField` (`makemigrations` will offer it interactively if it can detect the rename).
- ❌ **Letting `auto_xxxx` migration names accumulate.** Pass `-n descriptive_name` so PR diffs are readable.
- ❌ **Running `RunPython` on millions of rows in a single pass.** Use chunks; long-running transactions block other writes.

---

## Mini Quiz

**Q1.** Which command creates a new migration **file** without touching the database?

- A) `python manage.py migrate`
- B) `python manage.py makemigrations` ✔
- C) `python manage.py syncdb`
- D) `python manage.py runserver`

**Q2.** Inside a `RunPython` data migration, how should you reference a model?

- A) `from .models import Post`
- B) `apps.get_model("blog", "Post")` ✔
- C) `Model.objects.using("default")`
- D) Both A and B work equally well

**Q3.** What's the **safest** way to add a non-null column to a populated table?

- A) Add it as `NOT NULL` with a default and hope for the best
- B) Add nullable / blank → backfill in `RunPython` → tighten with `AlterField` ✔
- C) Drop the table and recreate it
- D) Always use `RunSQL`

**Q4.** Two teammates both run `makemigrations` on `blog` in their own branches. What command resolves the resulting two-leaf migration graph?

- A) `python manage.py squashmigrations blog`
- B) `python manage.py makemigrations --merge` ✔
- C) `python manage.py migrate --fake`
- D) `python manage.py reset_migrations blog`

**Q5.** What does `python manage.py migrate --fake blog 0007` do?

- A) Runs `0007` and any earlier unapplied migrations
- B) Marks `0007` as applied **without** running its operations ✔
- C) Reverts all blog migrations after `0007`
- D) Prints the SQL that `0007` would run

---

## Real World Example

A typical sprint touches all three migration types. Here's a realistic week.

### Monday — schema change

```python
# accounts/models.py
class User(AbstractUser):
    plan = models.CharField(max_length=20, default="free")        # NEW
```

```bash
python manage.py makemigrations accounts -n add_user_plan
git add accounts/migrations/0006_add_user_plan.py
git commit -m "Add User.plan field"
```

CI runs `migrate` against a fresh DB; deploy pipeline runs `migrate` against staging then production.

### Wednesday — data backfill

A new requirement: customers active in the last 30 days should be moved to a "trial" plan retroactively.

```bash
python manage.py makemigrations accounts --empty -n backfill_active_users_to_trial
```

```python
from django.db import migrations
from django.utils import timezone
from datetime import timedelta


def forwards(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    cutoff = timezone.now() - timedelta(days=30)
    User.objects.filter(plan="free", last_login__gte=cutoff).update(plan="trial")


def backwards(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    User.objects.filter(plan="trial").update(plan="free")


operations = [migrations.RunPython(forwards, backwards)]
```

Reviewable, reversible, idempotent — three things raw SQL `UPDATE` statements rarely are.

### Friday — rename the field cleanly

Rename `plan` → `plan_tier` everywhere:

```python
plan_tier = models.CharField(max_length=20, default="free")
```

```bash
python manage.py makemigrations accounts -n rename_plan_to_plan_tier
# Did you rename user.plan to user.plan_tier (a CharField)? [y/N] y
```

Django generates a `RenameField` — **the data is preserved**, no backfill needed.

### Quarterly — squash the noise

After 200 migrations, the project is sluggish to set up:

```bash
python manage.py squashmigrations accounts 0001 0200
git add accounts/migrations/0001_squashed_0001_0200.py
git rm accounts/migrations/0002...0200_*.py
```

New developers run `migrate` once and the schema is identical to a colleague who has been around for a year.

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Schema migration with safe default | Monday's `plan` field |
| Empty migration → `RunPython` | Wednesday's trial-plan backfill |
| `makemigrations --name` | Readable filenames in PRs |
| `RenameField` instead of remove + add | Friday's `plan` → `plan_tier` |
| `squashmigrations` | Quarterly cleanup keeping the project fast |
| Idempotent `WHERE` filters | Backfill can re-run safely |
| Reversible `backwards` function | `migrate --backwards` works |

This is the migration cadence of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ **Migrations** are the version-controlled history of your schema — every change starts as `makemigrations` and ships as `migrate`.
- ✔ **`makemigrations`** writes files; **`migrate`** applies them. Never confuse the two.
- ✔ Each migration is just `dependencies = [...]` + `operations = [...]`.
- ✔ **Schema** migrations change the shape (`AddField`, `AlterField`); **data** migrations change the contents (`RunPython`).
- ✔ Adding a non-null column to a populated table is a **3-step dance**: nullable schema → `RunPython` backfill → `AlterField` to tighten.
- ✔ Inside `RunPython`, always use **`apps.get_model("app", "Model")`** — never the imported model.
- ✔ Resolve diverged branches with **`makemigrations --merge`**; rename fields with **`RenameField`**, not delete+add.
- ✔ Use **`sqlmigrate`** to preview; use **`showmigrations`** to inspect; use **`--fake`** only when the schema genuinely already exists.
- ✔ **Squash** old migrations periodically; **commit** every migration; **never edit** a migration after it's been applied.
- ✔ Plan **zero-downtime** changes: keep each step a fast metadata operation, do heavy work in chunked `RunPython`.

### Key Takeaways

```text
✅ makemigrations locally, migrate everywhere
✅ Commit every migration file — they are code, not artifacts
✅ Use apps.get_model() inside RunPython — always
✅ Add nullable → backfill → tighten (the 3-step pattern)
✅ sqlmigrate before any production migration
✅ RenameField, not RemoveField + AddField
✅ Resolve conflicts with makemigrations --merge
✅ Squash long histories; never edit applied migrations
✅ --fake only for genuinely already-applied schema
✅ Chunk large RunPython updates; avoid huge transactions
```

### Migration Cheat Sheet

```bash
# Generate
python manage.py makemigrations                      # all apps
python manage.py makemigrations blog                 # one app
python manage.py makemigrations blog -n add_summary  # named
python manage.py makemigrations blog --empty -n backfill_x  # data migration stub
python manage.py makemigrations --merge              # resolve conflicts

# Inspect
python manage.py showmigrations                      # all apps + applied flag
python manage.py showmigrations blog
python manage.py sqlmigrate blog 0003                # preview SQL

# Apply / revert
python manage.py migrate                             # apply all pending
python manage.py migrate blog                        # one app
python manage.py migrate blog 0007                   # forward or backward to a target
python manage.py migrate blog zero                   # unapply every blog migration
python manage.py migrate --fake blog 0007            # mark as applied without running

# Maintenance
python manage.py squashmigrations blog 0050          # combine 0001..0050 into one file
```

Anatomy of a migration file:

```python
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("blog", "0002_initial")]
    operations = [
        migrations.AddField(...),
        migrations.AlterField(...),
        migrations.RemoveField(...),
        migrations.RenameField(...),
        migrations.RenameModel(...),
        migrations.AddIndex(...),
        migrations.RunPython(forwards, backwards),
        migrations.RunSQL("UPDATE ... ", "UPDATE ..."),  # rare; raw escape hatch
    ]
```

A `RunPython` template:

```python
def forwards(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.filter(...).update(...)

def backwards(apps, schema_editor):
    pass    # or write the inverse update

operations = [migrations.RunPython(forwards, backwards)]
```

### Glossary

| Term | Definition |
|------|------------|
| Migration | Versioned, code-generated description of a schema change |
| `makemigrations` | Generates migration files from `models.py` (no DB writes) |
| `migrate` | Applies pending migrations to the database |
| `showmigrations` | Lists every migration and whether it has been applied |
| `sqlmigrate` | Prints the SQL a migration would run, without running it |
| `dependencies` | The graph that determines migration order |
| `operations` | The list of changes a migration applies |
| Schema migration | Operations that change table shape |
| Data migration | Operations that change row contents (`RunPython`, `RunSQL`) |
| Historical model | The version of a model used inside `RunPython` (`apps.get_model`) |
| `--fake` | Marks a migration applied without running its operations |
| `--empty` | Generates an empty migration file as a stub |
| `--merge` | Resolves a two-leaf migration graph after a branch merge |
| `squashmigrations` | Combines a range of migrations into one file |
| `RenameField` / `RenameModel` | Operations that rename without dropping data |
| Zero-downtime migration | Multi-step deployment that never blocks the app |
| Idempotent | Can be re-run without changing the result after the first run |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Authentication](./ch08-authentication.md) | [Static and Media Files](./ch10-static-media-files.md) |
