Summary: Finds and connects you to a specified server's serial console
Name: rcon
Version: 0.9
Release: 1
Copyright: GPL
Group: System/Utility
Source: %{name}
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-root

%description 

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/%{name}
