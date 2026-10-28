---
name: salesforce-presentation-site
description: Build or restyle an interactive presentation website using Megan’s Upmarket site design, including Salesforce branding, chapter navigation, concise cards, image expansion, and presenter spotlight. Use when this presentation-site style or template is requested.
metadata:
  author: Megan McCullough
---

# Salesforce Presentation Site

Created by **Megan McCullough**.

Create a presentation-first website with the established Salesforce visual language and audience-friendly interactions. Use the bundled starter, which contains the working design and neutral example content; it does not depend on the original project or Google Slides.

## Start a site

Run the helper from this skill's directory, using a new output directory:

```sh
python3 scripts/create_site.py --output /absolute/path/new-presentation --title "Presentation title" --presenter "Presenter name" --organization "Team or organization"
```

The helper creates matching `index.html` and `public/index.html`, local assets, and the original code license. Adapt the generated HTML to the request; the chapter names and count are defaults, not requirements. For an existing site, preserve its content and structure unless the user asks to change them; apply relevant styles and interactions in place rather than overwriting it with the starter.

Read [references/design-and-components.md](references/design-and-components.md) when changing branding, arranging content, or adding a component. Read [references/interactions-and-delivery.md](references/interactions-and-delivery.md) before changing flip, spotlight, editing, image, keyboard, or export behavior.

## Preserve the template's identity

- Use Avant Garde Demi SFDC headings, Salesforce Sans body text, navy text, blue/cyan accents, pale blue/teal backgrounds, white rounded cards, original 3D icons, and the decorative cover artwork. Assets and fonts are bundled locally in `assets/template/assets/`.
- Use concise card fronts for the audience and backs or expandable panels for supporting detail. Keep a row's headings and summaries comparable in length and line count. Shorten or widen copy before reducing text size.
- Maintain matching card heights with scrollable back content where needed. Keep the POV-style overview compact enough for a presentation screen; expanded content may grow or scroll.
- Clicking a flip card flips and spotlights it. Clicking a static card spotlights it. Keep only one blue/cyan spotlight active. Preserve native controls and image expansion inside cards.
- Use semantic, editable HTML. Keep content out of images unless the image is intrinsically a screenshot or supplied media. Use the actual supplied media instead of generating substitutes.

## Content and source handling

The starter examples demonstrate layout, not facts. Replace them with the user's approved content. Do not carry personal photos, awards, customer claims, account figures, or internal analysis from the original Upmarket presentation into a new site. The bundle deliberately excludes them.

When slides or other documents are supplied, establish which version is current from the user's context. Sync only the requested material. This skill does not automatically require deck-first editing or authorize changes to the source deck. Keep detailed talk tracks separate from the public site unless requested.

Check grammar on each update: headings and noun-phrase labels have no terminal period; summaries are complete sentences with terminal punctuation; body copy uses complete sentences. Preserve proper names and evidence distinctions, such as potential versus closed value. Update accessibility labels when a visible heading changes.

Salesforce fonts, artwork, logos, and icons retain their owners' rights; the included MIT license covers the source code, not a new license to those brand assets. For another organization or a public deliverable, retain or replace branding according to the user's requested context and applicable usage rights.

## Verify and deliver

Run:

```sh
python3 scripts/check_site.py /absolute/path/new-presentation
python3 scripts/package_site.py /absolute/path/new-presentation
```

If Node is available, run `node scripts/test_interactions.cjs /absolute/path/new-presentation/index.html` to check first-click spotlight/flip behavior, static keyboard selection, edit guards, modal handling, and script syntax. When browser preview is available and permitted, inspect desktop and mobile, open a card back and image, move the spotlight, and check keyboard access. Structural checks alone do not prove visual fit; describe any unverified visual behavior honestly.

Keep root and `public` HTML/assets synchronized; the packager copies root changes into `public` before checking and packaging. Test meaningful interaction changes, especially nested controls and edit/export states. Do not publish or deploy solely because this skill is invoked. A local preview can use `python3 -m http.server 4173 --bind 127.0.0.1 --directory /absolute/path/new-presentation/public`; use an available port and report the actual address.
