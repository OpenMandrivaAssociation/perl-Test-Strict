%define upstream_name    Test-Strict
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Check syntax, presence of use strict; and test coverage
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Devel::Cover)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Simple)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
