"""Chapter-specific study guide appendices (~200 lines each)."""

def faq_section(title: str, pairs: list[tuple[str, str]]) -> str:
    lines = [f"### {title}", ""]
    for q, a in pairs:
        lines.append(f"**Q: {q}**")
        lines.append("")
        lines.append(a)
        lines.append("")
    return "\n".join(lines)


def ch_extra(num: int, title: str, faqs: list[tuple[str, str]], walkthrough: str, code_samples: list[str]) -> str:
    parts = [
        "---",
        "",
        f"## Extended Study Guide: Chapter {num}",
        "",
        f"> Use this section for review, interviews, and spaced repetition after completing **{title}**.",
        "",
        faq_section("Frequently Asked Questions", faqs),
        "",
        "### Step-by-Step Walkthrough",
        "",
        walkthrough,
        "",
        "### Additional Code Patterns",
        "",
    ]
    for i, code in enumerate(code_samples, 1):
        parts.extend([f"#### Pattern {num}.{i}", "", f"```python\n{code.strip()}\n```", ""])
    parts.extend([
        "### Review checklist",
        "",
        "```text",
        "[ ] I can explain the main concepts without notes",
        "[ ] I typed the code examples myself",
        "[ ] I completed all exercises",
        "[ ] I fixed at least one error using the traceback",
        "[ ] I read the linked official Django documentation",
        "```",
        "",
    ])
    return "\n".join(parts)


# Generate extras for all chapters
_STUDY_EXTRA = {}

def _register(num, title, faqs, walk, codes):
    _STUDY_EXTRA[num] = ch_extra(num, title, faqs, walk, codes)


_register(1, "Django Introduction", [
    ("Is Django only for websites?", "Django is primarily for web applications (HTML + APIs). Many teams pair it with Django REST Framework for JSON APIs and separate frontends."),
    ("Can I use Django if I only know basic Python?", "Yes, if you completed functions, classes, modules, and virtual environments in the CodeShelf Python course. This Django course builds on that foundation."),
    ("What is the difference between Django and Django REST Framework?", "Django is the full web framework. DRF is a library that adds REST API tools (serializers, API views) on top of Django."),
    ("Why MTV instead of MVC?", "Historical naming. Django's View is the controller-like logic; Template is the presentation. The pattern is the same idea as MVC."),
    ("What runs first on each request?", "Middleware runs before URL resolution. The view runs after a URL match. Middleware runs again on the response way out."),
    ("Is Django synchronous or asynchronous?", "Django supports both. Traditional views are sync; ASGI and async views exist for modern workloads."),
    ("What database does Django use by default?", "SQLite for new projects in development. Production typically uses PostgreSQL."),
    ("Do I need to know SQL?", "Helpful but not required to start. The ORM covers most needs. Learn SQL for complex reporting and optimization."),
    ("What is the admin used for?", "Internal staff tools: content moderation, support, data fixes. Not usually shown to public users."),
    ("How does Django help with security?", "CSRF middleware, XSS template escaping, ORM parameterization, password hashing, and security middleware headers."),
], """1. Read the chapter introduction and MTV diagram.
2. Sketch the request cycle on paper without looking.
3. List three sites or products that could use Django and why.
4. Install Django in a fresh virtual environment.
5. Browse docs.djangoproject.com intro pages for 15 minutes.
6. Write one paragraph: when you would choose Django vs Flask for a project.""", [
    "# Minimal view (preview)\nfrom django.http import HttpResponse\ndef index(request):\n    return HttpResponse('Hello')",
])

_register(2, "Setup and Project Structure", [
    ("Why django-admin vs manage.py?", "django-admin works globally before a project exists. manage.py is project-specific and sets DJANGO_SETTINGS_MODULE."),
    ("What if I forget to activate the virtual environment?", "You may install packages globally or use the wrong Python. Always check `which python` or `Get-Command python`."),
    ("Can I rename the project folder?", "Yes, but update references in settings, wsgi.py, manage.py, and ROOT_URLCONF if the inner package name changes."),
    ("Why create blog/urls.py manually?", "startapp does not create urls.py by default. You add routing per app."),
    ("What is BASE_DIR?", "Path to project root (parent of settings package). Used for templates, static, database file paths."),
    ("When does db.sqlite3 appear?", "After running migrate the first time."),
    ("Can two apps have the same model name?", "Yes, in different apps. Tables are namespaced: blog_post vs shop_product."),
    ("What does python manage.py check do?", "Validates settings and model configuration without running the server."),
    ("Why is SECRET_KEY important?", "Signs sessions, CSRF tokens, and password reset tokens. Compromise means forge sessions."),
    ("What port does runserver use?", "8000 by default. Pass port as argument to change."),
], """1. Create folder myblog and `python -m venv .venv`.
2. Activate venv and `pip install django`.
3. `django-admin startproject config .` (dot = current directory layout) OR classic startproject.
4. `python manage.py startapp blog`.
5. Add blog to INSTALLED_APPS.
6. Create blog/views.py index view and blog/urls.py.
7. Include blog.urls in project urls.py at path blog/.
8. runserver and visit /blog/.
9. migrate and createsuperuser; visit /admin/.""", [
    "INSTALLED_APPS = [..., 'blog']",
    "path('blog/', include('blog.urls'))",
])

