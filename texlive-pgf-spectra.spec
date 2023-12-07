Name:		texlive-pgf-spectra
Version:	66961
Release:	1
Summary:	Draw continuous or discrete spectra using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgf-spectra
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-spectra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-spectra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to draw the spectra of elements
in a simple way. It is based on the package pst-spectra, but
with some extra options. It relies on PGF/TikZ for drawing the
desired spectrum, continuous or discrete. There are data
available for the spectra of 98 elements and their ions (from
the NASA database and from NIST). It also allows the user to
draw spectra using their own data.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgf-spectra
%doc %{_texmfdistdir}/doc/latex/pgf-spectra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
