Summary:	Bash grammar for tree-sitter
Summary(pl.UTF-8):	Gramatyka Basha dla biblioteki Tree-sitter
Name:		tree-sitter-bash
Version:	0.25.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/tree-sitter/tree-sitter-bash/releases
Source0:	https://github.com/tree-sitter/tree-sitter-bash/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	97bcbab21f49b375bcf9e6834235f3ee
URL:		https://github.com/tree-sitter/tree-sitter-bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		soname_ver	0

%description
Bash grammar for tree-sitter.

%description -l pl.UTF-8
Gramatyka Basha dla tree-sittera.

%package -n neovim-parser-bash
Summary:	Bash parser for Neovim
Summary(pl.UTF-8):	Analizator składni Basha dla Neovima
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description -n neovim-parser-bash
Bash parser for Neovim.

%description -n neovim-parser-bash -l pl.UTF-8
Analizator składni Basha dla Neovima.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcppflags} %{rpmcflags} -fPIC -shared -Wl,-soname,libtree-sitter-bash.so.%{soname_ver} src/*.c -o libtree-sitter-bash.so.%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_libdir}/nvim/parser}

cp -p libtree-sitter-bash.so.%{version} $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} libtree-sitter-bash.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtree-sitter-bash.so.%{soname_ver}

%{__ln_s} %{_libdir}/libtree-sitter-bash.so.%{soname_ver} $RPM_BUILD_ROOT%{_libdir}/nvim/parser/bash.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/libtree-sitter-bash.so.*.*
%ghost %{_libdir}/libtree-sitter-bash.so.%{soname_ver}

%files -n neovim-parser-bash
%defattr(644,root,root,755)
%{_libdir}/nvim/parser/bash.so
