#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sm-client
Version  : 1.0
Release  : 2
URL      : file:///home/clr/stx-tar/sm-client-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/sm-client-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sm-client-bin = %{version}-%{release}
Requires: sm-client-python = %{version}-%{release}
Requires: sm-client-legacypython
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3

%description
Python bindings for the Service Management API
==============================================

%package bin
Summary: bin components for the sm-client package.
Group: Binaries

%description bin
bin components for the sm-client package.


%package legacypython
Summary: legacypython components for the sm-client package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the sm-client package.


%package python
Summary: python components for the sm-client package.
Group: Default

%description python
python components for the sm-client package.


%prep
%setup -q -n sm-client-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566376406
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
%global _buildsubdir %{_builddir}/%{name}-%{version}
## install_prepend end
python2 -tt setup.py build -b py2 install --root=%{buildroot}
## install_append content
install -d %{buildroot}/usr/bin
install -m 755 %{_buildsubdir}/usr/bin/smc %{buildroot}/usr/bin
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/smc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)