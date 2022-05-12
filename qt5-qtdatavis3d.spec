#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtdatavis3d
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Data Visualization library
Summary(pl.UTF-8):	Biblioteka Qt5 Data Visualization
Name:		qt5-%{orgname}
Version:	5.15.4
Release:	1
License:	LGPL v3 or GPL v2+ or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	459fe832158127f8a1acf4a9acdab674
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
BuildRequires:	qt5-doc-common >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Data Visualization library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 Data Visualization.

%package -n Qt5DataVisualization
Summary:	The Qt5 DataVisualization library
Summary(pl.UTF-8):	Biblioteka Qt5 DataVisualization
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}

%description -n Qt5DataVisualization
Qt5 DataVisualization library.

%description -n Qt5DataVisualization -l pl.UTF-8
Biblioteka Qt5 DataVisualization.

%package -n Qt5DataVisualization-devel
Summary:	Qt5 DataVisualization - development files
Summary(pl.UTF-8):	Biblioteka Qt5 DataVisualization - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5DataVisualization = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}

%description -n Qt5DataVisualization-devel
Qt5 DataVisualization - development files.

%description -n Qt5DataVisualization-devel -l pl.UTF-8
Biblioteka Qt5 DataVisualization - pliki programistyczne.

%package doc
Summary:	Qt5 DataVisualization documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 DataVisualization w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 DataVisualization documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 DataVisualization w formacie HTML.

%package doc-qch
Summary:	Qt5 DataVisualization documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 DataVisualization w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 DataVisualization documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 DataVisualization w formacie QCH.

%package examples
Summary:	Qt5 DataVisualization examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 DataVisualization
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 DataVisualization examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 DataVisualization.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5}
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# remove compiled examples (package only sources)
for d in $RPM_BUILD_ROOT%{_examplesdir}/qt5/datavisualization/* ; do
	[ -f "$d/$(basename $d)" ] && %{__rm} "$d/$(basename $d)"
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5DataVisualization -p /sbin/ldconfig
%postun	-n Qt5DataVisualization -p /sbin/ldconfig

%files -n Qt5DataVisualization
%defattr(644,root,root,755)
%doc README dist/changes-*
# R: Qt5Core Qt5Gui
%attr(755,root,root) %{_libdir}/libQt5DataVisualization.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5DataVisualization.so.5
%dir %{qt5dir}/qml/QtDataVisualization
# R: Qt5Core Qt5Gui Qt5Qml Qt5Quick
%attr(755,root,root) %{qt5dir}/qml/QtDataVisualization/libdatavisualizationqml2.so
%{qt5dir}/qml/QtDataVisualization/plugins.qmltypes
%{qt5dir}/qml/QtDataVisualization/qmldir
%{qt5dir}/qml/QtDataVisualization/designer

%files -n Qt5DataVisualization-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5DataVisualization.so
%{_libdir}/libQt5DataVisualization.prl
%{_includedir}/qt5/QtDataVisualization
%{_pkgconfigdir}/Qt5DataVisualization.pc
%{_libdir}/cmake/Qt5DataVisualization
%{qt5dir}/mkspecs/modules/qt_lib_datavisualization.pri
%{qt5dir}/mkspecs/modules/qt_lib_datavisualization_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtdatavisualization

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtdatavis3d.qch
%endif

%files examples
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%{_examplesdir}/qt5/datavisualization
