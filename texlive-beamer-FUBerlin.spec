Name:		texlive-beamer-FUBerlin
Version:	63161
Release:	2
Summary:	Beamer, using the style of FU Berlin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-FUBerlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-fuberlin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-fuberlin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a beamer-derived class and a theme style
file for the corporate design of the Free University in Berlin.
Users may use the class itself (FUbeamer) or use the theme in
the usual way with \usetheme{BerlinFU}. Examples of using both
the class and the theme are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamer-fuberlin
%doc %{_texmfdistdir}/doc/latex/beamer-fuberlin

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
