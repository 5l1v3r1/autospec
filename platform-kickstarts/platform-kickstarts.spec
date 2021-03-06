#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : platform-kickstarts
Version  : 1.0.0
Release  : 8
URL      : file:///home/clr/stx-tar/platform-kickstarts-1.0.0.tar.gz
Source0  : file:///home/clr/stx-tar/platform-kickstarts-1.0.0.tar.gz
Source1  : file:///home/clr/stx-tar/platform-kickstarts-license.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : perl
BuildRequires : perl(Getopt::Long)
BuildRequires : perl(POSIX)
Patch1: 0001-add-makefile.patch

%description
No detailed description available

%prep
%setup -q -n platform-kickstarts-1.0.0
cd ..
%setup -q -T -D -n platform-kickstarts-1.0.0 -b 1
%patch1 -p1

%build
## build_prepend content
./centos-ks-gen.pl --release %{name}-%{version}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568885867
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
export SOURCE_DATE_EPOCH=1568885867
rm -rf %{buildroot}
## install_prepend content
%define feed_dir /www/pages/feed/rel-%{name}-%{version}
## install_prepend end
install -d -m 0755 %{buildroot}%{feed_dir}
## install_append content
install -m 0444 generated/* %{buildroot}%{feed_dir}/
install -d -m 0755 %{buildroot}/pxeboot
install -D -m 0444 pxeboot/* %{buildroot}/pxeboot
install -d -m 0755 %{buildroot}/extra_cfgs
install -D -m 0444 extra_cfgs/* %{buildroot}/extra_cfgs
## install_append end

%files
%defattr(-,root,root,-)
/extra_cfgs/yow-tuxlab2_controller.cfg
/extra_cfgs/yow-tuxlab2_smallsystem.cfg
/extra_cfgs/yow-tuxlab2_smallsystem_lowlatency.cfg
/extra_cfgs/yow-tuxlab_controller.cfg
/extra_cfgs/yow-tuxlab_smallsystem.cfg
/extra_cfgs/yow-tuxlab_smallsystem_lowlatency.cfg
/extra_cfgs/yow_controller.cfg
/extra_cfgs/yow_smallsystem.cfg
/extra_cfgs/yow_smallsystem_lowlatency.cfg
/pxeboot/pxeboot_controller.cfg
/pxeboot/pxeboot_smallsystem.cfg
/pxeboot/pxeboot_smallsystem_lowlatency.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/controller_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_controller_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_smallsystem_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_smallsystem_lowlatency_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_storage_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_worker_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/net_worker_lowlatency_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/smallsystem_ks.cfg
/www/pages/feed/rel-platform-kickstarts-1.0.0/smallsystem_lowlatency_ks.cfg
