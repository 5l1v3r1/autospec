#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgcs-patch
Version  : 1.0
Release  : 4
URL      : file:///home/clear/tar/cgcs-patch-1.0.tar.gz
Source0  : file:///home/clear/tar/cgcs-patch-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: cgcs-patch-bin = %{version}-%{release}
Requires: cgcs-patch-python = %{version}-%{release}
Requires: cgcs-patch-python3 = %{version}-%{release}
Requires: cgcs-patch-services = %{version}-%{release}
Requires: /bin/bash
Requires: pycrypto
Requires: python-dev
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wheel
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package bin
Summary: bin components for the cgcs-patch package.
Group: Binaries
Requires: cgcs-patch-services = %{version}-%{release}

%description bin
bin components for the cgcs-patch package.


%package python
Summary: python components for the cgcs-patch package.
Group: Default
Requires: cgcs-patch-python3 = %{version}-%{release}

%description python
python components for the cgcs-patch package.


%package python3
Summary: python3 components for the cgcs-patch package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cgcs-patch package.


%package services
Summary: services components for the cgcs-patch package.
Group: Systemd services

%description services
services components for the cgcs-patch package.


%prep
%setup -q -n cgcs-patch-1.0
%patch1 -p1

%build
## build_prepend content
%define pythonroot           /usr/lib64/python2.7/site-packages
%define debug_package %{nil}
%define _sysconfdir /usr/local/etc
%define _unitdir /usr/lib/systemd/system/
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568960468
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
%{__python} setup.py install --root=$RPM_BUILD_ROOT \
--install-lib=%{pythonroot} \
--prefix=/usr \
--install-data=/usr/share \
--single-version-externally-managed
install -m 755 -d %{buildroot}%{_sbindir}
install -m 755 -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 755 -d %{buildroot}%{_sysconfdir}/goenabled.d
install -m 755 -d %{buildroot}%{_sysconfdir}/init.d
install -m 755 -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 755 -d %{buildroot}%{_sysconfdir}/patching
install -m 700 -d %{buildroot}%{_sysconfdir}/patching/patch-scripts
install -m 755 -d %{buildroot}%{_sysconfdir}/pmon.d
install -m 755 -d %{buildroot}%{_unitdir}
pwd
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-agent \
%{buildroot}%{_sbindir}/sw-patch-agent
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-controller-daemon \
%{buildroot}%{_sbindir}/sw-patch-controller-daemon
install -m 555 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch \
%{buildroot}%{_sbindir}/sw-patch
install -m 555 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/rpm-audit \
%{buildroot}%{_sbindir}/rpm-audit
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-controller-daemon-init.sh \
%{buildroot}%{_sysconfdir}/init.d/sw-patch-controller-daemon
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-agent-init.sh \
%{buildroot}%{_sysconfdir}/init.d/sw-patch-agent
install -m 600 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/patching.conf \
%{buildroot}%{_sysconfdir}/patching/patching.conf
install -m 644 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/policy.json \
%{buildroot}%{_sysconfdir}/patching/policy.json
install -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/pmon-sw-patch-controller-daemon.conf \
%{buildroot}%{_sysconfdir}/pmon.d/sw-patch-controller-daemon.conf
install -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/pmon-sw-patch-agent.conf \
%{buildroot}%{_sysconfdir}/pmon.d/sw-patch-agent.conf
install -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/*.service %{buildroot}%{_unitdir}
install -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch.completion %{buildroot}%{_sysconfdir}/bash_completion.d/sw-patch
install -m 400 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/patch-functions \
%{buildroot}%{_sysconfdir}/patching/patch-functions
install -D -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/patch-tmpdirs.conf \
%{buildroot}%{_tmpfilesdir}/patch-tmpdirs.conf
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/run-patch-scripts \
%{buildroot}%{_sbindir}/run-patch-scripts
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-controller-daemon-restart \
%{buildroot}%{_sbindir}/sw-patch-controller-daemon-restart
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-agent-restart \
%{buildroot}%{_sbindir}/sw-patch-agent-restart
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-init.sh \
%{buildroot}%{_sysconfdir}/init.d/sw-patch
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/sw-patch-controller-init.sh \
%{buildroot}%{_sysconfdir}/init.d/sw-patch-controller
install -m 555 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/patch_check_goenabled.sh \
%{buildroot}%{_sysconfdir}/goenabled.d/patch_check_goenabled.sh
install -m 444 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/patching.logrotate \
%{buildroot}%{_sysconfdir}/logrotate.d/patching
install -m 500 ${RPM_BUILD_DIR}/%{name}-%{version}/bin/upgrade-start-pkg-extract \
%{buildroot}%{_sbindir}/upgrade-start-pkg-extract
%clean
rm -rf $RPM_BUILD_ROOT
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/bash_completion.d/sw-patch
/usr/local/etc/goenabled.d/patch_check_goenabled.sh
/usr/local/etc/init.d/sw-patch
/usr/local/etc/init.d/sw-patch-agent
/usr/local/etc/init.d/sw-patch-controller
/usr/local/etc/init.d/sw-patch-controller-daemon
/usr/local/etc/logrotate.d/patching
/usr/local/etc/patching/patch-functions
/usr/local/etc/patching/patching.conf
/usr/local/etc/patching/policy.json
/usr/local/etc/pmon.d/sw-patch-agent.conf
/usr/local/etc/pmon.d/sw-patch-controller-daemon.conf

%files bin
%defattr(-,root,root,-)
/usr/bin/rpm-audit
/usr/bin/run-patch-scripts
/usr/bin/sw-patch
/usr/bin/sw-patch-agent
/usr/bin/sw-patch-agent-restart
/usr/bin/sw-patch-controller-daemon
/usr/bin/sw-patch-controller-daemon-restart
/usr/bin/upgrade-start-pkg-extract

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/sw-patch-agent.service
/usr/lib/systemd/system/sw-patch-controller-daemon.service
/usr/lib/systemd/system/sw-patch-controller.service
/usr/lib/systemd/system/sw-patch.service
