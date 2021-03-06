#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tboot
Version  : 1.9.6
Release  : 1
URL      : file:///home/clr/clearlinux/packages/tboot/tboot-1.9.6.tar.gz
Source0  : file:///home/clr/clearlinux/packages/tboot/tboot-1.9.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: tboot-bin = %{version}-%{release}
Requires: tboot-man = %{version}-%{release}
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : trousers-devel
BuildRequires : zlib-dev
Patch1: 0001-Fix-a-logical-error-in-function-bool-evtlog_append.patch
Patch2: 0002-Reset-debug-PCR16-to-zero.patch
Patch3: 0003-port-to-openssl-1.1.0.patch
Patch4: 0004-lcptools-v2-utilities-fixes.patch
Patch5: 0005-Make-policy-element-stm_elt-use-unique-type-name.patch
Patch6: 0006-Fix-openssl-1.0.2-double-frees.patch
Patch7: 0007-The-size-field-of-the-MB2-tag-is-the-size-of-the-tag.patch
Patch8: 0008-Fix-security-vulnerabilities-rooted-in-tpm_if-struct.patch
Patch9: 0009-Optimize-tboot-docs-installation.patch
Patch10: 0010-Fix-a-null-pointer-dereference-bug-when-Intel-TXT-is.patch
Patch11: 0011-Fix-TPM-1.2-locality-selection-issue.patch
Patch12: 0012-Fix-memory-leak-and-invalid-reads-and-writes-issues.patch
Patch13: 0013-Add-centos7-instructions-for-Use-in-EFI-boot-mode.patch
Patch14: 0014-Ensure-tboot-log-is-available-even-when-measured-lau.patch
Patch15: 0015-Add-support-for-appending-to-a-TPM2-TCG-style-event-.patch
Patch16: 0016-Add-an-option-in-tboot-to-force-SINIT-to-use-the-leg.patch
Patch17: 1000-tboot-for-tis.patch

%description
******************************************************************************
* This version of tboot will not work with Xen versions < 3.4 (c/s < 19115)  *
******************************************************************************

%package bin
Summary: bin components for the tboot package.
Group: Binaries

%description bin
bin components for the tboot package.


%package man
Summary: man components for the tboot package.
Group: Default

%description man
man components for the tboot package.


%prep
%setup -q -n tboot-1.9.6
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

%build
## build_prepend content
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569394886
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} debug=y


%install
export SOURCE_DATE_EPOCH=1569394886
rm -rf %{buildroot}
## install_prepend content
%define _sysconfdir	/usr/local/etc
## install_prepend end
make debug=y DISTDIR=$RPM_BUILD_ROOT install
## install_append content
%post
chattr +i /boot/tboot.gz /boot/tboot-syms
exit 0
## install_append end

%files
%defattr(-,root,root,-)
/boot/tboot-syms
/boot/tboot.gz

%files bin
%defattr(-,root,root,-)
/usr/sbin/acminfo
/usr/sbin/lcp2_crtpol
/usr/sbin/lcp2_crtpolelt
/usr/sbin/lcp2_crtpollist
/usr/sbin/lcp2_mlehash
/usr/sbin/lcp_crtpconf
/usr/sbin/lcp_crtpol
/usr/sbin/lcp_crtpol2
/usr/sbin/lcp_crtpolelt
/usr/sbin/lcp_crtpollist
/usr/sbin/lcp_mlehash
/usr/sbin/lcp_readpol
/usr/sbin/lcp_writepol
/usr/sbin/parse_err
/usr/sbin/tb_polgen
/usr/sbin/tpmnv_defindex
/usr/sbin/tpmnv_getcap
/usr/sbin/tpmnv_lock
/usr/sbin/tpmnv_relindex
/usr/sbin/txt-stat

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/acminfo.8
/usr/share/man/man8/lcp_crtpconf.8
/usr/share/man/man8/lcp_crtpol.8
/usr/share/man/man8/lcp_crtpol2.8
/usr/share/man/man8/lcp_crtpolelt.8
/usr/share/man/man8/lcp_crtpollist.8
/usr/share/man/man8/lcp_mlehash.8
/usr/share/man/man8/lcp_readpol.8
/usr/share/man/man8/lcp_writepol.8
/usr/share/man/man8/tb_polgen.8
/usr/share/man/man8/txt-stat.8
