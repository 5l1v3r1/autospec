#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rsync-config
Version  : 1.0
Release  : 1
URL      : file:///home/clr/stx-tar/rsync-config-1.0.tar.gz
Source0  : file:///home/clr/stx-tar/rsync-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rsync-config-data = %{version}-%{release}
Requires: rsync
Patch1: 0001-add-makefile.patch

%description
No detailed description available

%package data
Summary: data components for the rsync-config package.
Group: Data

%description data
data components for the rsync-config package.


%prep
%setup -q -n rsync-config-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568614157
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
export SOURCE_DATE_EPOCH=1568614157
rm -rf %{buildroot}
%{__install} -d  %{buildroot}%{_datadir}/starlingx/
## install_append content
%{__install} -m 644 rsyncd.conf  %{buildroot}%{_datadir}/starlingx/stx.rsyncd.conf
%post
if [ $1 -eq 1 ] ; then
cp -f %{_datadir}/starlingx/stx.rsyncd.conf  %{_sysconfdir}/rsyncd.conf
fi
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/starlingx/stx.rsyncd.conf
