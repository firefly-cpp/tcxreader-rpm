%global pypi_name tcxreader
%global fullversion 0.3.2

%global _description %{expand:
This is a simple TCX parser / reader which can read Garmin TCX file
extension files. The package currently does not support laps and merges the
whole exercise into one exercise object. The following data is currently
parsed: longitude, latitude, elevation, time, distance, hr_value, cadence,
watts, TPX_speed (extension).}

Name:           python-%{pypi_name}
Version:        %{?fullversion}
Release:        1%{?dist}
Summary:        tcxreader is a parser/reader for Garmin's TCX file format

License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(maya)
%description -n python3-%{pypi_name}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 05 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Initial package
