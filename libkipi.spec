%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Interface to use kipi-plugins for KDE
Name:		libkipi
Version:	15.08.0
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	automoc4

%description
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).

#------------------------------------------------

%package -n kipi-common
Summary:	Non-library files for the kipi library
Group:		System/Libraries

%description -n kipi-common
Common files and tools for the kipi library.

%files -n kipi-common
%doc README TODO AUTHORS COPYING
%{_kde_bindir}/kxmlkipicmd
%{_kde_appsdir}/kipi
%{_kde_appsdir}/kxmlkipicmd
%{_kde_iconsdir}/*/*/*/kipi.*
%{_kde_libdir}/kde4/kipiplugin_kxmlhelloworld.so
%{_kde_services}/kipiplugin_kxmlhelloworld.desktop
%{_kde_servicetypes}/kipiplugin.desktop

#------------------------------------------------

%define kipi_major 11
%define libkipi %mklibname kipi %{kipi_major}

%package -n %{libkipi}
Summary:	libkipi library
Group:		System/Libraries
Obsoletes:	%{_lib}kipi8 < 2:4.9.0
Obsoletes:	%{_lib}kipi9 < 2:4.10.0
Obsoletes:	%{_lib}kipi10 < 2:4.11.0

%description -n %{libkipi}
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).

%files -n %{libkipi}
%{_kde_libdir}/libkipi.so.%{kipi_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel >= 2:%{version}
Requires:	%{libkipi} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/%{name}
%{_kde_libdir}/libkipi.so
%{_kde_libdir}/pkgconfig/libkipi.pc

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
