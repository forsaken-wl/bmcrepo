# Rinix package repository

Rinix: two-time Linux — cuz why try once?

BMX is now Azure. Packages are managed with:

```sh
azure add <package>
azure del <package>
azure upd
```

Recipes use `.bbr` metadata in this repository and `.bconf` build definitions in
`pkgrepo/`. BCONF is a PKGBUILD-like shell format.

Rinix prefers non-GNU implementations where practical: BSD make rather than GNU
make, muon/samurai rather than GNU build tools, and musl/BusyBox in the base
system.
