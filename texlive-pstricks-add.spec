# revision 24826
# category Package
# catalog-ctan /graphics/pstricks/contrib/pstricks-add
# catalog-date 2011-12-11 19:04:10 +0100
# catalog-license lppl
# catalog-version 3.55
Name:		texlive-pstricks-add
Version:	3.55
Release:	1
Summary:	A collection of add-ons and bugfixes for PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pstricks-add
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.source.tar.xz
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks-add/pstricks-add.pro
%{_texmfdistdir}/tex/generic/pstricks-add/pstricks-add.tex
%{_texmfdistdir}/tex/latex/pstricks-add/pstricks-add.sty
%doc %{_texmfdistdir}/doc/generic/pstricks-add/Changes
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.bib
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.dat
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-add/pstricks-add-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pstricks-add/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
