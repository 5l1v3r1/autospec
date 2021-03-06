#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openvswitch-config
Version  : 1.0
Release  : 1
URL      : file:///home/clr/stx-tar/openvswitch-config-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/openvswitch-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: openvswitch-config-data = %{version}-%{release}
Requires: openvswitch
Patch1: 0001-add-makefile.patch

%description
No detailed description available

%package data
Summary: data components for the openvswitch-config package.
Group: Data

%description data
data components for the openvswitch-config package.


%prep
%setup -q -n openvswitch-config-1.0
%patch1 -p1

%build
## build_prepend content
%define debug_package %{nil}
%define _sysconfdir	/usr/local/etc
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568949449
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
export SOURCE_DATE_EPOCH=1568949449
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_sysconfdir}/openvswitch
## install_append content
install -m 0644 ovsdb-server.pmon.conf %{buildroot}%{_sysconfdir}/openvswitch/ovsdb-server.pmon.conf
install -m 0644 ovs-vswitchd.pmon.conf %{buildroot}%{_sysconfdir}/openvswitch/ovs-vswitchd.pmon.conf
install -d %{buildroot}%{_datadir}/starlingx
install -m 0640 etc_logrotate.d_openvswitch %{buildroot}%{_datadir}/starlingx/etc_logrotate.d_openvswitch
%post
if [ $1 -eq 1 ] ; then
cp -f %{_datadir}/starlingx/etc_logrotate.d_openvswitch %{_sysconfdir}/logrotate.d/openvswitch
chmod 644 %{_sysconfdir}/logrotate.d/openvswitch
fi
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/openvswitch/ovs-vswitchd.pmon.conf
/usr/local/etc/openvswitch/ovsdb-server.pmon.conf

%files data
%defattr(-,root,root,-)
/usr/share/starlingx/etc_logrotate.d_openvswitch
