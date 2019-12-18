%global __jar_repack 0

Name:		ovirt-engine-wildfly
Version:        17.0.1	
Release:	1
Summary:	WildFly Application Server for oVirt Engine
Group:		Virtualization/Management
License:	ASL 2.0
URL:		http://wildfly.org
Source:		wildfly-17.0.1.Final.zip

BuildRequires:	unzip
BuildRequires:	chrpath

# Prevent breaking packages that require e.g. libapr-1.so
AutoReqProv:	no


%description
WildFly Application Server for oVirt Engine.


%install
mkdir -p %{buildroot}%{_datadir}
unzip -d %{buildroot}%{_datadir} %{SOURCE0}
mv %{buildroot}%{_datadir}/wildfly-%{version}.Final %{buildroot}%{_datadir}/%{name}

# Remove the shared objects that aren't suitable for the architecture
# that the package is being built for:
function remove_shared_objects () {
  find \
      %{buildroot}%{_datadir}/%{name}/modules/system/layers/base \
      -depth \
      -type d \
      -name "$1" \
      -exec rm -rf {} \;
}
remove_shared_objects solaris-x86_64
remove_shared_objects solaris-sparcv9
%ifarch x86_64
remove_shared_objects linux-i686
%endif
%ifarch %{ix86}
remove_shared_objects linux-x86_64
%endif

# Delete the "rpath" of the remaining shared objects:
find \
    %{buildroot}%{_datadir}/%{name}/modules/system/layers/base \
    -type f \
    -name '*.so' \
    -exec chrpath --delete {} \;


%files
%{_datadir}/%{name}


%changelog
* Fri Nov 1 2019 Martin Perina <mperina@redhat.com> - 18.0.0-1
- Update to upstream version 18.0.0.Final

* Tue Jul 23 2019 Martin Perina <mperina@redhat.com> - 17.0.1-1
- Update to upstream version 17.0.1.Final

* Fri Jun 14 2019 Martin Perina <mperina@redhat.com> - 17.0.0-1
- Update to upstream version 17.0.0.Final

* Mon Apr 29 2019 Martin Perina <mperina@redhat.com> - 16.0.0-1
- Update to upstream version 16.0.0.Final

* Fri Feb 1 2019 Martin Perina <mperina@redhat.com> - 15.0.1-1
- Update to upstream version 15.0.1.Final

* Sat Oct 6 2018 Martin Perina <mperina@redhat.com> - 13.0.0-3
- Removes 'Provides: ovirt-engine-wildfly-13'

* Fri Sep 21 2018 Martin Perina <mperina@redhat.com> - 13.0.0-2
- Add 'Provides: ovirt-engine-wildfly-13' to simplify dependency issues in CI
  during upgrade of WildFly

* Mon Jun 18 2018 Martin Perina <mperina@redhat.com> - 13.0.0-1
- Update to upstream version 13.0.0.Final

* Tue Oct 24 2017 Martin Perina <mperina@redhat.com> - 11.0.0-1
- Update to upstream version 11.0.0.Final.
- Removed Solaris binaries from the package.

* Mon Aug 28 2017 Martin Perina <mperina@redhat.com> - 11.0.0-0.2
- Update to upstream version 11.0.0.CR1.

* Thu Aug 17 2017 Martin Perina <mperina@redhat.com> - 11.0.0-0.1
- Update to upstream version 11.0.0.Beta1.

* Fri Sep 09 2016 Martin Perina <mperina@redhat.com> - 10.1.0-1
- Update to upstream version 10.1.0.Final.

* Mon Feb 22 2016 Martin Perina <mperina@redhat.com> - 10.0.0-1
- Update to upstream version 10.0.0.Final.

* Thu Jan 07 2016 Martin Perina <mperina@redhat.com> - 10.0.0-0.4
- Update to upstream version 10.0.0.CR5.

* Wed Nov 04 2015 Martin Perina <mperina@redhat.com> - 10.0.0-0.3
- Update to upstream version 10.0.0.CR4.

* Thu Sep 17 2015 Juan Hernandez <juan.hernandez@redhat.com> - 10.0.0-0.1
- Update to upstream version 10.0.0.

* Tue Feb 17 2015 Juan Hernandez <juan.hernandez@redhat.com> - 8.2.0-1
- Update to upstream version 8.2.0.

* Thu Jul 17 2014 Juan Hernandez <juan.hernandez@redhat.com> - 8.1.0-1
- Initial release based on existing jboss-as spec file.
