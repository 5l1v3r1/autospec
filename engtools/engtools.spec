#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : engtools
Version  : 1.0
Release  : 4
URL      : file:///home/clear/clearlinux/packages/engtools/engtools-1.0.tar.gz
Source0  : file:///home/clear/clearlinux/packages/engtools/engtools-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: engtools-bin = %{version}-%{release}
Requires: engtools-services = %{version}-%{release}
Patch1: 0001-Makefile.patch

%description
No detailed description available

%package bin
Summary: bin components for the engtools package.
Group: Binaries
Requires: engtools-services = %{version}-%{release}

%description bin
bin components for the engtools package.


%package services
Summary: services components for the engtools package.
Group: Systemd services

%description services
services components for the engtools package.


%prep
%setup -q -n engtools-1.0
%patch1 -p1

%build
## build_prepend content
%define local_bindir /usr/bin/
%define local_initdir /usr/local/etc/init.d/
%define local_confdir /usr/local/etc/engtools/
%define local_systemddir /usr/lib/systemd/system/
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568191866
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
export SOURCE_DATE_EPOCH=1568191866
rm -rf %{buildroot}
install -d 755 %{buildroot}%{local_bindir}
## install_append content
install -d 755 %{buildroot}%{local_bindir}
install -m 755 buddyinfo.py %{buildroot}%{local_bindir}
install -m 755 chewmem %{buildroot}%{local_bindir}
install -m 755 ceph.sh %{buildroot}%{local_bindir}
install -m 755 cleanup-engtools.sh %{buildroot}%{local_bindir}
install -m 755 collect-engtools.sh %{buildroot}%{local_bindir}
install -m 755 diskstats.sh %{buildroot}%{local_bindir}
install -m 755 engtools_util.sh %{buildroot}%{local_bindir}
install -m 755 filestats.sh %{buildroot}%{local_bindir}
install -m 755 iostat.sh %{buildroot}%{local_bindir}
install -m 755 linux_benchmark.sh %{buildroot}%{local_bindir}
install -m 755 memstats.sh %{buildroot}%{local_bindir}
install -m 755 netstats.sh %{buildroot}%{local_bindir}
install -m 755 postgres.sh %{buildroot}%{local_bindir}
install -m 755 rabbitmq.sh %{buildroot}%{local_bindir}
install -m 755 remote/rbzip2-engtools.sh %{buildroot}%{local_bindir}
install -m 755 remote/rstart-engtools.sh %{buildroot}%{local_bindir}
install -m 755 remote/rstop-engtools.sh %{buildroot}%{local_bindir}
install -m 755 remote/rsync-engtools-data.sh %{buildroot}%{local_bindir}
install -m 755 slab.sh %{buildroot}%{local_bindir}
install -m 755 ticker.sh %{buildroot}%{local_bindir}
install -m 755 top.sh %{buildroot}%{local_bindir}
install -m 755 vswitch.sh %{buildroot}%{local_bindir}
install -m 755 live_stream.py %{buildroot}%{local_bindir}
install -d 755 %{buildroot}%{local_confdir}
install -m 644 -p -D cfg/engtools.conf %{buildroot}%{local_confdir}
install -d 755 %{buildroot}%{local_initdir}
install -m 755 init.d/collect-engtools.sh %{buildroot}%{local_initdir}
install -d 755 %{buildroot}%{local_systemddir}
install -m 644 -p -D collect-engtools.service %{buildroot}%{local_systemddir}
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/engtools/engtools.conf
/usr/local/etc/init.d/collect-engtools.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/buddyinfo.py
/usr/bin/ceph.sh
/usr/bin/chewmem
/usr/bin/cleanup-engtools.sh
/usr/bin/collect-engtools.sh
/usr/bin/diskstats.sh
/usr/bin/engtools_util.sh
/usr/bin/filestats.sh
/usr/bin/iostat.sh
/usr/bin/linux_benchmark.sh
/usr/bin/live_stream.py
/usr/bin/memstats.sh
/usr/bin/netstats.sh
/usr/bin/postgres.sh
/usr/bin/rabbitmq.sh
/usr/bin/rbzip2-engtools.sh
/usr/bin/rstart-engtools.sh
/usr/bin/rstop-engtools.sh
/usr/bin/rsync-engtools-data.sh
/usr/bin/slab.sh
/usr/bin/ticker.sh
/usr/bin/top.sh
/usr/bin/vswitch.sh

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/collect-engtools.service
