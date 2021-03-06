#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-ceph
Version  : 2.4.1
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-ceph-2.4.1.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-ceph-2.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-ceph-data = %{version}-%{release}
Requires: puppet-ceph-python = %{version}-%{release}
Requires: puppet-ceph-python3 = %{version}-%{release}
Requires: puppet >= 2.7.0
Requires: puppet-apache
Requires: puppet-concat
Requires: puppet-inifile
Requires: puppet-stdlib
BuildRequires : buildreq-distutils3
BuildRequires : pbr
Patch1: 0001-add-makefile.patch
Patch2: 0001-Roll-up-TIS-patches.patch
Patch3: 0002-Newton-rebase-fixes.patch
Patch4: 0003-Ceph-Jewel-rebase.patch
Patch5: 0004-US92424-Add-OSD-support-for-persistent-naming.patch
Patch6: 0005-Remove-puppetlabs-apt-as-ceph-requirement.patch
Patch7: 0006-ceph-disk-prepare-invalid-data-disk-value.patch
Patch8: 0007-Add-StarlingX-specific-restart-command-for-Ceph-moni.patch
Patch9: 0008-ceph-mimic-prepare-activate-osd.patch
Patch10: 0009-fix-ceph-osd-disk-partition-for-nvme-disks.patch
Patch11: 0010-wipe-unprepared-disks.patch

