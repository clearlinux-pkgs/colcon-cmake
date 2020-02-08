#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-cmake
Version  : 0.2.18
Release  : 23
URL      : https://files.pythonhosted.org/packages/16/6b/c285433457f9c13c8796d4fad1766c7accb964ef1c8670b99256c701f46d/colcon-cmake-0.2.18.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/6b/c285433457f9c13c8796d4fad1766c7accb964ef1c8670b99256c701f46d/colcon-cmake-0.2.18.tar.gz
Summary  : Extension for colcon to support CMake packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-cmake-python = %{version}-%{release}
Requires: colcon-cmake-python3 = %{version}-%{release}
Requires: colcon-core
Requires: colcon-library-path
Requires: colcon-test-result
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core
BuildRequires : colcon-library-path
BuildRequires : colcon-test-result

%description
colcon-cmake
============
An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to support `CMake <https://cmake.org>`_ projects.

%package python
Summary: python components for the colcon-cmake package.
Group: Default
Requires: colcon-cmake-python3 = %{version}-%{release}

%description python
python components for the colcon-cmake package.


%package python3
Summary: python3 components for the colcon-cmake package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-cmake package.


%prep
%setup -q -n colcon-cmake-0.2.18
cd %{_builddir}/colcon-cmake-0.2.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581185305
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
