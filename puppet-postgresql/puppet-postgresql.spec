#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : puppet-postgresql
Version  : 4.8.0
Release  : 1
URL      : file:///home/clr/stx-tar/puppet-postgresql-4.8.0.tar.gz
Source0  : file:///home/clr/stx-tar/puppet-postgresql-4.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: puppet-postgresql-data = %{version}-%{release}
Requires: puppet-concat
Requires: puppet-firewall
Requires: puppet-stdlib
BuildRequires : python-dev
Patch1: 0001-add-makefile.patch
Patch2: 0001-Roll-up-TIS-patches.patch
Patch3: 0002-remove-puppetlabs-apt-as-a-requirement.patch

%description
# postgresql
#### Table of Contents
1. [Module Description - What does the module do?](#module-description)
2. [Setup - The basics of getting started with postgresql module](#setup)
* [What postgresql affects](#what-postgresql-affects)
* [Getting started with postgresql](#getting-started-with-postgresql)
3. [Usage - Configuration options and additional functionality](#usage)
* [Configure a server](#configure-a-server)
* [Create a database](#create-a-database)
* [Manage users, roles, and permissions](#manage-users-roles-and-permissions)
* [Override defaults](#override-defaults)
* [Create an access rule for pg_hba.conf](#create-an-access-rule-for-pg_hbaconf)
* [Create user name maps for pg_ident.conf](#create-user-name-maps-for-pg_identconf)
* [Validate connectivity](#validate-connectivity)
4. [Reference - An under-the-hood peek at what the module is doing and how](#reference)
* [Classes](#classes)
* [Defined Types](#defined-types)
* [Types](#types)
* [Functions](#functions)
5. [Limitations - OS compatibility, etc.](#limitations)
6. [Development - Guide for contributing to the module](#development)
* [Contributors - List of module contributors](#contributors)
7. [Tests](#tests)
8. [Contributors - List of module contributors](#contributors)

%package data
Summary: data components for the puppet-postgresql package.
Group: Data

%description data
data components for the puppet-postgresql package.


%prep
%setup -q -n puppetlabs-postgresql
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568711916
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
export SOURCE_DATE_EPOCH=1568711916
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/puppet/modules/postgresql
## install_append content
cp -rp * %{buildroot}/%{_datadir}/puppet/modules/postgresql/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/puppet/modules/postgresql/CHANGELOG.md
/usr/share/puppet/modules/postgresql/CONTRIBUTING.md
/usr/share/puppet/modules/postgresql/Gemfile
/usr/share/puppet/modules/postgresql/LICENSE
/usr/share/puppet/modules/postgresql/Makefile
/usr/share/puppet/modules/postgresql/NOTICE
/usr/share/puppet/modules/postgresql/README.md
/usr/share/puppet/modules/postgresql/Rakefile
/usr/share/puppet/modules/postgresql/files/RPM-GPG-KEY-PGDG
/usr/share/puppet/modules/postgresql/files/validate_postgresql_connection.sh
/usr/share/puppet/modules/postgresql/lib/puppet/parser/functions/postgresql_acls_to_resources_hash.rb
/usr/share/puppet/modules/postgresql/lib/puppet/parser/functions/postgresql_escape.rb
/usr/share/puppet/modules/postgresql/lib/puppet/parser/functions/postgresql_password.rb
/usr/share/puppet/modules/postgresql/lib/puppet/provider/postgresql_conf/parsed.rb
/usr/share/puppet/modules/postgresql/lib/puppet/provider/postgresql_psql/ruby.rb
/usr/share/puppet/modules/postgresql/lib/puppet/provider/postgresql_replication_slot/ruby.rb
/usr/share/puppet/modules/postgresql/lib/puppet/type/postgresql_conf.rb
/usr/share/puppet/modules/postgresql/lib/puppet/type/postgresql_psql.rb
/usr/share/puppet/modules/postgresql/lib/puppet/type/postgresql_replication_slot.rb
/usr/share/puppet/modules/postgresql/manifests/client.pp
/usr/share/puppet/modules/postgresql/manifests/globals.pp
/usr/share/puppet/modules/postgresql/manifests/lib/devel.pp
/usr/share/puppet/modules/postgresql/manifests/lib/docs.pp
/usr/share/puppet/modules/postgresql/manifests/lib/java.pp
/usr/share/puppet/modules/postgresql/manifests/lib/perl.pp
/usr/share/puppet/modules/postgresql/manifests/lib/python.pp
/usr/share/puppet/modules/postgresql/manifests/params.pp
/usr/share/puppet/modules/postgresql/manifests/repo.pp
/usr/share/puppet/modules/postgresql/manifests/repo/apt_postgresql_org.pp
/usr/share/puppet/modules/postgresql/manifests/repo/yum_postgresql_org.pp
/usr/share/puppet/modules/postgresql/manifests/server.pp
/usr/share/puppet/modules/postgresql/manifests/server/config.pp
/usr/share/puppet/modules/postgresql/manifests/server/config_entry.pp
/usr/share/puppet/modules/postgresql/manifests/server/contrib.pp
/usr/share/puppet/modules/postgresql/manifests/server/database.pp
/usr/share/puppet/modules/postgresql/manifests/server/database_grant.pp
/usr/share/puppet/modules/postgresql/manifests/server/db.pp
/usr/share/puppet/modules/postgresql/manifests/server/extension.pp
/usr/share/puppet/modules/postgresql/manifests/server/grant.pp
/usr/share/puppet/modules/postgresql/manifests/server/grant_role.pp
/usr/share/puppet/modules/postgresql/manifests/server/initdb.pp
/usr/share/puppet/modules/postgresql/manifests/server/install.pp
/usr/share/puppet/modules/postgresql/manifests/server/passwd.pp
/usr/share/puppet/modules/postgresql/manifests/server/pg_hba_rule.pp
/usr/share/puppet/modules/postgresql/manifests/server/pg_ident_rule.pp
/usr/share/puppet/modules/postgresql/manifests/server/plperl.pp
/usr/share/puppet/modules/postgresql/manifests/server/plpython.pp
/usr/share/puppet/modules/postgresql/manifests/server/postgis.pp
/usr/share/puppet/modules/postgresql/manifests/server/recovery.pp
/usr/share/puppet/modules/postgresql/manifests/server/reload.pp
/usr/share/puppet/modules/postgresql/manifests/server/role.pp
/usr/share/puppet/modules/postgresql/manifests/server/schema.pp
/usr/share/puppet/modules/postgresql/manifests/server/service.pp
/usr/share/puppet/modules/postgresql/manifests/server/table_grant.pp
/usr/share/puppet/modules/postgresql/manifests/server/tablespace.pp
/usr/share/puppet/modules/postgresql/manifests/validate_db_connection.pp
/usr/share/puppet/modules/postgresql/metadata.json
/usr/share/puppet/modules/postgresql/spec/acceptance/00-utf8_encoding_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/alternative_port_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/db_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/default_parameters_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/centos-7-x64.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/debian-8-x64.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/default.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/docker/centos-7.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/docker/debian-8.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/nodesets/docker/ubuntu-14.04.yml
/usr/share/puppet/modules/postgresql/spec/acceptance/postgresql_psql_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/remote_access_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/server/grant_role_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/server/grant_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/server/recovery_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/server/schema_spec.rb
/usr/share/puppet/modules/postgresql/spec/acceptance/z_alternative_pgdata_spec.rb
/usr/share/puppet/modules/postgresql/spec/spec_helper.rb
/usr/share/puppet/modules/postgresql/spec/spec_helper_acceptance.rb
/usr/share/puppet/modules/postgresql/spec/spec_helper_local.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/client_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/globals_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/lib/devel_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/lib/java_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/lib/perl_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/lib/pgdocs_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/lib/python_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/params_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/repo_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/config_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/contrib_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/initdb_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/plperl_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/plpython_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server/postgis_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/classes/server_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/config_entry_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/database_grant_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/database_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/db_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/extension_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/grant_role_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/grant_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/pg_hba_rule_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/pg_ident_rule_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/recovery_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/role_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/schema_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/table_grant_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/server/tablespace_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/defines/validate_db_connection_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/functions/postgresql_acls_to_resources_hash_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/functions/postgresql_escape_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/functions/postgresql_password_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/provider/postgresql_conf/parsed_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/puppet/provider/postgresql_psql/ruby_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/puppet/provider/postgresql_replication_slot/ruby_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/puppet/type/postgresql_psql_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/puppet/type/postgresql_replication_slot_spec.rb
/usr/share/puppet/modules/postgresql/spec/unit/type/postgresql_conf_spec.rb
/usr/share/puppet/modules/postgresql/templates/pg_hba_rule.conf
/usr/share/puppet/modules/postgresql/templates/pg_ident_rule.conf
/usr/share/puppet/modules/postgresql/templates/recovery.conf.erb
/usr/share/puppet/modules/postgresql/templates/systemd-override.erb
