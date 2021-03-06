#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openldap-config
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/openldap-config-1.0.tar.gz
Source0  : file:///home/clear/tar/openldap-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: openldap-config-data = %{version}-%{release}
Requires: openldap-config-services = %{version}-%{release}
Requires: openldap-servers
Patch1: 0001-add_makefile.patch

%description
No detailed description available

%package data
Summary: data components for the openldap-config package.
Group: Data

%description data
data components for the openldap-config package.


%package services
Summary: services components for the openldap-config package.
Group: Systemd services

%description services
services components for the openldap-config package.


%prep
%setup -q -n openldap-config-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568689102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1568689102
rm -rf %{buildroot}
## install_prepend content
%define _sysconfdir /usr/local/etc
%define _unitdir /usr/lib/systemd/system/
%define debug_package %{nil}
## install_prepend end
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
## install_append content
install -m 755 initscript %{buildroot}%{_sysconfdir}/rc.d/init.d/openldap
install -d -m 740 %{buildroot}%{_sysconfdir}/openldap
install -m 600 slapd.conf %{buildroot}%{_sysconfdir}/openldap/slapd.conf
install -m 600 initial_config.ldif %{buildroot}%{_sysconfdir}/openldap/initial_config.ldif
install -d %{buildroot}%{_datadir}/starlingx
install -m 644 slapd.service %{buildroot}%{_datadir}/starlingx/slapd.service
install -m 644 slapd.sysconfig %{buildroot}%{_datadir}/starlingx/slapd.sysconfig
install -d -m 755 %{buildroot}%{_unitdir}
install -m 644 slapd.service %{buildroot}%{_unitdir}slapd.service
%post
if [ $1 -eq 1 ] ; then
cp -f %{_datadir}/starlingx/slapd.service %{_unitdir}/slapd.service
chmod 644 %{_unitdir}/slapd.service
cp -f %{_datadir}/starlingx/slapd.sysconfig %{_sysconfdir}/sysconfig/slapd
chmod 644 %{_unitdir}/slapd
fi
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/openldap/initial_config.ldif
/usr/local/etc/openldap/slapd.conf
/usr/local/etc/rc.d/init.d/openldap

%files data
%defattr(-,root,root,-)
/usr/share/starlingx/slapd.service
/usr/share/starlingx/slapd.sysconfig

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/slapd.service
