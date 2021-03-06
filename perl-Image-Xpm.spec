#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Image
%define		pnam	Xpm
Summary:	Image::Xpm - load, create, manipulate and save xpm image files
Summary(pl.UTF-8):	Image::Xpm - wczytaj, twórz, modyfikuj i zapisuj obrazy w formacie xpm
Name:		perl-Image-Xpm
Version:	1.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8dce284cd4c97b151bfbd1f0bbd1cb1
URL:		http://search.cpan.org/dist/Image-Xpm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Image-Base >= 1.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class module provides basic load, manipulate and save
functionality for the xpm file format. It inherits from Image::Base
which provides additional manipulation functionality, e.g.
new_from_image().

%description -l pl.UTF-8
Image::Xpm dostarcza prostej funkconalności do wczytywania,
manipulacji i zapisywania obrazów w formacie xpm. Dziedziczy po
Image::Base, dostarczającym dodatkowych funkcji manipulacyjnych; np.
new_from_image().

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
