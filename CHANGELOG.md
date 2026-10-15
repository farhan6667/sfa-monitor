# Changelog

## 1.5.2 (2026-10-15)

Security and stability release with four new features.

- Security: install and update no longer write into users' home folders as root (a local user could use a Desktop symlink to take over a root file). The updater now checks the version inside the signed setup file. Killing a process checks its start time. The status file no longer lists names.
- Memory: the widget leak fixed in 1.0.1 stays fixed, and the app's SSH alert list is now bounded.
- Fixes: wrong rates for second adapters and disks, hanging container logs, a refresh error freezing the app, non-English labels breaking the widget, Nvidia and stuck network drives freezing it, a damaged history database crash loop, 24 hour journal reads every 15 seconds, doubled disk I/O on LVM and RAID, fake network spikes, false UDP port alerts, many core bars, leftovers after removal, and the wrong update repository in the Rocky, Alma and RHEL package.
- New: desktop notification for critical alerts, process history on the charts, a Sensors page, CSV and PNG export and a PDF health report, and an optional alert webhook.
- After installing, log out and back in once to join the new sfa-monitor group. Rocky, Alma and RHEL installs need one manual update.

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
