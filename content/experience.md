---
title: 'Experience'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: resume-experience
    content:
      username: admin
    design:
      date_format: 'January 2006'
      is_education_first: false
  - block: resume-skills
    content:
      title: Technical Skills
      username: admin
    design:
      show_skill_percentage: true
  - block: markdown
    id: hobbies
    content:
      title: 'Hobbies & Interests'
      subtitle: 'When I\'m not building AI systems or writing papers'
      text: |-
        <div class="hobbies-grid">
        <div class="hobby-card">
        <div class="hobby-icon">📚</div>
        <div class="hobby-name">Reading Books</div>
        <div class="hobby-desc">Sci-fi, research papers, and everything in between</div>
        </div>
        <div class="hobby-card">
        <div class="hobby-icon">✨</div>
        <div class="hobby-name">Otaku</div>
        <div class="hobby-desc">Anime, manga, and Japanese pop culture enthusiast</div>
        </div>
        <div class="hobby-card">
        <div class="hobby-icon">🏔️</div>
        <div class="hobby-name">Hiking</div>
        <div class="hobby-desc">Exploring trails and finding perspective at altitude</div>
        </div>
        <div class="hobby-card">
        <div class="hobby-icon">🚴</div>
        <div class="hobby-name">Biking</div>
        <div class="hobby-desc">Road and trail cycling around the Bay Area</div>
        </div>
        <div class="hobby-card">
        <div class="hobby-icon">🍺</div>
        <div class="hobby-name">Appreciating Brews</div>
        <div class="hobby-desc">Coffee connoisseur and craft beer explorer</div>
        </div>
        </div>
        <style>
        .hobbies-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
          gap: 1.25rem;
          margin-top: 1.5rem;
        }
        .hobby-card {
          padding: 1.5rem 1.25rem;
          border: 1px solid var(--color-border, #e2e8f0);
          border-radius: 1rem;
          background: linear-gradient(135deg, rgba(99, 102, 241, 0.06), rgba(37, 99, 235, 0.03));
          text-align: center;
          transition: all 0.25s ease;
        }
        .hobby-card:hover {
          border-color: var(--color-primary, #6366f1);
          transform: translateY(-4px);
          box-shadow: 0 10px 30px rgba(99, 102, 241, 0.12);
        }
        .hobby-icon {
          font-size: 2.5rem;
          margin-bottom: 0.75rem;
          line-height: 1;
        }
        .hobby-name {
          font-size: 1rem;
          font-weight: 700;
          margin-bottom: 0.35rem;
        }
        .hobby-desc {
          font-size: 0.8125rem;
          opacity: 0.6;
          line-height: 1.4;
        }
        </style>
    design:
      columns: '1'
  - block: resume-awards
    content:
      title: Awards
      username: admin
  - block: resume-languages
    content:
      title: Languages
      username: admin
---
