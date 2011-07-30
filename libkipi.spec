Name: libkipi
Summary: Interface to use kipi-plugins for KDE
Version: 4.7.40
Release: 2
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).

#------------------------------------------------	

%package -n kipi-common
Summary: Non-library files for the kipi library
Group: System/Libraries

%description -n kipi-common
Common files for the kipi library.

%files -n kipi-common
%doc README TODO AUTHORS COPYING
%_kde_appsdir/kipi
%_kde_iconsdir/*/*/*/kipi.*
%_kde_servicetypes/kipiplugin.desktop

#------------------------------------------------	

%define	kipi_major 8
%define	libkipi %mklibname kipi %kipi_major

%package -n %libkipi
Summary: libkipi library
Group: System/Libraries


%description -n %libkipi
Libkipi is an interface to use kipi-plugins from a KDE image management
program like digiKam (http://www.digikam.org).


%files -n %libkipi
%_kde_libdir/libkipi.so.%{kipi_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: %{libkipi} = %epoch:%version-%release
Conflicts: kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%_includedir/%name
%_kde_libdir/libkipi.so
%_kde_libdir/pkgconfig/libkipi.pc

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

