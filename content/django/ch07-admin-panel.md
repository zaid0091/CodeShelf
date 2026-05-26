---
title: Admin Panel
description: Customize the Django admin with ModelAdmin — list_display, filters, search, fieldsets, inlines, actions, permissions, and branding
order: 7
tags: [django, admin, modeladmin, crud]
---

# Chapter 7 — Admin Panel

> Get a production-ready CRUD interface for free, then customize every detail with `ModelAdmin`.
>
> **Difficulty:** Beginner → Intermediate &nbsp;·&nbsp; **Estimated time:** 35 – 50 min &nbsp;·&nbsp; **Prerequisites:** [Chapter 3 — Models and ORM](./ch03-models-orm.md), a superuser created with `python manage.py createsuperuser`

---

## Learning Outcome

By the end of this lesson, you will be able to:

- ✔ Register models with the admin using **`@admin.register`** and **`admin.site.register`**
- ✔ Customize the changelist with **`list_display`**, **`list_filter`**, **`search_fields`**, and **`ordering`**
- ✔ Group fields on the change form using **`fieldsets`** and add **`readonly_fields`**
- ✔ Auto-fill slugs with **`prepopulated_fields`** and edit values inline with **`list_editable`**
- ✔ Manage related rows with **`TabularInline`** / **`StackedInline`**
- ✔ Add bulk **actions** with **`@admin.action`** for multi-row operations
- ✔ Restrict access by **overriding permissions** and **`get_queryset`** per user
- ✔ Render computed columns with **`@admin.display`**
- ✔ Brand the admin with **`site_header`**, **`site_title`**, and **`index_title`**
- ✔ Decide when the admin is the right tool — and when to build a custom UI instead

---

## Visual Preview

What you start with vs. what you can have, by the end of the lesson:

```text
DEFAULT (after admin.site.register(Post)):
┌─ Posts ──────────────────────────┐
│ Post object (1)                  │
│ Post object (2)                  │
│ Post object (3)                  │
└──────────────────────────────────┘

CUSTOMIZED (after ModelAdmin):
┌─ Posts ──────────── + Add post ──┐    ┌─ FILTER ────────────┐
│ ☑ Title       Author   Published │    │ Published           │
│ ☐ Hello!      Ada      ✅  Apr 1 │    │ ▣ Yes               │
│ ☐ Templates   Linus    ❌  Mar 9 │    │ ▢ No                │
│ ☐ DTL deep dive Ada    ✅  Mar 2 │    │ Author              │
│                                  │    │ ▣ Ada               │
│ Action: ▼ Publish ✓   [ Go ]     │    │ ▢ Linus             │
│ Search: [ q…       ]   ✓         │    └─────────────────────┘
└──────────────────────────────────┘
```

A few `ModelAdmin` attributes turn an unreadable list into a powerful internal dashboard — sortable columns, sidebar filters, full-text search, bulk actions, and inline editing.

---

## Core Concept

### What the Django admin actually is

> **Definition — Django admin:** An auto-generated CRUD interface mounted at `/admin/` that gives staff users a UI to create, read, update, and delete model instances — with authentication, permissions, search, filtering, and history baked in.

The admin is **not a public UI**. It is a tool for you, your team, and your client's internal staff. Public-facing screens belong in your normal views and templates.

### `ModelAdmin` is how you customize it

Every model you register can be paired with a `ModelAdmin` subclass. That subclass is just a configuration object — the attributes you set (`list_display`, `list_filter`, `search_fields`, …) tell Django how to render the changelist and the change form.

### Two registration styles, one result

```python
# Style 1: decorator (preferred)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]

# Style 2: function call
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]

admin.site.register(Post, PostAdmin)
```

### Permissions are real and enforced

Staff users only see models they have permission to view, change, add, or delete. Django generates four permissions per model automatically (`view_post`, `change_post`, `add_post`, `delete_post`). Mark `is_staff=True` on a user and assign permissions through groups.

### Admin vs. custom views

