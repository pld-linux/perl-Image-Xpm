#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Xpm
Summary:	Image::Xpm - Load, create, manipulate and save xpm image files
Summary(pl):	Image::Xpm - wczytaj, tw�rz, modyfikuj i zapisuj obrazy w formacie xpm
Name:		perl-Image-Xpm
Version:	1.09
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Image-Base >= 1.06
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class module provides basic load, manipulate and save functionality
for the xpm file format.  It inherits from Image::Base which provides
additional manipulation functionality, e.g. new_from_image().

%description -l pl
Image::Xpm dostarcza prostej funkconalno�ci do wczytywania, manipulacji
i zapisywania obraz�w w formacie xpm.  Dziedziczy po Image::Base,
dostarczaj�cym dodatkowych funkcji manipulacyjnych; np. new_from_image().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Image/*
%{_mandir}/man3/*
