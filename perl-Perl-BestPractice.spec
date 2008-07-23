%define	module	Perl-BestPractice
%define	name	perl-%{module}
%define version 0.01
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl Best Practices, the (unofficial) companion module 
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-PPI
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl::BestPractice is the (for now unofficial) companion module to the O'Reilly
"Perl Best Practices" by Damian Conway.

Using various bits of PPI magic, it provides functionality to automatically
locate (and in some cases repair) issues raised by the book.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Perl
%{_mandir}/man3/*

