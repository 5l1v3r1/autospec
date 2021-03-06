#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-nfv
Version  : 1.0.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-nfv-1.0.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-nfv-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-nfv-data = %{version}-%{release}
BuildRequires : python-dev
Patch1: 0001-fix-Makefile-dir.patch

%description
No detailed description available

%package data
Summary: data components for the puppet-nfv package.
Group: Data

%description data
data components for the puppet-nfv package.


%prep
%setup -q -n puppet-nfv-1.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568776128
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
export SOURCE_DATE_EPOCH=1568776128
rm -rf %{buildroot}
%make_install
## install_append content
make install MODULEDIR=%{buildroot}%{_datadir}/puppet/modules
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/puppet/modules/nfv/lib/puppet/provider/nfv_plugin_alarm_config/ini_setting.rb
/usr/share/puppet/modules/nfv/lib/puppet/provider/nfv_plugin_event_log_config/ini_setting.rb
/usr/share/puppet/modules/nfv/lib/puppet/provider/nfv_plugin_nfvi_config/ini_setting.rb
/usr/share/puppet/modules/nfv/lib/puppet/provider/nfv_vim_config/ini_setting.rb
/usr/share/puppet/modules/nfv/lib/puppet/type/nfv_plugin_alarm_config.rb
/usr/share/puppet/modules/nfv/lib/puppet/type/nfv_plugin_event_log_config.rb
/usr/share/puppet/modules/nfv/lib/puppet/type/nfv_plugin_nfvi_config.rb
/usr/share/puppet/modules/nfv/lib/puppet/type/nfv_vim_config.rb
/usr/share/puppet/modules/nfv/manifests/alarm.pp
/usr/share/puppet/modules/nfv/manifests/event_log.pp
/usr/share/puppet/modules/nfv/manifests/init.pp
/usr/share/puppet/modules/nfv/manifests/keystone/auth.pp
/usr/share/puppet/modules/nfv/manifests/nfvi.pp
/usr/share/puppet/modules/nfv/manifests/params.pp
/usr/share/puppet/modules/nfv/manifests/vim.pp