| | **Admin** | **Custom views** |
|---|-----------|------------------|
| Audience | Internal staff | End users |
| Setup time | Minutes | Hours / days |
| Customization ceiling | High but bounded | Unlimited |
| Best for | CRUD on every model, internal tools, MVPs | Marketing site, signup flow, dashboards |

Use the admin for everything you can — and graduate to custom views the moment a client says "can my team have a workflow that…".

---

## Syntax

The minimum admin registration:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

The minimum **customized** registration:

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]
    list_filter = ["published"]
    search_fields = ["title"]
```

The shape of every `ModelAdmin` you'll ever write:

```python
class XAdmin(admin.ModelAdmin):
    # Changelist (the table)
    list_display       = [...]
    list_display_links = [...]
    list_filter        = [...]
    search_fields      = [...]
    ordering           = [...]
    list_editable      = [...]
    list_per_page      = 25

    # Change form (the edit page)
    fieldsets           = (...)        # or use `fields = [...]`
    readonly_fields     = [...]
    prepopulated_fields = {...}
    autocomplete_fields = [...]

    # Related rows
    inlines = [...]

    # Actions
    actions = [...]

    # Permissions and queryset
    def get_queryset(self, request): ...
    def has_change_permission(self, request, obj=None): ...
```

---

## Live Code Playground

A complete, polished admin for a blog with `Post`, `Comment`, and `Tag` models.

### `blog/admin.py`

```python
from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment, Tag


# ── Inlines ───────────────────────────────────────────────────────────
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ["author", "body", "is_approved"]
    readonly_fields = []


# ── Bulk actions ──────────────────────────────────────────────────────
@admin.action(description="Mark selected posts as published")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(published=True)
    modeladmin.message_user(request, f"{updated} post(s) published.")


@admin.action(description="Mark selected posts as drafts")
def make_draft(modeladmin, request, queryset):
    queryset.update(published=False)


# ── Post admin ────────────────────────────────────────────────────────
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # changelist (the table)
    list_display       = ["title", "author", "published_badge", "created_at"]
    list_display_links = ["title"]
    list_filter        = ["published", "created_at", "tags"]
    search_fields      = ["title", "body", "author__name"]
    list_editable      = ["published_badge"]                     # ⚠ see note below
    ordering           = ["-created_at"]
    list_per_page      = 25
    date_hierarchy     = "created_at"

    # change form (the edit page)
    fieldsets = (
        ("Content",  {"fields": ("title", "slug", "body")}),
        ("Metadata", {"fields": ("author", "tags", "published"),
                      "classes": ("collapse",)}),
        ("Auditing", {"fields": ("created_at", "updated_at"),
                      "classes": ("collapse",)}),
    )
    readonly_fields     = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["author", "tags"]

    inlines = [CommentInline]
    actions = [make_published, make_draft]

    # custom column with HTML
    @admin.display(description="Status", ordering="published")
    def published_badge(self, obj):
        color = "#10b981" if obj.published else "#9ca3af"
        label = "Published" if obj.published else "Draft"
        return format_html(
            '<span style="color: white; background: {}; padding: 2px 8px; border-radius: 9999px;">{}</span>',
            color, label,
        )

    # only see your own posts unless superuser
    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("author")
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)


# ── Tag admin ─────────────────────────────────────────────────────────
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display  = ["name", "post_count"]
    search_fields = ["name"]

    @admin.display(description="# Posts")
    def post_count(self, obj):
        return obj.posts.count()
```

### `mysite/urls.py` — branding

```python
from django.contrib import admin

admin.site.site_header  = "CodeShelf Admin"
admin.site.site_title   = "CodeShelf Admin Portal"
admin.site.index_title  = "Welcome to CodeShelf"
```

> ⚠️ **Note:** `list_editable` doesn't work on a method like `published_badge`. To make the badge column editable, you'd put `published` itself in `list_editable` and use the badge purely for display. The combo above is shown for completeness — pick one or the other in real code.

---

## Step-by-Step Example

Build a `Post` admin from zero so each step is testable.

### Step 1 — Register the model the simplest way

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Visit `/admin/` → you see a "Posts" link, but the changelist shows `Post object (1)` for every row. Painful.

### Step 2 — Add a `__str__` to your model

```python
# blog/models.py
class Post(models.Model):
    ...
    def __str__(self):
        return self.title
