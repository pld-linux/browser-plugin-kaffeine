%define		_realname	kaffeine-mozilla
%define		_pluginname	kaffeineplugin
Summary:	Kaffeine player for webbrowsers
Summary(pl):	Odtwarzacz Kaffeine dla przegl±darek internetowych
Name:		browser-plugin-kaffeine
Version:	0.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kaffeine/%{_realname}-%{version}.tar.bz2
# Source0-md5:	c7bb24cbd20fdfeffbb0da452533cac4
Patch0:		%{name}-destdir.patch
URL:		http://kaffeine.sourceforge.net
BuildRequires:	rpmbuild(macros) >= 1.236
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	browser-plugins(%{_target_base_arch})
Conflicts:	mplayerplug-in
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# directory where you store the plugin
%define		_plugindir	%{_libdir}/browser-plugins

# TODO: galeon and skipstone.
# use macro, otherwise extra LF inserted along with the ifarch
%define	browsers mozilla, mozilla-firefox, konqueror, opera, seamonkey

%description
This package delivers a video/audio player plugin for web browsers.

Supported browsers: %{browsers}.

%description -l pl
Ta paczka dostarcza wtyczki odtwarzacza wideo/audio dla przegl±darek internetowych.

Obs³ugiwane przegl±darki: %{browsers}.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--prefix=%{_libdir}/browser-plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins %{_pluginname}.so

%triggerun -- mozilla-firefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins %{_pluginname}.so

%triggerin -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins %{_pluginname}.so

%triggerun -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins %{_pluginname}.so

%triggerin -- opera
%nsplugin_install -d %{_libdir}/opera/plugins %{_pluginname}.so

%triggerun -- opera
%nsplugin_uninstall -d %{_libdir}/opera/plugins %{_pluginname}.so

%triggerin -- konqueror
%nsplugin_install -d %{_libdir}/kde3/plugins/konqueror %{_pluginname}.so

%triggerun -- konqueror
%nsplugin_uninstall -d %{_libdir}/kde3/plugins/konqueror %{_pluginname}.so

%triggerin -- seamonkey
%nsplugin_install -d %{_libdir}/seamonkey/plugins %{_pluginname}.so

%triggerun -- seamonkey
%nsplugin_uninstall -d %{_libdir}/seamonkey/plugins %{_pluginname}.so

# as rpm removes the old obsoleted package files after the triggers
# are ran, add another trigger to make the links there.
%triggerpostun -- mozilla-firefox-plugin-macromedia-flash
%nsplugin_install -f -d %{_libdir}/mozilla-firefox/plugins libflashplayer.so flashplayer.xpt

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_plugindir}/%{_pluginname}.so
