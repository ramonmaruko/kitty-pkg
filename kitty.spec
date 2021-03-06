%define version_string 0.14.0

%global __python %{__python3}
%global commit 89692064503ccfbb66374a42d63401a96511501f
%global gittag refs/heads/master
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kitty
Version:        %{version_string}
Release:        0.1%{shortcommit}
Summary:        A modern, hack-able, feature full, OpenGL-based terminal emulator

License:        GPLv3
URL:            https://github.com/kovidgoyal/kitty
Source0:        https://github.com/kovidgoyal/kitty/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
ExclusiveArch:      x86_64

BuildRequires: gcc
BuildRequires: python3-devel >= 3.5.0 harfbuzz-devel >= 1.5.0 zlib pkg-config
BuildRequires: libpng-devel freetype-devel fontconfig-devel libXcursor-devel
BuildRequires: libXrandr-devel libXinerama-devel libxkbcommon-x11-devel
BuildRequires: mesa-libGL-devel libXi-devel
# Pip is only used to install python3-sphinx,
# this is probably not the best method
BuildRequires: python3-pip
# Wayland-protocols-devel is probably not used when running on X11
# It's probably better to create 2 packages for X11 and Wayland
BuildRequires: wayland-protocols-devel
# Add (gcc | clang) in the BuildRequires
BuildRequires: dbus-devel

Requires: harfbuzz libpng freetype fontconfig

%description
kitty - A terminal emulator
* Uses OpenGL for rendering, offloads rendering to the GPU for lower system
  load and buttery smooth scrolling. Uses threaded rendering
  to minimize input latency.
* Supports all modern terminal features: graphics (images), Unicode,
  true-color, OpenType ligatures, mouse protocol, focus tracking, bracketed
  paste and so on.
* Supports tiling multiple terminal windows side by side in different layouts
  without needing to use an extra program like tmux
* Can be controlled from scripts or the shell prompt, even over SSH.
* Has a framework for kittens, small terminal programs that can be used to
  extend kitty’s functionality. For example, they are used for Unicode
  input and URL hints.
* Supports startup sessions which allow you to specify the window/tab
  layout, working directories and programs to run on startup.
* Cross-platform support: kitty currently works on Linux and mac OS, but
  because it uses only OpenGL for rendering, it should be trivial to port
  to other platforms.
* Allows you to open the scroll-back buffer in a separate window using
  arbitrary programs of your choice. This is useful for browsing the
  history comfortably in a pager or editor.


%prep
%autosetup -v -n %{name}-%{commit}


%build
pip3 install --user sphinx
python3 setup.py --verbose linux-package --debug --libdir-name %{_lib}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr
cp -r linux-package/* %{buildroot}/usr


%check


%files
%{_bindir}/kitty
%{_libdir}/kitty/*
%{_datadir}/applications/kitty.desktop
%{_datadir}/terminfo/x/xterm-kitty
%{_datadir}/icons/hicolor/256x256/apps/kitty.png
%doc %{_mandir}/man1/kitty.1.gz
%doc CHANGELOG.rst README.asciidoc
%doc %{_docdir}/kitty
%license LICENSE

%changelog
* Thu Apr 11 2019 Ramon Marco Layam Navarro <marco@ramonmarco.codes> - 0.14.0-0.189692064
- Upgrade to pre-release 0.14.0 89692064503ccfbb66374a42d63401a96511501f

* Sat Jan 19 2019 Gerry Agbobada <gagbobada@gmail.com> - 0.13.3-1
- Upgrade to release 0.13.3

* Fri Jan 04 2019 Gerry Agbobada <gagbobada@gmail.com> - 0.13.2-1
- Upgrade to release 0.13.2

* Sun Dec 09 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.13.1-1
- Upgrade to release 0.13.1

* Tue Oct 02 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.12.3-1
- Upgrade to release 0.12.3

* Wed Sep 19 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.12.1-1
- Upgrade to release 0.12.1

* Tue Sep 04 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.12.0-1
- Upgrade to release 0.12.0
- Add dbus-devel to the BuildRequires

* Wed Jul 11 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.3-2
- Add gcc to BuildRequires

* Wed Jul 11 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.3-1
- Upgrade to release 0.11.3

* Mon Jul 9 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.2-2
- Rebuild to use Python 3.7

* Mon Jul 2 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.2-1
- Upgrade to release 0.11.2

* Sun Jun 17 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.1-1
- Upgrade to release 0.11.1

* Tue Jun 12 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.11.0-1
- Upgrade to release 0.11.0

* Wed Jun 6 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.10.1-2
- Lint the rpm and specify ExclusiveArch

* Fri May 25 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.10.1-1
- Upgrade to release 0.10.1

* Tue May 22 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.10.0-1
- Upgrade to release 0.10.0

* Fri May 11 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.9.1-1
- Upgrade to release 0.9.1

* Tue Apr 17 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.9.0-1
- Upgrade to release 0.9.0

* Tue Apr 3 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.4-1
- Upgrade to release 0.8.4

* Thu Mar 29 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.3-3
- Include commit 94d248d that fixes startup issue (see issue #421 upstream)

* Thu Mar 29 2018 Gerry Agbobada <gagbobada@gmail.com> - 0.8.3-2
- Upgrade to release 0.8.3

