#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-nslcd
Version  : 0.0.1
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-nslcd-0.0.1.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-nslcd-0.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-nslcd-data = %{version}-%{release}
Patch1: 0001-add-makefile.patch

%description
# Module: nslcd
[![Build Status](https://travis-ci.org/jlyheden/puppet-nslcd.png)](https://travis-ci.org/jlyheden/puppet-nslcd)

%package data
Summary: data components for the puppet-nslcd package.
Group: Data

%description data
data components for the puppet-nslcd package.


%prep
%setup -q -n packstack
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568773484
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
export SOURCE_DATE_EPOCH=1568773484
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/puppet/modules/nslcd
## install_append content
cp -R puppet/modules/nslcd %{buildroot}%{_datadir}/puppet/modules
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/puppet/modules/nslcd/.fixtures.yml
/usr/share/puppet/modules/nslcd/.gemfile
/usr/share/puppet/modules/nslcd/.gitignore
/usr/share/puppet/modules/nslcd/.travis.yml
/usr/share/puppet/modules/nslcd/Modulefile
/usr/share/puppet/modules/nslcd/README.markdown
/usr/share/puppet/modules/nslcd/Rakefile
/usr/share/puppet/modules/nslcd/manifests/init.pp
/usr/share/puppet/modules/nslcd/manifests/params.pp
/usr/share/puppet/modules/nslcd/spec/classes/nslcd_init_spec.rb
/usr/share/puppet/modules/nslcd/spec/spec_helper.rb
/usr/share/puppet/modules/nslcd/templates/nslcd.conf.erb
/usr/share/puppet/modules/nslcd/tests/init.pp