#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebTest
Version  : 2.0.32
Release  : 49
URL      : https://files.pythonhosted.org/packages/27/9f/9e74449d272ffbef4fb3012e6dbc53c0b24822d545e7a33a342f80131e59/WebTest-2.0.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/9f/9e74449d272ffbef4fb3012e6dbc53c0b24822d545e7a33a342f80131e59/WebTest-2.0.32.tar.gz
Summary  : Helper to test WSGI applications
Group    : Development/Tools
License  : MIT
Requires: WebTest-python3
Requires: WebTest-license
Requires: WebTest-python
Requires: PasteDeploy
Requires: Sphinx
Requires: WSGIProxy2
Requires: WebOb
Requires: beautifulsoup4
Requires: coverage
Requires: docutils
Requires: nose
Requires: pyquery
Requires: python-mock
Requires: six
Requires: waitress
BuildRequires : PasteDeploy
BuildRequires : PasteDeploy-python
BuildRequires : WSGIProxy2
BuildRequires : WebOb
BuildRequires : WebOb-python
BuildRequires : beautifulsoup4
BuildRequires : beautifulsoup4-python
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyquery
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : waitress
BuildRequires : waitress-python
Patch1: 0001-enable-test-require-for-nose-1.3.0.patch

%description
WebTest
        =======
        
        This wraps any WSGI application and makes it easy to send test
        requests to that application, without starting up an HTTP server.
        
        This provides convenient full-stack testing of applications written
        with any WSGI-compatible framework.

%package license
Summary: license components for the WebTest package.
Group: Default

%description license
license components for the WebTest package.


%package python
Summary: python components for the WebTest package.
Group: Default
Requires: WebTest-python3 = %{version}-%{release}
Provides: webtest-python

%description python
python components for the WebTest package.


%package python3
Summary: python3 components for the WebTest package.
Group: Default
Requires: python3-core

%description python3
python3 components for the WebTest package.


%prep
%setup -q -n WebTest-2.0.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538748072
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/WebTest
cp docs/license.rst %{buildroot}/usr/share/doc/WebTest/docs_license.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/WebTest/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
