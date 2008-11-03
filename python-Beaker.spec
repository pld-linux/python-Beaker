%define		fname	Beaker
Summary:	Session (and caching soon) WSGI Middleware
Summary(pl.UTF-8):	Middleware WSGI obsługi sesji (i wkrótce pamięci podręcznej)
Name:		python-%{fname}
Version:	0.9.2
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/B/Beaker/%{fname}-%{version}.tar.gz
# Source0-md5:	034e478bc4b91c1a38a0e25d42210d31
URL:		http://beaker.groovie.org/
BuildRequires:	python-setuptools
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
install tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{py_sitescriptdir}/beaker
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
