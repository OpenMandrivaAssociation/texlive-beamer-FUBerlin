Name:		texlive-beamer-FUBerlin
Version:	0.02b
Release:	1
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
%{_texmfdistdir}/tex/latex/beamer-FUBerlin
%doc %{_texmfdistdir}/doc/latex/beamer-FUBerlin

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}/tex/latex/beamer-FUBerlin
cp -fpar doc/latex/beamer-FUBerlin/tex/latex/* %{buildroot}%{_texmfdistdir}/tex/latex/beamer-FUBerlin
cp -fpar doc %{buildroot}%{_texmfdistdir}