_register(3, "Models and ORM", [
    ("What table name does Post create?", "By default app_label + model name lowercase: blog_post."),
    ("Can I rename the database table?", "Yes: Meta.db_table = 'custom_name'."),
    ("What is related_name?", "Name for reverse relation from ForeignKey target back to source."),
    ("Difference between save() and update()?", "save() per instance, runs signals, calls full_clean optionally. update() single SQL, no save() on each instance."),
    ("When does DoesNotExist happen?", "Model.objects.get() with zero matching rows."),
    ("Can QuerySets be chained?", "Yes. Each filter returns a new QuerySet."),
    ("What is pk?", "Shortcut for primary key field name, usually id."),
    ("How to do OR queries?", "Use Q objects: filter(Q(a=1) | Q(b=2))."),
    ("How to avoid N+1?", "select_related for FK, prefetch_related for M2M."),
    ("Should I use raw SQL?", "When ORM is awkward (complex reports). Always parameterize."),
], """1. Define Post model with fields from chapter.
2. makemigrations and migrate.
3. Open shell: create 3 posts.
4. Filter published=True.
5. Practice __icontains lookup.
6. Add author ForeignKey; migrate again.
7. Loop posts with select_related('author').
8. Try get() vs filter().first() behavior.""", [
    "Post.objects.filter(published=True).order_by('-created_at')",
    "Post.objects.select_related('author').all()",
])

_register(4, "Views and URLs", [
    ("What is URLconf?", "Python module urlpatterns list mapping paths to views callables."),
    ("path vs re_path?", "path uses simple converters; re_path uses regular expressions."),
    ("What is name= in path()?", "URL pattern name for reverse() and {% url %}."),
    ("What does include() do?", "Mounts another urlpatterns under a prefix."),
    ("What is request.GET?", "QueryDict of GET parameters."),
    ("What is request.POST?", "QueryDict of form POST body (not JSON body)."),
    ("How to return JSON?", "JsonResponse(data, safe=False) for lists."),
    ("What does get_object_or_404 do?", "Calls get() and raises Http404 on failure."),
    ("What is reverse_lazy?", "Lazy reverse for class attributes evaluated at import time."),
    ("Order of decorators?", "Bottom decorator is closest to the view function."),
], """1. Create post_list and post_detail views.
2. Wire URLs with int:pk converter.
3. Use render() with template names (create stubs if needed).
4. Add named URLs and test reverse() in shell.
5. Add ?q= search via request.GET.get('q','').
6. Add JsonResponse endpoint for API practice.""", [
    "return render(request, 'blog/post_list.html', {'posts': posts})",
    "return redirect('post-detail', pk=post.pk)",
])

# Chapters 5-14: similar structure with topic-specific FAQs
for n, title, topic in [
    (5, "Templates", "DTL"),
    (6, "Forms", "forms and CSRF"),
    (7, "Admin Panel", "ModelAdmin"),
    (8, "Authentication", "auth"),
    (9, "Migrations", "migrations"),
    (10, "Static and Media Files", "static files"),
    (11, "Class-Based Views", "CBV"),
    (12, "Deployment Basics", "deployment"),
    (13, "Django Best Practices", "best practices"),
    (14, "Interview Preparation", "interviews"),
]:
    _register(n, title, [
        (f"What is the main goal of the {topic} chapter?", f"Master {topic} patterns used in every Django project."),
        ("How does this fit MTV?", "Identify which layer (model, view, template) each example touches."),
        ("What is the most common beginner mistake here?", "See Common Mistakes section in the main chapter body."),
        ("What official docs page should I read?", f"Search docs.djangoproject.com for {topic}."),
        ("How do I practice effectively?", "Build a small blog feature using only this chapter's patterns."),
        ("What breaks in production vs development?", "Settings like DEBUG, static/media serving, and security flags."),
        ("How is this tested?", "Use Django TestCase and Client to assert responses."),
        ("What interview questions appear?", "See Interview Points in the main chapter."),
        ("How does this connect to the next chapter?", "Read the Next Chapter link at the bottom."),
        ("What command validates my project?", "python manage.py check"),
    ], f"""1. Re-read the chapter Table of Contents.
2. For each section, write a one-sentence summary in your notes.
3. Complete all four exercises without peeking at solutions first.
4. Break something on purpose and fix it using error messages.
5. Cross-link concepts to prior chapters (models, views, templates).
6. Optional: teach the chapter outline to someone else in 5 minutes.""", [
        "# Practice pattern\n# See main chapter for full examples",
    ])

STUDY_EXTRA_CH1 = _STUDY_EXTRA[1]
STUDY_EXTRA_CH2 = _STUDY_EXTRA[2]
STUDY_EXTRA_CH3 = _STUDY_EXTRA[3]
STUDY_EXTRA_CH4 = _STUDY_EXTRA[4]
STUDY_EXTRA_CH5 = _STUDY_EXTRA[5]
STUDY_EXTRA_CH6 = _STUDY_EXTRA[6]
STUDY_EXTRA_CH7 = _STUDY_EXTRA[7]
STUDY_EXTRA_CH8 = _STUDY_EXTRA[8]
STUDY_EXTRA_CH9 = _STUDY_EXTRA[9]
STUDY_EXTRA_CH10 = _STUDY_EXTRA[10]
STUDY_EXTRA_CH11 = _STUDY_EXTRA[11]
STUDY_EXTRA_CH12 = _STUDY_EXTRA[12]
STUDY_EXTRA_CH13 = _STUDY_EXTRA[13]
STUDY_EXTRA_CH14 = _STUDY_EXTRA[14]
