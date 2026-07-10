%global tl_name beamer-fuberlin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02b
Release:	%{tl_revision}.1
Summary:	Beamer, using the style of FU Berlin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-FUBerlin
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-fuberlin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-fuberlin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a beamer-derived class and a theme style file for
the corporate design of the Free University in Berlin. Users may use the
class itself (FUbeamer) or use the theme in the usual way with
\usetheme{BerlinFU}. Examples of using both the class and the theme are
provided; the PDF is visually identical, so the catalogue only lists
one; the sources of the examples do of course differ.