```

The admin and shell now display the title. **Always** define `__str__` on every model.

### Step 3 — Add `list_display`

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "created_at"]
```

You now have three sortable columns. Click any column header to sort.

### Step 4 — Add `list_filter` and `search_fields`

```python
list_filter   = ["published", "created_at"]
search_fields = ["title", "body"]
```

A sidebar with filters and a search box appear at the top of the changelist.

### Step 5 — Group fields with `fieldsets`

```python
fieldsets = (
    ("Content",  {"fields": ("title", "slug", "body")}),
    ("Metadata", {"fields": ("author", "tags", "published"),
                  "classes": ("collapse",)}),
)
```

The change form now has two collapsible sections instead of a wall of fields.

### Step 6 — Auto-fill the slug

```python
prepopulated_fields = {"slug": ("title",)}
```

Type a title — the slug field updates live in JavaScript.

### Step 7 — Make timestamps read-only

```python
readonly_fields = ["created_at", "updated_at"]
```

The fields show on the change form but can't be edited.

### Step 8 — Add a bulk action

```python
@admin.action(description="Publish selected posts")
def publish(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
    actions = [publish]
```

A new dropdown above the changelist lets you select rows and publish them in one click.

### Step 9 — Add inlines for related rows

```python
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
    inlines = [CommentInline]
```

Comments now appear inside the post change form — edit a post and its comments at once.

### Step 10 — Brand the admin

```python
# mysite/urls.py
from django.contrib import admin

admin.site.site_header = "CodeShelf Admin"
admin.site.site_title  = "CodeShelf"
admin.site.index_title = "Operations dashboard"
```

The header, browser tab, and homepage of `/admin/` now read "CodeShelf" instead of the default "Django administration".

---

## Try It Yourself

> **Task:** Build a polished `OrderAdmin` for an `Order` model with:
>
> 1. **List columns** — `id`, `customer`, `status`, `total_display`, `created_at`.
> 2. **Filters** — by `status` and `created_at`.
> 3. **Search** — by customer email and order ID.
> 4. **Inline `OrderLine`** rows on the change form (use `TabularInline`).
> 5. **A custom column `total_display`** that renders the total as `$1,234.50` using `format_html`.
> 6. **A bulk action** "Mark selected as shipped" that updates `status="shipped"` and shows a success message.
> 7. **Per-user filtering** — staff users see only their own orders; superusers see all.

Hints:

- Use `@admin.display(description="Total", ordering="total")` for the custom column.
- For the search, use `search_fields = ["id", "customer__email"]`.
- For per-user filtering, override `get_queryset` and check `request.user.is_superuser`.
- Use `modeladmin.message_user(request, "...")` to show the action's success message.

Try it before peeking at the solution.

---

## Solution

<details>
<summary>Click to reveal the solution</summary>

### `orders/admin.py`

```python
from django.contrib import admin
from django.utils.html import format_html
from .models import Order, OrderLine


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 1
    fields = ["product", "quantity", "unit_price"]


@admin.action(description="Mark selected as shipped")
def mark_shipped(modeladmin, request, queryset):
    updated = queryset.update(status="shipped")
    modeladmin.message_user(request, f"{updated} order(s) marked as shipped.")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ["id", "customer", "status", "total_display", "created_at"]
    list_filter    = ["status", "created_at"]
    search_fields  = ["id", "customer__email"]
    ordering       = ["-created_at"]
    date_hierarchy = "created_at"
    list_per_page  = 25

    fieldsets = (
        ("Order",   {"fields": ("customer", "status")}),
        ("Auditing", {"fields": ("created_at",), "classes": ("collapse",)}),
    )
    readonly_fields = ["created_at"]
    inlines         = [OrderLineInline]
    actions         = [mark_shipped]

    @admin.display(description="Total", ordering="total")
    def total_display(self, obj):
        return format_html("${:,.2f}", obj.total or 0)

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("customer")
        if request.user.is_superuser:
            return qs
        return qs.filter(staff=request.user)
```

