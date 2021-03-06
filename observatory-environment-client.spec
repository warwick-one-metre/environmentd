Name:      observatory-environment-client
Version:   4.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/environmentd
Summary:   Environment client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-environment

%description
Part of the observatory software for the Warwick La Palma telescopes.

environment is a commandline utility that queries the environment daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/environment %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/environment %{buildroot}/etc/bash_completion.d/environment

%files
%defattr(0755,root,root,-)
%{_bindir}/environment
/etc/bash_completion.d/environment

%changelog
