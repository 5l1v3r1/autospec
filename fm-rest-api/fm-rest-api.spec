#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fm-rest-api
Version  : 1.0
Release  : 5
URL      : file:///home/clr/stx-tar/fm-rest-api-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/fm-rest-api-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: fm-rest-api-bin = %{version}-%{release}
Requires: fm-rest-api-python = %{version}-%{release}
Requires: fm-rest-api-python3 = %{version}-%{release}
Requires: fm-rest-api-services = %{version}-%{release}
Requires: Paste
Requires: WebOb
Requires: eventlet
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : oslo.config
BuildRequires : oslo.db
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : systemd
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package bin
Summary: bin components for the fm-rest-api package.
Group: Binaries
Requires: fm-rest-api-services = %{version}-%{release}

%description bin
bin components for the fm-rest-api package.


%package python
Summary: python components for the fm-rest-api package.
Group: Default
Requires: fm-rest-api-python3 = %{version}-%{release}

%description python
python components for the fm-rest-api package.


%package python3
Summary: python3 components for the fm-rest-api package.
Group: Default
Requires: python3-core

%description python3
python3 components for the fm-rest-api package.


%package services
Summary: services components for the fm-rest-api package.
Group: Systemd services

%description services
services components for the fm-rest-api package.


%prep
%setup -q -n fm-rest-api-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568109703
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
## install_prepend content
%define local_bindir /usr/bin/
%define local_initddir /usr/local/etc/rc.d/init.d
%define pythonroot /usr/lib64/python2.7/site-packages
%define local_etc_pmond /usr/local/etc/pmon.d/
%define debug_package %{nil}
%define _unitdir /usr/lib/systemd/system/
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
echo "Start install"
export PBR_VERSION=%{version}
%{__python} setup.py install --root=%{buildroot} \
--install-lib=%{pythonroot} \
--prefix=/usr \
--install-data=/usr/share \
--single-version-externally-managed
install -p -D -m 644 scripts/fm-api.service %{buildroot}%{_unitdir}/fm-api.service
install -d -m 755 %{buildroot}%{local_initddir}
install -p -D -m 755 scripts/fm-api %{buildroot}%{local_initddir}/fm-api
install -d -m 755 %{buildroot}%{local_etc_pmond}
install -p -D -m 644 fm-api-pmond.conf %{buildroot}%{local_etc_pmond}/fm-api.conf
cd %{_builddir}/%{name}-%{version} && oslo-config-generator --config-file fm/config-generator.conf --output-file %{_builddir}/%{name}-%{version}/fm.conf.sample
install -p -D -m 644 %{_builddir}/%{name}-%{version}/fm.conf.sample %{buildroot}%{_sysconfdir}/fm/fm.conf
%clean
echo "CLEAN CALLED"
rm -rf $RPM_BUILD_ROOT
%post
/bin/systemctl enable fm-api.service >/dev/null 2>&1
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/pmon.d/fm-api.conf
/usr/local/etc/rc.d/init.d/fm-api

%files bin
%defattr(-,root,root,-)
/usr/bin/fm-api
/usr/bin/fm-dbsync

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fm-api.service
