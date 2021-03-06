#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : monitor-helm
Version  : 92b6289ae93816717a8453cfe62bad51cbdb8ad0
Release  : 2
URL      : file:///home/clear/tar/helm-charts-92b6289ae93816717a8453cfe62bad51cbdb8ad0.tar.gz
Source0  : file:///home/clear/tar/helm-charts-92b6289ae93816717a8453cfe62bad51cbdb8ad0.tar.gz
Source1  : file:///home/clear/tar/monitor-helm.tar
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : buildreq-golang
BuildRequires : helm
Patch1: 0001-Add-Makefile-for-helm-charts.patch
Patch2: 0002-kibana-workaround-checksum-for-configmap.yaml.patch
Patch3: 0003-helm-chart-changes-for-stx-monitor.patch

%description
# Helm Charts
Use this repository to submit official Charts for Helm. Charts are curated application definitions for Helm. For more information about installing and using Helm, see its

%prep
%setup -q -n helm-charts
cd ..
%setup -q -T -D -n helm-charts -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
%global helm_folder  /usr/lib/helm
%define helm_home %{getenv:HOME}/.helm
mkdir %{helm_home}
mkdir %{helm_home}/repository
mkdir %{helm_home}/repository/cache
mkdir %{helm_home}/repository/local
mkdir %{helm_home}/plugins
mkdir %{helm_home}/starters
mkdir %{helm_home}/cache
mkdir %{helm_home}/cache/archive
tar -xzvf %SOURCE1
cp repositories.yaml %{helm_home}/repository/repositories.yaml
cp index.yaml %{helm_home}/repository/local/index.yaml
cd stable
make elasticsearch
make filebeat
make metricbeat
make kube-state-metrics
make kibana
make nginx-ingress
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568624225
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} logstash


%install
export SOURCE_DATE_EPOCH=1568624225
rm -rf %{buildroot}
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
## install_append content
install -d -m 755 ${RPM_BUILD_ROOT}%{helm_folder}
install -p -D -m 755 stable/*.tgz ${RPM_BUILD_ROOT}%{helm_folder}
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/helm/elasticsearch-1.24.0.tgz
/usr/lib/helm/filebeat-1.5.1.tgz
/usr/lib/helm/kibana-2.2.0.tgz
/usr/lib/helm/kube-state-metrics-0.16.0.tgz
/usr/lib/helm/logstash-1.7.0.tgz
/usr/lib/helm/metricbeat-1.6.0.tgz
/usr/lib/helm/nginx-ingress-1.4.0.tgz
