# Security

## Reporting a problem

Please email **nexaforge.services@gmail.com** with "SFA Monitor security" in the subject. Include
the version (app > Settings > Updates), your distribution and what you found. Please do not open a
public issue for a security problem. You will get an answer within a week.

## How SFA Monitor is built to be safe

- **Signed updates.** Every `SFA-Monitor-Setup.run` in Releases has an Ed25519 signature
  (`.sig`). Your installed copy checks it against the public key it carries before it runs an
  update, and refuses the update if the check fails. Downloads come only from this repository's
  Releases.
- **Root only where needed.** A small collector service runs as root and only reads the system.
  Ending another user's process, starting or stopping a container, renaming the machine and
  installing an update go through `pkexec` and ask for the admin password each time.
- **No listening ports.** Nothing in SFA Monitor accepts network connections.
- **Outgoing requests** go only to `api.github.com` (update check) and `api.ipify.org` (public IP
  for the widget).

## Verify a download yourself

```sh
sha256sum -c SHA256SUMS.txt --ignore-missing
```

Public key used for the signatures:

```
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEA/GH24oLfdSunRFnYOW9d5IwfCjLRgWjGMFBSgbxVfGo=
-----END PUBLIC KEY-----
```

Save it as `sfa-monitor.pem`, then:

```sh
openssl pkeyutl -verify -pubin -inkey sfa-monitor.pem -rawin -in SFA-Monitor-Setup.run -sigfile SFA-Monitor-Setup.run.sig
```

It should print `Signature Verified Successfully`.
