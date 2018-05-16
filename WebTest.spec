#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebTest
Version  : 2.0.29
Release  : 39
URL      : https://pypi.python.org/packages/94/de/8f94738be649997da99c47b104aa3c3984ecec51a1d8153ed09638253d56/WebTest-2.0.29.tar.gz
Source0  : https://pypi.python.org/packages/94/de/8f94738be649997da99c47b104aa3c3984ecec51a1d8153ed09638253d56/WebTest-2.0.29.tar.gz
Summary  : Helper to test WSGI applications
Group    : Development/Tools
License  : MIT
Requires: WebTest-python3
Requires: WebTest-python
Requires: PasteDeploy
Requires: WSGIProxy2
Requires: WebOb
Requires: beautifulsoup4
Requires: coverage
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
BuildRequires : coverage
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyquery
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
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

%package python
Summary: python components for the WebTest package.
Group: Default
Requires: WebTest-python3
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
%setup -q -n WebTest-2.0.29
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522283054
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
