"""Optional full replacement bodies for thin generated chapters."""

def ch06_forms_body() -> str:
    return r'''
## Why Django Forms?

> **Definition:** A **Form** class describes fields, validation rules, and how input maps to Python types. Django renders HTML widgets, validates POST data, and populates `cleaned_data`.

| Benefit | Explanation |
|---------|-------------|
| Validation | Built-in and custom validators |
| HTML generation | Widgets and error display |
| Model integration | `ModelForm` from models |
| Security | CSRF integration |

---

## Basic Form Class

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
| `is_valid()` | Runs validators; fills `cleaned_data` |
| `clean_<field>()` | Field-specific validation |
| `clean()` | Cross-field validation |

---

## Form Validation Flow

```text
POST → Form(request.POST) → is_valid() → full_clean() → cleaned_data OR errors
```

---

## View Integration

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

---

## Rendering Forms in Templates

```django
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send</button>
</form>
```

Manual field loop gives full CSS control — see chapter main examples.

---

## ModelForm

```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "published"]
        widgets = {"body": forms.Textarea(attrs={"rows": 12})}
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

---

## CSRF Protection Deep Dive

> **Definition:** **CSRF** tricks a logged-in browser into submitting unwanted requests. Attackers cannot forge Django's CSRF token.

### Middleware

`CsrfViewMiddleware` validates tokens on unsafe methods (POST, PUT, PATCH, DELETE).

### Template

```django
<form method="post">{% csrf_token %}...</form>
```

### AJAX

Send header `X-CSRFToken` with cookie value `csrftoken`.

### Trusted origins

```python
CSRF_TRUSTED_ORIGINS = ["https://app.example.com"]
```

| Mistake | Risk |
|---------|------|
| No csrf_token | 403 on POST |
| csrf_exempt everywhere | Vulnerable |

---

## Widgets and Styling

```python
widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}
```

---

## Formsets

`modelformset_factory(Post, fields=["title"], extra=3)` edits multiple rows on one page.

---

## File Upload Forms

Use `enctype="multipart/form-data"` and `request.FILES` when binding the form.

---

'''


BODIES: dict = {}  # optional full-body overrides; use topic dicts by default