### What's happening

1. **`@admin.display(description=…, ordering=…)`** turns a method into a column. The `ordering` argument lets users click the header to sort by the underlying database field.
2. **`format_html("${:,.2f}", value)`** safely formats and escapes — never use Python f-strings to build HTML for the admin.
3. **`@admin.action`** registers a callable as a bulk action; selecting rows + choosing the action calls your function with the **selected QuerySet**. `update()` runs a single SQL `UPDATE`, not one per row.
4. **`get_queryset`** is the right place to scope rows by user. Filtering in `list_filter` doesn't enforce security — a clever URL bypasses it. Filtering in `get_queryset` is universal.
5. **`select_related("customer")`** kills the N+1 problem when rendering the customer column on the changelist.
6. **`message_user`** uses Django's messages framework — the green success bar appears at the top of the admin.

</details>

---

## Key Notes & Tips

> 💡 **Tip:** Always define `__str__` on every model. It's the difference between `Post object (1)` and `"Hello Django"` everywhere in the admin and shell.

> 💡 **Tip:** Use `@admin.register(Model)` instead of `admin.site.register(Model, ModelAdmin)`. It's shorter, harder to forget, and easier to spot in code review.

> 💡 **Tip:** **`autocomplete_fields = ["author", "tags"]`** turns FK and M2M widgets into searchable typeaheads. It only works if the target admin defines `search_fields`.

> 💡 **Tip:** **`date_hierarchy = "created_at"`** adds a clickable year/month/day drilldown bar at the top of the changelist — incredibly useful for time-series data.

> 💡 **Tip:** Use `format_html(...)` (not Python f-strings) when returning HTML from `@admin.display` methods. `format_html` escapes arguments automatically.

> ⚠️ **Warning:** Don't enforce user-scoped permissions with `list_filter` or `search_fields`. Override **`get_queryset(self, request)`** — filters are UI sugar, not security boundaries.

> ⚠️ **Warning:** **`list_editable`** runs an `UPDATE` for each saved row on every "Save" click. Avoid it on tables with thousands of rows or fields that fire signals.

> ⚠️ **Warning:** Don't use the admin as your public UI. The admin assumes the user is staff, has CSRF and session middleware, and is comfortable with technical layouts. Public users get a custom view + form.

> ⚠️ **Warning:** Marking a user **`is_staff=True`** lets them log into `/admin/`. Marking them **`is_superuser=True`** bypasses all permission checks. Use groups + permissions for fine-grained access; reserve superuser for two or three people.

---

## Common Mistakes

- ❌ **Forgetting `__str__`.** Everything in the admin shows `Post object (1)` until you fix this — and you have to fix it eventually.
- ❌ **Putting computed methods in `list_editable`.** Only writable model fields can be edited inline. Methods are read-only.
- ❌ **Calling `Model.objects.filter(...)` inside a list-display method.** That runs **one query per row**. Override `get_queryset` once with `select_related` / `prefetch_related`.
- ❌ **Using f-strings to render HTML in `@admin.display`.** Returns a raw string; user-controlled data is **not** escaped. Use `format_html`.
- ❌ **Leaving `list_filter` on a non-indexed column.** Filtering large tables on an unindexed column is slow. Add `db_index=True` or a composite index.
- ❌ **Confusing `is_staff` with `is_superuser`.** Staff means "can log into admin"; superuser means "bypasses every permission check". Most admin users should be **staff + group permissions**, not superusers.
- ❌ **Not registering the model at all.** No `admin.site.register` → it never appears in the admin.
- ❌ **Hard-coding URLs in admin templates.** The admin already does the right thing; resist the urge to override templates unless you've exhausted `ModelAdmin` options.

---

## Mini Quiz

**Q1.** Which admin attribute controls the **columns shown on the changelist** (the table view)?

- A) `fieldsets`
- B) `list_display` ✔
- C) `list_filter`
- D) `readonly_fields`

**Q2.** Where should you enforce **per-user row visibility** on the admin?

