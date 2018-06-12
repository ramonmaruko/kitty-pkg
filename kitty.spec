%define version_string 0.11.0

%global __python %{__python3}
%global git_rev  v%{version_string}
%global checkout %{git_date}git%(c=%{git_rev}; echo ${c:0:7})

Name:           kitty
Version:        %{version_string}
Release:        1%{?dist}
Summary:        A modern, hack-able, feature full, OpenGL-based terminal emulator

License:        GPLv3
URL:            https://github.com/kovidgoyal/kitty
Source0:        https://github.com/kovidgoyal/%{name}/archive/%{git_rev}.tar.gz
ExclusiveArch:      x86_64

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
%autosetup -v -n %{name}-%{version_string}


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
%{_mandir}/man1/kitty.1.gz
%doc CHANGELOG.rst README.asciidoc
%doc %{_docdir}/kitty/html/.*
%doc %{_docdir}/kitty/html/.buildinfo
%doc %{_docdir}/kitty/html/.nojekyll
%doc %{_docdir}/kitty/html/_images/diff.png
%doc %{_docdir}/kitty/html/_images/hints_mode.png
%doc %{_docdir}/kitty/html/_images/panel.png
%doc %{_docdir}/kitty/html/_images/screenshot.png
%doc %{_docdir}/kitty/html/_images/unicode.png
%doc %{_docdir}/kitty/html/_sources/binary.rst.txt
%doc %{_docdir}/kitty/html/_sources/build.rst.txt
%doc %{_docdir}/kitty/html/_sources/changelog.rst.txt
%doc %{_docdir}/kitty/html/_sources/conf.rst.txt
%doc %{_docdir}/kitty/html/_sources/faq.rst.txt
%doc %{_docdir}/kitty/html/_sources/graphics-protocol.rst.txt
%doc %{_docdir}/kitty/html/_sources/index.rst.txt
%doc %{_docdir}/kitty/html/_sources/invocation.rst.txt
%doc %{_docdir}/kitty/html/_sources/key-encoding.rst.txt
%doc %{_docdir}/kitty/html/_sources/performance.rst.txt
%doc %{_docdir}/kitty/html/_sources/protocol-extensions.rst.txt
%doc %{_docdir}/kitty/html/_sources/remote-control.rst.txt
%doc %{_docdir}/kitty/html/_sources/support.rst.txt
%doc %{_docdir}/kitty/html/_static/alabaster.css
%doc %{_docdir}/kitty/html/_static/basic.css
%doc %{_docdir}/kitty/html/_static/comment-bright.png
%doc %{_docdir}/kitty/html/_static/comment-close.png
%doc %{_docdir}/kitty/html/_static/comment.png
%doc %{_docdir}/kitty/html/_static/custom.css
%doc %{_docdir}/kitty/html/_static/doctools.js
%doc %{_docdir}/kitty/html/_static/documentation_options.js
%doc %{_docdir}/kitty/html/_static/down-pressed.png
%doc %{_docdir}/kitty/html/_static/down.png
%doc %{_docdir}/kitty/html/_static/file.png
%doc %{_docdir}/kitty/html/_static/jquery-3.2.1.js
%doc %{_docdir}/kitty/html/_static/jquery.js
%doc %{_docdir}/kitty/html/_static/kitty.png
%doc %{_docdir}/kitty/html/_static/minus.png
%doc %{_docdir}/kitty/html/_static/plus.png
%doc %{_docdir}/kitty/html/_static/pygments.css
%doc %{_docdir}/kitty/html/_static/searchtools.js
%doc %{_docdir}/kitty/html/_static/underscore-1.3.1.js
%doc %{_docdir}/kitty/html/_static/underscore.js
%doc %{_docdir}/kitty/html/_static/up-pressed.png
%doc %{_docdir}/kitty/html/_static/up.png
%doc %{_docdir}/kitty/html/_static/websupport.js
%doc %{_docdir}/kitty/html/kittens/clipboard.html
%doc %{_docdir}/kitty/html/kittens/diff.html
%doc %{_docdir}/kitty/html/kittens/hints.html
%doc %{_docdir}/kitty/html/kittens/icat.html
%doc %{_docdir}/kitty/html/kittens/panel.html
%doc %{_docdir}/kitty/html/kittens/unicode-input.html
%license LICENSE

%changelog
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

