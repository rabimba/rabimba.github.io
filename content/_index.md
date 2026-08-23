---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '3rem'

sections:
  - block: resume-biography-3
    content:
      username: admin
      text: ''
      button:
        text: Download CV
        url: uploads/resume.pdf?v=2
      headings:
        about: 'About Me'
        education: ''
        interests: ''
    design:
      css_class: hbx-bg-gradient
      avatar:
        size: medium
        shape: circle
  - block: markdown
    content:
      title: 'Research Overview'
      subtitle: ''
      text: |-
        I am a Staff Agent Researcher at PayPal and a PhD graduate from the University of Houston, advised by Prof. Weidong (Larry) Shi. My research sits at the intersection of **AI reasoning**, **decentralized systems**, and **software security**.

        **Core research areas:**
        - **LLM Reasoning & Code Generation** &mdash; Multi-agent architectures for reliable code/test generation (AgentTester, LogBabylon) and hallucination mitigation
        - **Blockchain & Smart Contract Security** &mdash; Cross-chain vulnerability detection, decentralized infrastructure, and formal verification of smart contracts
        - **Quantum-Enhanced ML** &mdash; Quantum contrastive embeddings for near-term devices (QuCoWE, AAAI 2026)

        I am a [Google Developer Expert](https://developers.google.com/community/experts) in Web Technologies & ML, a 3x Sui Foundation Research Award recipient, and serve as Associate Chair for CSCW 2026.
    design:
      columns: '1'
  - block: markdown
    id: achievements
    content:
      title: 'Key Achievements'
      subtitle: 'A snapshot of research impact, recognition, and community contributions'
      text: |-
        <div class="achievements-grid" role="list">
        <div class="achievement-card" role="listitem">
        <div class="achievement-number">35+</div>
        <div class="achievement-label">Peer-Reviewed Publications</div>
        <div class="achievement-detail">28 as first author across AAAI, IEEE ICBC, ACM FSE, USENIX Security, KDD, and more</div>
        </div>
        <div class="achievement-card" role="listitem">
        <div class="achievement-number">4</div>
        <div class="achievement-label">US Patents</div>
        <div class="achievement-detail">1 issued (US11025643B2) + 3 pending (PayPal) covering AI, voice commerce, and authentication</div>
        </div>
        <div class="achievement-card" role="listitem">
        <div class="achievement-number">4x</div>
        <div class="achievement-label">Research Grants</div>
        <div class="achievement-detail">$90K+ from Sui Foundation (3x) and Grant for Web as Principal Investigator</div>
        </div>
        <div class="achievement-card" role="listitem">
        <div class="achievement-number">85+</div>
        <div class="achievement-label">Invited Talks</div>
        <div class="achievement-detail">Google I/O, OSCON, NDC Sydney, FOSDEM, KubeCon, Stanford, MIT, Berkeley RDI, and more</div>
        </div>
        <div class="achievement-card achievement-award">
        <div class="achievement-icon">🏆</div>
        <div class="achievement-label">ACM SIGSOFT Distinguished Paper Award</div>
        <div class="achievement-detail">ACM AIWare 2025 — Securing the Multi-Chain Ecosystem</div>
        </div>
        <div class="achievement-card achievement-award">
        <div class="achievement-icon">🎓</div>
        <div class="achievement-label">Best Dissertation Award</div>
        <div class="achievement-detail">Dan E. Wells Outstanding Dissertation Award & UH CS Best Dissertation (2025)</div>
        </div>
        <div class="achievement-card achievement-award">
        <div class="achievement-icon">⭐</div>
        <div class="achievement-label">Google Developer Expert</div>
        <div class="achievement-detail">Web Technologies (2018–present) & Google Cloud AI/ML (2024–present)</div>
        </div>
        <div class="achievement-card achievement-award">
        <div class="achievement-icon">🔥</div>
        <div class="achievement-label">NVIDIA Developer Champion</div>
        <div class="achievement-detail">Recognized for contributions to AI and GPU computing community (2026)</div>
        </div>
        </div>

        <style>
        .achievements-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
          gap: 1rem;
          margin-top: 1.5rem;
        }
        .achievement-card {
          padding: 1.25rem;
          border: 1px solid var(--color-border, #e2e8f0);
          border-radius: 0.875rem;
          background: rgba(99, 102, 241, 0.04);
          text-align: center;
          transition: all 0.2s;
        }
        .achievement-card:hover {
          border-color: var(--color-primary, #6366f1);
          transform: translateY(-2px);
        }
        .achievement-number {
          font-size: 2rem;
          font-weight: 800;
          color: var(--color-primary, #6366f1);
          line-height: 1;
          margin-bottom: 0.35rem;
        }
        .achievement-label {
          font-size: 0.875rem;
          font-weight: 700;
          margin-bottom: 0.35rem;
        }
        .achievement-detail {
          font-size: 0.75rem;
          opacity: 0.65;
          line-height: 1.4;
        }
        .achievement-award .achievement-icon {
          font-size: 1.75rem;
          margin-bottom: 0.35rem;
        }
        .achievement-award .achievement-label {
          font-size: 0.8125rem;
        }
        </style>
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Distinguished Publications
      filters:
        folders:
          - publication
        tag: Distinguished
    design:
      view: article-grid
      columns: 2
  - block: markdown
    id: grants
    content:
      title: 'Grants & Funding'
      subtitle: ''
      text: |-
        - **Sui Foundation Academic Research Award** (2023, 2024, 2025) &mdash; Primary Investigator, $25,000/year for research on decentralized infrastructure and smart contract security
        - **Grant for Web** &mdash; Primary Investigator, $15,000 for advancing privacy-preserving and decentralized web technologies
        - **Google Cloud Research Innovator** (2023, 2024) &mdash; Cloud credits and research support for AI/ML projects
    design:
      columns: '1'
  - block: collection
    id: projects
    content:
      title: Research Projects
      filters:
        folders:
          - projects
    design:
      view: article-grid
      columns: 3
  - block: markdown
    id: open-source
    content:
      title: 'Open Source'
      subtitle: 'Research code, benchmarks, and tools I build and maintain'
      text: |-
        <div class="oss-grid" role="list">
        <a class="oss-card" role="listitem" href="https://github.com/rabimba/drmriai" target="_blank" rel="noopener">
        <div class="oss-name">Dr.MRI.AI</div>
        <div class="oss-desc">Privacy-first DICOM viewer that plans slice selection with Gemma 4 before multimodal review — ~99% fewer image tokens, fully in-browser via WebGPU.</div>
        <div class="oss-meta">TypeScript &middot; <a href="https://rabimba.github.io/drmriai/" target="_blank" rel="noopener">Live demo</a></div>
        </a>
        <a class="oss-card" role="listitem" href="https://github.com/rabimba/vllm-xla-bench" target="_blank" rel="noopener">
        <div class="oss-name">vllm-xla-bench</div>
        <div class="oss-desc">Single-variable benchmark harness for serving LLMs with vLLM across CUDA and OpenXLA/XLA backends — honest goodput under fixed SLOs.</div>
        <div class="oss-meta">Python &middot; presented at OpenXLA DevLab 2026</div>
        </a>
        <a class="oss-card" role="listitem" href="https://github.com/rabimba/speedracer-AI" target="_blank" rel="noopener">
        <div class="oss-name">speedracer-AI</div>
        <div class="oss-desc">The AI Race Coach Android dashboard from the Google I/O GDE Field Test — 10 Hz telemetry, Gemini reasoning, on-device Gemma 4 coaching.</div>
        <div class="oss-meta">Kotlin &middot; Jetpack Compose</div>
        </a>
        <a class="oss-card" role="listitem" href="https://github.com/rabimba/context-contamination-usenix26" target="_blank" rel="noopener">
        <div class="oss-name">context-contamination-usenix26</div>
        <div class="oss-desc">Artifacts for our USENIX Security 26 paper: the LogInject benchmark, Context Stitching attacks, and layered-defense mitigation evaluation.</div>
        <div class="oss-meta">Python &middot; USENIX Security 26</div>
        </a>
        <a class="oss-card" role="listitem" href="https://github.com/rabimba/trustable-ai-codelab" target="_blank" rel="noopener">
        <div class="oss-name">trustable-ai-codelab</div>
        <div class="oss-desc">Co-authored Google codelab &ldquo;Building Trustable AI at 100 MPH&rdquo; — split-brain architecture, telemetry streaming, guardrails, and Gemini strategy layers.</div>
        <div class="oss-meta">TypeScript &middot; <a href="https://codelabs.developers.google.com/codelabs/trustable-at-100-mph" target="_blank" rel="noopener">Official codelab</a></div>
        </a>
        <a class="oss-card oss-more" href="https://github.com/rabimba?tab=repositories" target="_blank" rel="noopener">
        <div class="oss-name">More on GitHub &rarr;</div>
        <div class="oss-desc">Research prototypes, agents, and tooling — from smart-contract security scanners to multi-agent routers.</div>
        <div class="oss-meta">github.com/rabimba</div>
        </a>
        </div>
        <style>
        .oss-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-top: 1.5rem; }
        .oss-card { display: flex; flex-direction: column; gap: 0.4rem; padding: 1.1rem 1.15rem; border: 1px solid var(--color-border, #e2e8f0); border-radius: 0.875rem; background: rgba(99, 102, 241, 0.04); text-decoration: none; color: inherit; transition: all 0.2s; }
        .oss-card:hover { border-color: var(--color-primary, #6366f1); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(99, 102, 241, 0.10); }
        .oss-name { font-weight: 800; font-size: 0.95rem; color: var(--color-primary, #6366f1); }
        .oss-desc { font-size: 0.8125rem; opacity: 0.75; line-height: 1.45; flex-grow: 1; }
        .oss-meta { font-size: 0.72rem; opacity: 0.55; }
        .oss-meta a { color: inherit; }
        </style>
  - block: markdown
    id: gde-community
    content:
      title: 'Google Developer Expert & Community'
      subtitle: 'Giving back to the developer community'
      text: |-
        - **Google Developer Expert** in AI/ML & Cloud (previously Chrome & Web, 2018&ndash;2024) &mdash; [directory profile](https://developers.google.com/community/experts/directory?specialization=ml%2Cgcp&text=rabimba)
        - **Co-author** of Google's official [Building Trustable AI at 100 MPH](https://codelabs.developers.google.com/codelabs/trustable-at-100-mph) codelab with a global GDE cohort
        - **Invited speaker** at Google I/O Field Tests (Sonoma Raceway 2026), OpenXLA DevLab Summer 2026, and the GDE Summit at Google I/O 2025
        - **Google Cloud Research Innovator** (2023) and **Google Cloud Champions Innovator** (2023&ndash;2025)
        - **Mentor & judge** for the Google Solutions Challenge and Women Techmakers Academy; earlier **Mozilla Tech Speaker** and Mozilla Research Fellowship (2018)
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - events
    design:
      view: card
  - block: collection
    id: blog
    content:
      title: Recent Blog Posts
      filters:
        folders:
          - blog
        count: 3
    design:
      view: article-grid
      columns: 3
  - block: markdown
    id: service
    content:
      title: 'Professional Service'
      subtitle: ''
      text: |-
        - **Associate Chair**, ACM CSCW 2026
        - **Scientific Advisory Committee**, Texas Quantum Initiative (2025)
        - **Google Developer Expert**, Web Technologies (2018-present) & Google Cloud (2024-present)
        - **Reviewer**: IEEE ICBC, ACM CSCW, BRAINS
    design:
      columns: '1'
  - block: markdown
    id: contact
    content:
      title: 'Get in Touch'
      subtitle: ''
      text: |-
        <p style="text-align:center; max-width: 42rem; margin: 0 auto 1.25rem; opacity: 0.75;">Happy to talk about research collaborations, industry problems, talks, or the GDE program. The fastest way to reach me is email or LinkedIn.</p>
        <div class="contact-grid">
        <a class="contact-btn contact-primary" href="mailto:rkaranjai@uh.edu">&#9993; Email</a>
        <a class="contact-btn" href="https://www.linkedin.com/in/rabimba/" target="_blank" rel="noopener">LinkedIn</a>
        <a class="contact-btn" href="https://github.com/rabimba" target="_blank" rel="noopener">GitHub</a>
        <a class="contact-btn" href="https://scholar.google.com/citations?user=PYmmdne2aRMC" target="_blank" rel="noopener">Google Scholar</a>
        </div>
        <style>
        .contact-grid { display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: center; margin-top: 1.25rem; }
        .contact-btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.6rem 1.3rem; border-radius: 0.6rem; border: 1px solid var(--color-border, #e2e8f0); font-weight: 600; font-size: 0.9rem; text-decoration: none; color: inherit; transition: all 0.2s; }
        .contact-btn:hover { border-color: var(--color-primary, #6366f1); color: var(--color-primary, #6366f1); transform: translateY(-2px); }
        .contact-primary { background: var(--color-primary, #6366f1); border-color: var(--color-primary, #6366f1); color: #fff; }
        .contact-primary:hover { color: #fff; opacity: 0.92; }
        </style>
---
