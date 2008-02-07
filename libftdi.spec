Summary:	Library to talk to FTDI's chips including the popular bitbang mode
Summary(pl.UTF-8):	Biblioteka do komunikacji z układami FTDI włącznie z trybem bitbang
Name:		libftdi
Version:	0.10
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.intra2net.com/de/produkte/opensource/ftdi/TGZ/%{name}-%{version}.tar.gz
# Source0-md5:	21ec9cc5aae63fa2e2b52c530882e483
URL:		http://www.intra2net.com/de/produkte/opensource/ftdi/
BuildRequires:	libusb-devel >= 0.1.7
Requires:	libusb >= 0.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libftdi is a library (using libusb) to talk to FTDI's FT232BM/245BM,
FT2232C/D and FT232/245R type chips including the popular bitbang
mode.

%description -l pl.UTF-8
libftdi to biblioteka (korzystająca z libusb) służąca do komunikacji
z układami FTDI typu FT232BM/245BM, FT2232C/D i FT232/245R włącznie z
popularnym trybem bitbang.

%package devel
Summary:	Header files for libftdi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libftdi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel >= 0.1.7

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
%configure
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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/bitbang
%attr(755,root,root) %{_bindir}/bitbang2
%attr(755,root,root) %{_bindir}/bitbang_cbus
%attr(755,root,root) %{_bindir}/bitbang_ft2232
%attr(755,root,root) %{_bindir}/ftdi_find_all
%attr(755,root,root) %{_libdir}/libftdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftdi.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libftdi-config
%attr(755,root,root) %{_libdir}/libftdi.so
%{_libdir}/libftdi.la
%{_includedir}/ftdi.h
%{_pkgconfigdir}/libftdi.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libftdi.a
