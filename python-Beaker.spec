%define		fname	Beaker
Summary:	Session (and caching soon) WSGI Middleware
Summary(pl):	Middleware WSGI do obs�ugi sesji (i wkr�tce pami�ci podr�cznej)
Name:		python-%{fname}
Version:	0.6.1
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/B/Beaker/%{fname}-%{version}.tar.gz
# Source0-md5:   58683737c7ebf54d9903ff849247cc3b
URL:		http://beaker.groovie.org/
BuildRequires:	python-setuptools
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
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

%description -l pl
Beaker to proste middleware WSGI do u�ywania API Myghty Container.

MythtyUtils zawiera bardzo mocne API Container do przechowywania
danych przy u�yciu r�nych backend�w. Beaker u�ywa tych API do
implementacji og�lnych wrapper�w aplikacji WWW, takich jak sesje czy
pami�� podr�czna wewn�trz middleware WSGI. Aktualnie zaimplementowane
jest jedynie middleware dla sesji, ale wkr�tce b�dzie wi�cej.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/beaker
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
