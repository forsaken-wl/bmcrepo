# .bbr recipe format

Each recipe is a text file with one field per line.

## Fields

- `-name : <name>`: canonical package name (colon required).
- `-provides <names>`: provided names or virtual capabilities.
- `-libprovides <sonames>`: runtime shared library sonames.
- `-depends <list>`: runtime dependencies.
- `-makedepends <list>`: compile-time-only dependencies.
- `-requiredby <list>`: explicit reverse dependencies.
- `-upstream <project>`: upstream project location.
- `-relurl <url>`: immutable source release URL.
- `-checksum <algo:hash>`: source checksum.
- `-prefix <path>`: installation prefix for source-only packages.

Dependencies are comma-separated. Buildroot-provided packages are listed in
`base/buildroot-manifest.txt` and must not be rebuilt by BMX.
