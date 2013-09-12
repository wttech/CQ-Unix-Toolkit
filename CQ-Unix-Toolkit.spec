# CQ Unix Toolkit
# Copyright (C) 2013 Cognifide Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
Summary: CQ Unix Toolkit
Name: cq-unix-toolkit
Version: 1.0.0
Release: 1
Copyright: GPL
Group: Applications/Sound
Source: https://github.com/Cognifide/CQ-Unix-Toolkit/archive/v1.0.0.tar.gz
URL: https://github.com/Cognifide/CQ-Unix-Toolkit
Vendor: Cognifide Limited
Packager: Arkadiusz Kita <arkadiusz.kita@cognifide.com>

%description
CQ Unix Toolkit is a set of POSIX shell tools
that calls curl and other 3rd party commands
to perform some different tasks on Adobe CQ/AEM
platform such as:

- Build, upload, list, download, install and 
  deletion of CRX zip packages
- Maintenance tasks: consistency checks, TarPM
  compaction and index merge, DataStore garbage
  collection
- Active workflow instances list

%prep
%setup

%build

%install

%files
/usr/bin/cqapi
/usr/bin/cqbld
/usr/bin/cqchk
/usr/bin/cqcp
/usr/bin/cqdel
/usr/bin/cqgc
/usr/bin/cqget
/usr/bin/cqls
/usr/bin/cqmrg
/usr/bin/cqput
/usr/bin/cqrun
/usr/bin/cqtpm
/usr/bin/cqwfl

