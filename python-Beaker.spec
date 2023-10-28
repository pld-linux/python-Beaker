# TODO
# - rename to python-beaker?
#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

%define		module	Beaker
Summary:	Session (and caching soon) WSGI Middleware
Summary(pl.UTF-8):	Middleware WSGI obsługi sesji (i wkrótce pamięci podręcznej)
Name:		python-%{module}
# keep 1.11.x here for python2 support
Version:	1.11.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/beaker/
Source0:	https://files.pythonhosted.org/packages/source/B/Beaker/%{module}-%{version}.tar.gz
# Source0-md5:	21e1464acaf5358d90133d1e0cc189b6
URL:		https://beaker.readthedocs.io/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography
BuildRequires:	python-funcsigs
BuildRequires:	python-memcached
BuildRequires:	python-mock
BuildRequires:	python-modules-sqlite
BuildRequires:	python-nose
BuildRequires:	python-pycparser = 2.18
BuildRequires:	python-pycryptodome
BuildRequires:	python-pylibmc
BuildRequires:	python-pymongo
BuildRequires:	python-redis
BuildRequires:	python-sqlalchemy
BuildRequires:	python-webtest < 2.0.24
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/beaker
%{py_sitescriptdir}/Beaker-%{version}-py*.egg-info
