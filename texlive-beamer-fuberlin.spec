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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a beamer-derived class and a theme style file for
the corporate design of the Free University in Berlin. Users may use the
class itself (FUbeamer) or use the theme in the usual way with
\usetheme{BerlinFU}. Examples of using both the class and the theme are
provided; the PDF is visually identical, so the catalogue only lists
one; the sources of the examples do of course differ.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin
%dir %{_datadir}/texmf-dist/tex/latex/beamer-fuberlin
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/Changes
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/README
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/README.doc
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/exampleClass.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/exampleClass.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/exampleTheme.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer-fuberlin/exampleTheme.tex
%{_datadir}/texmf-dist/tex/latex/beamer-fuberlin/FUbeamer.cls
%{_datadir}/texmf-dist/tex/latex/beamer-fuberlin/beamercolorthemeBerlinFU.sty
%{_datadir}/texmf-dist/tex/latex/beamer-fuberlin/beamerfontthemeBerlinFU.sty
%{_datadir}/texmf-dist/tex/latex/beamer-fuberlin/beamerouterthemeBerlinFU.sty
%{_datadir}/texmf-dist/tex/latex/beamer-fuberlin/beamerthemeBerlinFU.sty
