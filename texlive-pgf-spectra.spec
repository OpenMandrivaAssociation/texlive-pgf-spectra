%global tl_name pgf-spectra
%global tl_revision 75535

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.2
Release:	%{tl_revision}.1
Summary:	Draw continuous or discrete spectra using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-spectra
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-spectra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-spectra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The purpose of this package is to draw the spectrum of elements in a
simple way. It relies on PGF/TikZ to draw the desired spectrum,
continuous or discrete. Data for the spectra of 98 elements and their
ions are available (from the NASA database and from NIST). Lines data
ranges from Extreme UV to Near IR (from 10 to 4000 nanometers). It also
allows the user to draw spectra using their own data. It is possible to
redshift the lines of a spectrum, by directly entering the redshift
value or the velocity and the angle to compute the redshift value.
Spectral lines data can be presented in a table or exported to a file.
The package also provides color conversion (correlated color
temperature), shadings for use with TikZ and/or pgfplots and color maps
for use with pgfplots.

