#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	RegExp
Summary:	XML::RegExp - regular expressions for XML tokens
Summary(pl.UTF-8):	XML::RegExp - wyrażenia regularne dla tokenów XML
Name:		perl-XML-RegExp
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e38ea2340f2d2eb56bd81c4d739fbe0
URL:		http://search.cpan.org/dist/XML-RegExp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains regular expressions for the following XML
tokens: BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar,
NameChar, EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

%description -l pl.UTF-8
Ten pakiet zawiera wyrażenia regularne dla następujących tokenów XML:
BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar,
NameChar, EntityRef, CharRef, Reference, Name, NmToken oraz AttValue.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/RegExp.pm
%{_mandir}/man3/*
