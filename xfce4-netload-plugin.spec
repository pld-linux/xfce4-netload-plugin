Summary:	A netload plugin for the Xfce panel
Summary(pl):	Wtyczka obci��anie sieci dla panelu Xfce
Name:		xfce4-netload-plugin
Version:	0.3.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-netload-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	755dcc170fb33274378c7b110cf21f56
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current load of the network interfaces of
your choice in the panel.

%description -l pl
Wtyczka ta wy�wietla aktualne obci��enie wybranych interfejs�w
sieciowych na panelu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang xfce4-netload

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfce4-netload.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
