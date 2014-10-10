%define upstream_name    Data-UUID-LibUUID
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:    Drop in L<Data::UUID> replacement
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl-asa
BuildRequires: perl-devel
BuildRequires: libuuid-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides bindings for libuuid shipped with e2fsprogs or
uuid-dev on debian, and also works with the system _uuid.h_ on darwin.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.50.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.50.0-4
+ Revision: 681385
- mass rebuild

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.50.0-3mdv2011.0
+ Revision: 563407
- Changed the uuid builrequries to something better (and portable)
- Add the missing devel(libuuid)
- import perl-Data-UUID-LibUUID


* Fri Feb 05 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
