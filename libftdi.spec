#
# Conditional build:
%bcond_without	python		# Python (3.x) binding
%bcond_without	static_libs	# static libraries

Summary:	Library to talk to FTDI's chips including the popular bitbang mode
Summary(pl.UTF-8):	Biblioteka do komunikacji z układami FTDI włącznie z trybem bitbang
Name:		libftdi
Version:	0.20
Release:	6
License:	LGPL v2
Group:		Libraries
#Source0Download: http://www.intra2net.com/en/developer/libftdi/download.php
Source0:	http://www.intra2net.com/en/developer/libftdi/download/%{name}-%{version}.tar.gz
# Source0-md5:	355d4474e3faa81b485d6a604b06951f
Patch0:		%{name}-python3.patch
URL:		http://www.intra2net.com/en/developer/libftdi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.33
BuildRequires:	libconfuse-devel
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel >= 0.1.0
%{?with_python:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpmbuild(macros) >= 1.527
%{?with_python:BuildRequires:	swig-python >= 2}
BuildConflicts:	libftdi-devel < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libftdi is a library (using libusb) to talk to FTDI's UART/FIFO chips
including the popular bitbang mode. The following chips are supported:
- FT4232H / FT2232H
- FT232R  / FT245R
- FT2232L / FT2232D / FT2232C
- FT232BM / FT245BM (and the BL/BQ variants)
- FT8U232AM / FT8U245AM

%description -l pl.UTF-8
libftdi to korzystająca z libusb biblioteka, służąca do komunikacji z
układami FTDI typu UART/FIFO, włącznie z popularnym trybem bitbang.
Obsługiwane są układy:
- FT4232H / FT2232H
- FT232R  / FT245R
- FT2232L / FT2232D / FT2232C
- FT232BM / FT245BM (wraz z wariantami BL/BQ)
- FT8U232AM / FT8U245AM

%package devel
Summary:	Header files for libftdi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libftdi
License:	LGPL v2
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
License:	LGPL v2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libftdi library.

%description static -l pl.UTF-8
Statyczna biblioteka libftdi.

%package c++
Summary:	C++ wrapper for libftdi
Summary(pl.UTF-8):	Interfejs C++ do libftdi
License:	GPL v2 with linking exception
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
libftdipp - C++ wrapper for libftdi.

%description c++ -l pl.UTF-8
libftdipp - intefejs C++ do libftdi.

%package c++-devel
Summary:	Header file for libftdipp library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libftdipp
License:	GPL v2 with linking exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	boost-devel >= 1.33
Requires:	libstdc++-devel

%description c++-devel
Header file for libftdipp library.

%description c++-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libftdipp.

%package c++-static
Summary:	Static libftdipp library
Summary(pl.UTF-8):	Statyczna biblioteka libftdipp
License:	GPL v2 with linking exception
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libftdipp library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka libftdipp.

%package -n python3-libftdi
Summary:	Python 3 binding for libftdi
Summary(pl.UTF-8):	Wiązanie Pythona 3 do libftdi
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-libftdi < 0.20-6

%description -n python3-libftdi
Python 3 binding for libftdi.

%description -n python3-libftdi -l pl.UTF-8
Wiązanie Pythona 3 do libftdi.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	%{__enable_disable static_libs static} \
	--enable-libftdipp \
	%{?with_python:--enable-python-binding} \
	--with-boost-libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless example
%{__rm} $RPM_BUILD_ROOT%{_bindir}/simple
# maybe useful
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{find_all,ftdi_find_all}
# functionally the same as find_all, just adds C++ dependency
%{__rm} $RPM_BUILD_ROOT%{_bindir}/find_all_pp

%if %{with python}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/baud_test
%attr(755,root,root) %{_bindir}/bitbang
%attr(755,root,root) %{_bindir}/bitbang2
%attr(755,root,root) %{_bindir}/bitbang_cbus
%attr(755,root,root) %{_bindir}/bitbang_ft2232
%attr(755,root,root) %{_bindir}/ftdi_find_all
%attr(755,root,root) %{_bindir}/serial_test
%{_libdir}/libftdi.so.*.*.*
%ghost %{_libdir}/libftdi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libftdi-config
%{_libdir}/libftdi.so
%{_libdir}/libftdi.la
%{_includedir}/ftdi.h
%{_pkgconfigdir}/libftdi.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libftdi.a
%endif

%files c++
%defattr(644,root,root,755)
%{_libdir}/libftdipp.so.*.*.*
%ghost %{_libdir}/libftdipp.so.1

%files c++-devel
%defattr(644,root,root,755)
%{_libdir}/libftdipp.so
%{_libdir}/libftdipp.la
%{_includedir}/ftdi.hpp
%{_pkgconfigdir}/libftdipp.pc

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libftdipp.a
%endif

%if %{with python}
%files -n python3-libftdi
%defattr(644,root,root,755)
%{py3_sitedir}/_ftdi.cpython-*.so
%{py3_sitedir}/ftdi.py
%{py3_sitedir}/__pycache__/ftdi.cpython-*.py[co]
%{py3_sitedir}/libftdi-%{version}-py*.egg-info
%endif
