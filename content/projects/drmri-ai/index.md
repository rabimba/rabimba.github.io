---
title: "Dr.MRI.AI"
summary: "Open-source, privacy-first DICOM viewer that uses Gemma 4 and a three-stage AI architecture (Plan, Review, Synthesize) to intelligently select medical image slices — cutting image tokens by ~99% while running fully in the browser via WebGPU."
tags:
- AI
- Healthcare
- WebGPU
- Gemma 4
- Open Source
date: "2026-05-18"
reading_time: false
featured: true

links:
- icon: globe
  icon_pack: fas
  name: Live Demo
  url: https://rabimba.github.io/drmriai/
- icon: github
  icon_pack: fab
  name: GitHub
  url: https://github.com/rabimba/drmriai
- icon: blog
  icon_pack: fas
  name: Blog Post
  url: https://rkrants.blogspot.com/2026/05/my-partners-mri-didnt-come-with-manual.html
---

Dr.MRI.AI is a web-based DICOM viewer built on a simple observation: the hard part of medical AI isn't the model, it's knowing what to send it. A typical MRI study contains 200+ slices, but only a handful carry the signal. Dr.MRI.AI plans the slice selection before any multimodal analysis runs.

**How it works — Plan → Review → Synthesize:**
- **Plan**: Gemma 4 produces a structured plan (which series, slice range, window/level) from your clinical question in plain English. You can accept, edit, or reject it.
- **Review**: The multimodal model analyzes only the focused subset — 200+ slices reduced to ~16 frames, ~99% fewer image tokens.
- **Synthesize**: A final text-only pass produces a structured report with clickable slice references; export findings plus reviewed evidence as one bundle.

**Privacy-first architecture:**
- DICOM files are processed entirely in the browser — no data is uploaded to any server
- Fully browser-local inference via `onnx-community/gemma-4-E2B-it-ONNX` through Transformers.js + WebGPU
- Provider-agnostic: Gemini API, OpenAI-compatible endpoints, Ollama (MedGemma planning + Gemma 4 review), or fully on-device Gemma 4 Browser

Built with React 19 + TypeScript + Vite and Cornerstone3D for medical image rendering. Featured in the Google Developer Experts May–Jun 2026 AI community roundup. Educational/research tool — not certified as a medical device.
