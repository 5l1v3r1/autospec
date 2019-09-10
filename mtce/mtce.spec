#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : mtce
Version  : 1.0
Release  : 17
URL      : file:///home/clear/tar/mtce-1.0.tar.gz
Source0  : file:///home/clear/tar/mtce-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mtce-bin = %{version}-%{release}
Requires: mtce-lib = %{version}-%{release}
Requires: mtce-services = %{version}-%{release}
Requires: /bin/bash
Requires: /bin/sh
Requires: /usr/bin/expect
Requires: /usr/bin/ipmitool
Requires: dpkg
Requires: expect
Requires: fm-common >= 1.0
Requires: libamon.so.1()(64bit)
Requires: libc.so.6()(64bit)
Requires: libc.so.6(GLIBC_2.14)(64bit)
Requires: libc.so.6(GLIBC_2.2.5)(64bit)
Requires: libc.so.6(GLIBC_2.3)(64bit)
Requires: libc.so.6(GLIBC_2.4)(64bit)
Requires: libevent >= 2.0.21
Requires: libevent-2.1.so.6()(64bit)
Requires: libfmcommon.so.1()(64bit)
Requires: libgcc_s.so.1()(64bit)
Requires: libgcc_s.so.1(GCC_3.0)(64bit)
Requires: libjson-c.so.4()(64bit)
Requires: libm.so.6()(64bit)
Requires: libpthread.so.0()(64bit)
Requires: libpthread.so.0(GLIBC_2.2.5)(64bit)
Requires: librt.so.1()(64bit)
Requires: librt.so.1(GLIBC_2.2.5)(64bit)
Requires: librt.so.1(GLIBC_2.3.3)(64bit)
Requires: libssh2.so.1()(64bit)
Requires: libstdc++.so.6()(64bit)
Requires: libstdc++.so.6(CXXABI_1.3)(64bit)
Requires: libstdc++.so.6(GLIBCXX_3.4)(64bit)
Requires: libstdc++.so.6(GLIBCXX_3.4.11)(64bit)
Requires: libstdc++.so.6(GLIBCXX_3.4.14)(64bit)
Requires: libstdc++.so.6(GLIBCXX_3.4.15)(64bit)
Requires: libstdc++.so.6(GLIBCXX_3.4.9)(64bit)
Requires: libuuid.so.1()(64bit)
Requires: rtld(GNU_HASH)
Requires: rtslib-fb
Requires: systemd
Requires: time
Requires: util-linux
BuildRequires : cppcheck
BuildRequires : expect
BuildRequires : fm-common
BuildRequires : fm-common-dev
BuildRequires : fm-mgr
BuildRequires : json-c
BuildRequires : json-c-devel
BuildRequires : libevent
BuildRequires : libevent-devel
BuildRequires : libssh2
BuildRequires : libssh2-devel
BuildRequires : mtce-common-dev >= 1.0
BuildRequires : mtce-common-staticdev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : postgresql
BuildRequires : systemd-devel
BuildRequires : util-linux-dev
Patch1: 0001-change-sysconfig-dir.patch

%description
No detailed description available

%package bin
Summary: bin components for the mtce package.
Group: Binaries
Requires: mtce-services = %{version}-%{release}

%description bin
bin components for the mtce package.


%package dev
Summary: dev components for the mtce package.
Group: Development
Requires: mtce-lib = %{version}-%{release}
Requires: mtce-bin = %{version}-%{release}
Provides: mtce-devel = %{version}-%{release}
Requires: mtce = %{version}-%{release}

%description dev
dev components for the mtce package.


%package lib
Summary: lib components for the mtce package.
Group: Libraries

%description lib
lib components for the mtce package.


%package services
Summary: services components for the mtce package.
Group: Systemd services

%description services
services components for the mtce package.


%prep
%setup -q -n mtce-1.0
%patch1 -p1

%build
## build_prepend content
%define local_dir /usr/local
%define local_bindir %{local_dir}/bin
%define local_sbindir %{local_dir}/sbin
%define local_etc_pmond      %{_sysconfdir}/pmon.d
%define local_etc_goenabledd %{_sysconfdir}/goenabled.d
%define local_etc_servicesd  %{_sysconfdir}/services.d
%define local_etc_logrotated %{_sysconfdir}/logrotate.d
%define bmc_profilesd        %{_sysconfdir}/bmc/server_profiles.d
%define ocf_resourced /usr/lib/ocf/resource.d
%define _sysconfdir /usr/local/etc
%define _unitdir /usr/lib/systemd/system/
%global _buildsubdir %{_builddir}/%{name}-%{version}
VER=%{version}
MAJOR=$(echo $VER | awk -F . '{print $1}')
MINOR=$(echo $VER | awk -F . '{print $2}')
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567648491
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} MAJOR=$MAJOR MINOR=$MINOR build


