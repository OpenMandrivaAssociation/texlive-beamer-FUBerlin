# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/beamer-FUBerlin
# catalog-date 2009-08-11 19:19:50 +0200
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-beamer-FUBerlin
Version:	0.02
Release:	8
Summary:	Beamer, using the style of FU Berlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-FUBerlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-FUBerlin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-FUBerlin.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/beamer-FUBerlin/FUbeamer.cls
%{_texmfdistdir}/tex/latex/beamer-FUBerlin/beamercolorthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-FUBerlin/beamerfontthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-FUBerlin/beamerouterthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-FUBerlin/beamerthemeBerlinFU.sty
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/Changes
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/FULogo.png
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/FUbib.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/FUlogo.pdf
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/README
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/exampleClass.pdf
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/exampleClass.tex
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/exampleTheme.pdf
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/exampleTheme.tex
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/geo.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin/silberlaube2.jpg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.02-2
+ Revision: 749529
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.02-1
+ Revision: 717897
- texlive-beamer-FUBerlin
- texlive-beamer-FUBerlin
- texlive-beamer-FUBerlin
- texlive-beamer-FUBerlin
- texlive-beamer-FUBerlin

