# bmcrepo

BMX (Burn More Xapps) recipe repository for BMC Linux.

Recipes use the `.bbr` format. Dependencies are resolved as a graph and built in
dependency-first order. Packages already provided by the Buildroot base system are
not rebuilt by BMX.

## Layout

- `core/`: recipes for packages intended for normal BMC systems.
- `extra/`: optional addons and non-essential packages.
- `base/`: Buildroot base-system package inventory.
- `docs/`: recipe and workflow documentation.

## .bbr fields

- `-name`: canonical package name.
- `-provides`: names or virtual capabilities provided.
- `-libprovides`: runtime shared-library sonames.
- `-depends`: runtime dependencies.
- `-makedepends`: compile-time-only dependencies.
- `-requiredby`: reverse dependencies when explicitly maintained.
- `-upstream`: upstream project location.
- `-relurl`: immutable source release URL.
- `-checksum`: source checksum (algorithm:hex).
