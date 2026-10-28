# Design and component guide

## Visual tokens

| Role | Value |
|---|---|
| Heading font | Avant Garde Demi SFDC, bundled WOFF2 |
| Body font | Salesforce Sans, regular and bold WOFF2 |
| Navy ink | `#001e5b` |
| Royal blue | `#022ac0` |
| Action blue | `#066afe` |
| Cyan | `#00b3ff` |
| Teal | `#04e1cb` |
| Yellow, pink, violet accents | `#fcc003`, `#ff538a`, `#d17dfe` |
| Content treatment | Pale blue/teal landscape background and white cards |
| Container | Maximum 1280px, responsive side padding |
| Card shape | Approximately 16–20px corner radius |

The starter preserves the live site's accumulated CSS so the established appearance is retained. Later component rules override earlier base rules. Before changing a component, inspect the last matching rules, including media queries and ID-specific selectors. Prefer a targeted edit to introducing conflicting broad overrides. Old layout-specific selectors may be unused in a new composition; remove them only when safe.

The source style was derived from the user's Dreamforce reference deck: `https://docs.google.com/presentation/d/17fBKzs-ASiBY65VFattMm08Ss-n66taL_rCoLwp4F3E`. Reading that deck is not required to use this self-contained starter. The source code began with `https://github.com/charles-ensley/enterprise-tech-nextgen-presentation`; retain the bundled code license.

## Presentation structure

The neutral starter has eight screens in four chapters:

1. Cover and agenda.
2. Background and values/evidence.
3. Customer overview and solution vision.
4. Perspective and closing contribution/roadmap.

These are reusable narrative roles. Rename or consolidate them to match the task, updating navigation links, section IDs, `data-chapter` values, and accessible heading references together. `data-slide` marks a presentation screen. Multiple screens can share a chapter.

## Component choices

- `.punch-card`: static overview or roadmap box; click selects its spotlight.
- `[data-flip-card]`: headline, one-sentence summary, and optional decorative 3D icon on the front; fuller context on the back. Use the existing native toggle button and unique IDs.
- `.background-theme-row`: text with supporting photography. Align photos to the meaning of the row; do not invent a new screen for extra images unless requested.
- `.foundation--flow` and `.foundation-products`: five logical capabilities by default. Keep each product's role and image together when reordering. This display is not necessarily a one-direction runtime pipeline.
- `.pov-experience-item`: native details panel for supporting experience; keep collapsed summaries short.
- `.journey-tabs`: a compact walkthrough with keyboard-operable tabs and linked panels.
- `[data-recognition-src]`: image expansion. The shared image dialog works with any supplied image, despite the inherited attribute name.

Icon map: 0 coins; 1 database; 2 checklist; 3 speech bubble; 4 magnifier; 5 badge; 6 person/check; 7 books; 8 profile; 9 cubes; 10 clipboard; 11 shield. Use meaningful icons and mark decorative images `alt="" aria-hidden="true"`.

## Content fit

Match parallel headings to approximately two lines with deliberate breaks. Keep card summaries similar in length. Avoid single orphan words and shrinking a whole row to accommodate one long card. Use concise front copy, editable supporting copy on backs, expandable screenshots, and separate rehearsal notes. Chart previews can be small if their full version expands, but nearby labels should explain what the image represents.

The compact POV uses 350px card heights on desktop and 300px on mobile, with scrollable backs. Other components have different deliberate sizes; do not apply those dimensions to the entire site. The default three-column POV continues to 760px, then stacks; inspect intermediate widths if headings change.

## Branded assets

`deck-cover-art.webp` and `deck-cover-base.webp` form the cover. `deck-content-background.webp` supports content screens. `deck-brand-mark.webp` is the Salesforce mark. `deck-manufacturing.webp` is an optional industry motif. Assets named `deck-icon-N.webp` are original 3D icons. All are kept local with the fonts so a generated site does not depend on remote font or image services.
