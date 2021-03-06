#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cloud-init
Version  : 0.7.9
Release  : 6
URL      : file:///home/clear/tar/cloud-init-0.7.9.tar.gz
Source0  : file:///home/clear/tar/cloud-init-0.7.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: cloud-init-bin = %{version}-%{release}
Requires: cloud-init-config = %{version}-%{release}
Requires: cloud-init-python = %{version}-%{release}
Requires: cloud-init-python3 = %{version}-%{release}
Requires: cloud-init-services = %{version}-%{release}
Requires: Jinja2
Requires: PyYAML
Requires: configobj
Requires: dmidecode
Requires: e2fsprogs
Requires: iproute2
Requires: jsonpatch
Requires: net-tools
Requires: prettytable
Requires: procps-ng
Requires: pyserial
Requires: requests
Requires: setuptools
Requires: shadow
Requires: systemd
BuildRequires : buildreq-distutils3
BuildRequires : git
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : systemd
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-configuration-changes-for-RHEL-package.patch
Patch2: 0002-do-not-use-git-to-determine-version.patch
Patch3: 0003-util-teach-write_file-about-copy_mode-option.patch
Patch4: 0004-Do-not-write-NM_CONTROLLED-no-in-generated-interface.patch
Patch5: 0005-url_helper-fail-gracefully-if-oauthlib-is-not-availa.patch
Patch6: 0006-rsyslog-replace-with-stop.patch
Patch7: 0007-OpenStack-Use-timeout-and-retries-from-config-in-get.patch
Patch8: 0008-correct-errors-in-cloudinit-net-sysconfig.py.patch
Patch9: 0009-net-do-not-raise-exception-for-3-nameservers.patch
Patch10: 0010-net-support-both-ipv4-and-ipv6-gateways-in-sysconfig.patch
Patch11: 0011-systemd-replace-generator-with-unit-conditionals.patch
Patch12: 0012-OpenStack-add-dvs-to-the-list-of-physical-link-types.patch
Patch13: 0013-Bounce-network-interface-for-Azure-when-using-the-bu.patch
Patch14: 0014-limit-permissions-on-def_log_file.patch
Patch15: 0015-remove-tee-command-from-logging-configuration.patch
Patch16: 0016-add-power-state-change-module-to-cloud_final_modules.patch
Patch17: 0017-sysconfig-Raise-ValueError-when-multiple-default-gat.patch
Patch18: 0018-Fix-dual-stack-IPv4-IPv6-configuration-for-RHEL.patch
Patch19: 0019-Add-missing-sysconfig-unit-test-data.patch
Patch20: 0020-Fix-ipv6-subnet-detection.patch
Patch21: 0022-RHEL-CentOS-Fix-default-routes-for-IPv4-IPv6-configu.patch
Patch22: 0023-DatasourceEc2-add-warning-message-when-not-on-AWS.patch
Patch23: 0024-Identify-Brightbox-as-an-Ec2-datasource-user.patch
Patch24: 0025-AliYun-Enable-platform-identification-and-enable-by-.patch
Patch25: 0026-Fix-alibaba-cloud-unit-tests-to-work-with-0.7.9.patch
Patch26: 0027-Fix-eni-rendering-of-multiple-IPs-per-interface.patch
Patch27: 0028-systemd-create-run-cloud-init-enabled.patch
Patch28: 0029-support-loopback-as-a-device-type.patch
Patch29: 0030-sysconfig-include-GATEWAY-value-if-set-in-subnet.patch
Patch30: 0031-rh_subscription-Perform-null-checks-for-enabled-and-.patch
Patch31: 0032-net-Allow-for-NetworkManager-configuration.patch
Patch32: 0033-Render-DNS-and-DOMAIN-lines-for-sysconfig.patch
Patch33: 0034-Start_cloud_init_after_dbus.patch
Patch34: 0035-sysconfig-Render-IPV6_DEFAULTGW-correctly.patch
Patch35: 0036-sysconfig-Don-t-write-BOOTPROTO-dhcp-for-ipv6-dhcp.patch
Patch36: 0037-sysconfig-Fix-traceback.patch
Patch37: 0038-Fix-bug-that-resulted-in-an-attempt-to-rename-bonds.patch
Patch38: 0039-azure-Fix-publishing-of-hostname.patch
Patch39: ci-Revert-azure-Fix-publishing-of-hostname.patch
Patch40: ci-DataSourceAzure.py-use-hostnamectl-to-set-hostname.patch
Patch41: ci-sysconfig-Don-t-disable-IPV6_AUTOCONF.patch
Patch42: cloud-init-add-centos-os.patch
Patch43: cloud-init-interactive-parted.patch

