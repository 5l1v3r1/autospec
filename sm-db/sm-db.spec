#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sm-db
Version  : 1.0.0
Release  : 2
URL      : file:///home/clr/stx-tar/sm-db-1.0.0.tar.gz
Source0  : file:///home/clr/stx-tar/sm-db-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sm-db-lib = %{version}-%{release}
BuildRequires : gcc
BuildRequires : glib-dev
BuildRequires : glibc
BuildRequires : sm-common-dev
BuildRequires : sqlite-autoconf-dev
Patch1: 0001-strncpy-specified-bound-equals-destination-size.patch
Patch2: 0002-modify-sm_common-lib-flag-location.patch

%description
The SM database is generated by the corresponding SQL scripts:
create_sm_db.sql -> sm.db
create_sm_hb_db.sql -> sm.db.hb

%package dev
Summary: dev components for the sm-db package.
Group: Development
Requires: sm-db-lib = %{version}-%{release}
Provides: sm-db-devel = %{version}-%{release}
Requires: sm-db = %{version}-%{release}

%description dev
dev components for the sm-db package.


%package lib
Summary: lib components for the sm-db package.
Group: Libraries

%description lib
lib components for the sm-db package.


%prep
%setup -q -n sm-db-1.0.0
%patch1 -p1
%patch2 -p1

%build
## build_prepend content
sqlite3 database/sm.db < database/create_sm_db.sql
sqlite3 database/sm.hb.db < database/create_sm_hb_db.sql
VER=%{version}
MAJOR=`echo $VER | awk -F . '{print $1}'`
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566355623
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} VER=${VER} VER_MJR=$MAJOR


%install
export SOURCE_DATE_EPOCH=1566355623
rm -rf %{buildroot}
## install_prepend content
VER=%{version}
MAJOR=`echo $VER | awk -F . '{print $1}'`
## install_prepend end
make DEST_DIR=$RPM_BUILD_ROOT VER=$VER VER_MJR=$MAJOR install

%files
%defattr(-,root,root,-)
/var/lib/sm/patches/sm-patch.sql
/var/lib/sm/sm.db
/var/lib/sm/sm.hb.db

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libsm_db.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsm_db.so.1
/usr/lib64/libsm_db.so.1.0.0
