#
# Conditional build:
%bcond_without	static_libs # don't build static library
#
Summary:	C++ wrappers for libgda
Summary(pl.UTF-8):	Interfejsy C++ dla libgda
Name:		libgdamm
Version:	1.3.7
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdamm/1.3/%{name}-%{version}.tar.gz
# Source0-md5:	1983066281586eec6a6a5cc13adedf4d
BuildRequires:	glibmm-devel >= 2.11.3
BuildRequires:	libgda-devel >= 1:1.2.3
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgda.

%description -l pl.UTF-8
Interfejsy C++ dla libgda.

%package devel
Summary:	Header files for libgdamm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdamm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.11.3
Requires:	libgda-devel >= 1:1.2.3

%description devel
Header files for libgdamm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgdamm.

%package static
Summary:	Static libgdamm library
Summary(pl.UTF-8):	Statyczna biblioteka libgdamm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdamm library.

%description static -l pl.UTF-8
Statyczna biblioteka libgdamm.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static=yes}

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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
