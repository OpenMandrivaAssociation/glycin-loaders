%define _empty_manifest_terminate_build 0
%global tarball_version %%(echo %{version} | tr '~' '.')

%define major 0

%define libname %mklibname glycin
%define devname %mklibname -d glycin
%define girname %mklibname glycin-gir
 
Name:           glycin-loaders
Version:        1.2.3
Release:        1
Summary:        Sandboxed image rendering
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin/%{tarball_version}/glycin-%{tarball_version}.tar.xz
#Source2:        vendor.tar.xz
#Source3:        cargo_config

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(harfbuzz-gobject)
BuildRequires:  pkgconfig(lcms2)
#BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

Requires:	%{libname} = %{EVRD}

%description
Sandboxed and extendable image decoding.

%package -n %{libname}
Summary:        Shared library for %{name}
Requires:	%{girname} = %{EVRD}

%description -n %{libname}
This package contains the shared library files.

%package -n %{girname}
Summary:        Introspection file for %{name}

%description -n %{girname}
This package contains introspection file for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Requires: %{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.
 
%prep
%autosetup -n glycin-%{version} -p1 
#-a2
#mkdir .cargo
#cp %{SOURCE3} .cargo/config

%build
%meson \
  -Dglycin-loaders=true \
  -Dlibglycin=true \
  -Dintrospection=true \
  -Dvapi=true \
  -Dloaders=glycin-image-rs,glycin-jxl,glycin-svg \
  -Dtest_skip_install=true

%meson_build

%install
%meson_install

%files
%license LICENSE LICENSE-LGPL-2.1 LICENSE-MPL-2.0
%doc NEWS README.md
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/

%files -n %{libname}
%{_libdir}/libglycin-1.so.%{major}
%{_libdir}/libglycin-gtk4-1.so.%{major}

%files -n %{girname}
%{_libdir}/girepository-1.0/Gly-1.typelib
%{_libdir}/girepository-1.0/GlyGtk4-1.typelib

%files -n %{devname}
%{_libdir}/libglycin-1.so
%{_libdir}/libglycin-gtk4-1.so
%{_libdir}/pkgconfig/glycin-1.pc
%{_libdir}/pkgconfig/glycin-gtk4-1.pc
%{_includedir}/glycin-1/glycin.h
%{_includedir}/glycin-gtk4-1/glycin-gtk4.h
%{_datadir}/gir-1.0/Gly-1.gir
%{_datadir}/gir-1.0/GlyGtk4-1.gir
%{_datadir}/vala/vapi/glycin-1.deps
%{_datadir}/vala/vapi/glycin-1.vapi
%{_datadir}/vala/vapi/glycin-gtk4-1.deps
%{_datadir}/vala/vapi/glycin-gtk4-1.vapi

 
