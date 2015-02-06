%define upstream_name    Test-Strict
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check syntax, presence of use strict; and test coverage
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Cover)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
The most basic test one can write is "does it compile ?". This module tests if
the code compiles and play nice with Test::Simple modules.

Another good practice this module can test is to "use strict;" in all perl
files.

By setting a minimum test coverage through all_cover_ok(), a code author can
ensure his code is tested above a preset level of kwality throughout the
development cycle.

Along with Test::Pod, this module can provide the first tests to setup for a
module author.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 505679
- update to 0.14

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 405596
- rebuild using %%perl_convert_version

* Sun Feb 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.1
+ Revision: 336238
- update to new version 0.13

* Thu Jan 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
+ Revision: 335366
- update to new version 0.12

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 331594
- update to new version 0.11

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2009.0
+ Revision: 268740
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 213738
- import perl-Test-Strict


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
- first mdv release


