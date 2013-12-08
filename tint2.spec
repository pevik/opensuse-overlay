Name:           tint2
Version:        0.11
Release:        1
License:        GPL v2 or later
Source:         tint2-%{version}.tar.bz2
Patch1:         add-power-now-support.patch
Patch2:         fix_defunct_processes.patch
Url:            http://code.google.com/p/tint2/
Group:          System/GUI/Other
Summary:        A lightweight panel/taskbar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  pkg-config
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  imlib2-devel
BuildRequires:  xorg-x11-devel

%description
A lightweight panel/taskbar

%prep
%setup -q
%patch1
%patch2

%build
cmake -DENABLE_BATTERY=ON -DENABLE_TINT2CONF=OFF -DENABLE_EXAMPLES=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr -DDOCDIR=%{_docdir}/%{name} .
make %{?_smp_mflags}

%install
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS COPYING README*
%dir %{_sysconfdir}/xdg/tint2
%config %{_sysconfdir}/xdg/tint2/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/tint2

%changelog
