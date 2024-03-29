#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebTest
Version  : 3.0.0
Release  : 81
URL      : https://files.pythonhosted.org/packages/26/c8/8ffba1782700eb06e9b9169156698c6ba95c05b66cda3fc9e025b6b3b649/WebTest-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/26/c8/8ffba1782700eb06e9b9169156698c6ba95c05b66cda3fc9e025b6b3b649/WebTest-3.0.0.tar.gz
Summary  : Helper to test WSGI applications
Group    : Development/Tools
License  : MIT
Requires: WebTest-license = %{version}-%{release}
Requires: WebTest-python = %{version}-%{release}
Requires: WebTest-python3 = %{version}-%{release}
Requires: WebOb
Requires: beautifulsoup4
Requires: waitress
BuildRequires : PasteDeploy
BuildRequires : WSGIProxy2
BuildRequires : WebOb
BuildRequires : beautifulsoup4
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : pyquery
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : python-mock
BuildRequires : six
BuildRequires : waitress

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
Provides: pypi(webtest)
Requires: pypi(beautifulsoup4)
Requires: pypi(waitress)
Requires: pypi(webob)

%description python3
python3 components for the WebTest package.


%prep
%setup -q -n WebTest-3.0.0
cd %{_builddir}/WebTest-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631501916
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WebTest
cp %{_builddir}/WebTest-3.0.0/license.rst %{buildroot}/usr/share/package-licenses/WebTest/93f88a0f4df0e1130383927f839a05c85d2f675f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WebTest/93f88a0f4df0e1130383927f839a05c85d2f675f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
