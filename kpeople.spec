%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Frameworks 5 people contacts module
Name:		kpeople
Version:	5.9.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)

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

%files i18n -f libkpeople.lang

#----------------------------------------------------------------------------

%define qmlKF5People %mklibname KF5People-qml

%package -n %{qmlKF5People}
Summary:	QML plugin for KDE Frameworks 5 KPeople
Group:		System/Libraries
Provides:	KF5People-qml = %{EVRD}

%description -n %{qmlKF5People}
QML plugin for KDE Frameworks 5 KPeople.

%files -n %{qmlKF5People}
%dir %{_kde5_qmldir}/org/kde/people/
%{_kde5_qmldir}/org/kde/people/*

#----------------------------------------------------------------------------

%define KF5People_major 5
%define libKF5People %mklibname KF5People %{KF5People_major}

%package -n %{libKF5People}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{name}-i18n = %{EVRD}
Requires:	%{qmlKF5People} = %{EVRD}

%description -n %{libKF5People}
KDE Frameworks 5 people contacts shared library.

%files -n %{libKF5People}
%{_kde5_libdir}/libKF5People.so.%{KF5People_major}*

#----------------------------------------------------------------------------

%define KF5PeopleBackend_major 5
%define libKF5PeopleBackend %mklibname KF5PeopleBackend %{KF5PeopleBackend_major}

%package -n %{libKF5PeopleBackend}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{name}-i18n = %{EVRD}
Requires:	%{qmlKF5People} = %{EVRD}

%description -n %{libKF5PeopleBackend}
KDE Frameworks 5 people contacts shared library.

%files -n %{libKF5PeopleBackend}
%{_kde5_libdir}/libKF5PeopleBackend.so.%{KF5PeopleBackend_major}*

#----------------------------------------------------------------------------

%define KF5PeopleWidgets_major 5
%define libKF5PeopleWidgets %mklibname KF5PeopleWidgets %{KF5PeopleWidgets_major}

%package -n %{libKF5PeopleWidgets}
Summary:	KDE Frameworks 5 people contacts shared library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{name}-i18n = %{EVRD}
Requires:	%{qmlKF5People} = %{EVRD}

%description -n %{libKF5PeopleWidgets}
KDE Frameworks 5 people contacts shared library.

%files -n %{libKF5PeopleWidgets}
%{_kde5_libdir}/libKF5PeopleWidgets.so.%{KF5PeopleWidgets_major}*

#----------------------------------------------------------------------------

%define devKF5People %mklibname KF5People -d

%package -n %{devKF5People}
Summary:	Development files for KDE Frameworks 5 people contacts module
Group:		Development/KDE and Qt
Requires:	%{libKF5People} = %{EVRD}
Requires:	%{libKF5PeopleBackend} = %{EVRD}
Requires:	%{libKF5PeopleWidgets} = %{EVRD}

%description -n %{devKF5People}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devKF5People}
%{_kde5_includedir}/KF5/KPeople
%{_kde5_libdir}/cmake/KF5People
%{_kde5_libdir}/libKF5People.so
%{_kde5_libdir}/libKF5PeopleBackend.so
%{_kde5_libdir}/libKF5PeopleWidgets.so
%{_kde5_mkspecsdir}/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkpeople
