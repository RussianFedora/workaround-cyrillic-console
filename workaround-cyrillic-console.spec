%global         wcc_name        setup-cyrfont
%global         wcc_unitname    %{wcc_name}@.service

Name:           workaround-cyrillic-console
Version:        1.0
Release:        4%{?dist}
Summary:        This is package with workaround old bug with incorrectly russian consoles

License:        GPLv3
URL:            http://russianfedora.ru
#Source0:        %{name}-%{version}.tar.xz
Source0:        https://raw.github.com/elemc/%{name}/master/%{wcc_unitname}
Source1:        https://raw.github.com/elemc/%{name}/master/README

Requires:       systemd kbd
BuildArch:      noarch

%description
This is package with workaround old bug with incorrectly russian consoles

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_unitdir}/%{wcc_unitname}

%files
%{_unitdir}/%{wcc_unitname}
%doc README

%post
%if 0%{?systemd_post:1}
%systemd_post %{wcc_unitname}
%else
if [ $1 = 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
if [ $1 = 1 ]; then
    /bin/systemctl enable %{wcc_unitname}
fi

%preun
%if 0%{?systemd_preun:1}
%systemd_preun %{wcc_unitname}
%else
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{wcc_unitname} >/dev/null 2>&1 || :
fi
%endif

%changelog
* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-3
- Remove script and sources, move all in one .service

* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-2
- Enable service after install it

* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-1
- Initial build
