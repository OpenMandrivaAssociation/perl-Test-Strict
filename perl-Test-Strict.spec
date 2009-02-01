%define module   Test-Strict
%define version    0.13
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Check syntax, presence of use strict; and test coverage
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires: perl(Devel::Cover)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Simple)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/Test

