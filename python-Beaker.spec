# TODO
# - rename to python-beaker to conform to pld python package naming
%define		module	Beaker
Summary:	Session (and caching soon) WSGI Middleware
Summary(pl.UTF-8):	Middleware WSGI obsługi sesji (i wkrótce pamięci podręcznej)
Name:		python-%{module}
Version:	1.6.4
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/B/Beaker/%{module}-%{version}.tar.gz
# Source0-md5:	c2e102870ed4c53104dec48ceadf8e9d
URL:		http://beaker.rtfd.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beaker is a simple WSGI middleware to use the Myghty Container API.

MyghtyUtils contains a very robust Container API for storing data
using various backends. Beaker uses those APIs to implement common web
application wrappers, like sessions and caching, in WSGI middleware.
Currently the only middleware implemented is that for sessions but
more is coming soon.

%description -l pl.UTF-8
Beaker jest prostym middleware WSGI do użytku API Myghty Container.

MythtyUtils zawiera bardzo mocne API Container do przechowywania
danych przy użyciu różnych backendów. Beaker używa tych API do
implementacji ogólnych wrapperów aplikacji WWW, takich jak sesje czy
pamięć podręczna wewnątrz middleware WSGI. Aktualnie zaimplementowane
jest jedynie middleware dla sesji, ale wkrótce będzie więcej.

%prep
%setup -qn %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%dir %{py_sitescriptdir}/beaker
%{py_sitescriptdir}/beaker/*.py[co]
%{py_sitescriptdir}/beaker/crypto
%{py_sitescriptdir}/beaker/ext
%{py_sitescriptdir}/Beaker-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
