# xdotool built for EL10 (Rocky/Alma/RHEL 10), where EPEL 10 has no xdotool package yet.
# Upstream: github.com/jordansissel/xdotool (BSD-3-Clause). The SFA widget uses it to be dragged.
Name:           xdotool
Version:        %{xver}
Release:        1.sfa%{?dist}
Summary:        Fake keyboard/mouse input and window management for X (SFA build)
License:        BSD-3-Clause
URL:            https://github.com/jordansissel/xdotool
Source0:        xdotool-%{version}.tar.gz
%global debug_package %{nil}
BuildRequires:  gcc, make, libX11-devel, libXtst-devel, libXinerama-devel, libxkbcommon-devel, perl-podlators

%description
Command line X11 automation: search windows, read the mouse position, move windows.

%prep
%autosetup -n xdotool-%{version}

%build
make %{?_smp_mflags} WITHOUT_RPATH_FIX=1 CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} INSTALLLIB=%{_libdir} INSTALLMAN=%{_mandir} WITHOUT_RPATH_FIX=1
rm -f %{buildroot}%{_libdir}/libxdo.so %{buildroot}%{_includedir}/xdo.h
rm -rf %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_mandir}
chmod 755 %{buildroot}%{_libdir}/libxdo.so.*

%files
%license COPYRIGHT
%{_bindir}/xdotool
%{_libdir}/libxdo.so.*

%changelog
* Fri Oct 09 2026 SFA - %{xver}-1.sfa
- Build for EL10, where EPEL has no xdotool
