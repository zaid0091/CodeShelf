---
title: Forms
description: Django Form and ModelForm, validation, CSRF, and form rendering in templates
order: 6
tags: [django, forms, csrf]
---

# Chapter 6: Forms

## 6.1 Why Django forms?

> **Definition:** A **Form** class describes fields and validation logic. Django renders HTML, validates POST data, and converts input to Python types — reducing boilerplate and security mistakes.

Use forms with [views](./ch04-views-urls.md) and [templates](./ch05-templates.md).

## 6.2 Basic Form class

```python
# blog/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, min_length=10)

    def clean_message(self):
        message = self.cleaned_data["message"]
        if "spam" in message.lower():
            raise forms.ValidationError("Message looks like spam.")
        return message
```

| Method | Purpose |
|--------|---------|
| `is_valid()` | Run validators; populate `cleaned_data` |
| `clean_<field>()` | Field-specific validation |
| `clean()` | Cross-field validation |

## 6.3 View integration

```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("contact-success")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})
```

## 6.4 Rendering in templates

```django
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send</button>
</form>
```

| Helper | Output |
|--------|--------|
| `as_p` | Fields wrapped in `<p>` |
| `as_table` | Table rows |
| `as_ul` | List items |
| Manual | Full markup control |

Manual rendering:

```django
{% for field in form %}
  <div class="field">
    {{ field.label_tag }}
    {{ field }}
    {{ field.errors }}
  </div>
{% endfor %}
```

## 6.5 ModelForm

```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "published"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 10}),
        }
```

```python
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post-detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})
```

## 6.6 CSRF protection

> **Definition:** **CSRF** (Cross-Site Request Forgery) tricks a logged-in user's browser into submitting unwanted requests to your site. The browser may send session cookies automatically, but an attacker cannot read or forge Django's CSRF token — so forged requests fail validation.

### 6.6.1 CSRF middleware is always in the request cycle

Django uses:

```python
# settings.py — default middleware stack includes:
"django.middleware.csrf.CsrfViewMiddleware",
```

This middleware runs on **every request** and is responsible for:

| Responsibility | What it does |
|----------------|--------------|
| Token generation | Creates and rotates CSRF tokens when needed |
| Token verification | Validates tokens on unsafe methods (POST, PUT, PATCH, DELETE, etc.) |

> **Key takeaway:** CSRF protection is not optional in a default Django project — it is wired into the middleware pipeline unless you remove it deliberately (never do that in production).

### 6.6.2 Token generation (sent to the client)

When a page is rendered (usually a form), Django:

1. Generates a random CSRF token
2. Stores it in:
   - a **cookie** (`csrftoken`)
   - and/or **embedded in the form** via the template tag

Example in template:

```django
<form method="post">
    {% csrf_token %}
    {# ... your fields ... #}
</form>
```

This renders something like:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="abc123...random...">
```

The cookie and form field work together so Django can verify the submission came from your site.

### 6.6.3 What happens on a POST request

When the user submits a form, Django checks two things.

#### A. Does the request include a CSRF token?

Django looks for the token in:

| Source | Typical use |
|--------|-------------|
| POST data | `csrfmiddlewaretoken` from `{% csrf_token %}` |
| Headers | AJAX: `X-CSRFToken` (must be set in JavaScript) |

Example for fetch/AJAX (read token from cookie):

```javascript
function getCookie(name) {
  const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  return match ? match[2] : null;
}

fetch("/api/submit/", {
  method: "POST",
  headers: {
    "X-CSRFToken": getCookie("csrftoken"),
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ title: "Hello" }),
});
```

#### B. Does it match the cookie token?

Django compares:

```text
Token in request (form field or header)  →  must match  →  Token in csrftoken cookie
```

| Result | HTTP response |
|--------|-----------------|
| Match | Request continues to your view |
| Mismatch or missing | **403 Forbidden** — view never runs |

### 6.6.4 Origin / Referer validation

For extra safety, Django also checks:

| Header | Role |
|--------|------|
| `Origin` | Preferred on modern browsers |
| `Referer` | Fallback when Origin is absent |

If the request appears to come from another domain (and fails trusted-origin rules), it can be blocked even when a token is present.

Configure trusted origins when needed (e.g. separate frontend domain):

```python
# settings.py
CSRF_TRUSTED_ORIGINS = [
    "https://app.example.com",
    "https://www.example.com",
]
```

### 6.6.5 Why this works

CSRF attacks rely on:

```text
1. Browser automatically sends cookies (sessionid, etc.)
2. Victim is logged in and unknowingly triggers a request
```

The attacker can make the victim's browser **send** a POST with cookies, but they **cannot**:

- Read the CSRF token from your page (same-origin policy)
- Guess a valid token (cryptographically random)

So forged requests fail validation at the middleware layer.

```text
Attacker site                    Your Django site
     |                                  |
     |  POST /transfer/ (no valid       |
     |  CSRF token)                     |
     +--------------------------------->|
                                        X 403 Forbidden
```

### 6.6.6 Common mistakes

| Mistake | Risk |
|---------|------|
| Removing `CsrfViewMiddleware` | All POST endpoints vulnerable |
| Using `@csrf_exempt` everywhere | Same as above for those views |
| Forgetting `{% csrf_token %}` | Form POST returns 403 |
| AJAX without `X-CSRFToken` | API calls from your own JS fail or are insecure |

Use `@csrf_exempt` only for carefully reviewed endpoints (e.g. webhooks with their own signature auth) — not for regular user forms.

> **Key takeaway:** Always include `{% csrf_token %}` in POST forms. For AJAX, send `X-CSRFToken` from the `csrftoken` cookie. Let the middleware do its job — do not disable CSRF globally in production.

## 6.7 Field types reference

| Field | HTML input |
|-------|------------|
| `CharField` | text |
| `EmailField` | email |
| `IntegerField` | number |
| `BooleanField` | checkbox |
| `ChoiceField` | select |
| `DateField` | date |
| `FileField` | file |

```python
status = forms.ChoiceField(choices=Post.STATUS_CHOICES)
tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
```

## 6.8 Widgets and CSS classes

```python
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",
            }),
        }
```

## 6.9 Displaying errors

```django
{% if form.non_field_errors %}
  <div class="error">{{ form.non_field_errors }}</div>
{% endif %}
```

Non-field errors originate from `Form.clean()`.

## 6.10 ModelForm Meta options

```python
class Meta:
    model = Post
    fields = ["title", "body", "published"]
    exclude = ["author", "created_at"]
    labels = {"body": "Content"}
    help_texts = {"slug": "URL-friendly identifier"}
```

Prefer explicit `fields` over broad `exclude` for security — only expose intended inputs.

## 6.11 Formsets (brief)

```python
from django.forms import modelformset_factory

PostFormSet = modelformset_factory(Post, fields=["title"], extra=3)
```

Use formsets for editing multiple related objects on one page.

## Exercises

1. Create `ContactForm` with name, email, message; validate minimum message length.
2. Build `PostForm` ModelForm and a create view with author assignment.
3. Render the form manually with custom CSS classes per field.
4. Submit invalid data and confirm field-level errors display correctly.

## Summary

Forms centralize validation and HTML generation. Use `ModelForm` for [models](./ch03-models-orm.md) and always include `{% csrf_token %}` on POST forms.

## Next chapter

Continue to [Admin Panel](./ch07-admin-panel.md).
