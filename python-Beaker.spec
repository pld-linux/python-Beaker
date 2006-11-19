%define 	module	        beaker
%define     fname           Beaker
%define     python_version  2.4
Summary:	Session (and caching soon) WSGI Middleware
Name:		python-%{fname}
Version:	0.6.1
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/B/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:   58683737c7ebf54d9903ff849247cc3b
URL:		http://beaker.groovie.org/
BuildRequires:  python-setuptools
Requires:	python >= %{python_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beaker is a simple WSGI middleware to use the Myghty Container API

MyghtyUtils contains a very robust Container API for storing data using
various backend. Beakeruses those APIs to implement common web application
wrappers, like sessions and caching, in WSGI middleware. Currently the only
middleware implemented is that for sessions but more is coming soon.

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
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-py%{python_version}.egg-info
