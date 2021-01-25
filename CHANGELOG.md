# 1.2.0

## New features/improvements

- instance autologin to avoid typing `-i`/`-u`/`-p` parameters all the time
- error handling improvements
- better URL encoding
- [new tool] OSGi configuration management - `cqcfg`/`cqcfgdel`/`cqcfgls`
- [new tool] CRUD operations on JCR nodes - `cqjcr`
- [new tool] local CRX package manipulations - `cqrepkg`
- [new tool] package rollbacks - `cqrev`
- [new tool] CRX package snapshot management - `cqsnp`
- Shellcheck fixes across all scripts

## Bugfixes

- output formatting fixes for `cqls`/`cqosgi`/`cqwfl` commands

## Others

- Cognifide -> Wunderman Thompson Technology rebranding

# 1.1.2

---

- Fixed incorrect total number of bundles shown for cqosgi
- Fixed missing \n for cqosgi with -m option supplied
- Fixed the issue: https://github.com/Cognifide/CQ-Unix-Toolkit/issues/17

# 1.1.1

---

- Package upload fix for cqput (stderr OK message fixed)

# 1.1.0

---

## New features/improvements:

- Universal tool to clear dispatcher cache -- cqclr
- Tool to define empty Vault package -- cqpkg
- Tool to check state of OSGI bundle and to manage them (stop/start) -- cqosgi
- Install script improvements (possibility to override some symbolic links)
- Prepared noarch RPM spec file

## Bugfixes:

- On cygwin filename contains double quotes (which is incorrect behavior)
- Unable to work with packages with spaces in package group or package name
- cqwfl is working slowly and it aborts execution for many active workflows
- Problem with accessing tools with whitespace characters included in path
- Displaying version (-v) option doesn't work correctly when calling tool using
  symbolic link
- Increase toolkit portability with all \*BSD
- cqls provides packages lists way too slowly on Windows boxes