%description
This project is cloud-init it is hosted on launchpad at
https://launchpad.net/cloud-init

%package bin
Summary: bin components for the cloud-init package.
Group: Binaries
Requires: cloud-init-config = %{version}-%{release}
Requires: cloud-init-services = %{version}-%{release}

%description bin
bin components for the cloud-init package.


%package config
Summary: config components for the cloud-init package.
Group: Default

%description config
config components for the cloud-init package.


%package doc
Summary: doc components for the cloud-init package.
Group: Documentation

%description doc
doc components for the cloud-init package.


%package python
Summary: python components for the cloud-init package.
Group: Default
Requires: cloud-init-python3 = %{version}-%{release}

%description python
python components for the cloud-init package.


%package python3
Summary: python3 components for the cloud-init package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cloud-init package.


%package services
Summary: services components for the cloud-init package.
Group: Systemd services

%description services
services components for the cloud-init package.


%prep
%setup -q -n cloud-init-0.7.9
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569208314
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
%define _unitdir /usr/lib/systemd/system/
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT%{python_sitelib}/tests
mkdir -p $RPM_BUILD_ROOT/var/lib/cloud
mkdir -p $RPM_BUILD_ROOT/run/cloud-init
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
cp -p rhel/cloud-init-tmpfiles.conf $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf
cp -p rhel/cloud.cfg $RPM_BUILD_ROOT/%{_sysconfdir}/cloud/cloud.cfg
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d
cp -p tools/21-cloudinit.conf $RPM_BUILD_ROOT/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
mv $RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d/hook-network-manager \
$RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d/cloud-init-azure-hook
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp rhel/systemd/* $RPM_BUILD_ROOT%{_unitdir}/
%clean
rm -rf $RPM_BUILD_ROOT
%post
if [ $1 -eq 1 ] ; then
/bin/systemctl enable cloud-config.service     >/dev/null 2>&1 || :
/bin/systemctl enable cloud-final.service      >/dev/null 2>&1 || :
/bin/systemctl enable cloud-init.service       >/dev/null 2>&1 || :
/bin/systemctl enable cloud-init-local.service >/dev/null 2>&1 || :
elif [ $1 -eq 2 ]; then
/bin/systemctl is-enabled cloud-config.service >/dev/null 2>&1 &&
/bin/systemctl reenable cloud-config.service >/dev/null 2>&1 || :
/bin/systemctl is-enabled cloud-final.service >/dev/null 2>&1 &&
/bin/systemctl reenable cloud-final.service >/dev/null 2>&1 || :
/bin/systemctl is-enabled cloud-init.service >/dev/null 2>&1 &&
/bin/systemctl reenable cloud-init.service >/dev/null 2>&1 || :
/bin/systemctl is-enabled cloud-init-local.service >/dev/null 2>&1 &&
/bin/systemctl reenable cloud-init-local.service >/dev/null 2>&1 || :
fi
%preun
if [ $1 -eq 0 ] ; then
/bin/systemctl --no-reload disable cloud-config.service >/dev/null 2>&1 || :
/bin/systemctl --no-reload disable cloud-final.service  >/dev/null 2>&1 || :
/bin/systemctl --no-reload disable cloud-init.service   >/dev/null 2>&1 || :
/bin/systemctl --no-reload disable cloud-init-local.service >/dev/null 2>&1 || :
fi
%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
## install_append end

%files
%defattr(-,root,root,-)
/%{_tmpfilesdir}/cloud-init.conf
/usr/lib/cloud-init/uncloud-init
/usr/lib/cloud-init/write-ssh-key-fingerprints

%files bin
%defattr(-,root,root,-)
/usr/bin/cloud-init
/usr/bin/cloud-init-per

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/66-azure-ephemeral.rules

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cloud\-init/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cloud-config.service
/usr/lib/systemd/system/cloud-config.target
/usr/lib/systemd/system/cloud-final.service
/usr/lib/systemd/system/cloud-init-local.service
/usr/lib/systemd/system/cloud-init.service
