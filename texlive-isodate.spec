%global tl_name isodate
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.28
Release:	%{tl_revision}.1
Summary:	Tune the output format of dates according to language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isodate
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides ten output formats of the commands \today,
\printdate, \printdateTeX, and \daterange (partly language dependent).
Formats available are: ISO (yyyy-mm-dd), numeric (e.g. dd.\,mm.~yyyy),
short (e.g. dd.\,mm.\,yy), TeX (yyyy/mm/dd), original (e.g. dd. mmm
yyyy), short original (e.g. dd. mmm yy), as well as numerical formats
with Roman numerals for the month. The commands \printdate and
\printdateTeX print any date. The command \daterange prints a date range
and leaves out unnecessary year or month entries. This package supports
German (old and new rules), Austrian, US English, British English,
French, Danish, Swedish, and Norwegian.

