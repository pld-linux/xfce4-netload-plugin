Summary:	A netload plugin for the Xfce panel
Summary(pl):	Wtyczka obci±¿anie sieci dla panelu Xfce
Name:		xfce4-netload-plugin
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-netload-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	a15ee479089ba7703c5dde33ff439573
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current load of the network interfaces of
your choice in the panel.

%description -l pl
Wtyczka ta wy¶wietla aktualne obci±¿enie wybranych interfejsów
sieciowych na panelu.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-netload-plugin
%{_datadir}/xfce4/panel-plugins/netload.desktop
