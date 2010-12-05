#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	NoWarnings
Summary:	Test::NoWarnings - Make sure you didn't emit any warnings while testing
Summary(pl.UTF-8):	Test::NoWarnings - sprawdzanie braku ostrzeżeń podczas testów
Name:		perl-Test-NoWarnings
Version:	0.084
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26341294a4062e9e7d8a643485ca78d4
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

%description -l pl.UTF-8
W ogólności testy nie powinny generować ostrzeżeń. Ten moduł powoduje,
że wszystkie ostrzeżenia są przechwytywane i zapisywane. Automatycznie
dodaje dodatkowy test uruchamiany po zakończeniu skryptu, sprawdzający
czy nie było ostrzeżeń. Jeśli wystąpiły jakiekolwiek ostrzeżenia, test
wypisze "not ok" i dane diagnostyczne, w którym miejscu, kiedy i jakie
było ostrzeżenie, wraz ze śladem stosu tego, co działo się w chwili
jego wystąpienia.

Jeśli jakieś testy mają wygenerować ostrzeżenia, należy je wyłapać i
sprawdzić przy użyciu Test::Warn - tak, żeby Test::NoWarnings ich nie
zobaczył.

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
