#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	NoWarnings
Summary:	Test::NoWarnings - Make sure you didn't emit any warnings while testing
Summary(pl):	Test::NoWarnings - sprawdzanie braku ostrze¿eñ podczas testów
Name:		perl-Test-NoWarnings
Version:	0.082
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	702143eab77ffc335a08beccac47dca4
URL:		http://search.cpan.org/dist/Test-NoWarnings/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Tester >= 0.103
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In general, your tests shouldn't produce warnings. This modules causes
any warnings to be captured and stored. It automatically adds an extra
test that will run when your script ends to check that there were no
warnings. If there were any warings, the test will give a "not ok" and
diagnostics of where, when and what the warning was, including a stack
trace of what was going on when the it occurred.

If some of your tests are supposed to produce warnings then you should
be capturing and checking them with Test::Warn, that way
Test::NoWarnings will not see them and so not complain.

%description -l pl
W ogólno¶ci testy nie powinny generowaæ ostrze¿eñ. Ten modu³ powoduje,
¿e wszystkie ostrze¿enia s± przechwytywane i zapisywane. Automatycznie
dodaje dodatkowy test uruchamiany po zakoñczeniu skryptu, sprawdzaj±cy
czy nie by³o ostrze¿eñ. Je¶li wyst±pi³y jakiekolwiek ostrze¿enia, test
wypisze "not ok" i dane diagnostyczne, w którym miejscu, kiedy i jakie
by³o ostrze¿enie, wraz ze ¶ladem stosu tego, co dzia³o siê w chwili
jego wyst±pienia.

Je¶li jakie¶ testy maj± wygenerowaæ ostrze¿enia, nale¿y je wy³apaæ i
sprawdziæ przy u¿yciu Test::Warn - tak, ¿eby Test::NoWarnings ich nie
zobaczy³.

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
%doc CHANGES README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/NoWarnings
%{_mandir}/man3/*
