#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldapscripts
Version  : 2.0.8
Release  : 2
URL      : file:///home/clear/tar/ldapscripts-2.0.8.tgz
Source0  : file:///home/clear/tar/ldapscripts-2.0.8.tgz
Source1  : file:///home/clear/tar/ldapscripts-source.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Patch1: sudo-support.patch
Patch2: sudo-delete-support.patch
Patch3: log_timestamp.patch
Patch4: ldap-user-setup-support.patch
Patch5: allow-anonymous-bind-for-ldap-search.patch

%description
*************************
Description :
*************
The ldapscripts are originally designed to be used within Samba 3.x's
smb.conf file. They allow to manipulate POSIX entries for users, groups
and machines in an LDAP directory. They are written in shell and need ldap
client commands to work correctly (ldapadd, ldapdelete, ldapmodify,
ldapsearch). Other scripts also are provided as simple tools to (manually)
query your LDAP directory : ldapfinger, ldapid, lsldap (...).

%prep
%setup -q -n ldapscripts-2.0.8
cd ..
%setup -q -T -D -n ldapscripts-2.0.8 -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
## build_prepend content
%define debug_package %{nil}
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568602957
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
export SOURCE_DATE_EPOCH=1568602957
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
## install_append content
rm -Rf %{buildroot}/usr/local/man
rm -f %{buildroot}/usr/local/sbin/*machine*
rm -f %{buildroot}/usr/local/etc/ldapscripts/ldapaddmachine.template.sample
install -d %{buildroot}/usr/local/etc/
tar -xzvf %{SOURCE1}
install -m 644 ldapscripts.conf.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapscripts.conf
install -m 644 ldapadduser.template.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapadduser.template.cgcs
install -m 644 ldapaddgroup.template.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapaddgroup.template.cgcs
install -m 644 ldapmoduser.template.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapmoduser.template.cgcs
install -m 644 ldapaddsudo.template.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapaddsudo.template.cgcs
install -m 644 ldapmodsudo.template.cgcs %{buildroot}/usr/local/etc/ldapscripts/ldapmodsudo.template.cgcs
install -m 600 ldapscripts.passwd %{buildroot}/usr/local/etc/ldapscripts/ldapscripts.passwd
## install_append end

%files
%defattr(-,root,root,-)
/usr/local/etc/ldapscripts/ldapaddgroup.template.cgcs
/usr/local/etc/ldapscripts/ldapaddgroup.template.sample
/usr/local/etc/ldapscripts/ldapaddsudo.template.cgcs
/usr/local/etc/ldapscripts/ldapadduser.template.cgcs
/usr/local/etc/ldapscripts/ldapadduser.template.sample
/usr/local/etc/ldapscripts/ldapmodsudo.template.cgcs
/usr/local/etc/ldapscripts/ldapmoduser.template.cgcs
/usr/local/etc/ldapscripts/ldapscripts.conf
/usr/local/etc/ldapscripts/ldapscripts.conf.sample
/usr/local/etc/ldapscripts/ldapscripts.passwd
/usr/local/etc/ldapscripts/ldapscripts.passwd.sample
/usr/local/lib/ldapscripts/runtime
/usr/local/sbin/ldapaddgroup
/usr/local/sbin/ldapaddsudo
/usr/local/sbin/ldapadduser
/usr/local/sbin/ldapaddusertogroup
/usr/local/sbin/ldapdeletegroup
/usr/local/sbin/ldapdeletesudo
/usr/local/sbin/ldapdeleteuser
/usr/local/sbin/ldapdeleteuserfromgroup
/usr/local/sbin/ldapfinger
/usr/local/sbin/ldapgid
/usr/local/sbin/ldapid
/usr/local/sbin/ldapinit
/usr/local/sbin/ldapmodifygroup
/usr/local/sbin/ldapmodifysudo
/usr/local/sbin/ldapmodifyuser
/usr/local/sbin/ldaprenamegroup
/usr/local/sbin/ldaprenameuser
/usr/local/sbin/ldapsetpasswd
/usr/local/sbin/ldapsetprimarygroup
/usr/local/sbin/ldapusersetup
/usr/local/sbin/lsldap
