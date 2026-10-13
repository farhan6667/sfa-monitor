# Changelog

## 1.0.1 (2026-10-13)

Fix: the desktop widget no longer grows in memory over time.

- The widget made a new text measurement structure on every redraw (twice a second) and Lua never
  freed it, so a widget left running for days could reach several GB of RAM. It now makes one
  when it starts and reuses it. Found on a machine where two widgets had grown to about 4 GB each
  after five days.
- Nothing else changed. Installed copies pick this up through the normal signed update.

## 1.0.0 (2026-10-09)

First public release.

- Desktop widget for every account: CPU, RAM and disk gauges, network graph, top processes,
  health strip, four colour themes, three layouts, drag to move.
- Task manager app (Ctrl+Shift+Esc): processes grouped by application with End Task, CPU,
  memory, disk, network, GPU, services, containers, security and logs pages, 7 days of history.
- One setup file for Kali, Debian 13+, Ubuntu 24.04+, Rocky, Alma and RHEL 9 and 10.
- Signed updates from GitHub Releases with a notice in the widget and app.
- Screenshot button: Flameshot where available, the desktop's own tool elsewhere.
