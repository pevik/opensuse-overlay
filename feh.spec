Summary:        Fast and Lightweight Image Viewer
License:        MIT and LGPL-2.0+
Group:          Productivity/Graphics/Viewers
Name:           feh
Version:        2.9.3
Release:        0
Source:         https://derf.homelinux.org/projects/feh/feh-%{version}.tar.bz2

# PATCH-FIX-OPENSUSE feh-makefile_optflags.patch https://github.com/derf/feh/issues/71 pascal.bleser@opensuse.org -- pass OPTFLAGS to make instead of hard-coded -O2 -g
Patch1:         feh-makefile_optflags.patch
# PATCH-FIX-UPSTREAM feh-fix_pointer_arithmetics.patch https://github.com/derf/feh/issues/69 pascal.bleser@opensuse.org -- fix compiler warnings on casting pointers as ints
Patch2:         feh-fix_pointer_arithmetics.patch
# PATCH-FIX-OPENSUSE feh-no_date.patch - pascal.bleser@opensuse.org -- avoid injecting the current date into the man page, which causes needless rebuilds
Patch4:         feh-no_date.patch
# PATCH-FIX-UPSTREAM feh-fix_sighandler.patch https://github.com/derf/feh/issues/70 pascal.bleser@opensuse.org -- bad prototype for a sighandler_t and a funky unportable pointer cast
Patch5:         feh-fix_sighandler.patch
Url:            http://feh.finalrewind.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  freetype2-devel
BuildRequires:  giblib-devel
BuildRequires:  imlib2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng16-devel
BuildRequires:  xorg-x11-devel

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%setup -q
%patch1 -p1
%patch2
%patch4
%patch5

%build
%__make %{?_smp_flags} \
    curl=0 \
    exif=0 \
    xinerama=1 \
    debug=0 \
    PREFIX="%{_prefix}" \
    OPTFLAGS="%{optflags} -Wall -Wextra"

%install
%__make \
    PREFIX="%{buildroot}%{_prefix}" \
    install

%__rm -rf "%{buildroot}%{_datadir}/doc"
%__rm -rf "%{buildroot}/usr/share/applications/feh.desktop"

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/feh
%{_bindir}/feh-cam
%{_bindir}/gen-cam-menu
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%doc %{_mandir}/man1/feh.1%{ext_man}
%doc %{_mandir}/man1/feh-cam.1%{ext_man}
%doc %{_mandir}/man1/gen-cam-menu.1%{ext_man}

%changelog
