#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-oslo
Version  : 11.3.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-oslo-11.3.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-oslo-11.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-oslo-data = %{version}-%{release}
Requires: puppet-oslo-python = %{version}-%{release}
Requires: puppet-oslo-python3 = %{version}-%{release}
Requires: puppet >= 2.7.0
Requires: puppet-inifile
Requires: puppet-openstacklib
Requires: puppet-stdlib
BuildRequires : buildreq-distutils3
BuildRequires : pbr
Patch1: 0001-add-makefile.patch
Patch2: 0001-Remove-log_dir-from-conf-files.patch
Patch3: 0002-add-psycopg2-drivername-to-postgresql-settings.patch

%description
Team and repository tags
========================
[![Team and repository tags](http://governance.openstack.org/badges/puppet-oslo.svg)](http://governance.openstack.org/reference/tags/index.html)

%package data
Summary: data components for the puppet-oslo package.
Group: Data

%description data
data components for the puppet-oslo package.


%package python
Summary: python components for the puppet-oslo package.
Group: Default
Requires: puppet-oslo-python3 = %{version}-%{release}

%description python
python components for the puppet-oslo package.


%package python3
Summary: python3 components for the puppet-oslo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the puppet-oslo package.


%prep
%setup -q -n openstack-oslo-11.3.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568769331
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
install -d -m 0755 %{buildroot}%{_datadir}/openstack-puppet/modules/oslo/
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
cp -rp * %{buildroot}%{_datadir}/openstack-puppet/modules/oslo/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/openstack-puppet/modules/oslo/Gemfile
/usr/share/openstack-puppet/modules/oslo/LICENSE
/usr/share/openstack-puppet/modules/oslo/Makefile
/usr/share/openstack-puppet/modules/oslo/README.md
/usr/share/openstack-puppet/modules/oslo/Rakefile
/usr/share/openstack-puppet/modules/oslo/bindep.txt
/usr/share/openstack-puppet/modules/oslo/checksums.json
/usr/share/openstack-puppet/modules/oslo/lib/puppet/provider/oslo_config/ini_setting.rb
/usr/share/openstack-puppet/modules/oslo/lib/puppet/type/oslo_config.rb
/usr/share/openstack-puppet/modules/oslo/manifests/cache.pp
/usr/share/openstack-puppet/modules/oslo/manifests/concurrency.pp
/usr/share/openstack-puppet/modules/oslo/manifests/cors.pp
/usr/share/openstack-puppet/modules/oslo/manifests/db.pp
/usr/share/openstack-puppet/modules/oslo/manifests/init.pp
/usr/share/openstack-puppet/modules/oslo/manifests/log.pp
/usr/share/openstack-puppet/modules/oslo/manifests/messaging/amqp.pp
/usr/share/openstack-puppet/modules/oslo/manifests/messaging/default.pp
/usr/share/openstack-puppet/modules/oslo/manifests/messaging/notifications.pp
/usr/share/openstack-puppet/modules/oslo/manifests/messaging/rabbit.pp
/usr/share/openstack-puppet/modules/oslo/manifests/messaging/zmq.pp
/usr/share/openstack-puppet/modules/oslo/manifests/middleware.pp
/usr/share/openstack-puppet/modules/oslo/manifests/params.pp
/usr/share/openstack-puppet/modules/oslo/manifests/policy.pp
/usr/share/openstack-puppet/modules/oslo/manifests/privsep.pp
/usr/share/openstack-puppet/modules/oslo/manifests/releasenotes/notes/rabbitmq-connection-params-1a8ace0c23e7249e.yaml
/usr/share/openstack-puppet/modules/oslo/manifests/service.pp
/usr/share/openstack-puppet/modules/oslo/manifests/versionedobjects.pp
/usr/share/openstack-puppet/modules/oslo/metadata.json
/usr/share/openstack-puppet/modules/oslo/puppet_oslo.egg-info/PKG-INFO
/usr/share/openstack-puppet/modules/oslo/puppet_oslo.egg-info/SOURCES.txt
/usr/share/openstack-puppet/modules/oslo/puppet_oslo.egg-info/dependency_links.txt
/usr/share/openstack-puppet/modules/oslo/puppet_oslo.egg-info/not-zip-safe
/usr/share/openstack-puppet/modules/oslo/puppet_oslo.egg-info/top_level.txt
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/add_oslo_privsep-3f125445bce8b431.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/add_zmq_messaging-7ea20df747c78035.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/backend_package_ensure-54b4525895ce9acd.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/deprecate_config_sqlite_db-1a239175d42378e3.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/deprecate_rabbit_max_retries-813a568923f2335d.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/first_release-a7268e1c8959eca3.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/fix_log_dir_documentation-050052366584e83e.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/remove_verbose-0b599cd4810a8c51.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/secure-transport-url-d67d307cf85a16b1.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/notes/update-amqp-opts-1f14b8d3648b2b30.yaml
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/_static/.placeholder
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/conf.py
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/index.rst
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/newton.rst
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/ocata.rst
/usr/share/openstack-puppet/modules/oslo/releasenotes/source/unreleased.rst
/usr/share/openstack-puppet/modules/oslo/setup.cfg
/usr/share/openstack-puppet/modules/oslo/setup.py
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/centos-70-x64.yml
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/default.yml
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/nodepool-centos7.yml
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/nodepool-trusty.yml
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/nodepool-xenial.yml
/usr/share/openstack-puppet/modules/oslo/spec/acceptance/nodesets/ubuntu-server-1404-x64.yml
/usr/share/openstack-puppet/modules/oslo/spec/classes/oslo_init_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_cache_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_concurrency_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_cors_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_db_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_log_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_messaging_amqp_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_messaging_default_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_messaging_notifications_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_messaging_rabbit_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_messaging_zmq_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_middleware_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_policy_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_privsep_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_service_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/defines/oslo_versionedobjects_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/shared_examples.rb
/usr/share/openstack-puppet/modules/oslo/spec/spec_helper.rb
/usr/share/openstack-puppet/modules/oslo/spec/spec_helper_acceptance.rb
/usr/share/openstack-puppet/modules/oslo/spec/unit/provider/oslo_config/ini_setting_spec.rb
/usr/share/openstack-puppet/modules/oslo/spec/unit/type/oslo_config_spec.rb
/usr/share/openstack-puppet/modules/oslo/test-requirements.txt
/usr/share/openstack-puppet/modules/oslo/tests/init.pp
/usr/share/openstack-puppet/modules/oslo/tox.ini

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
