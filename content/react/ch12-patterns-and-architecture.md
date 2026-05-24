---
title: Patterns & Architecture
description: Lifting state, compound components, render props, container/presentational split, and folder structure.
order: 12
tags: [react, patterns, architecture, compound-components, lifting-state]
---

# Chapter 12: Patterns & Architecture

> **Structure code so features grow without tangled spaghetti.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Lifting State Up](#lifting-state-up)
2. [Container vs Presentational](#container-vs-presentational)
3. [Compound Components](#compound-components)
4. [Render Props](#render-props)
5. [Slot Composition](#slot-composition)
6. [State Colocation](#state-colocation)
7. [Feature Folders](#feature-folders)
8. [Pages Folder](#pages-folder)
9. [Custom Hook Extraction](#custom-hook-extraction)
10. [Error Boundaries in Features](#error-boundaries-in-features)
11. [Controlled Boundaries](#controlled-boundaries)
12. [Scaling Teams](#scaling-teams)
13. [Common Mistakes](#common-mistakes)
14. [Interview Points](#interview-points)
15. [Exercises](#exercises)
16. [Chapter Summary](#chapter-summary)

---

## Lifting State Up

Shared sibling state in parent.

#### Why this matters for `Lifting State Up`

Understanding **Lifting State Up** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Container vs Presentational

Logic vs pure UI — hooks replace many containers.

#### Why this matters for `Container vs Presentational`

Understanding **Container vs Presentational** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Compound Components

Tabs with Context sharing activeIndex.

#### Why this matters for `Compound Components`

Understanding **Compound Components** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Render Props

Function as child/prop — hooks often replace.

#### Why this matters for `Render Props`

Understanding **Render Props** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Slot Composition

header, sidebar props.

#### Why this matters for `Slot Composition`

Understanding **Slot Composition** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## State Colocation

Keep state as low as possible.

#### Why this matters for `State Colocation`

Understanding **State Colocation** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Feature Folders

features/auth, components/ui.

#### Why this matters for `Feature Folders`

Understanding **Feature Folders** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Pages Folder

Route-level components.

#### Why this matters for `Pages Folder`

Understanding **Pages Folder** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Custom Hook Extraction

useTodos from TodoList.

#### Why this matters for `Custom Hook Extraction`

Understanding **Custom Hook Extraction** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Error Boundaries in Features

Co-locate error UI.

#### Why this matters for `Error Boundaries in Features`

Understanding **Error Boundaries in Features** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Controlled Boundaries

Expose onSubmit not raw state.

#### Why this matters for `Controlled Boundaries`

Understanding **Controlled Boundaries** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Scaling Teams

Consistent exports and naming.

#### Why this matters for `Scaling Teams`

Understanding **Scaling Teams** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---


## Extended Practice 1 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice1.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice1')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 2 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice2.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice2')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 3 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice3.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice3')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 4 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice4.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice4')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 5 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice5.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice5')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 6 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice6.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice6')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 7 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice7.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice7')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 8 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice8.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice8')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 9 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice9.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice9')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 10 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice10.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice10')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 11 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice11.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice11')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 12 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice12.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice12')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 13 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice13.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice13')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 14 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice14.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice14')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 15 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice15.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice15')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---

## Extended Practice 16 — Patterns & Architecture

Apply one idea from this chapter in isolation:

1. Create `Practice16.jsx` in your Vite `src/` folder.
2. Import it from `App.jsx` and render it.
3. Add a `console.log('render Practice16')` at the top of the component function.
4. Change props or state and watch the console — notice when React re-renders.
5. Open React DevTools → Components and find your practice component.

**Reflection questions:**

- What was the smallest working example you could build?
- What error did you hit first when experimenting?
- How would you explain this topic to someone who only knows JavaScript?

**Stretch goal:** Combine this practice with one concept from the previous chapter and one hook or pattern you already know.

---
## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| State too high | Unnecessary re-renders | Colocate |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Lifting state?**

Move shared state to common parent.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Currency converter ⭐

**Task:** Two synced inputs.

<details>
<summary>💡 Hint (click to reveal)</summary>



</details>

<details>
<summary>✅ Solution (click to reveal)</summary>

Build the solution in your Vite project and compare with examples in this chapter.

</details>

---

## Chapter Summary

| Concept | Takeaway |
|---------|----------|
| **Lifting** | Shared parent state |
| **Compound** | Flexible API |

## Next Chapter

Continue to [Chapter 13: Testing](./ch13-testing.md).

