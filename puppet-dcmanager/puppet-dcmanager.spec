#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-dcmanager
Version  : 1.0.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-dcmanager-1.0.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-dcmanager-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-dcmanager-data = %{version}-%{release}
BuildRequires : python-dev
Patch1: 0001-fix-Makefile-dir.patch

%description
No detailed description available

%package data
Summary: data components for the puppet-dcmanager package.
Group: Data

%description data
data components for the puppet-dcmanager package.


%prep
%setup -q -n puppet-dcmanager-1.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568797106
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
export SOURCE_DATE_EPOCH=1568797106
rm -rf %{buildroot}
%make_install
## install_append content
make install MODULEDIR=%{buildroot}%{_datadir}/puppet/modules
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/puppet/modules/dcmanager/.fixtures.yml
/usr/share/puppet/modules/dcmanager/Gemfile
/usr/share/puppet/modules/dcmanager/LICENSE
/usr/share/puppet/modules/dcmanager/Modulefile
/usr/share/puppet/modules/dcmanager/Rakefile
/usr/share/puppet/modules/dcmanager/lib/puppet/provider/dcmanager_config/ini_setting.rb
/usr/share/puppet/modules/dcmanager/lib/puppet/type/dcmanager_config.rb
/usr/share/puppet/modules/dcmanager/manifests/api.pp
/usr/share/puppet/modules/dcmanager/manifests/client.pp
/usr/share/puppet/modules/dcmanager/manifests/db/postgresql.pp
/usr/share/puppet/modules/dcmanager/manifests/db/sync.pp
/usr/share/puppet/modules/dcmanager/manifests/deps.pp
/usr/share/puppet/modules/dcmanager/manifests/init.pp
/usr/share/puppet/modules/dcmanager/manifests/keystone/auth.pp
/usr/share/puppet/modules/dcmanager/manifests/manager.pp
/usr/share/puppet/modules/dcmanager/manifests/params.pp
/usr/share/puppet/modules/dcmanager/manifests/rabbitmq.pp
