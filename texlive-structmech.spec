Name:		texlive-structmech
Version:	66724
Release:	1
Summary:	A TikZ command set for structural mechanics drawings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/structmech
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/structmech.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/structmech.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a collection of TikZ commands that allow
users to draw basic elements in material/structural mechanics.
It is thus possible to draw member forces, nodal
forces/displacements, various boundary conditions, internal
force distributions, etc.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/structmech
%doc %{_texmfdistdir}/doc/latex/structmech

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
