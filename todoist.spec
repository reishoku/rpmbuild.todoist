%global debug_package %{nil}

Name:           todoist
Version:        0.23.0
Release:        1%{?dist}
Summary:        Todoist CLI client

License:        MIT
URL:            https://github.com/sachaos/todoist
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch:  %{go_arches}

# Build-time dependencies
BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros

# Run-time dependencies
Recommends:     fzf

%description
Todoist CLI Client, written in Golang.

%prep
%autosetup -n %{name}-%{version}
go mod vendor

%build
export CGO_ENABLED=1
go build -mod=vendor -buildmode pie -compiler gc -ldflags "-s -w" -trimpath -o %{name} .

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 todoist_functions_fzf.sh -t %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm 0644 todoist_functions_fzf_bash.sh -t %{buildroot}%{_datadir}/bash-completion/completions/

%check
go test -mod=vendor -vet=off ./...

%files
%{_bindir}/%{name}
%{_datadir}/zsh/site-functions/todoist_functions_fzf.sh
%{_datadir}/bash-completion/completions/todoist_functions_fzf_bash.sh
%license LICENSE
%doc README.md

%changelog
* Sat Jan 25 2026 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.23.0-1
- Update to 0.23.0
- Use Go RPM macros for ExclusiveArch

* Thu Nov 4 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.22.0-2
- Modify Spec

* Mon Oct 13 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.22.0-1
- Initial RPM package for todoist
- Release 0.22.0
