CQ-Unix-Toolkit
===============

CQ Unix Toolkit is a set of POSIX shell tools that calls curl and other 3rd
party commands to perform some different tasks on Adobe CQ platform such as:

* Build, upload, list, download, install and deletion of CRX zip packages
* Maintenance tasks: consistency checks, TarPM compaction and index merge,
  DataStore garbage collection
* Active workflow instances list

Each action is wrapped in separate stand-alone script with additional usage
output that allows to perform these tasks easily.

Basically every tool requires authorized connection to CQ instance which
is performed by toolkit using three basic options:

   * -u (username)
   * -p (password)
   * -i (URL to instance) i.e. https://localhost:5510

Which for what?
===============

Below is list of separate tools and purpose of each other

* cqbld -- Builds remotely uploaded CQ package using connection parameters
* cqcp -- Makes a copy of remote CQ package to your local environment 
* cqget -- Makes a copy of CQ resource to your local environment
* cqrun -- Install uploaded CQ package on remote instanse
* cqdel -- Remove completely remotely available CQ package 
* cqput -- Upload package from your local environment
* cqls -- List packages uploaded/installed in remote CQ
* cqchk -- Checks remote CQ instance repository if it's consistent
* cqgc -- Deletes effectively removed content from instance to reclaim free 
          space 
* cqmrg -- Merge CQ TarPM indexes
* cqtpm -- Deletes effectively removed content from TarPM CQ storage
* cqwfl -- Display active (or broken) workflow instances

More information you can find in *GUIDE.md* file.

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

Supported shell environments 
----------------------------

Currently CQ Unix Toolkit supports only some subset of shell environments.
Default shell will be used and it is indicated by /bin/sh symbolic link
in your system.

* bash (tested and fully supported)
* dash (tested and fully supported)
* bash on cygwin (line breaks problem, missing commands)

Notes on Cygwin compatibility
-----------------------------

In order to use toolkit on cygwin make sure you have util-linux cygwin package
installed. Please rememeber that files should have \n endingings only.
Using git clone they can be changes automatically to \r\n so please use one
of the following solutions:

* Change git config option to core.autocrlf = false:


        $ git config --global core.autocrlf input


* Prefix each call with bash -o igncr


        $ ./cqapi
        ./cqapi: line 16: syntax error `$'\r''
        '/cqapi: line 16: `_usage()


        $ bash -o igncr ./cqapi
        Usage: cqapi [OPTION...]
        ...


  This requires changing cqapi line endings using


        $ dos2unix cqapi



CQ Compatibilty
---------------

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
