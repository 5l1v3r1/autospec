#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : snmp-ext
Version  : 1.0
Release  : 1
URL      : file:///home/clear/tar/snmp-ext-1.0.tar.gz
Source0  : file:///home/clear/tar/snmp-ext-1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: snmp-ext-data = %{version}-%{release}
Requires: snmp-ext-lib = %{version}-%{release}
Requires: fm-common
Requires: net-snmp
BuildRequires : fm-common-dev
BuildRequires : net-snmp-dev
BuildRequires : openssl-dev
BuildRequires : util-linux-dev

%description
No detailed description available

%package data
Summary: data components for the snmp-ext package.
Group: Data

%description data
data components for the snmp-ext package.


%package dev
Summary: dev components for the snmp-ext package.
Group: Development
Requires: snmp-ext-lib = %{version}-%{release}
Requires: snmp-ext-data = %{version}-%{release}
Provides: snmp-ext-devel = %{version}-%{release}
Requires: snmp-ext = %{version}-%{release}

%description dev
dev components for the snmp-ext package.


%package lib
Summary: lib components for the snmp-ext package.
Group: Libraries
Requires: snmp-ext-data = %{version}-%{release}

%description lib
lib components for the snmp-ext package.


%prep
%setup -q -n snmp-ext-1.0

%build
## build_prepend content
MAJOR=`echo %{version} | awk -F . '{print $1}'`
MINOR=`echo %{version} | awk -F . '{print $2}'`
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570782197
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} MAJOR=$MAJOR MINOR=$MINOR PATCH=%{release}


%install
export SOURCE_DATE_EPOCH=1570782197
rm -rf %{buildroot}
## install_prepend content
MAJOR=`echo %{version} | awk -F . '{print $1}'`
MINOR=`echo %{version} | awk -F . '{print $2}'`
## install_prepend end
make DEST_DIR=%{buildroot} LIB_DIR=%{_libdir} MAJOR=$MAJOR MINOR=$MINOR MIBVER=%{mib_ver} PATCH=%{release} install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/snmp/mibs/wrsAlarmMib.mib.txt
/usr/share/snmp/mibs/wrsEnterpriseReg.mib.txt

%files dev
%defattr(-,root,root,-)
/usr/lib64/libcgtsAgentPlugin.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcgtsAgentPlugin.so.1
/usr/lib64/libcgtsAgentPlugin.so.1.0.1
