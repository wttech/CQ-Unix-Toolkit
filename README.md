CQ-Unix-Toolkit
===============

CQ Unix Toolkit is a set of POSIX shell tools that calls curl and other 3rd
party commands to perform some different tasks such as:

* Build, upload, list, download, install and deletion of CRX zip packages
* Maintenance tasks: consistency checks, TarPM compaction and index merge,
  DataStore garbage collection

Each separate action is wrapped to separate stand-alone script with additional
usage output that allows to perform these tasks easily.

Each script can be executed *without parameters* from your terminal i.e.:

  $ ./cqbld
  Usage: cqbld [OPTION...] package-name
  Build (rebuild) already uploaded package by group id and name in CQ Package
  Manager using instance URL.

  Examples:
    cqbld -u admin pack            # Build package named pack
    cqbld -u admin -g GRP pack     # Build package named pack in group GRP
    cqbld -i http://localhost:5510 # Build package for localhost instance on tcp
          -g com.group stuff       # port 5510 named stuff in group:com.group
          -p secret                # with password provided: secret

  Options:

    -u                    use specified usernamed for connection
    -p                    use provided password for authentication
    -i                    use specified instance URL to connect
    -g                    locate package by additional group ID


so you can find out how to operate and specify required arguments.

Compatibilty
------------

*  Compatible with CRX 2.2 or higher
   * cqbld
   * cqcp
   * cqget
   * cqrun
   * cqdel
   * cqput
   * cqls
*  Compatible with CQ 5.5 or higher
   * cqchk
   * cqgc
   * cqmrg
   * cqtpm
*  Compatible with CQ 5.4 or higher
   * cqwfl

Installation
------------

Above scripts don't require special installation. If you want these scripts to
be visible system-wide you can invoke `install` script provided in repository
that creates symbolic link in /usr/local/bin directory or you can change
`INSTALL_DIR` variable in script if you want to something else.
