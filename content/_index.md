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
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf?v=2
      headings:
        about: 'About Me'
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        I am a Staff Agent Researcher at Paypal and a PhD graduate from the University of Houston. My research focuses on Artificial Intelligence, specifically Large Language Models (LLMs), reasoning, and secure generation.

        My work spans across AI reasoning, decentralized systems, blockchain applications, and mobile computing. I investigate how to design and implement systems that can efficiently handle the challenges of distributed, resource-constrained environments while ensuring security and privacy.

        Feel free to reach out for research collaborations or discussions!
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
---
