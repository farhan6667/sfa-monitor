# Third-party builds

Rocky Linux 10, AlmaLinux 10 and RHEL 10 do not ship conky or xdotool yet, so the SFA Monitor
setup carries its own builds of both and installs them only on those systems. The sources are
unchanged upstream releases. These RPM spec files are the full build recipes.

| Package | Version | Licence | Upstream source |
|---|---|---|---|
| conky | 1.24.2 | GPL-3.0-or-later | https://github.com/brndnmtthws/conky/archive/refs/tags/v1.24.2.tar.gz |
| xdotool | 3.20211022.1 | BSD-3-Clause | https://github.com/jordansissel/xdotool/releases/download/v3.20211022.1/xdotool-3.20211022.1.tar.gz |

To rebuild on Rocky Linux 10 with EPEL and CRB enabled:

```sh
dnf install -y rpm-build rpmdevtools dnf-plugins-core
rpmdev-setuptree
curl -L -o ~/rpmbuild/SOURCES/conky-1.24.2.tar.gz https://github.com/brndnmtthws/conky/archive/refs/tags/v1.24.2.tar.gz
echo "1366b6efcee2cd2c56e5d3430c9d8a1f16d6fef76c5560ff1d8f3fc59dd23959  conky-1.24.2.tar.gz" | sha256sum -c --strict - --ignore-missing
dnf builddep -y --define "cver 1.24.2" conky-sfa.spec
rpmbuild -bb --define "cver 1.24.2" conky-sfa.spec
```

(xdotool the same way with `--define "xver 3.20211022.1"`, checksum
`96f0facfde6d78eacad35b91b0f46fecd0b35e474c03e00e30da3fdd345f9ada`.)

Both checksums above were computed from the tarballs at the upstream URLs listed in the table,
so you can confirm a fresh download matches before it ever reaches `rpmbuild`. A GitHub tag can
in principle be moved to point at different content later, so treat a checksum mismatch as a
reason to stop and compare against the upstream project's own release notes before rebuilding.

If you received one of these binaries from us and want the exact source we built it from,
email nexaforge.services@gmail.com and we will send it, as the GPL asks.
