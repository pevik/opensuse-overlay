Summary:        Screen capture utility using imlib2 library
License:        MIT and LGPL-2.0+
Group:          Productivity/Graphics/Viewers
Name:           scrot
Version:        0.8
Release:        0
Source:         http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Url:            http://linuxbrit.co.uk/software/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  giblib-devel
BuildRequires:  imlib2-devel

%description
scrot (SCReen shOT) is a simple commandline screen capture utility that 
uses imlib2 to grab and save images. Multiple image formats are supported 
through imlib2's dynamic saver modules.

%prep
%setup -q

%build
%configure
%__make %{?_smp_flags} 

%install
%__make DESTDIR="%{buildroot}" install
%__rm -r %{buildroot}/usr/doc

%files
%defattr(-, root, root)
%doc ChangeLog
%{_bindir}/scrot
%doc %{_mandir}/man1/scrot.1%{ext_man}

%changelog
