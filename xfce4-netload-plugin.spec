Summary:	A netload plugin for the XFce panel
Summary(pl):	Wtyczka obci±¿anie sieci dla panela XFce
Name:		xfce4-netload-plugin
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	48f7ceea5756b25e2a6476fa9fe8327c
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99
Requires:	xfce4-panel >= 3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current load of the network interfaces of your
choice in the panel.

%description -l pl
Wtyczka ta wy¶wietla aktualne obci±¿enie wybranych interfejsów sieciowych
na panelu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.{a,la}

%find_lang xfce4-netload

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfce4-netload.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
