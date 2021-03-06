#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgcs-users
Version  : 0.3e
Release  : 1
URL      : file:///home/clear/tar/ibsh-0.3e.tar.gz
Source0  : file:///home/clear/tar/ibsh-0.3e.tar.gz
Source1  : file:///home/clear/tar/cgcs-users.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: cgcs-users-bin = %{version}-%{release}
Patch1: ibsh-0.3e.patch
Patch2: ibsh-0.3e-cgcs.patch
Patch3: ibsh-0.3e-cgcs-copyright.patch

%description
Iron Bars SHell - a restricted interactive shell.
Overview
For long i have been in the search of a decent restricted shell, but in vain.
The few i found, were really easy to hack, and there were quite a few docs
around on the web about hacking restricted shells with a menu interface.
For my definitions, a restricted shell must not only prevent the user to
escape her jail, but also not to access any files outside the jail.
The system administrator must have total control over the restricted shell.
These are the major features incorporated and realized by ibsh.

%package bin
Summary: bin components for the cgcs-users package.
Group: Binaries

%description bin
bin components for the cgcs-users package.


%prep
%setup -q -n cgcs-users-1.0
cd ..
%setup -q -T -D -n cgcs-users-1.0 -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
%define _sysconfdir /usr/local/etc
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568769741
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} ibsh


%install
export SOURCE_DATE_EPOCH=1568769741
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds
## install_append content
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/xtns
cp globals.cmds ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/
cp globals.xtns ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/
pwd
tar -xzvf %{SOURCE1}
cp admin.cmds ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/
cp admin.xtns ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/xtns/
cp operator.cmds ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/
cp operator.xtns ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/xtns/
cp secadmin.cmds ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/
cp secadmin.xtns ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/xtns/
install -d 755 ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 ibsh ${RPM_BUILD_ROOT}%{_bindir}/ibsh
%post
chown root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh
chgrp root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh
chown root:root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/globals.*
chown root:root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/admin.cmds
chown root:root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/operator.cmds
chown root:root ${RPM_BUILD_ROOT}/%{_sysconfdir}/ibsh/cmds/secadmin.cmds
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/ibsh/cmds/admin.cmds
/usr/local/etc/ibsh/cmds/operator.cmds
/usr/local/etc/ibsh/cmds/secadmin.cmds
/usr/local/etc/ibsh/globals.cmds
/usr/local/etc/ibsh/globals.xtns
/usr/local/etc/ibsh/xtns/admin.xtns
/usr/local/etc/ibsh/xtns/operator.xtns
/usr/local/etc/ibsh/xtns/secadmin.xtns

%files bin
%defattr(-,root,root,-)
/usr/bin/ibsh
