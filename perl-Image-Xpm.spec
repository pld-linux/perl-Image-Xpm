%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Xpm
Summary:	Image::Xpm perl module
Summary(pl):	Modu� perla Image::Xpm
Name:		perl-Image-Xpm
Version:	1.09
Release:	2
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Image-Base >= 1.06
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Xpm - Load, create, manipulate and save xpm image files.

%description -l pl
Modu� Image::Xpm - pozwalaj�cy wczytywa�, tworzy�, modyfikowa� oraz
zapisywa� pliki obrazk�w xpm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Image/*
%{_mandir}/man3/*
