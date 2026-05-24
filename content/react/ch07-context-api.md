---
title: Context API
description: createContext, Provider, useContext, and when to use Context vs other state solutions.
order: 7
tags: [react, context, useContext, provider, global-state]
---

# Chapter 7: Context API

> **Context shares data across the tree without drilling props at every level.**
> Take your time with each section — understanding beats speed.

---

## Table of Contents

1. [Prop Drilling Problem](#prop-drilling-problem)
2. [createContext](#createcontext)
3. [Provider](#provider)
4. [useContext](#usecontext)
5. [Theme Example](#theme-example)
6. [Default Values](#default-values)
7. [Multiple Contexts](#multiple-contexts)
8. [Performance — New value Object](#performance-new-value-object)
9. [Split Contexts](#split-contexts)
10. [Context vs Redux](#context-vs-redux)
11. [Auth Context Example](#auth-context-example)
12. [Provider Composition](#provider-composition)
13. [composeProviders Helper](#composeproviders-helper)
14. [When Not to Use Context](#when-not-to-use-context)
15. [Testing with Providers](#testing-with-providers)
16. [Common Mistakes](#common-mistakes)
17. [Interview Points](#interview-points)
18. [Exercises](#exercises)
19. [Chapter Summary](#chapter-summary)

---

## Prop Drilling Problem

Passing props through layers that don't need them.

#### Why this matters for `Prop Drilling Problem`

Understanding **Prop Drilling Problem** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## createContext

`const Ctx = createContext(defaultValue)`

#### Why this matters for `createContext`

Understanding **createContext** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Provider

`<Ctx.Provider value={v}>{children}</Ctx.Provider>`

#### Why this matters for `Provider`

Understanding **Provider** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## useContext

Read nearest Provider value.

#### Why this matters for `useContext`

Understanding **useContext** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Theme Example

Full ThemeProvider + useTheme hook.

#### Why this matters for `Theme Example`

Understanding **Theme Example** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Default Values

Used only without Provider above.

#### Why this matters for `Default Values`

Understanding **Default Values** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Multiple Contexts

Split theme, auth, locale.

#### Why this matters for `Multiple Contexts`

Understanding **Multiple Contexts** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Performance — New value Object

Memoize `{ user, setUser }` with useMemo.

#### Why this matters for `Performance — New value Object`

Understanding **Performance — New value Object** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Split Contexts

Fast-changing vs slow-changing data.

#### Why this matters for `Split Contexts`

Understanding **Split Contexts** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Context vs Redux

Context for moderate global; Redux/Zustand for complex.

#### Why this matters for `Context vs Redux`

Understanding **Context vs Redux** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Auth Context Example

login, logout, user, loading.

#### Why this matters for `Auth Context Example`

Understanding **Auth Context Example** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Provider Composition

Nest AuthProvider > ThemeProvider.

#### Why this matters for `Provider Composition`

Understanding **Provider Composition** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## composeProviders Helper

Reduce nesting boilerplate.

#### Why this matters for `composeProviders Helper`

Understanding **composeProviders Helper** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## When Not to Use Context

Don't replace every prop — local state first.

#### Why this matters for `When Not to Use Context`

Understanding **When Not to Use Context** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---

## Testing with Providers

Wrap test render in providers.

#### Why this matters for `Testing with Providers`

Understanding **Testing with Providers** helps you avoid bugs that are hard to debug later. In interviews, you should be able to explain the idea in one or two sentences and show a minimal code example.

#### Quick recap

- Re-read the code sample above and type it yourself in a Vite React app.
- Change one line at a time and observe what breaks in the browser or terminal.
- Use React DevTools to see how parent and child components connect.

#### Connection to other chapters

This topic builds on earlier JavaScript skills (variables, functions, arrays, async) and connects to later React chapters. Keep a running notes file of patterns you reuse across projects.

---


## Extended Practice 1 — Context API

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

## Extended Practice 2 — Context API

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

## Extended Practice 3 — Context API

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

## Extended Practice 4 — Context API

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

## Extended Practice 5 — Context API

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

## Extended Practice 6 — Context API

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

## Extended Practice 7 — Context API

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

## Extended Practice 8 — Context API

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

## Extended Practice 9 — Context API

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

## Extended Practice 10 — Context API

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

## Extended Practice 11 — Context API

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

## Extended Practice 12 — Context API

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

## Extended Practice 13 — Context API

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
## Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|---------------|-----|
| New object each render | All consumers re-render | useMemo value |

---

## Interview Points

Study these before technical interviews. Practice answering out loud in 60–90 seconds.

---

> **📌 Interview Point 1: Context purpose?**

Share value to subtree without prop drilling.

---

## Exercises

Practice by building small pieces in a Vite React app. Try each exercise before opening solutions.

---

### Exercise 1: Theme toggle ⭐

**Task:** Light/dark via context.

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
| **Context** | Provider + useContext |

## Next Chapter

Continue to [Chapter 8: React Router](./ch08-react-router.md).

