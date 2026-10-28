# Salesforce Presentation Site

### Created by Megan McCullough

A reusable Codex skill for building interactive, Salesforce-branded presentation websites. It packages the design and presentation controls developed for Megan’s Upmarket presentation into a neutral starter that other solution engineers can adapt.

## What is included

- Salesforce fonts, navy/blue/cyan palette, pale content backgrounds, white rounded cards, and 3D artwork.
- Chapter navigation, responsive layouts, concise flip cards, expandable images, and supporting experience panels.
- A presenter spotlight that highlights the selected box and works alongside card flipping.
- Keyboard navigation, text editing, fullscreen, HTML export, and a portable ZIP packager.
- A neutral starter with four default chapters and eight screens, plus setup, validation, and interaction-check scripts.

Personal photos, customer details, internal analysis, awards, and the original presentation’s speaker notes are excluded.

## Install in Codex

Download `salesforce-presentation-site.zip` from this repository or its Releases page. Extract it and place the enclosed `salesforce-presentation-site` folder in `~/.codex/skills/` (or `$CODEX_HOME/skills/` if configured). The folder should contain `SKILL.md`, `agents/`, `assets/`, `references/`, and `scripts/`.

Restart Codex if the skill does not appear immediately, then ask:

> Use $salesforce-presentation-site to build a presentation website about [your topic].

Alternatively, give Codex this repository’s URL and ask it to install the skill. Local installations do not update automatically when this repository changes.

## Generate a starter directly

From the skill directory, with Python 3.9 or newer:

```sh
python3 scripts/create_site.py --output /absolute/path/my-presentation --title "My presentation" --presenter "Your name" --organization "Your team"
python3 scripts/check_site.py /absolute/path/my-presentation
python3 scripts/package_site.py /absolute/path/my-presentation
```

Preview locally:

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory /absolute/path/my-presentation/public
```

Open http://localhost:4173/. If that port is in use, choose another available port.

## Attribution and asset rights

**Skill packaging, adapted presentation experience, and design guidance: Megan McCullough.**

The underlying website code originated from [Charles Ensley’s enterprise-tech-nextgen-presentation](https://github.com/charles-ensley/enterprise-tech-nextgen-presentation). Its MIT license is preserved in `assets/template/LICENSE`.

Salesforce fonts, logos, icons, and artwork remain the property of their respective owners. The source-code license does not grant additional rights to those branding assets. Use the assets in accordance with the applicable brand and asset permissions. This is a community-created skill, not an official Salesforce product.
