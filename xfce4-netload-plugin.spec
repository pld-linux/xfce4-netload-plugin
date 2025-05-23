Summary:	A netload plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka obciążanie sieci dla panelu Xfce
Name:		xfce4-netload-plugin
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-netload-plugin/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	b1c5226d0dac6f942f2747159f11060f
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current load of the network interfaces of
your choice in the panel.

%description -l pl.UTF-8
Wtyczka ta wyświetla aktualne obciążenie wybranych interfejsów
sieciowych na panelu.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/netload.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
