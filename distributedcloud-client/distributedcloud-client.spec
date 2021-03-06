#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distributedcloud-client
Version  : 1.0.0
Release  : 1
URL      : file:///home/clear/tar/distributedcloud-client-1.0.0.tar.gz
Source0  : file:///home/clear/tar/distributedcloud-client-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: distributedcloud-client-bin = %{version}-%{release}
Requires: distributedcloud-client-python = %{version}-%{release}
Requires: distributedcloud-client-python3 = %{version}-%{release}
Requires: pbr
BuildRequires : Babel
BuildRequires : Routes >= 1.12.3
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : git
BuildRequires : jsonschema >= 2.0.0
BuildRequires : keystonemiddleware
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : pbr
BuildRequires : pbr >= 1.8
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : sphinxcontrib-httpdomain
BuildRequires : systemd

%description
Dcmanagerclient
================
Wind River's Distributed Cloud system supports an edge computing solution by providing
central management and orchestration for a geographically distributed network of Titanium
Cloud systems.

%package bin
Summary: bin components for the distributedcloud-client package.
Group: Binaries

%description bin
bin components for the distributedcloud-client package.


%package python
Summary: python components for the distributedcloud-client package.
Group: Default
Requires: distributedcloud-client-python3 = %{version}-%{release}

%description python
python components for the distributedcloud-client package.


%package python3
Summary: python3 components for the distributedcloud-client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the distributedcloud-client package.


%prep
%setup -q -n distributedcloud-client-1.0.0

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567146579
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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
rm -rf {test-,}requirements.txt tools/{pip,test}-requires
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export PBR_VERSION=%{version}
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
%{__python} setup.py install --skip-build --root %{buildroot}
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dcmanager

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
