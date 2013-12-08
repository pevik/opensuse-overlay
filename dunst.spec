Name:           dunst
Version:        1.0.0
Release:        0
License:        BSD
Source:         http://www.knopwob.org/public/dunst-release/%{name}-%{version}.tar.bz2
Url:            http://www.knopwob.org/dunst/
Group:          System/GUI/Other
Summary:        customizable and lightweight notification-daemon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  glib2-devel
BuildRequires:  libxdg-basedir-devel
BuildRequires:  pkg-config
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  dbus-1-devel
BuildRequires:  xorg-x11-devel
BuildRequires:	perl

%description
customizable and lightweight notification-daemon

%prep
%setup -q
%__sed -ie "/^CFLAGS/ { 
                        s:-g::
                        s:-O.:: 
                      }" config.mk 
%__sed -ie "/^all:/ s:dunstify::" Makefile


%build
%__make %{?_smp_mflags}

%install
%__make DESTDIR=%{buildroot} PREFIX=/usr install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_usr}/share/dbus-1/services/org.knopwob.dunst.service
%{_usr}/share/dunst/dunstrc

%changelog
