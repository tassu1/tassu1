# Md Tahseen Alam

**Backend-Focused Full Stack Developer**

Building reliable APIs, secure systems, and scalable web applications. I take a problem from initial requirements through to a working, deployed product — with a particular interest in the parts of a system most people never see.

`Open to opportunities` · Backend / Full Stack · Jaipur, India

[Portfolio ↗](https://tassu1.vercel.app/) · [LinkedIn ↗](https://www.linkedin.com/in/md-tahseen-alam-892317263/) · [Email ↗](mailto:tassutahsee@gmail.com) · [LeetCode ↗](https://leetcode.com/u/tahseen_/)

---

### `01 /` What I work on

- Backend architecture and API design
- Authentication, authorization, and multi-tenant systems
- Databases, caching, and background job processing
- Cloud deployment and production reliability

---

### `02 /` Selected work

**[EduManage](https://github.com/tassu1/edumanage)** — Multi-tenant school management
A role-based school management platform with school-level data isolation, attendance, exams, timetables, and an AI tutor — 5 roles, tested across 4 schools with 35+ demo accounts.
`React` `Node.js` `Express` `MongoDB` `Socket.IO` `JWT/RBAC` `OpenRouter`
> **How do you stop one school from seeing another's data?** Every protected route runs a school-context check, and every query is filtered by `schoolId` — a shared database with enforced logical isolation, rather than a separate database per school. The tradeoff is that isolation depends on that filter being applied consistently everywhere, with no room for a missed check.

[Live demo](https://edumanageai.vercel.app/) · [Source](https://github.com/tassu1/edumanage)

**[MockMate](https://github.com/tassu1/mockmate)** — AI interview platform
An interview practice tool where AI-generated reports are handled asynchronously so the API never blocks on generation.
`Node.js` `Express` `Redis` `BullMQ` `SSE` `OpenRouter`
> **Why a background worker instead of generating the report in the request?** LLM report generation runs far longer than an HTTP cycle should hold open. A BullMQ queue on Redis hands the job to a separate worker (3× retry, exponential backoff), and progress streams back over SSE — more moving parts, but the API stays responsive.

[Live demo](https://getmockmate.vercel.app/) · [Source](https://github.com/tassu1/mockmate)

**[Lexica AI](https://github.com/tassu1/Lexica)** — AI document generation
Turns a single prompt into a structured, exportable document — pitches, market analyses, synopses, proposals — as PDF or DOCX.
`Next.js` `TypeScript` `NextAuth` `MongoDB` `OpenRouter`
> **How do you keep long-form generation from failing partway through?** One large prompt-to-document call is fragile and risks hitting token limits. The pipeline splits into a prompt-enhancement pass and a separate generation pass, so a failure is cheaper to detect and retry — at the cost of extra orchestration and latency.

[Live demo](https://lexicaai.vercel.app/) · [Source](https://github.com/tassu1/Lexica)

**[InnerLight](https://github.com/tassu1/innerlight)** — AI wellness companion
Mood tracking, journaling, and an AI companion (Lumi) in one app, with JWT-protected data per user and Cloudinary-backed media storage.
`React` `Node.js` `Express` `MongoDB` `JWT` `Cloudinary`
> **Why split the client and API instead of one monolith?** It keeps app services, user data, and external media storage cleanly separated — the tradeoff is handling CORS and environment config across two deployed pieces instead of one.

[Live demo](https://innerlightai.vercel.app/) · [Source](https://github.com/tassu1/innerlight)

---

### `03 /` My toolkit

**Backend** — Node.js · Express · TypeScript · REST APIs · JWT · RBAC · Socket.IO
**Data & infrastructure** — MongoDB · PostgreSQL · Redis · BullMQ · Docker · AWS EC2/S3 · Vercel
**Frontend** — React · Next.js · Redux · Tailwind CSS
**AI & integrations** — OpenRouter API · NextAuth · Google OAuth · Cloudinary

---

### `04 /` How I think about engineering

I try to understand the problem before choosing the implementation — user needs, data boundaries, security, and where the system is likely to break, before writing code. Most of what I've built came out of a real constraint: keeping five schools' data apart on shared infrastructure, a queue that couldn't afford to block on AI generation, a document pipeline that had to survive a bad generation attempt. The edge cases are usually where the actual engineering is.

Outside of product work: 300+ problems solved across LeetCode and other platforms, and Branch Topper in my Diploma (82.17%).

---

### `05 /` Let's connect

Open to backend engineering and full-stack roles — reach out via [email](mailto:tassutahsee@gmail.com) or [LinkedIn](https://www.linkedin.com/in/md-tahseen-alam-892317263/).
