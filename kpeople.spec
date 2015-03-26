%define fw_version 5.8

Summary:	KDE Frameworks 5 people contacts module
Name:		kpeople
Version:	5.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/frameworks/%{fw_version}/%{name}-%{version}.tar.xz
Patch0:		kpeople-5.8.0-rename-translations.patch
BuildRequires:	extra-cmake-modules
BuildRequires:	kf5coreaddons-devel >= %{version}
BuildRequires:	kf5i18n-devel >= %{version}
BuildRequires:	kf5itemviews-devel >= %{version}
BuildRequires:	kf5service-devel >= %{version}
BuildRequires:	kf5widgetsaddons-devel >= %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
KDE Frameworks 5 people contacts module.

KPeople offers unified access to our contacts from different sources,
grouping them by person while still exposing all the data.

Furthermore, KPeople will also provide facilities to integrate the data
provided in user interfaces by providing QML and Qt Widgets components.

The sources are plugin-based, allowing to easily extend the contacts
collection.

%files
%{_kde5_datadir}/kf5/kpeople/dummy_avatar.png
%{_kde5_servicetypes}/kpeople_data_source.desktop
%{_kde5_servicetypes}/kpeople_plugin.desktop
%{_kde5_servicetypes}/persondetailsplugin.desktop

#----------------------------------------------------------------------------

%package i18n
Summary:	KPeople translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
KPeople translations.

%files i18n -f libkpeople5.lang

#----------------------------------------------------------------------------

%define qmlkf5people %mklibname kf5people-qml

%package -n %{qmlkf5people}
Summary:	QML plugin for KDE Frameworks 5 KPeople
Group:		System/Libraries
Provides:	kf5people-qml = %{EVRD}

%description -n %{qmlkf5people}
QML plugin for KDE Frameworks 5 KPeople.

%files -n %{qmlkf5people}
%dir %{_kde5_qmldir}/org/kde/people/
%{_kde5_qmldir}/org/kde/people/*

#----------------------------------------------------------------------------

%define kf5people_major 5
%define libkf5people %mklibname kf5people %{kf5people_major}

%package -n %{libkf5people}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name}
Requires:	%{name}-i18n
Requires:	%{qmlkf5people}

%description -n %{libkf5people}
KDE Frameworks 5 people contacts shared library.

%files -n %{libkf5people}
%{_kde5_libdir}/libKF5People.so.%{kf5people_major}*

#----------------------------------------------------------------------------

%define kf5peoplebackend_major 5
%define libkf5peoplebackend %mklibname kf5peoplebackend %{kf5peoplebackend_major}

%package -n %{libkf5peoplebackend}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name}
Requires:	%{name}-i18n
Requires:	%{qmlkf5people}

%description -n %{libkf5peoplebackend}
KDE Frameworks 5 people contacts shared library.

%files -n %{libkf5peoplebackend}
%{_kde5_libdir}/libKF5PeopleBackend.so.%{kf5peoplebackend_major}*

#----------------------------------------------------------------------------

%define kf5peoplewidgets_major 5
%define libkf5peoplewidgets %mklibname kf5peoplewidgets %{kf5peoplewidgets_major}

%package -n %{libkf5peoplewidgets}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name}
Requires:	%{name}-i18n
Requires:	%{qmlkf5people}

%description -n %{libkf5peoplewidgets}
KDE Frameworks 5 people contacts shared library.

%files -n %{libkf5peoplewidgets}
%{_kde5_libdir}/libKF5PeopleWidgets.so.%{kf5peoplewidgets_major}*

#----------------------------------------------------------------------------

%define devkf5people %mklibname kf5people -d

%package -n %{devkf5people}
Summary:	Development files for KDE Frameworks 5 people contacts module
Group:		Development/KDE and Qt
Requires:	%{libkf5people} = %{EVRD}
Requires:	%{libkf5peoplebackend} = %{EVRD}
Requires:	%{libkf5peoplewidgets} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	kf5people-devel = %{version}

%description -n %{devkf5people}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf5people}
%{_kde5_includedir}/KF5/KPeople
%{_kde5_libdir}/cmake/KF5People
%{_kde5_libdir}/libKF5People.so
%{_kde5_libdir}/libKF5PeopleBackend.so
%{_kde5_libdir}/libKF5PeopleWidgets.so
%{_kde5_mkspecsdir}/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

for oldlang in po/*/*.po
do
    newlang=`echo $oldlang | sed s,\.po,5\.po,g`
    mv $oldlang $newlang
done

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

%find_lang libkpeople5
