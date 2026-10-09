# conky built for EL10 (Rocky/Alma/RHEL 10), where EPEL 10 has no conky package yet.
# X11 + Lua + cairo only: exactly what the SFA widget needs. Upstream: github.com/brndnmtthws/conky (GPLv3).
Name:           conky
Version:        %{cver}
Release:        1.sfa%{?dist}
Summary:        Light-weight system monitor for X (SFA build: X11, Lua, cairo)
License:        GPL-3.0-or-later
URL:            https://github.com/brndnmtthws/conky
Source0:        conky-%{version}.tar.gz
%global debug_package %{nil}
BuildRequires:  cmake, gcc-c++, make, gperf, lua-devel, cairo-devel, libX11-devel, libXft-devel, libXdamage-devel
BuildRequires:  libXext-devel, libXfixes-devel, libXinerama-devel, libXi-devel, freetype-devel, fontconfig-devel, libXrender-devel
BuildRequires:  python3, python3-pyyaml, python3-jinja2, git

%description
Conky draws system information on the desktop. This build keeps only the X11 window, Lua
scripting and the cairo bindings, which the SFA monitor widget uses.

%prep
%autosetup -n conky-%{version}

%build
%cmake -DRELEASE=ON -DMAINTAINER_MODE=OFF -DBUILD_X11=ON -DBUILD_WAYLAND=OFF -DBUILD_LUA_CAIRO=ON -DBUILD_LUA_CAIRO_XLIB=ON \
       -DBUILD_LUA_IMLIB2=OFF -DBUILD_LUA_RSVG=OFF -DBUILD_IMLIB2=OFF -DBUILD_CURL=OFF -DBUILD_RSS=OFF \
       -DBUILD_NCURSES=OFF -DBUILD_WLAN=OFF -DBUILD_AUDACIOUS=OFF -DBUILD_MPD=OFF -DBUILD_MOC=OFF \
       -DBUILD_XMMS2=OFF -DBUILD_PULSEAUDIO=OFF -DBUILD_NVIDIA=OFF -DBUILD_DOCS=OFF -DBUILD_EXTRAS=OFF \
       -DBUILD_TESTS=OFF -DBUILD_XINPUT=ON -DBUILD_MOUSE_EVENTS=ON -DBUILD_XDBE=ON -DBUILD_ARGB=ON -DBUILD_XFT=ON
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/conky* %{buildroot}%{_mandir}

%files
%license COPYING
%{_bindir}/conky
%{_libdir}/conky
%{_libdir}/libtcp-portmon.so
%exclude %{_datadir}/applications/conky.desktop
%exclude %{_datadir}/icons

%changelog
* Fri Oct 09 2026 SFA - %{cver}-1.sfa
- X11, Lua and cairo only build for the SFA monitor widget on EL10
