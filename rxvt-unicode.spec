Name:           rxvt-unicode
Version:        9.19
Release:        0
License:        GPL-2
Group:          System/X11/Terminals
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
BuildRequires:  ncurses-devel
BuildRequires:  xorg-x11-devel
Requires:       terminfo-base
%requires_eq    perl
Url:            http://software.schmorp.de/#rxvt-unicode
Source:         http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Patch0:         rxvt-unicode-9.14-CVE-2008-1142-DISPLAY.patch
Patch1:         rxvt-unicode-9.06-case-insensitive-fs.patch
Patch2:	        rxvt-unicode-9.15-xsubpp.patch	
Patch3:		rxvt-unicode-9.19-fading.patch
Patch4:		rxvt-unicode-9.06-no-urgency-if-focused.diff
Patch5:		rxvt-unicode-9.06-popups-hangs.patch
Patch6:	 	rxvt-unicode-9.05_no-MOTIF-WM-INFO.patch	
Patch7:		rxvt-unicode-9.14-clear.patch
Patch8:		rxvt-unicode-9.06-font-width.patch
Summary:        Rxvt clone with xft and unicode support

%description
rxvt-unicode is a clone of the well-known terminal emulator rxvt,
modified to store text in Unicode (either UCS-2 or UCS-4) and to use
locale-correct input and output. It also supports mixing multiple fonts
at the same time, including Xft fonts.

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1
#%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
find -type d -name CVS -print0 | xargs -r0 %__rm -r

%build
patch -p1 < doc/wcwidth.patch
export CFLAGS="%{optflags} -fno-strict-aliasing -Wno-unused"
export CXXFLAGS="$CFLAGS"

%configure --enable-256-color \
    --disable-warnings \
    --enable-unicode3 \
    --enable-combining \
    --enable-xft \
    --enable-font-styles \
    --enable-pixbuf \
    --disable-transparency \
    --enable-fading \
    --enable-startup-notification \
    --enable-next-scroll \
    --enable-rxvt-scroll \
    --enable-xterm-scroll \
    --enable-perl \
    --enable-xim \
    --enable-iso14755 \
    --enable-keepscrolling \
    --enable-selectionscrolling \
    --disable-mousewheel \
    --enable-slipwheeling \
    --disable-smart-resize \
    --disable-text-blink \
    --enable-pointer-blank \
    --enable-utmp \
    --enable-wtmp \
    --enable-lastlog \
    --with-codesets=all \
    --with-terminfo=/usr/share/terminfo

%__make %{?_smp_mflags}

%makeinstall

%clean
%{__rm} -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc Changes README* doc/README* doc/changes.txt
%doc doc/etc
%{_bindir}/urxvt*
#%exclude /usr/share/terminfo/r/%{name}
#%exclude /usr/share/terminfo/r/rxvt-unicode-256color
%{_mandir}/man1/urxvt*.1
%{_mandir}/man3/urxvt*.3
%{_mandir}/man7/urxvt*.7
%dir %{_libdir}/urxvt/
%dir %{_libdir}/urxvt/perl
%{_libdir}/urxvt/urxvt.pm
%{_libdir}/urxvt/perl/digital-clock
%{_libdir}/urxvt/perl/example-refresh-hooks
%{_libdir}/urxvt/perl/selection
%{_libdir}/urxvt/perl/block-graphics-to-ascii
%{_libdir}/urxvt/perl/matcher
%{_libdir}/urxvt/perl/option-popup
%{_libdir}/urxvt/perl/searchable-scrollback
%{_libdir}/urxvt/perl/selection-autotransform
%{_libdir}/urxvt/perl/selection-popup
%{_libdir}/urxvt/perl/urxvt-popup
%{_libdir}/urxvt/perl/selection-pastebin
%{_libdir}/urxvt/perl/readline
%{_libdir}/urxvt/perl/tabbed
%{_libdir}/urxvt/perl/remote-clipboard
%{_libdir}/urxvt/perl/xim-onthespot
%{_libdir}/urxvt/perl/kuake
%{_libdir}/urxvt/perl/macosx-clipboard
%{_libdir}/urxvt/perl/macosx-clipboard-native
%{_libdir}/urxvt/perl/background
%{_libdir}/urxvt/perl/overlay-osc
%{_libdir}/urxvt/perl/clipboard-osc
%{_libdir}/urxvt/perl/confirm-paste
%{_libdir}/urxvt/perl/bell-command
%{_libdir}/urxvt/perl/keysym-list

%changelog
