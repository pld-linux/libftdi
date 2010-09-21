Summary:	Library to talk to FTDI's chips including the popular bitbang mode
Summary(pl.UTF-8):	Biblioteka do komunikacji z układami FTDI włącznie z trybem bitbang
Name:		libftdi
Version:	0.18
Release:	1
License:	LGPL v2 (libftdi), GPL v2 with linking exception (libftdipp)
Group:		Libraries
Source0:	http://www.intra2net.com/en/developer/libftdi/download/%{name}-%{version}.tar.gz
# Source0-md5:	916f65fa68d154621fc0cf1f405f2726
URL:		http://www.intra2net.com/en/developer/libftdi/
BuildRequires:	boost-devel >= 1.33
BuildRequires:	libusb-compat-devel >= 0.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libftdi is a library (using libusb) to talk to FTDI's FT232BM/245BM,
FT2232C/D and FT232/245R type chips including the popular bitbang
mode.

%description -l pl.UTF-8
libftdi to biblioteka (korzystająca z libusb) służąca do komunikacji z
układami FTDI typu FT232BM/245BM, FT2232C/D i FT232/245R włącznie z
popularnym trybem bitbang.

%package devel
Summary:	Header files for libftdi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libftdi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-compat-devel >= 0.1.0

%description devel
Header files for libftdi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libftdi.

%package static
Summary:	Static libftdi library
Summary(pl.UTF-8):	Statyczna biblioteka libftdi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libftdi library.

%description static -l pl.UTF-8
Statyczna biblioteka libftdi.

%prep
%setup -q

%build
%configure \
	--with-boost-libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless example
rm $RPM_BUILD_ROOT%{_bindir}/simple
# maybe useful
mv $RPM_BUILD_ROOT%{_bindir}/{find_all,ftdi_find_all}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/baud_test
%attr(755,root,root) %{_bindir}/bitbang
%attr(755,root,root) %{_bindir}/bitbang2
%attr(755,root,root) %{_bindir}/bitbang_cbus
%attr(755,root,root) %{_bindir}/bitbang_ft2232
%attr(755,root,root) %{_bindir}/ftdi_find_all
%attr(755,root,root) %{_bindir}/find_all_pp
%attr(755,root,root) %{_bindir}/serial_read
%attr(755,root,root) %{_libdir}/libftdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftdi.so.1
%attr(755,root,root) %{_libdir}/libftdipp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftdipp.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libftdi-config
%attr(755,root,root) %{_libdir}/libftdi.so
%attr(755,root,root) %{_libdir}/libftdipp.so
%{_libdir}/libftdi.la
%{_libdir}/libftdipp.la
%{_includedir}/ftdi.h
%{_includedir}/ftdi.hpp
%{_pkgconfigdir}/libftdi.pc
%{_pkgconfigdir}/libftdipp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libftdi.a
%{_libdir}/libftdipp.a
