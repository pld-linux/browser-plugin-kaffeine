%define		_realname	kaffeine-mozilla
%define		_pluginname	kaffeineplugin
Summary:	Kaffeine player for webbrowsers
Summary(pl.UTF-8):	Odtwarzacz Kaffeine dla przeglądarek internetowych
Name:		browser-plugin-kaffeine
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kaffeine/%{_realname}-%{version}.tar.bz2
# Source0-md5:	c7bb24cbd20fdfeffbb0da452533cac4
Patch0:		%{name}-destdir.patch
URL:		http://kaffeine.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.236
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	browser-plugins >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package delivers a video/audio player plugin for web browsers.

Supported browsers: %{browsers}.

%description -l pl.UTF-8
Ta paczka dostarcza wtyczki odtwarzacza wideo/audio dla przeglądarek
internetowych.

Obsługiwane przeglądarki: %{browsers}.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--prefix=%{_browserpluginsdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/kaffeineplugin.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_browserpluginsdir}/%{_pluginname}.so
