%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-launch-system-modes
Version:        0.9.0
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS launch_system_modes package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python3
Requires:       python3-PyYAML
Requires:       ros-rolling-ament-index-python
Requires:       ros-rolling-launch
Requires:       ros-rolling-osrf-pycommon
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-system-modes-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3
BuildRequires:  python3-PyYAML
BuildRequires:  ros-rolling-ament-index-python
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-osrf-pycommon
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-system-modes-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python3-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
%endif

%description
System modes specific extensions to the launch tool, i.e. launch actions,
events, and event handlers for system modes.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Jun 20 2023 Arne Nordmann <arne.nordmann@de.bosch.com> - 0.9.0-4
- Autogenerated by Bloom

