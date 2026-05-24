---
title: Views and URLs
description: Function-based views, URLconf, HttpRequest, HttpResponse, and redirects
order: 4
tags: [django, views, urls]
---

# Chapter 4: Views and URLs

> **URLs route requests to views — the bridge between the browser and your Python code.**

---

## Table of Contents

1. [URL Routing and URLconf](#url-routing-and-urlconf)
2. [Function-Based Views](#function-based-views)
3. [The HttpRequest Object](#the-httprequest-object)
4. [HttpResponse Types](#httpresponse-types)
5. [Named URLs and reverse()](#named-urls-and-reverse)
6. [include() and URL Namespaces](#include-and-url-namespaces)
7. [Handling POST Requests](#handling-post-requests)
8. [View Decorators](#view-decorators)
9. [Custom Error Handlers](#custom-error-handlers)
10. [HTTP Methods Summary](#http-methods-summary)
11. [Redirects](#redirects)
12. [Permanent vs Temporary Redirects](#permanent-vs-temporary-redirects)
13. [Best Practices](#best-practices)
14. [Common Mistakes](#common-mistakes)
15. [Interview Points](#interview-points)
16. [Exercises](#exercises)
17. [Chapter Summary](#chapter-summary)

---
## URL Routing and URLconf

> **Definition:** **URLconf** is a list of URL patterns Django matches against the request path.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("<int:pk>/", views.post_detail, name="post-detail"),
    path("create/", views.post_create, name="post-create"),
]
```

| Converter | Matches |
|-----------|---------|
| `str` | Non-empty string (no `/`) |
| `int` | Positive integers |
| `slug` | Slug characters |
| `uuid` | UUID |
| `path` | Any path including `/` |

```python
path("archive/<int:year>/", views.archive_year),
re_path(r"^legacy/(?P<id>\d+)/$", views.legacy),
```

### Why this matters

Understanding **URL Routing and URLconf** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **URL Routing and URLconf** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Function-Based Views

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})
```

| Helper | Purpose |
|--------|---------|
| `render()` | Template + context -> HttpResponse |
| `get_object_or_404()` | get() or HTTP 404 |
| `redirect()` | Short redirect response |
| `reverse()` | Build URL from name |

### Why this matters

Understanding **Function-Based Views** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Function-Based Views** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## The HttpRequest Object

```python
def debug_request(request):
    print(request.method)      # GET, POST, ...
    print(request.path)        # /blog/5/
    print(request.GET)         # query string
    print(request.POST)        # form body
    print(request.user)        # auth user
    print(request.session)     # session dict
    print(request.headers)     # HTTP headers
    print(request.FILES)       # uploads
```

```python
q = request.GET.get("q", "")
page = int(request.GET.get("page", 1))
```

Always validate and bound user input (max page size, sanitize search terms).

### Why this matters

Understanding **The HttpRequest Object** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **The HttpRequest Object** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## HttpResponse Types

```python
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404

def plain(request):
    return HttpResponse("Hello", content_type="text/plain")

def json_posts(request):
    data = list(Post.objects.values("id", "title"))
    return JsonResponse(data, safe=False)

def raise_404(request):
    raise Http404("Post not found")
```

| Class | Use |
|-------|-----|
| `HttpResponse` | Arbitrary body |
| `JsonResponse` | JSON API |
| `HttpResponseRedirect` | 302 redirect |
| `HttpResponseNotFound` | 404 without exception |

### Why this matters

Understanding **HttpResponse Types** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **HttpResponse Types** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Named URLs and reverse()

```python
from django.urls import reverse
from django.shortcuts import redirect

def after_create(request, post):
    return redirect("post-detail", pk=post.pk)
    # equivalent: redirect(reverse("post-detail", kwargs={"pk": post.pk}))
```

Template:

```django
<a href="{% url 'post-detail' pk=post.pk %}">Read more</a>
```

Never hard-code `/blog/5/` in multiple files — rename URLs once via `name=`.

### Why this matters

Understanding **Named URLs and reverse()** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Named URLs and reverse()** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## include() and URL Namespaces

```python
# project urls.py
path("blog/", include("blog.urls", namespace="blog")),

# blog/urls.py
app_name = "blog"
urlpatterns = [...]
```

```python
reverse("blog:post-detail", kwargs={"pk": 1})
```

```django
{% url 'blog:post-detail' pk=post.pk %}
```

Namespaces prevent name collisions between apps (`blog:post-list` vs `shop:post-list`).

### Why this matters

Understanding **include() and URL Namespaces** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **include() and URL Namespaces** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Handling POST Requests

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            post = Post.objects.create(title=title, body="", slug="temp")
            return redirect("post-detail", pk=post.pk)
    return render(request, "blog/post_form.html")
```

Prefer [Django Forms](./ch06-forms.md) over raw `request.POST` for validation.

### Why this matters

Understanding **Handling POST Requests** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Handling POST Requests** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## View Decorators

```python
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.cache import cache_page

@login_required
@require_POST
def publish(request, pk):
    ...

@cache_page(60 * 15)
def post_list(request):
    ...
```

Decorators wrap views — order matters (bottom decorator runs first on the way in).

### Why this matters

Understanding **View Decorators** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **View Decorators** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Custom Error Handlers

```python
# urls.py (project level)
handler404 = "mysite.views.page_not_found"
handler500 = "mysite.views.server_error"
```

```python
# views.py
def page_not_found(request, exception):
    return render(request, "404.html", status=404)
```

With `DEBUG=True`, you see debug pages instead of custom handlers.

### Why this matters

Understanding **Custom Error Handlers** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Custom Error Handlers** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## HTTP Methods Summary

| Method | Typical use in Django |
|--------|----------------------|
| GET | Display pages, safe reads |
| POST | Create, update via forms |
| PUT/PATCH | APIs (DRF) |
| DELETE | APIs or DeleteView POST |

Use `@require_http_methods` or `@require_GET` to restrict views.

### Why this matters

Understanding **HTTP Methods Summary** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **HTTP Methods Summary** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Redirects

```python
from django.shortcuts import redirect
return redirect("post-list")
return redirect("post-detail", pk=42)
from django.http import HttpResponseRedirect
return HttpResponseRedirect("/legacy/")
```

### Why this matters

Understanding **Redirects** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Redirects** in one sentence?
- What breaks if you skip or misconfigure this?
- Which official Django documentation page covers this topic?


---

## Permanent vs Temporary Redirects

`redirect()` defaults to 302. Use `redirect(..., permanent=True)` for 301 when URLs move permanently.

### Why this matters

Understanding **Permanent vs Temporary Redirects** helps you build maintainable Django projects and answer common interview questions. Connect this section to the MTV flow: identify which models, views, and templates are involved.

### Try it yourself

1. Open your practice project and locate the files mentioned above.
2. Type the code examples manually — do not copy-paste without reading.
3. Change one line intentionally to cause an error, then read the traceback.
4. Run `python manage.py check` and `python manage.py test` after changes.

### Check your understanding

- Can you explain **Permanent vs Temporary Redirects** in one sentence?
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

**Q: Summarize chapter 4 in one sentence.** — See chapter summary.

**Q: Where does this fit in MTV?** — Identify model, view, template roles.

**Q: What breaks if misconfigured?** — Trace request/response and settings.

---

## Exercises

> Practice is how Django becomes muscle memory. Complete these after reading the chapter.

### Exercise 4.1: Hands-on practice

Implement one feature from Chapter 4 in a local project.

<details>
<summary>Click to reveal solution for Exercise 4.1</summary>

Follow step-by-step sections in this chapter.

</details>

---

### Exercise 4.2: Read the docs

Find the official Django documentation page for this chapter's topic.

<details>
<summary>Click to reveal solution for Exercise 4.2</summary>

docs.djangoproject.com — use search for the topic name.

</details>

---

### Exercise 4.3: Debug exercise

Intentionally cause one error (e.g. wrong template path) and fix using the traceback.

<details>
<summary>Click to reveal solution for Exercise 4.3</summary>

Read TemplateDoesNotExist or NoReverseMatch paths in the error page.

</details>

---

### Exercise 4.4: Explain aloud

Explain Chapter 4 concepts to a friend without looking at notes.

<details>
<summary>Click to reveal solution for Exercise 4.4</summary>

If you stumble, re-read the section you could not explain.

</details>

---
## Chapter Summary

Excellent work completing Chapter 4. Here is what you learned:

- Completed Chapter 4: Views and URLs
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

**➡️ [Next Chapter →](./ch05-templates.md)**

---

*Chapter 4 of the Complete Django Guide | [Report an issue](https://github.com/zaid0091/CodeShelf/issues)*

---

## Extended Study Guide: Views and URLs

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

## Extended Study Guide: Chapter 4

> Use this section for review, interviews, and spaced repetition after completing **Views and URLs**.

### Frequently Asked Questions

**Q: What is URLconf?**

Python module urlpatterns list mapping paths to views callables.

**Q: path vs re_path?**

path uses simple converters; re_path uses regular expressions.

**Q: What is name= in path()?**

URL pattern name for reverse() and {% url %}.

**Q: What does include() do?**

Mounts another urlpatterns under a prefix.

**Q: What is request.GET?**

QueryDict of GET parameters.

**Q: What is request.POST?**

QueryDict of form POST body (not JSON body).

**Q: How to return JSON?**

JsonResponse(data, safe=False) for lists.

**Q: What does get_object_or_404 do?**

Calls get() and raises Http404 on failure.

**Q: What is reverse_lazy?**

Lazy reverse for class attributes evaluated at import time.

**Q: Order of decorators?**

Bottom decorator is closest to the view function.


### Step-by-Step Walkthrough

1. Create post_list and post_detail views.
2. Wire URLs with int:pk converter.
3. Use render() with template names (create stubs if needed).
4. Add named URLs and test reverse() in shell.
5. Add ?q= search via request.GET.get('q','').
6. Add JsonResponse endpoint for API practice.

### Additional Code Patterns

#### Pattern 4.1

```python
return render(request, 'blog/post_list.html', {'posts': posts})
```

#### Pattern 4.2

```python
return redirect('post-detail', pk=post.pk)
```

### Review checklist

```text
[ ] I can explain the main concepts without notes
[ ] I typed the code examples myself
[ ] I completed all exercises
[ ] I fixed at least one error using the traceback
[ ] I read the linked official Django documentation
```
