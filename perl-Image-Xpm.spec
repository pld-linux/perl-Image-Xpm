#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Xpm
Summary:	Image::Xpm - load, create, manipulate and save xpm image files
Summary(pl):	Image::Xpm - wczytaj, tw�rz, modyfikuj i zapisuj obrazy w formacie xpm
Name:		perl-Image-Xpm
Version:	1.09
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1efd12d6f90c184b518282bff980a7f1
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Image/*
%{_mandir}/man3/*
