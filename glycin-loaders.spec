%define _empty_manifest_terminate_build 0
%global tarball_version %%(echo %{version} | tr '~' '.')
 
Name:           glycin-loaders
Version:        0.1.1
Release:        1
Summary:        Sandboxed image rendering
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin-loaders/0.1/glycin-loaders-%{tarball_version}.tar.xz
Source2:        vendor.tar.xz
Source3:        cargo_config
# Fedora-packaged rust-image doesn't have openexr support
#Patch:          0001-Drop-OpenEXR-decoders-since-they-are-not-enabled-in-.patch
# libheif and jxl rust wrappers aren't packaged yet
#Patch:          0002-Disable-JPEG-XL-and-HEIF-loaders-missing-dependencie.patch
# Fedora currently has librsvg 2.57.0-beta.2
#Patch:          0003-Temporarily-downgrade-librsvg-dependency-to-allow-2..patch
 
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
  -Dloaders=glycin-image-rs,glycin-jxl,glycin-svg,glycin-heif \
  -Dtest_skip_install=true

%meson_build

%install
%meson_install

%files
%license LICENSE LICENSE-LGPL-2.1 LICENSE-MPL-2.0
%doc NEWS README.md
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/
 
