Summary:	A netload plugin for the Xfce panel
Summary(pl):	Wtyczka obci±¿anie sieci dla panelu Xfce
Name:		xfce4-netload-plugin
Version:	0.3.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	8d8c062ff97bb79494604eea6cbac6ff
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
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