- A) `list_filter`
- B) `search_fields`
- C) `get_queryset(self, request)` ✔
- D) `list_display_links`

**Q3.** Which decorator turns a method into a clickable, sortable admin column?

- A) `@admin.action`
- B) `@admin.register`
- C) `@admin.display(description=..., ordering=...)` ✔
- D) `@cached_property`

**Q4.** What does **`prepopulated_fields = {"slug": ("title",)}`** do?

- A) Auto-saves the slug whenever the title changes
- B) Auto-fills the slug input live in JavaScript as you type the title ✔
- C) Marks the slug as read-only
- D) Indexes the slug column in the database

**Q5.** Which user attribute lets someone **log into `/admin/`**?

- A) `is_active`
- B) `is_authenticated`
- C) `is_staff` ✔
- D) `is_superuser`

---

## Real World Example

A typical SaaS admin for a multi-tenant app combines inlines, custom columns, scoped querysets, and branded chrome.

### `tenants/admin.py`

```python
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Tenant, Member, Invoice


class MemberInline(admin.TabularInline):
    model = Member
    extra = 0
    autocomplete_fields = ["user"]
    fields = ["user", "role", "joined_at"]
    readonly_fields = ["joined_at"]


class InvoiceInline(admin.TabularInline):
    model = Invoice
    extra = 0
    fields = ["amount", "status", "due_date"]
    readonly_fields = ["due_date"]
    show_change_link = True


@admin.action(description="Suspend selected tenants")
def suspend(modeladmin, request, queryset):
    queryset.update(status="suspended")
    modeladmin.message_user(request, f"{queryset.count()} tenant(s) suspended.")


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display       = ["name", "plan", "status_badge", "member_count", "view_site_link"]
    list_filter        = ["plan", "status", "created_at"]
    search_fields      = ["name", "owner__email"]
    ordering           = ["-created_at"]
    date_hierarchy     = "created_at"
    list_per_page      = 25

    fieldsets = (
        ("Identity", {"fields": ("name", "slug", "owner")}),
        ("Plan & Billing", {"fields": ("plan", "status", "trial_ends_at")}),
        ("Auditing", {"fields": ("created_at",), "classes": ("collapse",)}),
    )
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields     = ["created_at"]
    autocomplete_fields = ["owner"]

    inlines = [MemberInline, InvoiceInline]
    actions = [suspend]

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        colors = {"active": "#10b981", "trial": "#f59e0b", "suspended": "#ef4444"}
        return format_html(
            '<span style="color:white;background:{};padding:2px 10px;border-radius:9999px">{}</span>',
            colors.get(obj.status, "#6b7280"), obj.status.title(),
        )

    @admin.display(description="Members")
    def member_count(self, obj):
        return obj.members.count()

    @admin.display(description="Site")
    def view_site_link(self, obj):
        return format_html('<a href="https://{}.example.com" target="_blank">Open ↗</a>', obj.slug)

    def get_queryset(self, request):
        return (
            super().get_queryset(request)
            .select_related("owner")
            .prefetch_related("members")
        )
```

### `mysite/urls.py`

```python
admin.site.site_header = "Acme Admin"
admin.site.site_title  = "Acme Internal"
admin.site.index_title = "Operations dashboard"
```

**What this demonstrates:**

| Pattern | Where |
|---------|-------|
| Two inlines on one parent | `Member` + `Invoice` inside the tenant change form |
| `@admin.display` for badges | `status_badge` returns colored pills via `format_html` |
| `@admin.display` for counts | `member_count` uses prefetch to avoid N+1 |
| `@admin.display` for external links | `view_site_link` opens the tenant's public site in a new tab |
| `select_related` + `prefetch_related` | Performant changelist even with thousands of tenants |
| `@admin.action` | Bulk-suspend with `message_user` feedback |
| Branded chrome | `site_header`, `site_title`, `index_title` |
| `autocomplete_fields` | Searchable owner picker instead of a dropdown of every user |

This is the admin layer of a real Django product, condensed into one screen.

---

## Summary

Today you learned:

