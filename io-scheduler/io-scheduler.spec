#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : io-scheduler
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/io-scheduler-1.0.tar.gz
Source0  : file:///home/clear/tar/io-scheduler-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

%description
No detailed description available

%prep
%setup -q -n io-scheduler-1.0

%build
## build_prepend content
%define _sysconfdir /usr/local/etc
%define udev_rules_d %{_sysconfdir}/udev/rules.d
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568598566
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
export SOURCE_DATE_EPOCH=1568598566
rm -rf %{buildroot}
mkdir -p %{buildroot}%{udev_rules_d}
## install_append content
install -m 644 %{SOURCE0} %{buildroot}%{udev_rules_d}/60-io-scheduler.rules
%post
/bin/udevadm control --reload-rules
/bin/udevadm trigger --type=devices --subsystem-match=block
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/udev/rules.d/60-io-scheduler.rules
