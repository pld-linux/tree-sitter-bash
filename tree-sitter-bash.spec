Summary:	Bash grammar for tree-sitter
Name:		tree-sitter-bash
Version:	0.20.5
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/tree-sitter/tree-sitter-bash/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fca0289b077a0aedf8b66ee9b9de6e6d
URL:		https://github.com/tree-sitter/tree-sitter-bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ts_bash_soname	libtree-sitter-bash.so.0

%description
Bash grammar for tree-sitter.

%package -n neovim-parser-bash
Summary:	Bash parser for Neovim
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description -n neovim-parser-bash
Bash parser for Neovim.

%prep
%setup -q

%build
%{__cc} %{rpmcppflags} %{rpmcflags} -fPIC -shared -Wl,-soname,%{ts_bash_soname} src/*.c -o libtree-sitter-bash.so.%{version} %{rpmldflags}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_libdir}/nvim/parser}

cp -p libtree-sitter-bash.so.%{version} $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} libtree-sitter-bash.so.%{version} $RPM_BUILD_ROOT%{_libdir}/%{ts_bash_soname}

%{__ln_s} %{_libdir}/%{ts_bash_soname} $RPM_BUILD_ROOT%{_libdir}/nvim/parser/bash.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libtree-sitter-bash.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{ts_bash_soname}

%files -n neovim-parser-bash
%defattr(644,root,root,755)
%{_libdir}/nvim/parser/bash.so