- ✔ The admin is **auto-generated CRUD** at `/admin/` for staff users — perfect for internal tools and MVPs.
- ✔ Customize it with a **`ModelAdmin`** subclass — `list_display`, `list_filter`, `search_fields`, `fieldsets`, and friends.
- ✔ **`@admin.register(Model)`** is the preferred registration style.
- ✔ **`@admin.display`** turns methods into sortable, labeled columns; **`@admin.action`** turns methods into bulk operations.
- ✔ **`prepopulated_fields`**, **`readonly_fields`**, **`autocomplete_fields`**, and **`date_hierarchy`** make the change form dramatically nicer.
- ✔ Inlines (**`TabularInline`** / **`StackedInline`**) edit related rows from the parent's change form.
- ✔ Enforce row-level security in **`get_queryset`** — never `list_filter`.
- ✔ Brand the admin with **`site_header`**, **`site_title`**, and **`index_title`**.
- ✔ Use the admin where it shines (internal CRUD); ship custom views for public-facing screens.

### Key Takeaways

```text
✅ Always define __str__ on every model
✅ Prefer @admin.register(Model) over admin.site.register
✅ list_display + list_filter + search_fields = a usable changelist
✅ Group fields with fieldsets and (collapse,)
✅ Use prepopulated_fields={"slug": ("title",)} for slugs
✅ Mark created_at / updated_at readonly_fields
✅ Override get_queryset for per-user / per-tenant scoping
✅ Use format_html (never f-strings) when returning HTML
✅ Reserve is_superuser for very few people; use groups otherwise
```

### ModelAdmin Cheat Sheet

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ── Changelist ────────────────────────────────────────────────
    list_display       = ["title", "author", "published", "created_at"]
    list_display_links = ["title"]
    list_filter        = ["published", "created_at"]
    search_fields      = ["title", "body", "author__name"]
    ordering           = ["-created_at"]
    list_editable      = ["published"]
    list_per_page      = 25
    date_hierarchy     = "created_at"

    # ── Change form ──────────────────────────────────────────────
    fieldsets = (
        ("Content",  {"fields": ("title", "slug", "body")}),
        ("Metadata", {"fields": ("author", "tags"), "classes": ("collapse",)}),
    )
    readonly_fields     = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["author", "tags"]

    # ── Inlines & actions ────────────────────────────────────────
    inlines = [CommentInline]
    actions = [publish, draft]

    # ── Computed columns ─────────────────────────────────────────
    @admin.display(description="Status", ordering="published")
    def status_badge(self, obj):
        return format_html("<b>{}</b>", "Live" if obj.published else "Draft")

    # ── Per-user scoping ─────────────────────────────────────────
    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related("author")
        return qs if request.user.is_superuser else qs.filter(author__user=request.user)
```

### Glossary

| Term | Definition |
|------|------------|
| Admin | Auto-generated CRUD UI at `/admin/` for staff users |
| `ModelAdmin` | Subclass that customizes how a model appears in the admin |
| Changelist | The table view listing all instances of a model |
| Change form | The edit form for one instance |
| `list_display` | Columns shown on the changelist |
| `list_filter` | Sidebar filter widget |
| `search_fields` | Fields the search box queries |
| `fieldsets` | Grouping of fields on the change form |
| `readonly_fields` | Fields shown but not editable |
| `prepopulated_fields` | JS-driven auto-fill (e.g., slug from title) |
| `list_editable` | Fields editable inline on the changelist |
| Inline | Editable related rows on the parent's change form |
| `@admin.display` | Decorator that registers a method as a column |
| `@admin.action` | Decorator that registers a bulk operation |
| `autocomplete_fields` | Searchable typeahead for FK / M2M widgets |
| `date_hierarchy` | Year / month / day drilldown above the changelist |
| `is_staff` | Allows login to `/admin/` |
| `is_superuser` | Bypasses all permission checks |

---

## Next Lesson Navigation

| ← Previous Lesson | Next Lesson → |
|-------------------|---------------|
| [Forms](./ch06-forms.md) | [Authentication](./ch08-authentication.md) |
