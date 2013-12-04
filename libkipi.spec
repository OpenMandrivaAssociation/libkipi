Summary:	Interface to use kipi-plugins for KDE
Name:		libkipi
Version:	4.11.4
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source:		ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
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
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0
- New library major 11
- Obsolete old library

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- New library major 10
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Sun Jul 01 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- Update to 4.8.95
- New library major 9

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762494
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758082
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744561
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739316
- New upstream tarball $NEW_VERSION

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 732317
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80

* Tue Aug 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-2
+ Revision: 696280
- New version 4.7.41
- Rebuild to try to push in main

* Thu Jul 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.40-1
+ Revision: 692102
- import libkipi


* Mon Dec 04 2006 Angelo Naselli <anaselli@mandriva.org> 0.1.5-2mdv2007.0
+ Revision: 90417
- forgot to fix release
- fixed Provides field for devel package

* Sun Dec 03 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.5-1mdv2007.1
+ Revision: 90266
- new version 0.1.5
- Import libkipi

* Sun Aug 06 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1:0.1.4-3
- add BuildRequires: libxt-devel

* Tue Jun 20 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.4-2mdk
- Rebuild

* Thu May 18 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.4-1mdk
- new release

* Mon May 15 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.3-2mdk
- Fix build problem

* Mon May 08 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.3-1mdk
new release

* Sun Jan 08 2006 Angelo Naselli <anaselli@mandriva.org> 1:0.1.2-2mdk
- backport from svn admin to allow compiling under kde 3.5

* Tue Sep 27 2005 Angelo Naselli <anaselli@mandriva.org> 1:0.1.2-1mdk
- new release

* Sat May 07 2005 Laurent MONTEL <lmontel@mandriva.com> 0.1.1-4
- Rebuild

* Wed Mar 09 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.1.1-3mdk
- fix build on lib64 platforms

* Sun Feb 13 2005 Angelo Naselli <anaselli@mandrake.org> 0.1.1-2mdk
- DistroSpecificReleaseTag support

* Wed Feb 09 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.1-1mdk
- 0.1.1

* Tue Dec 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1-4mdk
- Rebuild with new libkipi

* Wed Dec 15 2004 Stefan van der Eijk <stefan@mandrake.org> 0.1-3mdk
- BuildRequires

* Fri Dec 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1-2mdk
- Fix spec file

* Sun Oct 17 2004 Angelo Naselli <anaselli@mandrake.org> 0.1-1mdk
- new version

* Tue Sep 21 2004 Angelo Naselli <anaselli@mandrake.org> 20040919-1mdk
- new version (gwenview snapshot)

* Thu Sep 09 2004 Angelo Naselli <anaselli@mandrake.org> 20040801-3mdk
- changed the URL with the official one

* Wed Aug 25 2004 Angelo Naselli <anaselli@mandrake.org> 20040801-2mdk
- changed Summary

* Wed Aug 25 2004 Angelo Naselli <anaselli@mandrake.org> 20040801-1mdk
- built mdk version

* Sun Jun 13 2004 Angelo Naselli <random_lx@yahoo.com> 20040611-1mdk
- built mdk version

* Tue May 11 2004 Angelo Naselli <random_lx@yahoo.com> 20040509-1mdk
- built mdk version

