# revision 32179
# category Package
# catalog-ctan /graphics/pstricks/contrib/pstricks-add
# catalog-date 2013-11-15 07:22:56 +0100
# catalog-license lppl
# catalog-version 3.62
Name:		texlive-pstricks-add
Version:	3.62
Release:	5
Summary:	A collection of add-ons and bugfixes for PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pstricks-add
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Collects together examples that have been posted to the
pstricks mailing list, together with many additional features
for the basic pstricks, pst-plot and pst-node, including: -
bugfixes; - new options for the pspicture environment; -
arrows; - braces as node connection/linestyle; - extended axes
for plots (e.g., logarithm axes); - polar plots; - plotting
tangent lines of curves or functions; - solving and printing
differential equationd; - box plots; - matrix plots; and - pie
charts. The package makes use of PostScript routines provided
by pst-math.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks-add/pstricks-add.pro
%{_texmfdistdir}/tex/generic/pstricks-add/pstricks-add.tex
%{_texmfdistdir}/tex/latex/pstricks-add/pstricks-add.cfg
%{_texmfdistdir}/tex/latex/pstricks-add/pstricks-add.sty
%doc %{_texmfdistdir}/doc/generic/pstricks-add/Changes
%doc %{_texmfdistdir}/doc/generic/pstricks-add/README
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.bib
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.dat
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
