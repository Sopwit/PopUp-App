# Release process

## Version source

The package version is defined in `pyproject.toml`; `src/popupapp/__init__.py` must expose the same version. Update `docs/CHANGELOG.md` before creating a release tag.

## Pre-release gate

```bash
make check
APP_VERSION=<version> make appimage
```

Verify the generated filename, architecture suffix, executable bit, and SHA-256 digest.

## GitHub release flow

1. Commit the version and changelog updates.
2. Create and push a signed `v<version>` tag.
3. GitHub Actions builds and attaches `.AppImage` files to the release.
4. Confirm the release body includes both architecture names and SHA-256 values.

Current release assets use these suffixes:

| Architecture | Asset suffix |
| --- | --- |
| x86_64 | `-x86_64.AppImage` |
| ARM64 | `-aarch64.AppImage` |

## Existing-release rebuilds

The **Rebuild ARM64 Release Asset** workflow can rebuild an ARM64 AppImage for an existing tag. It builds from that tag, uploads the architecture-specific artifact, and refreshes release notes with both checksums.
