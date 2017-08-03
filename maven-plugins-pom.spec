%{?scl:%scl_package %{short_name}-pom}
%{!?scl:%global pkg_name %{name}}

%global short_name maven-plugins

Name:           %{?scl_prefix}%{short_name}-pom
Version:        28
Release:        5.2%{?dist}
Summary:        Maven Plugins POM
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/
BuildArch:      noarch

Source:         http://repo.maven.apache.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
%setup -q -n %{short_name}-%{version}
# Enforcer plugin is used to ban plexus-component-api.
%pom_remove_plugin :maven-enforcer-plugin
# maven-scm-publish-plugin is not usable in Fedora.
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 28-5.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 28-5.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 28-4
- Remove BR on maven-site-plugin

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 28-3
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 28-1
- Update to upstream version 28

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 27-2
- Add missing BR on maven-site-plugin

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 27-1
- Update to upstream version 27

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-1
- Update to upstream version 26

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 25-2
- Rebuild to regenerate Maven auto-requires

* Wed Apr  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 25-1
- Update to upstream version 25

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 24-1
- Update to upstream version 24
- Disable maven-scm-publish-plugin

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 23-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-4
- Disable maven-enforcer-plugin
- Build with xmvn

* Thu Nov 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-3
- Add missing R: maven-enforcer-plugin

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-2
- Install license files

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-1
- Initial packaging
