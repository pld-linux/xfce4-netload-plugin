Summary:	A netload plugin for the Xfce panel
Summary(pl):	Wtyczka obci±¿anie sieci dla panelu Xfce
Name:		xfce4-netload-plugin
Version:	0.2.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	bd65ff55a743d98cc8f20fc9596b5a1b
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99.2
Requires:	xfce4-panel >= 3.99.2
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