%install
export SOURCE_DATE_EPOCH=1567648491
rm -rf %{buildroot}
## install_prepend content
VER=%{version}
MAJOR=$(echo $VER | awk -F . '{print $1}')
MINOR=$(echo $VER | awk -F . '{print $2}')
## install_prepend end
install -m 755 -d %{buildroot}%{_sysconfdir}
## install_append content
install -m 755 -d %{buildroot}/usr
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 -d %{buildroot}/usr/local
install -m 755 -d %{buildroot}%{local_bindir}
install -m 755 -d %{buildroot}/usr/local/sbin
install -m 755 -d %{buildroot}/%{_sbindir}
install -m 755 -d %{buildroot}/lib
install -m 755 -d %{buildroot}%{_sysconfdir}/mtc
install -m 755 -d %{buildroot}%{_sysconfdir}/mtc/tmp
install -m 755 -d %{buildroot}/usr/lib
install -m 755 -d %{buildroot}/usr/lib/ocf
install -m 755 -d %{buildroot}/usr/lib/ocf/resource.d
install -m 755 -d %{buildroot}/usr/lib/ocf/resource.d/platform
install -m 755 -p -D %{_buildsubdir}/scripts/mtcAgent %{buildroot}/usr/lib/ocf/resource.d/platform/mtcAgent
install -m 755 -p -D %{_buildsubdir}/hwmon/scripts/ocf/hwmon %{buildroot}/usr/lib/ocf/resource.d/platform/hwmon
install -m 644 -p -D %{_buildsubdir}/scripts/mtc.ini %{buildroot}%{_sysconfdir}/mtc.ini
install -m 644 -p -D %{_buildsubdir}/scripts/mtc.conf %{buildroot}%{_sysconfdir}/mtc.conf
install -m 644 -p -D %{_buildsubdir}/fsmon/scripts/fsmond.conf %{buildroot}%{_sysconfdir}/mtc/fsmond.conf
install -m 644 -p -D %{_buildsubdir}/hwmon/scripts/hwmond.conf %{buildroot}%{_sysconfdir}/mtc/hwmond.conf
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/pmond.conf %{buildroot}%{_sysconfdir}/mtc/pmond.conf
install -m 644 -p -D %{_buildsubdir}/lmon/scripts/lmond.conf %{buildroot}%{_sysconfdir}/mtc/lmond.conf
install -m 644 -p -D %{_buildsubdir}/hostw/scripts/hostwd.conf %{buildroot}%{_sysconfdir}/mtc/hostwd.conf
install -m 755 -d %{buildroot}/%{_sysconfdir}/etc/bmc/server_profiles.d
install -m 644 -p -D %{_buildsubdir}/scripts/sensor_hp360_v1_ilo_v4.profile %{buildroot}/%{_sysconfdir}/bmc/server_profiles.d/sensor_hp360_v1_ilo_v4.profile
install -m 644 -p -D %{_buildsubdir}/scripts/sensor_hp380_v1_ilo_v4.profile %{buildroot}/%{_sysconfdir}/bmc/server_profiles.d/sensor_hp380_v1_ilo_v4.profile
install -m 644 -p -D %{_buildsubdir}/scripts/sensor_quanta_v1_ilo_v4.profile %{buildroot}/%{_sysconfdir}/bmc/server_profiles.d/sensor_quanta_v1_ilo_v4.profile
install -m 755 -p -D %{_buildsubdir}/maintenance/mtcAgent %{buildroot}/%{local_bindir}/mtcAgent
install -m 755 -p -D %{_buildsubdir}/maintenance/mtcClient %{buildroot}/%{local_bindir}/mtcClient
install -m 755 -p -D %{_buildsubdir}/heartbeat/hbsAgent %{buildroot}/%{local_bindir}/hbsAgent
install -m 755 -p -D %{_buildsubdir}/heartbeat/hbsClient %{buildroot}/%{local_bindir}/hbsClient
install -m 755 -p -D %{_buildsubdir}/pmon/pmond %{buildroot}/%{local_bindir}/pmond
install -m 755 -p -D %{_buildsubdir}/lmon/lmond %{buildroot}/%{local_bindir}/lmond
install -m 755 -p -D %{_buildsubdir}/hostw/hostwd %{buildroot}/%{local_bindir}/hostwd
install -m 755 -p -D %{_buildsubdir}/fsmon/fsmond %{buildroot}/%{local_bindir}/fsmond
install -m 755 -p -D %{_buildsubdir}/hwmon/hwmond %{buildroot}/%{local_bindir}/hwmond
install -m 755 -p -D %{_buildsubdir}/mtclog/mtclogd %{buildroot}/%{local_bindir}/mtclogd
install -m 755 -p -D %{_buildsubdir}/alarm/mtcalarmd %{buildroot}/%{local_bindir}/mtcalarmd
install -m 755 -p -D %{_buildsubdir}/scripts/wipedisk %{buildroot}/%{local_bindir}/wipedisk
install -m 755 -p -D %{_buildsubdir}/fsync/fsync %{buildroot}/%{_sbindir}/fsync
install -m 700 -p -D %{_buildsubdir}/pmon/scripts/pmon-restart %{buildroot}/%{local_sbindir}/pmon-restart
install -m 700 -p -D %{_buildsubdir}/pmon/scripts/pmon-start %{buildroot}/%{local_sbindir}/pmon-start
install -m 700 -p -D %{_buildsubdir}/pmon/scripts/pmon-stop %{buildroot}/%{local_sbindir}/pmon-stop
install -m 755 -p -D %{_buildsubdir}/scripts/mtcClient %{buildroot}%{_sysconfdir}/init.d/mtcClient
install -m 755 -p -D %{_buildsubdir}/scripts/hbsClient %{buildroot}%{_sysconfdir}/init.d/hbsClient
install -m 755 -p -D %{_buildsubdir}/hwmon/scripts/lsb/hwmon %{buildroot}%{_sysconfdir}/init.d/hwmon
install -m 755 -p -D %{_buildsubdir}/fsmon/scripts/fsmon %{buildroot}%{_sysconfdir}/init.d/fsmon
install -m 755 -p -D %{_buildsubdir}/scripts/mtclog %{buildroot}%{_sysconfdir}/init.d/mtclog
install -m 755 -p -D %{_buildsubdir}/pmon/scripts/pmon %{buildroot}%{_sysconfdir}/init.d/pmon
install -m 755 -p -D %{_buildsubdir}/lmon/scripts/lmon %{buildroot}%{_sysconfdir}/init.d/lmon
install -m 755 -p -D %{_buildsubdir}/hostw/scripts/hostw %{buildroot}%{_sysconfdir}/init.d/hostw
install -m 755 -p -D %{_buildsubdir}/alarm/scripts/mtcalarm.init %{buildroot}%{_sysconfdir}/init.d/mtcalarm
install -m 755 -p -D %{_buildsubdir}/scripts/hwclock.sh %{buildroot}%{_sysconfdir}/init.d/hwclock.sh
install -m 644 -p -D %{_buildsubdir}/scripts/hwclock.service %{buildroot}%{_unitdir}/hwclock.service
install -m 644 -p -D %{_buildsubdir}/fsmon/scripts/fsmon.service %{buildroot}%{_unitdir}/fsmon.service
install -m 644 -p -D %{_buildsubdir}/hwmon/scripts/hwmon.service %{buildroot}%{_unitdir}/hwmon.service
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/pmon.service %{buildroot}%{_unitdir}/pmon.service
install -m 644 -p -D %{_buildsubdir}/hostw/scripts/hostw.service %{buildroot}%{_unitdir}/hostw.service
install -m 644 -p -D %{_buildsubdir}/scripts/mtcClient.service %{buildroot}%{_unitdir}/mtcClient.service
install -m 644 -p -D %{_buildsubdir}/scripts/hbsClient.service %{buildroot}%{_unitdir}/hbsClient.service
install -m 644 -p -D %{_buildsubdir}/scripts/mtclog.service %{buildroot}%{_unitdir}/mtclog.service
install -m 644 -p -D %{_buildsubdir}/scripts/goenabled.service %{buildroot}%{_unitdir}/goenabled.service
install -m 644 -p -D %{_buildsubdir}/scripts/runservices.service %{buildroot}%{_unitdir}/runservices.service
install -m 644 -p -D %{_buildsubdir}/alarm/scripts/mtcalarm.service %{buildroot}%{_unitdir}/mtcalarm.service
install -m 644 -p -D %{_buildsubdir}/lmon/scripts/lmon.service %{buildroot}%{_unitdir}/lmon.service
install -m 755 -d %{buildroot}%{local_etc_goenabledd}
install -m 755 -p -D %{_buildsubdir}/scripts/goenabled %{buildroot}%{_sysconfdir}/init.d/goenabled
install -m 755 -d %{buildroot}%{local_etc_servicesd}
install -m 755 -d %{buildroot}%{local_etc_servicesd}/controller
install -m 755 -d %{buildroot}%{local_etc_servicesd}/worker
install -m 755 -d %{buildroot}%{local_etc_servicesd}/storage
install -m 755 -p -D %{_buildsubdir}/scripts/mtcTest %{buildroot}/%{local_etc_servicesd}/worker
install -m 755 -p -D %{_buildsubdir}/scripts/mtcTest %{buildroot}/%{local_etc_servicesd}/controller
install -m 755 -p -D %{_buildsubdir}/scripts/mtcTest %{buildroot}/%{local_etc_servicesd}/storage
install -m 755 -p -D %{_buildsubdir}/scripts/runservices %{buildroot}%{_sysconfdir}/init.d/runservices
install -m 755 -p -D %{_buildsubdir}/scripts/dmemchk.sh %{buildroot}%{local_sbindir}
install -m 755 -d %{buildroot}%{local_etc_pmond}
install -m 644 -p -D %{_buildsubdir}/scripts/mtcClient.conf %{buildroot}%{local_etc_pmond}/mtcClient.conf
install -m 644 -p -D %{_buildsubdir}/scripts/hbsClient.conf %{buildroot}%{local_etc_pmond}/hbsClient.conf
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/acpid.conf %{buildroot}%{local_etc_pmond}/acpid.conf
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/sshd.conf %{buildroot}%{local_etc_pmond}/sshd.conf
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/syslog-ng.conf %{buildroot}%{local_etc_pmond}/syslog-ng.conf
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/nslcd.conf %{buildroot}%{local_etc_pmond}/nslcd.conf
install -m 644 -p -D %{_buildsubdir}/fsmon/scripts/fsmon.conf %{buildroot}%{local_etc_pmond}/fsmon.conf
install -m 644 -p -D %{_buildsubdir}/scripts/mtclogd.conf %{buildroot}%{local_etc_pmond}/mtclogd.conf
install -m 644 -p -D %{_buildsubdir}/alarm/scripts/mtcalarm.pmon.conf %{buildroot}%{local_etc_pmond}/mtcalarm.conf
install -m 644 -p -D %{_buildsubdir}/lmon/scripts/lmon.pmon.conf %{buildroot}%{local_etc_pmond}/lmon.conf
install -m 755 -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p -D %{_buildsubdir}/scripts/mtce.logrotate %{buildroot}%{local_etc_logrotated}/mtce.logrotate
install -m 644 -p -D %{_buildsubdir}/hostw/scripts/hostw.logrotate %{buildroot}%{local_etc_logrotated}/hostw.logrotate
install -m 644 -p -D %{_buildsubdir}/pmon/scripts/pmon.logrotate %{buildroot}%{local_etc_logrotated}/pmon.logrotate
install -m 644 -p -D %{_buildsubdir}/lmon/scripts/lmon.logrotate %{buildroot}%{local_etc_logrotated}/lmon.logrotate
install -m 644 -p -D %{_buildsubdir}/fsmon/scripts/fsmon.logrotate %{buildroot}%{local_etc_logrotated}/fsmon.logrotate
install -m 644 -p -D %{_buildsubdir}/hwmon/scripts/hwmon.logrotate %{buildroot}%{local_etc_logrotated}/hwmon.logrotate
install -m 644 -p -D %{_buildsubdir}/alarm/scripts/mtcalarm.logrotate %{buildroot}%{local_etc_logrotated}/mtcalarm.logrotate
install -m 644 -p -D %{_buildsubdir}/heartbeat/mtceHbsCluster.h %{buildroot}/%{_includedir}/mtceHbsCluster.h
install -m 755 -p -D %{_buildsubdir}/public/libamon.so.$MAJOR %{buildroot}%{_libdir}/libamon.so.$MAJOR
cd %{buildroot}%{_libdir} ; ln -s libamon.so.$MAJOR libamon.so.$MAJOR.$MINOR
cd %{buildroot}%{_libdir} ; ln -s libamon.so.$MAJOR libamon.so
cd %{_buildsubdir}
install -m 755 -d %{buildroot}/var
install -m 755 -d %{buildroot}/var/run
%post
systemctl enable fsmon.service
systemctl enable mtcClient.service
systemctl enable hbsClient.service
systemctl enable mtclog.service
systemctl enable iscsid.service
systemctl enable rsyncd.service
systemctl enable goenabled.service
systemctl enable mtcalarm.service
systemctl enable hostw.service
systemctl enable pmon.service
systemctl enable lmon.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/ocf/resource.d/platform/hwmon
/usr/lib/ocf/resource.d/platform/mtcAgent
/usr/local/bin/fsmond
/usr/local/bin/hbsAgent
/usr/local/bin/hbsClient
/usr/local/bin/hostwd
/usr/local/bin/hwmond
/usr/local/bin/lmond
/usr/local/bin/mtcAgent
/usr/local/bin/mtcClient
/usr/local/bin/mtcalarmd
/usr/local/bin/mtclogd
/usr/local/bin/pmond
/usr/local/bin/wipedisk
/usr/local/etc/bmc/server_profiles.d/sensor_hp360_v1_ilo_v4.profile
/usr/local/etc/bmc/server_profiles.d/sensor_hp380_v1_ilo_v4.profile
/usr/local/etc/bmc/server_profiles.d/sensor_quanta_v1_ilo_v4.profile
/usr/local/etc/init.d/fsmon
/usr/local/etc/init.d/goenabled
/usr/local/etc/init.d/hbsClient
/usr/local/etc/init.d/hostw
/usr/local/etc/init.d/hwclock.sh
/usr/local/etc/init.d/hwmon
/usr/local/etc/init.d/lmon
/usr/local/etc/init.d/mtcClient
/usr/local/etc/init.d/mtcalarm
/usr/local/etc/init.d/mtclog
/usr/local/etc/init.d/pmon
/usr/local/etc/init.d/runservices
/usr/local/etc/logrotate.d/fsmon.logrotate
/usr/local/etc/logrotate.d/hostw.logrotate
/usr/local/etc/logrotate.d/hwmon.logrotate
/usr/local/etc/logrotate.d/lmon.logrotate
/usr/local/etc/logrotate.d/mtcalarm.logrotate
/usr/local/etc/logrotate.d/mtce.logrotate
/usr/local/etc/logrotate.d/pmon.logrotate
/usr/local/etc/mtc.conf
/usr/local/etc/mtc.ini
/usr/local/etc/mtc/fsmond.conf
/usr/local/etc/mtc/hostwd.conf
/usr/local/etc/mtc/hwmond.conf
/usr/local/etc/mtc/lmond.conf
/usr/local/etc/mtc/pmond.conf
/usr/local/etc/pmon.d/acpid.conf
/usr/local/etc/pmon.d/fsmon.conf
/usr/local/etc/pmon.d/hbsClient.conf
/usr/local/etc/pmon.d/lmon.conf
/usr/local/etc/pmon.d/mtcClient.conf
/usr/local/etc/pmon.d/mtcalarm.conf
/usr/local/etc/pmon.d/mtclogd.conf
/usr/local/etc/pmon.d/nslcd.conf
/usr/local/etc/pmon.d/sshd.conf
/usr/local/etc/pmon.d/syslog-ng.conf
/usr/local/etc/services.d/controller/mtcTest
/usr/local/etc/services.d/storage/mtcTest
/usr/local/etc/services.d/worker/mtcTest
/usr/local/sbin/dmemchk.sh
/usr/local/sbin/pmon-restart
/usr/local/sbin/pmon-start
/usr/local/sbin/pmon-stop

%files bin
%defattr(-,root,root,-)
/usr/bin/fsync

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libamon.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libamon.so.1
/usr/lib64/libamon.so.1.0

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fsmon.service
/usr/lib/systemd/system/goenabled.service
/usr/lib/systemd/system/hbsClient.service
/usr/lib/systemd/system/hostw.service
/usr/lib/systemd/system/hwclock.service
/usr/lib/systemd/system/hwmon.service
/usr/lib/systemd/system/lmon.service
/usr/lib/systemd/system/mtcClient.service
/usr/lib/systemd/system/mtcalarm.service
/usr/lib/systemd/system/mtclog.service
/usr/lib/systemd/system/pmon.service
/usr/lib/systemd/system/runservices.service