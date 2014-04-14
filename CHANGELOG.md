What's new in...
================

1.1.0
-----

New features/improvements:

* Universal tool to clear dispatcher cache -- cqclr
* Tool to define empty Vault package -- cqpkg
* Tool to check state of OSGI bundle and to manage them (stop/start) -- cqosgi
* Install script improvements (possibility to override some symbolic links)
* Prepared noarch RPM spec file

Bugfixes:

* On cygwin filename contains double quotes (which is incorrect behavior)
* Unable to work with packages with spaces in package group or package name
* cqwfl is working slowly and it aborts execution for many active workflows
* Problem with accessing tools with whitespace characters included in path
* Displaying version (-v) option doesn't work correctly when calling tool using 
  symbolic link
* Increase toolkit portability with all *BSD
* cqls provides packages lists way too slowly on Windows boxes

