
#
# todo:
# - add spread user and group or maybe run it as nobody?
# - change default config file: logging, etc.
#

Summary:	High performance messaging service toolkit resilient to faults across networks
Summary(pl):	Zestaw narz±dzi do wydajnej komunikacji odpornej na defekty sieci
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

%description -l pl
Spread to zestaw narzêdzi zapewniaj±cych wysoko wydajn± komunikacjê
odporn± na defekty zarówno zewnêtrznych, jak i wewnêtrznych sieci.
Spread funkcjonuje jako ujednolicony kana³ komunikacji dla
rozproszonych aplikacji i dostarcza dobrze dostrojon± obs³ugê
multicastów i komunikacji grupowej na poziomie aplikacji. Us³ugi
Spreada obejmuj± zakres od niezawodnego przekazywania wiadomo¶ci do
ca³kowicie uporz±dkowanych wiadomo¶ci z gwarancj± dostarczenia, nawet
w przypadku awarii komputera czy podzia³ów sieci. Spread jest
zaprojektowany do opakowywania wyzywaj±cych aspektów sieci
asynchronicznych i umo¿liwienia tworzenia skalowanych, rozproszonych
aplikacji, umo¿liwiaj±c twórcom aplikacji skupienie siê na ró¿ni±cych
siê komponentach ich aplikacji.

%package libs
Summary:	Spread client library
Summary(pl):	Biblioteka kliencka Spreada
Group:		Libraries

%description libs
Spread client library.

%description libs -l pl
Biblioteka kliencka Spreada.

%package devel
Summary:	Header files for Spread client library
Summary(pl):	Pliki nag³ówkowe biblioteki klienckiej Spreada
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Spread client library.

%description devel -l pl
Pliki nag³ówkowe biblioteki klienckiej Spreada.

%package static
Summary:	Static Spread client library
Summary(pl):	Statyczna biblioteka kliencka Spreada
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Spread client library.

%description static -l pl
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
