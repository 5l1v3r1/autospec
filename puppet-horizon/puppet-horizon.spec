#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-horizon
Version  : 11.5.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-horizon-11.5.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-horizon-11.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-horizon-data = %{version}-%{release}
Requires: puppet-horizon-python = %{version}-%{release}
Requires: puppet-horizon-python3 = %{version}-%{release}
Requires: puppet >= 2.7.0
Requires: puppet-apache
Requires: puppet-memcached
Requires: puppet-stdlib
BuildRequires : buildreq-distutils3
BuildRequires : pbr
Patch1: 0001-add-makefile.patch
Patch2: 0001-update-memcached-dependency.patch

%description
Team and repository tags
========================
[![Team and repository tags](http://governance.openstack.org/badges/puppet-horizon.svg)](http://governance.openstack.org/reference/tags/index.html)

%package data
Summary: data components for the puppet-horizon package.
Group: Data

%description data
data components for the puppet-horizon package.


%package python
Summary: python components for the puppet-horizon package.
Group: Default
Requires: puppet-horizon-python3 = %{version}-%{release}

%description python
python components for the puppet-horizon package.


%package python3
Summary: python3 components for the puppet-horizon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the puppet-horizon package.


%prep
%setup -q -n openstack-horizon-11.5.0
%patch1 -p1
%patch2 -p1

%build
## build_prepend content
export PBR_VERSION=%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568791109
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
install -d -m 0755 %{buildroot}%{_datadir}/openstack-puppet/modules/horizon/
## install_prepend end
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
cp -rp * %{buildroot}%{_datadir}/openstack-puppet/modules/horizon/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/openstack-puppet/modules/horizon/CHANGELOG.md
/usr/share/openstack-puppet/modules/horizon/Gemfile
/usr/share/openstack-puppet/modules/horizon/LICENSE
/usr/share/openstack-puppet/modules/horizon/Makefile
/usr/share/openstack-puppet/modules/horizon/README.md
/usr/share/openstack-puppet/modules/horizon/Rakefile
/usr/share/openstack-puppet/modules/horizon/bindep.txt
/usr/share/openstack-puppet/modules/horizon/checksums.json
/usr/share/openstack-puppet/modules/horizon/lib/puppet/parser/functions/os_any2array.rb
/usr/share/openstack-puppet/modules/horizon/manifests/init.pp
/usr/share/openstack-puppet/modules/horizon/manifests/params.pp
/usr/share/openstack-puppet/modules/horizon/manifests/wsgi/apache.pp
/usr/share/openstack-puppet/modules/horizon/metadata.json
/usr/share/openstack-puppet/modules/horizon/puppet_horizon.egg-info/PKG-INFO
/usr/share/openstack-puppet/modules/horizon/puppet_horizon.egg-info/SOURCES.txt
/usr/share/openstack-puppet/modules/horizon/puppet_horizon.egg-info/dependency_links.txt
/usr/share/openstack-puppet/modules/horizon/puppet_horizon.egg-info/not-zip-safe
/usr/share/openstack-puppet/modules/horizon/puppet_horizon.egg-info/top_level.txt
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/add-customization-module-config-option-798d0bb4e00737c3.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/add-images-panel-parameter-cb010871c8e1d0d1.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/add-support-for-SECURE_PROXY_SSL_HEADER-fbd83ad4f85bd52b.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/add-support-for-WEBSSO-options-a2d7e7f757b747d1.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/added_instance_default_config_options-123cc41099d5e098.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/added_new_theme_params_deprecated_custome_theme_path-e872713d93c45044.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/apache_ports-5d0eb0ca775ad7d1.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/disable-password-reveal-3ce6cbddf0bdb67e.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/disallow_iframe_embed-f0ffa1cabeca5b1e.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/empty-root-url-495e1f1f47372f47.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/enable-password-retrieve-b0bfa91053b24186.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/enable_user_pass-c30e80d0705b0954.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/enforce_password_check-7e29e1e968874e04.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/fix_ssl_handshake_errors-aece1e80e78820a2.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/horizon_django_cache_compress_ubuntu-e1807c69e52048fd.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/keystone_v3-d381e37592d3b29b.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/local-settings-permissions-666e7cd5d55cf813.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/password_validator-fdb08ff1d27aa652.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/rectify-static-alias-prefix-7c182dd08a98a8ea.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/remove_lesscpy-b4b677de57351078.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/root_path-4dbbddfa82bc6b56.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/root_url-cede3a4a7ecafdf9.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/rspec-puppet-facts-7ec9c688aba3e69e.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/trigger_collectstatic-fb465ebec48b3bc7.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/tuskar-9fa7bbe0df150fd1.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/update_local_settings_mitaka-f182327ce660fda0.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/notes/use-reno-1caaec4ba5aa4285.yaml
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/_static/.placeholder
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/conf.py
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/index.rst
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/mitaka.rst
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/newton.rst
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/ocata.rst
/usr/share/openstack-puppet/modules/horizon/releasenotes/source/unreleased.rst
/usr/share/openstack-puppet/modules/horizon/setup.cfg
/usr/share/openstack-puppet/modules/horizon/setup.py
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/horizon_with_apache_spec.rb
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/centos-70-x64.yml
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/default.yml
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/nodepool-centos7.yml
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/nodepool-trusty.yml
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/nodepool-xenial.yml
/usr/share/openstack-puppet/modules/horizon/spec/acceptance/nodesets/ubuntu-server-1404-x64.yml
/usr/share/openstack-puppet/modules/horizon/spec/classes/horizon_init_spec.rb
/usr/share/openstack-puppet/modules/horizon/spec/classes/horizon_wsgi_apache_spec.rb
/usr/share/openstack-puppet/modules/horizon/spec/fixtures/override_local_settings.py.erb
/usr/share/openstack-puppet/modules/horizon/spec/shared_examples.rb
/usr/share/openstack-puppet/modules/horizon/spec/spec_helper.rb
/usr/share/openstack-puppet/modules/horizon/spec/spec_helper_acceptance.rb
/usr/share/openstack-puppet/modules/horizon/spec/unit/puppet/parser/functions/os_any2array_spec.rb
/usr/share/openstack-puppet/modules/horizon/templates/local_settings.py.erb
/usr/share/openstack-puppet/modules/horizon/test-requirements.txt
/usr/share/openstack-puppet/modules/horizon/tox.ini

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
