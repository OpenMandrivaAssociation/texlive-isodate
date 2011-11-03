# revision 16613
# category Package
# catalog-ctan /macros/latex/contrib/isodate
# catalog-date 2006-12-08 14:34:19 +0100
# catalog-license lppl
# catalog-version 2.28
Name:		texlive-isodate
Version:	2.28
Release:	1
Summary:	Tune the output format of dates according to language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isodate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isodate.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
