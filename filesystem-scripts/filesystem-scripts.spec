#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : filesystem-scripts
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/filesystem-scripts-1.0.tar.gz
Source0  : file:///home/clear/tar/filesystem-scripts-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: filesystem-scripts-bin = %{version}-%{release}
Requires: filesystem-scripts-services = %{version}-%{release}
Requires: /bin/systemctl
BuildRequires : systemd-devel
Patch1: 0001-add_makefile.patch

%description
No detailed description available

%package bin
Summary: bin components for the filesystem-scripts package.
Group: Binaries
Requires: filesystem-scripts-services = %{version}-%{release}

%description bin
bin components for the filesystem-scripts package.


%package services
Summary: services components for the filesystem-scripts package.
Group: Systemd services

%description services
services components for the filesystem-scripts package.


%prep
%setup -q -n filesystem-scripts-1.0
%patch1 -p1

%build
## build_prepend content
%define local_bindir /usr/bin/
%define local_etc_initd /usr/local/etc/init.d/
%define local_ocfdir /usr/lib/ocf/resource.d/platform/
%define _unitdir /usr/lib/systemd/system/
%define debug_package %{nil}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568275308
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
export SOURCE_DATE_EPOCH=1568275308
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{local_etc_initd}
## install_append content
install -p -D -m 755 uexportfs %{buildroot}%{local_etc_initd}/uexportfs
install -d -m 755 %{buildroot}%{local_ocfdir}
install -p -D -m 755 nfsserver-mgmt %{buildroot}%{local_ocfdir}/nfsserver-mgmt
install -d -m 755 %{buildroot}%{local_bindir}
install -p -D -m 755 nfs-mount %{buildroot}%{local_bindir}/nfs-mount
install -p -D -m 644 uexportfs.service %{buildroot}%{_unitdir}/uexportfs.service
%post
/bin/systemctl enable uexportfs.service
%clean
rm -rf $RPM_BUILD_ROOT
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/ocf/resource.d/platform/nfsserver-mgmt
/usr/local/etc/init.d/uexportfs

%files bin
%defattr(-,root,root,-)
/usr/bin/nfs-mount

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/uexportfs.service