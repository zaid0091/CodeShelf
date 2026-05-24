---
title: useEffect
description: Side effects in React, useEffect hook, cleanup functions, and dependency array rules.
order: 5
tags: [react, useEffect, side-effects, cleanup, dependencies]
---

# Chapter 5: useEffect

> **Effects connect your components to the outside world. Used carefully, they are powerful; overused, they cause bugs.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [What Are Side Effects?](#what-are-side-effects)
2. [useEffect Syntax](#useeffect-syntax)
3. [Dependency Array — None](#dependency-array-none)
4. [Dependency Array — Empty](#dependency-array-empty)
5. [Dependency Array — With Values](#dependency-array-with-values)
6. [exhaustive-deps Rule](#exhaustive-deps-rule)
7. [Cleanup — Event Listeners](#cleanup-event-listeners)
8. [Cleanup — Timers](#cleanup-timers)
9. [Cleanup — AbortController](#cleanup-abortcontroller)
10. [Document Title Pattern](#document-title-pattern)
11. [localStorage Sync](#localstorage-sync)
12. [Fetch on Id Change](#fetch-on-id-change)
13. [Effect vs Event Handler](#effect-vs-event-handler)
14. [Strict Mode Double Invoke](#strict-mode-double-invoke)
15. [When NOT to useEffect](#when-not-to-useeffect)
16. [useLayoutEffect Brief](#uselayouteffect-brief)
17. [Common Mistakes](#common-mistakes)
18. [Interview Points](#interview-points)
19. [Exercises](#exercises)
20. [Chapter Summary](#chapter-summary)

---

## What Are Side Effects?

> **Definition:** Effects touch systems outside render: fetch, timers, document.title, subscriptions.

#### Why this matters for `What Are Side Effects?`

Understanding **What Are Side Effects?** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## useEffect Syntax

```jsx
useEffect(() => {
  // effect
  return () => { /* cleanup */ };
}, [deps]);
```

#### Why this matters for `useEffect Syntax`

Understanding **useEffect Syntax** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Dependency Array — None

Runs after every render — rarely needed.

#### Why this matters for `Dependency Array — None`

Understanding **Dependency Array — None** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Dependency Array — Empty

`[]` runs once on mount (plus Strict Mode dev double-run).

#### Why this matters for `Dependency Array — Empty`

Understanding **Dependency Array — Empty** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Dependency Array — With Values

Re-runs when listed deps change.

#### Why this matters for `Dependency Array — With Values`

Understanding **Dependency Array — With Values** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## exhaustive-deps Rule

Include every value from component scope used inside effect.

#### Why this matters for `exhaustive-deps Rule`

Understanding **exhaustive-deps Rule** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Cleanup — Event Listeners

Return function removing listener.

#### Why this matters for `Cleanup — Event Listeners`

Understanding **Cleanup — Event Listeners** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Cleanup — Timers

`clearInterval` in cleanup.

#### Why this matters for `Cleanup — Timers`

Understanding **Cleanup — Timers** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Cleanup — AbortController

Abort fetch on unmount or url change.

#### Why this matters for `Cleanup — AbortController`

Understanding **Cleanup — AbortController** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Document Title Pattern

Sync `document.title` with state in effect.

#### Why this matters for `Document Title Pattern`

Understanding **Document Title Pattern** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## localStorage Sync

Load initial state lazily; persist in effect on change.

#### Why this matters for `localStorage Sync`

Understanding **localStorage Sync** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Fetch on Id Change

Cancelled flag or AbortController when `userId` changes.

#### Why this matters for `Fetch on Id Change`

Understanding **Fetch on Id Change** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Effect vs Event Handler

Fetch on click → handler. Sync with prop → effect.

#### Why this matters for `Effect vs Event Handler`

Understanding **Effect vs Event Handler** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Strict Mode Double Invoke

Dev-only; cleanup must be correct.

#### Why this matters for `Strict Mode Double Invoke`

Understanding **Strict Mode Double Invoke** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## When NOT to useEffect

Don't sync derived state — compute in render.

#### Why this matters for `When NOT to useEffect`

Understanding **When NOT to useEffect** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## useLayoutEffect Brief

Runs before paint — measurements; default to useEffect.

#### Why this matters for `useLayoutEffect Brief`

Understanding **useLayoutEffect Brief** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---


## Extended Practice 1 — useEffect

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

## Extended Practice 2 — useEffect

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

## Extended Practice 3 — useEffect

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

## Extended Practice 4 — useEffect

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

## Extended Practice 5 — useEffect

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

## Extended Practice 6 — useEffect

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

## Extended Practice 7 — useEffect

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

## Extended Practice 8 — useEffect

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

## Extended Practice 9 — useEffect

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

## Extended Practice 10 — useEffect

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

## Extended Practice 11 — useEffect

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

## Extended Practice 12 — useEffect

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
## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| Missing deps | Stale data | Add to array or fix logic |
| No cleanup | Leaks | Return cleanup fn |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: useEffect purpose?**

Run side effects after render.

---

> **📌 Interview Point 2: Cleanup when?**

Before re-run and unmount.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Document title ⭐

**Task:** Update title with count.

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
| **useEffect** | Side effects after paint |
| **deps** | Control re-runs |

## Next Chapter

Continue to [Chapter 6: Hooks Deep Dive](./ch06-hooks-deep-dive.md).

