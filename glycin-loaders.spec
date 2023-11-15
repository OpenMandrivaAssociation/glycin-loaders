%define _empty_manifest_terminate_build 0
%global tarball_version %%(echo %{version} | tr '~' '.')
 
Name:           glycin-loaders
Version:        0.1.2
Release:        1
Summary:        Sandboxed image rendering
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin-loaders/0.1/glycin-loaders-%{tarball_version}.tar.xz
Source2:        vendor.tar.xz
Source3:        cargo_config

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
#BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libssh2)

 
%description
Sandboxed and extendable image decoding.
 
%prep
%autosetup -p1 -a2
#mkdir .cargo
cp %{SOURCE3} .cargo/config

%build
%meson \
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
 
