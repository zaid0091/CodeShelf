---
title: Forms
description: Controlled and uncontrolled inputs, form submission, validation patterns, and accessibility.
order: 9
tags: [react, forms, validation, controlled, uncontrolled]
---

# Chapter 9: Forms

## 9.1 Forms in React

HTML forms collect user input and submit data. In React, you choose how tightly the DOM and state stay synchronized.

> **Definition:** A **controlled input** has its value owned by React state. An **uncontrolled input** stores value in the DOM and is read via refs.

## 9.2 Controlled forms (recommended)

```jsx
import { useState } from 'react';

function SignupForm() {
  const [form, setForm] = useState({
    name: '',
    email: '',
    password: '',
  });
  const [errors, setErrors] = useState({});

  function handleChange(e) {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  }

  function validate() {
    const next = {};
    if (!form.name.trim()) next.name = 'Name is required';
    if (!form.email.includes('@')) next.email = 'Invalid email';
    if (form.password.length < 8) next.password = 'Min 8 characters';
    return next;
  }

  function handleSubmit(e) {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    setErrors({});
    console.log('Submit:', form);
  }

  return (
    <form onSubmit={handleSubmit} noValidate>
      <label>
        Name
        <input name="name" value={form.name} onChange={handleChange} />
        {errors.name && <span className="error">{errors.name}</span>}
      </label>

      <label>
        Email
        <input
          name="email"
          type="email"
          value={form.email}
          onChange={handleChange}
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </label>

      <label>
        Password
        <input
          name="password"
          type="password"
          value={form.password}
          onChange={handleChange}
        />
        {errors.password && <span className="error">{errors.password}</span>}
      </label>

      <button type="submit">Sign up</button>
    </form>
  );
}
```

### Controlled vs uncontrolled

| | Controlled | Uncontrolled |
|---|------------|--------------|
| Value source | React state | DOM |
| Read value | From state | `ref.current.value` |
| Validation timing | On change / submit | Usually on submit |
| React recommendation | Default choice | File inputs, integrations |

## 9.3 Uncontrolled inputs with useRef

```jsx
import { useRef } from 'react';

function QuickSearch() {
  const inputRef = useRef(null);

  function handleSubmit(e) {
    e.preventDefault();
    const query = inputRef.current.value;
    console.log('Search:', query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} defaultValue="" placeholder="Search..." />
      <button type="submit">Go</button>
    </form>
  );
}
```

Use `defaultValue` (not `value`) for uncontrolled inputs.

## 9.4 Handling different input types

```jsx
function Preferences() {
  const [prefs, setPrefs] = useState({
    newsletter: false,
    role: 'developer',
    bio: '',
  });

  function handleChange(e) {
    const { name, type, value, checked } = e.target;
    setPrefs(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  }

  return (
    <form>
      <label>
        <input
          type="checkbox"
          name="newsletter"
          checked={prefs.newsletter}
          onChange={handleChange}
        />
        Subscribe to newsletter
      </label>

      <select name="role" value={prefs.role} onChange={handleChange}>
        <option value="developer">Developer</option>
        <option value="designer">Designer</option>
      </select>

      <textarea name="bio" value={prefs.bio} onChange={handleChange} rows={4} />
    </form>
  );
}
```

## 9.5 Validation strategies

### Client-side validation layers

| Layer | When | Purpose |
|-------|------|---------|
| Inline | On blur / change | Immediate feedback |
| On submit | Form submit | Block invalid requests |
| Server | API response | Authoritative rules |

### Displaying errors

```jsx
<input
  name="email"
  value={email}
  onChange={handleChange}
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? 'email-error' : undefined}
/>
{errors.email && (
  <span id="email-error" role="alert" className="error">
    {errors.email}
  </span>
)}
```

### Disabling submit while invalid

```jsx
const isValid = form.email && form.password.length >= 8;

<button type="submit" disabled={!isValid || isSubmitting}>
  {isSubmitting ? 'Saving...' : 'Save'}
</button>
```

## 9.6 Form libraries

For large forms, consider:

| Library | Strength |
|---------|----------|
| **React Hook Form** | Performance, minimal re-renders |
| **Formik** | Mature ecosystem |
| **Zod / Yup** | Schema validation |

```jsx
// React Hook Form + Zod (conceptual)
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

function Login() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: zodResolver(schema),
  });

  return (
    <form onSubmit={handleSubmit(data => console.log(data))}>
      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}
      <button type="submit">Login</button>
    </form>
  );
}
```

## 9.7 Multi-step forms

```jsx
function Wizard() {
  const [step, setStep] = useState(0);
  const [data, setData] = useState({});

  const steps = [
    <StepAccount data={data} onChange={setData} />,
    <StepProfile data={data} onChange={setData} />,
    <StepReview data={data} />,
  ];

  return (
    <div>
      {steps[step]}
      <button disabled={step === 0} onClick={() => setStep(s => s - 1)}>
        Back
      </button>
      {step < steps.length - 1 ? (
        <button onClick={() => setStep(s => s + 1)}>Next</button>
      ) : (
        <button onClick={() => submit(data)}>Submit</button>
      )}
    </div>
  );
}
```

Lift shared form state to the wizard parent; validate each step before advancing.

## 9.8 Security reminders

- Never trust client validation alone — always validate on the server
- Sanitize user content before rendering HTML
- Use HTTPS for credential submission
- Consider CSRF tokens for cookie-based auth

## Exercises

1. **Login form** — Email/password with inline validation and disabled submit.
2. **Survey** — Mix checkbox, radio, select, and textarea in one controlled form.
3. **Multi-step** — 3-step registration with progress indicator.
4. **Accessibility** — Add `aria-*` attributes and associate labels with inputs.

## Summary

| Topic | Key point |
|-------|-----------|
| Controlled | `value` + `onChange` synced with state |
| Uncontrolled | `ref` + `defaultValue` |
| Validation | Client UX + server authority |
| Libraries | React Hook Form for complex forms |
| a11y | Labels, `aria-invalid`, error announcements |

## Next chapter

Continue to [Chapter 10: Data Fetching](./ch10-data-fetching.md).
