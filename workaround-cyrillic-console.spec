%global         wcc_name        setup-cyrfont
%global         wcc_unitname    %{wcc_name}@.service

Name:           workaround-cyrillic-console
Version:        1.1
Release:        3%{?dist}
Summary:        This is package with workaround old bug with incorrectly Russian consoles

License:        GPLv3
URL:            http://ru.fedoracommunity.org
Source0:        https://raw.github.com/RussianFedora/%{name}/master/%{wcc_unitname}
Source1:        https://raw.github.com/RussianFedora/%{name}/master/README.md

Requires:       systemd kbd
BuildRequires:  systemd-units

Requires(post): systemd
Requires(preun): systemd

BuildArch:      noarch

%description
This is package with workaround old bug with incorrectly Russian consoles

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
#nothing to build

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_unitdir}/%{wcc_unitname}

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
    for i in {1..6}; do
        /bin/systemctl enable %{wcc_name}@tty$i.service
    done
fi

%preun
%if 0%{?systemd_preun:1}
%systemd_preun %{wcc_unitname}
%else
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{wcc_unitname} >/dev/null 2>&1 || :
    for i in {1..6}; do
        /bin/systemctl --no-reload disable %{wcc_name}@tty$i >/dev/null 2>&1 || :
    done
fi
%endif

%files
%{_unitdir}/%{wcc_unitname}
%doc README.md

%changelog
* Sun Mar 29 2015 Alexei Panov <me AT elemc DOT name> 1.1-3.R
- Fix RF#1437 

* Mon Mar 02 2015 Alexei Panov <me AT elemc DOT name> 1.1-2.R
- Added systemd-units to BuildRequires

* Mon Mar 02 2015 Alexei Panov <me AT elemc DOT name> 1.1-1.R
- Upgrade unit and spec for new reallity

* Tue May  7 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.0-5.R
- set latarcyrheb-sun16 as default font

* Tue Mar 12 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.0-4.R
- update spec file
  added missing requires
  update urls

* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-3
- Remove script and sources, move all in one .service

* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-2
- Enable service after install it

* Wed Mar 06 2013 Alexei Panov <me AT elemc DOT name> 1.0-1
- Initial build
