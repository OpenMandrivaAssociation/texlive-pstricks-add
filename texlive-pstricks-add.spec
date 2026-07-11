%global tl_name pstricks-add
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.94
Release:	%{tl_revision}.1
Summary:	A collection of add-ons and bugfixes for PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pstricks-add
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-add.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Collects together examples that have been posted to the PSTricks mailing
list, together with many additional features for the basic pstricks,
pst-plot and pst-node, including: bugfixes; new options for the
pspicture environment; arrows; braces as node connection/linestyle;
extended axes for plots (e.g., logarithm axes); polar plots; plotting
tangent lines of curves or functions; solving and printing differential
equations; box plots; matrix plots; and pie charts. The package makes
use of PostScript routines provided by pst-math.

