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
  - block: collection
    id: papers
    content:
      title: Distinguished Publications
      filters:
        folders:
          - publication
        featured_only: true
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
