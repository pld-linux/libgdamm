Summary:	C++ wrappers for libgda
Summary(pl):	Interfejsy C++ dla libgda
Name:		libgdamm
Version:	1.3.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/1.3/%{name}-%{version}.tar.gz
# Source0-md5:	794bcd7fcfe9baeddb7dce3542793271
BuildRequires:	glibmm-devel >= 2.4.4
BuildRequires:	libgda-devel >= 1.2.0
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgda.

%description -l pl
Interfejsy C++ dla libgda.

%package devel
Summary:	Header files for libgdamm library
Summary(pl):	Pliki nag³ówkowe biblioteki libgdamm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.4.4
Requires:	libgda-devel >= 1.2.0

%description devel
Header files for libgdamm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgdamm.

%package static
Summary:	Static libgdamm library
Summary(pl):	Statyczna biblioteka libgdamm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdamm library.

%description static -l pl
Statyczna biblioteka libgdamm.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libgdamm-2.0
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
