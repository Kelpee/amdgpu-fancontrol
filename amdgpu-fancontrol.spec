Summary:	Simple tool to control AMD graphics card fan
Name:		amdgpu-fancontrol	
Version:	1.0
Release:	1
License:	GPLv3
Group:		Monitoring
Url:		https://github.com/Kelpee/amdgpu-fancontrol
Source0:    https://github.com/Kelpee/amdgpu-fancontrol/archive/%{version}.tar.gz
BuildArch:  noarch

Requires:	bash


%description
Simple bash script to control AMD Radeon graphics cards fan pwm.
Adjust temp/pwm values and hysteresis/interval in the script as desired.
Other adjustments, such as the correct hwmon path might be required as well.
ROSA Fresh R11.


%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.cfg
%{_unitdir}/%{name}.service

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir} %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -p -m 644 etc-%{name}.cfg %{buildroot}%{_sysconfdir}/%{name}.cfg
install -p -m 644 %{name}.service %{buildroot}%{_unitdir}


%post
systemctl enable %{name}.service
systemctl start  %{name}.service
