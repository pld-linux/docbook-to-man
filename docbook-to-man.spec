Summary:	Converter from DocBook SGML into roff man macros
Summary(pl.UTF-8):	Konwerter z formatu DocBook SGML do roff (używanego przez program man)
Name:		docbook-to-man
Version:	2.0.0
Release:	3
License:	MIT
Group:		Applications/Publishing/SGML
# original: http://www.oasis-open.org/docbook/tools/dtm/%{name}.tar.gz
# we use ANS version, available in Debian
Source0:	http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
# Source0-md5:	84946e13a0e54057e9cbf8ad7eec4afa
Patch0:		http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}-28.diff.gz
# Patch0-md5:	ac83d1d8852bcaadeb6bb81d559ea5c9
Patch1:		%{name}-opt.patch
Patch2:		%{name}-PLD.patch
Patch3:		includes.patch
Patch4:		types.patch
Patch5:		format-security.patch
Patch6:		link.patch
URL:		http://www.oasis-open.org/docbook/tools/dtm/
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	opensp
Requires:	docbook-dtd41-sgml
Requires:	opensp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
docbook-to-man is a batch converter that transforms UNIX-style
manpages from the DocBook SGML format into nroff/troff man macros.

This is not the original version by Fred Dalrymple, but one with the
modifications by David Bolen with Debian changes.

%description -l pl.UTF-8
docbook-to-man to wsadowy konwerter przekształcający strony manuala
uniksowego z formatu DocBook SGML do makr nroffa/troffa.

Nie jest to oryginalna wersja autorstwa Freda Dalrymple'a, lecz wersja
z modyfikacjami Davida Bolena oraz zmianami z Debiana.

%prep
%setup -q -n %{name}-%{version}.orig
%patch -P0 -p1
for patch in $(cat debian/patches/00list); do
	%{__patch} -p1 -s < debian/patches/$patch.dpatch
done
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	ROOT=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/sgml,%{_mandir}/man{1,5}}
%{__make} install \
	ROOT=$RPM_BUILD_ROOT%{_prefix}

cp -p Doc/{docbook-to-man.1,instant.1} $RPM_BUILD_ROOT%{_mandir}/man1
cp -p Doc/transpec.1 $RPM_BUILD_ROOT%{_mandir}/man5/transpec.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ANS
%attr(755,root,root) %{_bindir}/docbook-to-man
%attr(755,root,root) %{_bindir}/instant
%{_datadir}/sgml/transpec
%{_mandir}/man1/docbook-to-man.1*
%{_mandir}/man1/instant.1*
%{_mandir}/man5/transpec.5*
