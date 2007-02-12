
#
# todo:
# - add spread user and group or maybe run it as nobody?
# - change default config file: logging, etc.
#

Summary:	High performance messaging service toolkit resilient to faults across networks
Summary(pl.UTF-8):   Zestaw narządzi do wydajnej komunikacji odpornej na defekty sieci
Name:		spread
Version:	3.17.3
Release:	0.3
Epoch:		0
License:	Spread Open Source License
Group:		Development
# from http://www.spread.org/download.html
# (No direct URL)
Source0:	%{name}-src-%{version}.tar.gz
# Source0-md5:	2eec25b5adc96fd840aa251e44325f9f
Patch0:		%{name}-soname.patch
URL:		http://www.spread.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spread is a toolkit that provides a high performance messaging service
that is resilient to faults across external or internal networks.
Spread functions as a unified message bus for distributed
applications, and provides highly tuned application-level multicast
and group communication support. Spread services range from reliable
message passing to fully ordered messages with delivery guarantees,
even in case of computer failures and network partitions. Spread is
designed to encapsulate the challenging aspects of asynchronous
networks and enable the construction of scalable distributed
applications, allowing application builders to focus on the
differentiating components of their application.

%description -l pl.UTF-8
Spread to zestaw narzędzi zapewniających wysoko wydajną komunikację
odporną na defekty zarówno zewnętrznych, jak i wewnętrznych sieci.
Spread funkcjonuje jako ujednolicony kanał komunikacji dla
rozproszonych aplikacji i dostarcza dobrze dostrojoną obsługę
multicastów i komunikacji grupowej na poziomie aplikacji. Usługi
Spreada obejmują zakres od niezawodnego przekazywania wiadomości do
całkowicie uporządkowanych wiadomości z gwarancją dostarczenia, nawet
w przypadku awarii komputera czy podziałów sieci. Spread jest
zaprojektowany do opakowywania wyzywających aspektów sieci
asynchronicznych i umożliwienia tworzenia skalowanych, rozproszonych
aplikacji, umożliwiając twórcom aplikacji skupienie się na różniących
się komponentach ich aplikacji.

%package libs
Summary:	Spread client library
Summary(pl.UTF-8):   Biblioteka kliencka Spreada
Group:		Libraries

%description libs
Spread client library.

%description libs -l pl.UTF-8
Biblioteka kliencka Spreada.

%package devel
Summary:	Header files for Spread client library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki klienckiej Spreada
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Spread client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej Spreada.

%package static
Summary:	Static Spread client library
Summary(pl.UTF-8):   Statyczna biblioteka kliencka Spreada
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Spread client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka Spreada.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO *.txt Changelog
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
