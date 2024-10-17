Name:		texlive-isodate
Version:	16613
Release:	2
Summary:	Tune the output format of dates according to language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isodate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides ten output formats of the commands
\today, \printdate, \printdateTeX, and \daterange (partly
language dependent). Formats available are: ISO (yyyy-mm-dd),
numeric (e.g. dd.\,mm.~yyyy), short (e.g. dd.\,mm.\,yy), TeX
(yyyy/mm/dd), original (e.g. dd. mmm yyyy), short original
(e.g. dd. mmm yy), as well as numerical formats with Roman
numerals for the month. The commands \printdate and
\printdateTeX print any date. The command \daterange prints a
date range and leaves out unnecessary year or month entries.
This package supports German (old and new rules), Austrian, US
English, British English, French, Danish, Swedish, and
Norwegian.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isodate/danish.idf
%{_texmfdistdir}/tex/latex/isodate/english.idf
%{_texmfdistdir}/tex/latex/isodate/french.idf
%{_texmfdistdir}/tex/latex/isodate/german.idf
%{_texmfdistdir}/tex/latex/isodate/isodate.sty
%{_texmfdistdir}/tex/latex/isodate/isodateo.sty
%{_texmfdistdir}/tex/latex/isodate/italian.idf
%{_texmfdistdir}/tex/latex/isodate/norsk.idf
%{_texmfdistdir}/tex/latex/isodate/swedish.idf
%doc %{_texmfdistdir}/doc/latex/isodate/ChangeLog
%doc %{_texmfdistdir}/doc/latex/isodate/README
%doc %{_texmfdistdir}/doc/latex/isodate/getversion.tex
%doc %{_texmfdistdir}/doc/latex/isodate/isodate.pdf
%doc %{_texmfdistdir}/doc/latex/isodate/isodate.xml
%doc %{_texmfdistdir}/doc/latex/isodate/isodateo.pdf
%doc %{_texmfdistdir}/doc/latex/isodate/testdate.pdf
%doc %{_texmfdistdir}/doc/latex/isodate/testdate.tex
%doc %{_texmfdistdir}/doc/latex/isodate/testisodate_without_babel.tex
#- source
%doc %{_texmfdistdir}/source/latex/isodate/Makefile
%doc %{_texmfdistdir}/source/latex/isodate/isodate.dtx
%doc %{_texmfdistdir}/source/latex/isodate/isodate.ins
%doc %{_texmfdistdir}/source/latex/isodate/isodateo.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