%description
Team and repository tags
========================
[![Team and repository tags](http://governance.openstack.org/badges/puppet-ceph.svg)](http://governance.openstack.org/reference/tags/index.html)

%package data
Summary: data components for the puppet-ceph package.
Group: Data

%description data
data components for the puppet-ceph package.


%package python
Summary: python components for the puppet-ceph package.
Group: Default
Requires: puppet-ceph-python3 = %{version}-%{release}

%description python
python components for the puppet-ceph package.


%package python3
Summary: python3 components for the puppet-ceph package.
Group: Default
Requires: python3-core

%description python3
python3 components for the puppet-ceph package.


%prep
%setup -q -n openstack-ceph-2.4.1
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

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568800424
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
echo "dont need check"
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export PBR_VERSION=%{version}
install -d -m 0755 %{buildroot}%{_datadir}/openstack-puppet/modules/ceph
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
cp -rp * %{buildroot}%{_datadir}/openstack-puppet/modules/ceph/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/openstack-puppet/modules/ceph/Gemfile
/usr/share/openstack-puppet/modules/ceph/LICENSE
/usr/share/openstack-puppet/modules/ceph/Makefile
/usr/share/openstack-puppet/modules/ceph/README.md
/usr/share/openstack-puppet/modules/ceph/Rakefile
/usr/share/openstack-puppet/modules/ceph/USECASES.md
/usr/share/openstack-puppet/modules/ceph/bindep.txt
/usr/share/openstack-puppet/modules/ceph/checksums.json
/usr/share/openstack-puppet/modules/ceph/examples/common.yaml
/usr/share/openstack-puppet/modules/ceph/examples/hiera.yaml
/usr/share/openstack-puppet/modules/ceph/examples/nodes/client.yaml
/usr/share/openstack-puppet/modules/ceph/examples/nodes/first.yaml
/usr/share/openstack-puppet/modules/ceph/examples/nodes/second.yaml
/usr/share/openstack-puppet/modules/ceph/lib/puppet/provider/ceph_config/ini_setting.rb
/usr/share/openstack-puppet/modules/ceph/lib/puppet/type/ceph_config.rb
/usr/share/openstack-puppet/modules/ceph/manifests/conf.pp
/usr/share/openstack-puppet/modules/ceph/manifests/fs.pp
/usr/share/openstack-puppet/modules/ceph/manifests/init.pp
/usr/share/openstack-puppet/modules/ceph/manifests/key.pp
/usr/share/openstack-puppet/modules/ceph/manifests/keys.pp
/usr/share/openstack-puppet/modules/ceph/manifests/mds.pp
/usr/share/openstack-puppet/modules/ceph/manifests/mgr.pp
/usr/share/openstack-puppet/modules/ceph/manifests/mirror.pp
/usr/share/openstack-puppet/modules/ceph/manifests/mon.pp
/usr/share/openstack-puppet/modules/ceph/manifests/mons.pp
/usr/share/openstack-puppet/modules/ceph/manifests/osd.pp
/usr/share/openstack-puppet/modules/ceph/manifests/osds.pp
/usr/share/openstack-puppet/modules/ceph/manifests/params.pp
/usr/share/openstack-puppet/modules/ceph/manifests/pool.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/base.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/client.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/fs.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/mds.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/mgr.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/mirror.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/mon.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/osd.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/params.pp
/usr/share/openstack-puppet/modules/ceph/manifests/profile/rgw.pp
/usr/share/openstack-puppet/modules/ceph/manifests/repo.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/apache.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/apache_fastcgi.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/apache_proxy_fcgi.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/civetweb.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/keystone.pp
/usr/share/openstack-puppet/modules/ceph/manifests/rgw/keystone/auth.pp
/usr/share/openstack-puppet/modules/ceph/metadata.json
/usr/share/openstack-puppet/modules/ceph/puppet_ceph.egg-info/PKG-INFO
/usr/share/openstack-puppet/modules/ceph/puppet_ceph.egg-info/SOURCES.txt
/usr/share/openstack-puppet/modules/ceph/puppet_ceph.egg-info/dependency_links.txt
/usr/share/openstack-puppet/modules/ceph/puppet_ceph.egg-info/not-zip-safe
/usr/share/openstack-puppet/modules/ceph/puppet_ceph.egg-info/top_level.txt
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/add-ceph-mgr-support-d2a5e9104021f81a.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/allow_changing_pidmax_on_osd_nodes-d1a98328f666a895.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/centos-mirror-71fd6fb3f5916d5d.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/first_release-a7268e1c8959eca3.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/jewel-218ac52343f4e165.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/jewel-a3169eb769be4e48.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/mds-support-improvements-e30c7c4fdb838439.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/osd-check-fsid-mismatch-a5cb615be1b4e40f.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/osd-check-non-existent-block-device-6f827dba142a3aa5.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/osd-level-5ebc22c7377e0300.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/osd_define_explicit_conditional-ceaadb2e4ea34595.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/radosgw-keystone-v3-93b3895e24b5f913.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/rbd-mirror-e8c13699bb0e71d8.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/remove-rgw-syslog-2a6909362b702b15.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/service-management-9483b9cfc067c736.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/stdlib-min-requirements-9ca51e3ad52aa3f8.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/support-nvme0n1-as-osd-46e4a00ec699f718.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/notes/systemd-8b86dee2f9df5a14.yaml
/usr/share/openstack-puppet/modules/ceph/releasenotes/source/_static/.placeholder
/usr/share/openstack-puppet/modules/ceph/releasenotes/source/conf.py
/usr/share/openstack-puppet/modules/ceph/releasenotes/source/index.rst
/usr/share/openstack-puppet/modules/ceph/releasenotes/source/unreleased.rst
/usr/share/openstack-puppet/modules/ceph/setup.cfg
/usr/share/openstack-puppet/modules/ceph/setup.py
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/ceph_mon_osd_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/centos-70-x64.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/default.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/nodepool-centos7.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/nodepool-trusty.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/nodepool-xenial.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/two-centos-70-x64.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/two-ubuntu-server-1404-x64.yml
/usr/share/openstack-puppet/modules/ceph/spec/acceptance/nodesets/ubuntu-server-1404-x64.yml
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_conf_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_init_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_mds_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_mons_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_osds_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_base_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_client_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_fs_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_mds_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_mgr_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_mon_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_osd_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_profile_params_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_repo_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/classes/ceph_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_fs_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_key_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_mgr_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_mon_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_osd_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_pool_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rbd_mirror_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_apache_fastcgi_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_apache_proxy_fcgi_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_apache_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_civetweb_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_keystone_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/defines/ceph_rgw_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/shared_examples.rb
/usr/share/openstack-puppet/modules/ceph/spec/spec_helper.rb
/usr/share/openstack-puppet/modules/ceph/spec/spec_helper_acceptance.rb
/usr/share/openstack-puppet/modules/ceph/spec/unit/provider/ceph_config/ini_setting_spec.rb
/usr/share/openstack-puppet/modules/ceph/spec/unit/type/ceph_config_spec.rb
/usr/share/openstack-puppet/modules/ceph/test-requirements.txt
/usr/share/openstack-puppet/modules/ceph/tox.ini

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
