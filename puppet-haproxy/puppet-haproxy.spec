#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-haproxy
Version  : 1.5.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-haproxy-1.5.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-haproxy-1.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-haproxy-data = %{version}-%{release}
Requires: puppet >= 2.7.0
Requires: puppet-concat
Requires: puppet-stdlib
Patch1: 0001-add-makefile.patch
Patch2: 0001-Roll-up-TIS-patches.patch
Patch3: 0002-disable-config-validation-prechecks.patch
Patch4: 0003-Fix-global_options-log-default-value.patch
Patch5: 0004-Stop-invalid-warning-message

%description
#haproxy
####Table of Contents
1. [Overview](#overview)
2. [Module Description - What the module does and why it is useful](#module-description)
3. [Setup - The basics of getting started with haproxy](#setup)
* [Beginning with haproxy](#beginning-with-haproxy)
4. [Usage - Configuration options and additional functionality](#usage)
* [Configure HAProxy options](#configure-haproxy-options)
* [Configure HAProxy daemon listener](#configure-haproxy-daemon-listener)
* [Configure multi-network daemon listener](#configure-multi-network-daemon-listener)
* [Configure HAProxy load-balanced member nodes](#configure-haproxy-load-balanced-member-nodes)
* [Configure a load balancer with exported resources](#configure-a-load-balancer-with-exported-resources)
* [Set up a frontend service](#set-up-a-frontend-service)
* [Set up a backend service](#set-up-a-backend-service)
* [Configure multiple haproxy instances on one machine](#configure-multiple-haproxy-instances-on-one-machine)
* [Manage a map file](#manage-a-map-file)
5. [Reference - An under-the-hood peek at what the module is doing and how](#reference)
6. [Limitations - OS compatibility, etc.](#limitations)
7. [Development - Guide for contributing to the module](#development)

%package data
Summary: data components for the puppet-haproxy package.
Group: Data

%description data
data components for the puppet-haproxy package.


%prep
%setup -q -n puppetlabs-haproxy-6ffcb071cce02735a831bf1b9bc4f7e83f3e53c5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568791828
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
export SOURCE_DATE_EPOCH=1568791828
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/openstack-puppet/modules/haproxy/
## install_append content
cp -rp * %{buildroot}%{_datadir}/openstack-puppet/modules/haproxy/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/openstack-puppet/modules/haproxy/CHANGELOG.md
/usr/share/openstack-puppet/modules/haproxy/CONTRIBUTING.md
/usr/share/openstack-puppet/modules/haproxy/Gemfile
/usr/share/openstack-puppet/modules/haproxy/LICENSE
/usr/share/openstack-puppet/modules/haproxy/MAINTAINERS.md
/usr/share/openstack-puppet/modules/haproxy/Makefile
/usr/share/openstack-puppet/modules/haproxy/NOTICE
/usr/share/openstack-puppet/modules/haproxy/README.md
/usr/share/openstack-puppet/modules/haproxy/Rakefile
/usr/share/openstack-puppet/modules/haproxy/examples/init.pp
/usr/share/openstack-puppet/modules/haproxy/lib/facter/haproxy_version.rb
/usr/share/openstack-puppet/modules/haproxy/locales/config.yaml
/usr/share/openstack-puppet/modules/haproxy/manifests/backend.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/balancermember.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/balancermember/collect_exported.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/config.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/defaults.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/frontend.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/globals.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/init.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/install.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/instance.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/instance_service.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/listen.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/mailer.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/mailer/collect_exported.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/mailers.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/mapfile.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/params.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/peer.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/peer/collect_exported.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/peers.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/service.pp
/usr/share/openstack-puppet/modules/haproxy/manifests/userlist.pp
/usr/share/openstack-puppet/modules/haproxy/metadata.json
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/basic_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/defaults_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/frontbackend_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/listen_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/centos-7-x64.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/debian-8-x64.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/default.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/docker/centos-7.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/docker/debian-8.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/nodesets/docker/ubuntu-14.04.yml
/usr/share/openstack-puppet/modules/haproxy/spec/acceptance/userlist_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/classes/haproxy_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/backend_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/balancermember_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/defaults_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/frontend_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/instance_service_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/instance_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/listen_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/mailer_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/mailers_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/mapfile_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/peer_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/peers_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/defines/userlist_spec.rb
/usr/share/openstack-puppet/modules/haproxy/spec/spec_helper.rb
/usr/share/openstack-puppet/modules/haproxy/spec/spec_helper_acceptance.rb
/usr/share/openstack-puppet/modules/haproxy/spec/unit/facter/haproxy_version_spec.rb
/usr/share/openstack-puppet/modules/haproxy/templates/empty.erb
/usr/share/openstack-puppet/modules/haproxy/templates/fragments/_bind.erb
/usr/share/openstack-puppet/modules/haproxy/templates/fragments/_mode.erb
/usr/share/openstack-puppet/modules/haproxy/templates/fragments/_options.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy-base.cfg.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_backend_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_balancermember.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_defaults_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_frontend_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_listen_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_mailer.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_mailers_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_mapfile.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_peer.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_peers_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/haproxy_userlist_block.erb
/usr/share/openstack-puppet/modules/haproxy/templates/instance_service_unit_example.erb
