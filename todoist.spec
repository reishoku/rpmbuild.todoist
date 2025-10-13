
Name:           todoist
Version:        0.22.0
Release:        1%{?dist}
Summary:        Todoist CLI client

License:        MIT
URL:            https://github.com/sachaos/todoist
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: gcc

Provides: %{name} = %{version}

Recommends: fzf

%description
Todoist CLI Client, written in Golang.

%global debug_package %{nil}
%define gomodulesmode GO111MODULE=auto

%prep
%setup -q -n %{name}-%{version}
go mod vendor

%build
export CGO_ENABLED=1
go build -a -v -x -mod=vendor -buildmode pie -compiler gc -ldflags "-s -w" -trimpath -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 todoist_functions_fzf.sh -t %{buildroot}%{zsh_completions_dir}
install -Dpm 0644 todoist_functions_fzf_bash.sh -t %{buildroot}%{bash_completions_dir}

%check
go test -v

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{zsh_completions_dir}/todoist_functions_fzf.sh
%{bash_completions_dir}/todoist_functions_fzf_bash.sh
%license LICENSE
%doc README.md

%changelog
* Mon Oct 13 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.22.0-1
- Initial RPM package for todoist
- Release 0.22.0
