%define real_version 2005-12-21

Name:           wormsofprey-data
Version:        20051221
Release:        11%{?dist}
Summary:        Data for worms of prey
Group:          Amusements/Games
License:        GPL+
URL:            http://wormsofprey.org
Source0:        http://wormsofprey.org/download/wopdata-%{real_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       wormsofprey >= 0.4.3

%description
Data for the game worms of prey


%prep
%setup -q -n wopdata-%{real_version}


# %build
# nothing to Build, data only!


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wormsofprey
cp -r * $RPM_BUILD_ROOT%{_datadir}/wormsofprey


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/wormsofprey/*


%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20051221-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20051221-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20051221-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20051221-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 20051221-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20051221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20051221-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 20051221-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 20051221-3
- rebuild for new F11 features

* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20051221-2
- Release bump for rpmfusion

* Wed Aug  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20051221-1%{?dist}
- Initial Fedora Extras package
