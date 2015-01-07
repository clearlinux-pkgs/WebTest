#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebTest
Version  : 2.0.18
Release  : 10
URL      : https://pypi.python.org/packages/source/W/WebTest/WebTest-2.0.18.zip
Source0  : https://pypi.python.org/packages/source/W/WebTest/WebTest-2.0.18.zip
Summary  : Helper to test WSGI applications
Group    : Development/Tools
License  : MIT
Requires: WebTest-python
BuildRequires : PasteDeploy
BuildRequires : WSGIProxy2
BuildRequires : WebOb
BuildRequires : beautifulsoup4
BuildRequires : coverage
BuildRequires : cssselect-python
BuildRequires : funcsigs-python
BuildRequires : lxml-python
BuildRequires : nose
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
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : waitress
Patch1: 0001-enable-test-require-for-nose-1.3.0.patch

%description
=======
WebTest
=======
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

%package python
Summary: python components for the WebTest package.
Group: Default
Provides: webtest-python

%description python
python components for the WebTest package.


%prep
%setup -q -n WebTest-2.0.18
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
