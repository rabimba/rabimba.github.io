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
        <div class="achievements-grid">
        <div class="achievement-card">
        <div class="achievement-number">35+</div>
        <div class="achievement-label">Peer-Reviewed Publications</div>
        <div class="achievement-detail">28 as first author across AAAI, IEEE ICBC, ACM FSE, USENIX Security, KDD, and more</div>
        </div>
        <div class="achievement-card">
        <div class="achievement-number">4</div>
        <div class="achievement-label">US Patents</div>
        <div class="achievement-detail">1 issued (US11025643B2) + 3 pending (PayPal) covering AI, voice commerce, and authentication</div>
        </div>
        <div class="achievement-card">
        <div class="achievement-number">4x</div>
        <div class="achievement-label">Research Grants</div>
        <div class="achievement-detail">$90K+ from Sui Foundation (3x) and Grant for Web as Principal Investigator</div>
        </div>
        <div class="achievement-card">
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
---
