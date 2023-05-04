Name:		texlive-pstricks-add
Version:	66887
Release:	1
Summary:	A collection of add-ons and bugfixes for PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pstricks-add
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Collects together examples that have been posted to the
pstricks mailing list, together with many additional features
for the basic pstricks, pst-plot and pst-node, including:
bugfixes; new options for the pspicture environment; arrows;
braces as node connection/linestyle; extended axes for plots
(e.g., logarithm axes); polar plots; plotting tangent lines of
curves or functions; solving and printing differential
equations; box plots; matrix plots; and pie charts. The package
makes use of PostScript routines provided by pst-math.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks-add
%{_texmfdistdir}/tex/generic/pstricks-add
%{_texmfdistdir}/tex/latex/pstricks-add
%doc %{_texmfdistdir}/doc/generic/pstricks-add

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
