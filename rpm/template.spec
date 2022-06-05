%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-system-modes
Version:        0.9.0
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS system_modes package

License:        Apache License 2.0
URL:            https://micro.ros.org/docs/concepts/client_library/lifecycle_and_system_modes/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-builtin-interfaces
Requires:       ros-galactic-launch-ros
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-lifecycle
Requires:       ros-galactic-system-modes-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-builtin-interfaces
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-lifecycle
BuildRequires:  ros-galactic-system-modes-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-galactic-ament-cmake-cppcheck
BuildRequires:  ros-galactic-ament-cmake-cpplint
BuildRequires:  ros-galactic-ament-cmake-flake8
BuildRequires:  ros-galactic-ament-cmake-gmock
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-ament-cmake-pep257
BuildRequires:  ros-galactic-ament-cmake-uncrustify
BuildRequires:  ros-galactic-ament-index-python
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-launch-testing-ament-cmake
BuildRequires:  ros-galactic-launch-testing-ros
BuildRequires:  ros-galactic-ros2run
%endif

%description
The system modes concept assumes that a robotics system is built from components
with a lifecycle. It adds a notion of (sub-)systems, hiararchically grouping
these nodes, as well as a notion of modes that determine the configuration of
these nodes and (sub-)systems in terms of their parameter values.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Sun Jun 05 2022 Arne Nordmann <arne.nordmann@bosch.com> - 0.9.0-3
- Autogenerated by Bloom

* Sun Jun 05 2022 Arne Nordmann <arne.nordmann@bosch.com> - 0.9.0-2
- Autogenerated by Bloom

* Wed Jul 21 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.9.0-1
- Autogenerated by Bloom

* Tue Jun 08 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.8.0-1
- Autogenerated by Bloom

* Mon May 17 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.7.1-3
- Autogenerated by Bloom

* Tue May 04 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.7.1-2
- Autogenerated by Bloom

* Thu Apr 29 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.7.1-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.6.0-2
- Autogenerated by Bloom

* Fri Apr 09 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.6.0-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.5.0-2
- Autogenerated by Bloom

* Thu Mar 18 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.5.0-1
- Autogenerated by Bloom

* Fri Mar 12 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.4.2-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.4.2-1
- Autogenerated by Bloom
