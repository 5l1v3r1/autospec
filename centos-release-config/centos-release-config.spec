#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : centos-release-config
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/centos-release-config-1.0.tar.gz
Source0  : file:///home/clear/tar/centos-release-config-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: centos-release-config-data = %{version}-%{release}
Patch1: 0001-add_makefile.patch

%description
No detailed description available

%package data
Summary: data components for the centos-release-config package.
Group: Data

%description data
data components for the centos-release-config package.


%prep
%setup -q -n centos-release-config-1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568603905
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
export SOURCE_DATE_EPOCH=1568603905
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/starlingx
## install_append content
install -m 0644 issue %{buildroot}%{_datadir}/starlingx/stx.issue
install -m 0644 issue.net %{buildroot}%{_datadir}/starlingx/stx.issue.net
sed -i -e "s/@PLATFORM_RELEASE@/%{platform_release}/g" \
%{buildroot}%{_datadir}/starlingx/stx.issue \
%{buildroot}%{_datadir}/starlingx/stx.issue.net
%post
if [ $1 -eq 1 ] ; then
cp -f %{_datadir}/starlingx/stx.issue %{_sysconfdir}/issue
cp -f %{_datadir}/starlingx/stx.issue.net %{_sysconfdir}/issue.net
chmod 644 %{_sysconfdir}/issue
chmod 644 %{_sysconfdir}/issue.net
fi
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/starlingx/stx.issue
/usr/share/starlingx/stx.issue.net
