%define real_version 2005-12-21

Name:           wormsofprey-data
Version:        20051221
Release:        2%{?dist}
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
* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20051221-2
- Release bump for rpmfusion

* Wed Aug  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 20051221-1%{?dist}
- Initial Fedora Extras package
