Name:           xtrlock
Version:	2.3
Release:	1
License:	GPL-3
Summary:	A simplistic screen locking program for X
Url:		http://ftp.debian.org/debian/pool/main/x/xtrlock/
Group:		System/GUI/Other
Source:		http://ftp.debian.org/debian/pool/main/x/xtrlock/%{name}_%{version}.tar.gz
BuildRequires:  imake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simplistic screen locking program for X

%prep
%setup -q

%build
xmkmf
%__make -f Makefile.noimake %{?_smp_mflags} CFLAGS="-DSHADOW_PWD" LDLIBS="-lX11 -lcrypt" xtrlock

%install
%__install -D xtrlock %buildroot/usr/bin/xtrlock
%__install -D xtrlock.man %buildroot%_mandir/man1/xtrlock.1

%files
%defattr(-,root,root)
%doc debian/changelog
%attr(4755,root,root) /usr/bin/xtrlock
%_mandir/man1/*

%changelog

