%define major 5
%define libname %mklibname KF5Kipi %{major}
%define devname %mklibname KF5Kipi -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Interface to use kipi-plugins for KDE
Name:		libkipi
Version:	20.03.80
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KExiv2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
Obsoletes:	kxmlkipicmd < 2:16.08.3-1
Provides:	kxmlkipicmd = 2:16.08.3-1

%description
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).

#------------------------------------------------

%package -n kipi-common
Summary:	Non-library files for the kipi library
Group:		System/Libraries
BuildArch:	noarch
Obsoletes:	kipi-common < 2:15.12.0

%description -n kipi-common
Common files and tools for the kipi library.

%files -n kipi-common
%doc README TODO AUTHORS
%{_iconsdir}/*/*/*/kipi.*
%{_datadir}/kservicetypes5/kipiplugin.desktop
%dir %{_datadir}/kxmlgui5/kipi

#------------------------------------------------

%package -n kipi-plugin-kxmlhelloword
Summary:	A demo kipi tool using KDE XML-GUI technology
Group:		Graphics
Requires:	kipi-common

%description -n kipi-plugin-kxmlhelloword
This package provides kxmlhelloword which is a demo kipi tool using KDE XML-GUI
technology.

%files -n kipi-plugin-kxmlhelloword
%{_qt5_plugindir}/kipiplugin_kxmlhelloworld.so
%{_datadir}/kservices5/kipiplugin_kxmlhelloworld.desktop
%{_datadir}/kxmlgui5/kipi/*

#------------------------------------------------

%package -n %{libname}
Summary:	Libkipi runtime library
Group:		System/Libraries
Obsoletes:	%{_lib}kipi8 < 2:4.9.0
Obsoletes:	%{_lib}kipi9 < 2:4.10.0
Obsoletes:	%{_lib}kipi10 < 2:4.11.0
Obsoletes:	%{_lib}kipi11 < 2:15.12.0

%description -n %{libname}
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).

This package provides the runtime library.

%files -n %{libname}
%{_libdir}/libKF5Kipi.so.%{major}*
%{_libdir}/libKF5Kipi.so.32*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development library for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90
Conflicts:	libkipi-devel < 2:4.9.2-2
Obsoletes:	libkipi-devel < 2:15.12.0-3

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KF5/KIPI
%{_includedir}/KF5/libkipi_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5Kipi

#----------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
