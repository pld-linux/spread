#
Summary:	Toolkit that provides a high performance messaging service that is resilient to faults across external or internal networks
Name:		spread
Version:	3.17.3
Release:	0.1
Epoch:		0
License:	BSD-like
Group:		Development
Source0:	http://www.cnds.jhu.edu/download/download_spread.cgi/%{name}-src-%{version}.tar.gz
# Source0-md5:	2eec25b5adc96fd840aa251e44325f9f
# check the license first before removing line below
NoSource:	0
URL:		http://www.spread.com/
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spread is a toolkit that provides a high performance messaging service that
is resilient to faults across external or internal networks. Spread
functions as a unified message bus for distributed applications, and
provides highly tuned application-level multicast and group communication
support. Spread services range from reliable message passing to fully
ordered messages with delivery guarantees, even in case of computer
failures and network partitions. Spread is designed to encapsulate the
challenging aspects of asynchronous networks and enable the construction of
scalable distributed applications, allowing application builders to focus
on the differentiating components of their application. 

%package libs
Summary:	Spread library
Group:		Libraries

%description libs
Spread library.

%package devel
Summary:	Header files for Spread library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Spread library.

%package static
Summary:	Static Spread library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Spread library.

%prep
%setup	-q	-n %{name}-src-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO docs/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
