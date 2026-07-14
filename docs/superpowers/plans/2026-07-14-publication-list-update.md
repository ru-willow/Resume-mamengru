# Publication List Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish two accepted 2026 conference papers in the requested publication lists and positions.

**Architecture:** The site keeps equivalent resume markup in the repository root and `docs/`. Apply the same two list-item additions to both HTML files so either GitHub Pages source remains correct.

**Tech Stack:** Static HTML, GitHub Pages, Git.

## Global Constraints

- Preserve the supplied author order, titles, venues, year, and “Accept.” wording.
- Bold Ma Mengru/Mengru Ma consistently with existing publication entries.
- Add a `CCF A` tag only to the ACM MM paper, as supplied by the user.

---

### Task 1: Synchronize publication lists

**Files:**
- Modify: `index.html`
- Modify: `docs/index.html`

**Interfaces:**
- Consumes: Existing ordered publication lists in static HTML.
- Produces: Two synchronized HTML pages containing both new publications.

- [x] **Step 1: Insert the DFPR entry**

Add this as the first list item under “First-author & Corresponding-author Publications” in both files:

```html
<li><strong>Ma Mengru</strong>, Liang Shuo, Ma Wenping, Li Lingling, Liu Xu, Xu Cong. DFPR: Dynamic Fine-Grained Perceptive Bidirectional Image-Text Retrieval. <span class="venue">ACM MM</span>, 2026. Accept. <span class="tag">CCF A</span></li>
```

- [x] **Step 2: Insert the Local Concept Learning entry**

Add this as the last list item under “Collaborative Publications” in both files:

```html
<li>Shuo Li, Mingkun Chang, Pengfang Li, Jiahao Wang, Yang Liu, <strong>Mengru Ma</strong>. Local Concept Learning for Personalized Federated Learning. <span class="venue">PRCV</span>, 2026. Accept.</li>
```

- [x] **Step 3: Verify content and ordering**

Run a PowerShell check that parses each publication section, confirms one occurrence per file, and checks that DFPR is first and Local Concept Learning is last. Expected result: all checks print `True`.

- [x] **Step 4: Review and publish**

Run `git diff --check`, inspect `git diff`, commit the two HTML files and supporting notes, then push `main` to `origin`.
