Name:           giblib
Version:        1.2.4
Release:        0
Summary:        Giblib is a utility library.
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://linuxbrit.co.uk/giblib/
Source0:        http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Source90:       giblib-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       freetype2
Requires:       imlib2 >= 1.2.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype2-devel
BuildRequires:  glibc-devel
BuildRequires:  imlib2-devel >= 1.2.0
BuildRequires:  libtool
BuildRequires:  xorg-x11-devel

%description
giblib is a utility library. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2.

%package devel
Summary:        giblib development files.
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
giblib development files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make \
	DESTDIR=%{buildroot} \
	LIBDIR=%{buildroot}%{_libdir} \
	install%{?!debugrpm:-strip}

rm -rf %{buildroot}%{_prefix}/doc 

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README AUTHORS ChangeLog TODO COPYING NEWS
%{_libdir}/libgiblib.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/giblib-config
%{_libdir}/libgiblib.a
%{_libdir}/libgiblib.la
%{_libdir}/libgiblib.so
%{_libdir}/pkgconfig/giblib.pc
%dir %{_includedir}/giblib
%{_includedir}/giblib/gib*.h

%changelog
