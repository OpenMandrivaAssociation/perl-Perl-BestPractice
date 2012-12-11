%define	module	Perl-BestPractice

Name:		perl-%{module}
Version:	0.01
Release:	7
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl Best Practices, the (unofficial) companion module 
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	perl(PPI)
BuildArch:	noarch

%description
Perl::BestPractice is the (for now unofficial) companion module to the O'Reilly
"Perl Best Practices" by Damian Conway.

Using various bits of PPI magic, it provides functionality to automatically
locate (and in some cases repair) issues raised by the book.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Perl
%{_mandir}/man3/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.01-6mdv2010.0
+ Revision: 430524
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-5mdv2009.0
+ Revision: 241814
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdv2008.0
+ Revision: 86793
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2007.0
- Rebuild

* Thu Nov 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdk
- first mdk release

