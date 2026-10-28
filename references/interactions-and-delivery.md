# Interaction and delivery invariants

## Cards and spotlight

`setFlip` synchronizes the visible face, `aria-hidden`, `inert`, `aria-expanded`, and the toggle label. The wrapper click handler ignores native controls and editable text so an image button or link does not accidentally flip a card. Preserve this exclusion when adding controls.

Spotlight selection runs in the document's capture phase before the flip handler. Thus the first click both selects and flips; it must not consume that click or require a second click. One steady blue border/cyan halo is active at a time. A repeated click retains the spotlight while the flip control returns to the other face.

Plain static boxes receive keyboard button semantics only when they do not contain interactive descendants or nested spotlight boxes. Avoid nested button roles. Enter/Space selects a keyboard-focused static box. Existing links, buttons, and native details keep their native actions and also select their associated box. Escape clears the spotlight; flip cards also close their back on Escape. Image dialogs retain their own Escape behavior. Selection clears when the selected box leaves the viewport or editing begins.

The selector covers flip cards, static punch cards, theme rows, experience panels, timeline items, and foundation elements. Extend it for a new box class when appropriate; normalize nested targets to their nearest eligible box.

## Images

Use a button with `data-recognition-src`, `data-recognition-alt`, and an informative accessible label to open `#recognition-lightbox`. Put the image URL in a local asset path and use accurate alt text. Keep `#recognition-lightbox-image`, `#recognition-lightbox-frame`, and `#recognition-lightbox-close` IDs consistent with the script.

The optional `data-slide-crop="true"` mechanism is inherited for one original screenshot crop. Do not apply it to arbitrary images: its hard-coded crop geometry is specific to that source. For new media, preserve its aspect ratio; use contain for charts/screenshots and a carefully chosen crop only for decorative photography.

## Navigation and controls

Chapter navigation reflects the screen being viewed. Arrow keys, Page Up/Down, Home, and End move among screens when focus is not inside an interactive control. F toggles fullscreen. Tab sets use Arrow Left/Right, Home, and End. Navigation shortcuts pause during image-dialog viewing and editing. Native `summary` controls are excluded from navigation shortcuts.

Keep the editing controls (`deckEditToggle`, `deckDownloadHtml`) and fullscreen button (`fullscreenToggle`) together with their script. If removing them, remove corresponding listeners and dependencies too. Preserve skip navigation and unique accessible heading IDs.

## Editing and export

Editing disables flipping and spotlight selection. HTML export removes editable state, resets cards to their front faces, closes the image dialog, removes the active spotlight, and resets generated static-card button attributes before reinitialization. It downloads HTML only; it still needs the asset directory. The ZIP packaging helper supplies the complete portable site.

Root `index.html` is the working file. `public/index.html` and assets are the deployment mirror. The packager synchronizes them, checks structural references, and ZIPs the deployment mirror with the code license. It does not deploy anything.

## Checks

Use `scripts/check_site.py` for balanced markup, unique IDs, local media/font paths, internal anchors and accessibility references, mirror consistency, and flip-card state/control structure. It does not inspect appearance or run JavaScript. Syntax-check inline JavaScript with Node when available. For interaction changes, test selection exclusivity, flip-plus-spotlight on the first click, static keyboard access, nested image controls, modal Escape behavior, editing guards, and export reset. Use browser checks only when the environment permits them.
