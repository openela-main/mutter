%global gtk3_version 3.19.8
%global glib_version 2.53.2
%global gsettings_desktop_schemas_version 3.21.4
%global json_glib_version 0.12.0
%global libinput_version 1.4
%global pipewire_version 0.3.0
%global mutter_api_version 4

Name:          mutter
Version:       3.32.2
Release:       70%{?dist}
Summary:       Window and compositing manager based on Clutter

License:       GPLv2+
#VCS:          git:git://git.gnome.org/mutter
URL:           http://www.gnome.org
Source0:       http://download.gnome.org/sources/%{name}/3.32/%{name}-%{version}.tar.xz

# Work-around for OpenJDK's compliance test
Patch0:        0001-window-actor-Special-case-shaped-Java-windows.patch

# Allow Xwayland grabs by default, on a selected set of X11 apps
# https://bugzilla.redhat.com/1500399
Patch1: 0001-wayland-Allow-Xwayland-grabs-on-selected-apps.patch

Patch2: fix-text-selection-drawing.patch
Patch3: covscan-fixes.patch
Patch4: 0001-enum-types-Use-basename-in-header-comment.patch
Patch5: 0001-workspace-manager-Expose-layout-properties.patch

# RHEL 7 downstream patches
Patch100: deal-more-gracefully-with-oversized-windows.patch
# Work-around for Xvnc resizing (rhbz#1265511)
Patch101: 0001-monitor-manager-xrandr-Work-around-spurious-hotplugs.patch
Patch102: 0001-monitor-manager-xrandr-Force-an-update-when-resuming.patch
Patch103: 0001-monitor-manager-Consider-external-layout-before-defa.patch
Patch104: 0001-events-Don-t-move-sloppy-focus-while-buttons-are-pre.patch
Patch105: 0001-backends-x11-Support-synaptics-configuration.patch
Patch107: 0001-clutter-Extend-touchpad-device-property-check-for-Sy.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=733277
Patch109: 0001-Add-support-for-quad-buffer-stereo.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1618632
# https://bugzilla.redhat.com/show_bug.cgi?id=1497303
Patch110: 0001-monitor-manager-only-reuse-initial-config-if-monitor.patch
Patch112: add-support-for-plain-old-x-device-configuration.patch
Patch113: 0001-main-be-more-aggressive-in-assuming-X11-backend.patch
Patch114: 0001-clutter-Only-reset-scroll-axes-on-slave-devices.patch

# Inherit xorg.conf (rhbz#1690506)
Patch115: inherit-xrandr-metamodes.patch

# Fix test blocker when running on cirrus (rhbz#1735382)
Patch116: 0001-iconcache-Avoid-xrender-picture-formats-when-creatin.patch

# Don't focus or activate unmanaging windows (rhbz#1741547)
Patch117: 0001-workspace-Focus-only-ancestors-that-are-focusable.patch
Patch118: 0002-window-Emit-an-error-and-return-when-trying-to-activ.patch

# Don't freeze on rapid input (rhbz#1759525)
Patch119: 0001-events-Sync-pending-pointer-events-without-a-window.patch

# Don't freeze if input happens after many days of inactivity (rhbz#1766649)
Patch120: input-after-long-idle-fix.patch

# Fix invalid read in idle monitor (rhbz#1766695)
Patch121: idle-monitor-reset-fix.patch

# Improve shadow-fb performance on llvmpipe
# https://bugzilla.redhat.com/1737553
Patch201: 0001-cogl-Remove-unused-OFFSCREEN_BLIT-feature-flag.patch
Patch202: 0002-cogl-Fix-doc-for-_cogl_blit_framebuffer.patch
Patch203: 0003-cogl-Replace-ANGLE-with-GLES3-and-NV-framebuffer_bli.patch
Patch204: 0004-cogl-Relax-formats-on-glBlitFramebuffer.patch
Patch205: 0005-cogl-Allow-glBlitFramebuffer-between-onscreen-offscr.patch
Patch206: 0006-cogl-Rename-feature-OFFSCREEN_BLIT-to-BLIT_FRAMEBUFF.patch
Patch207: 0007-cogl-Expose-cogl_blit_framebuffer.patch
Patch208: 0008-clutter-stage-view-Use-cogl_blit_framebuffer-for-sha.patch
Patch209: 0009-clutter-stage-view-Ignore-clipping-rectangle-for-off.patch
Patch210: 0010-cogl-Flush-journal-before-blitting.patch
Patch211: 0011-clutter-stage-view-Separate-offscreen-and-shadowfb.patch
Patch212: 0012-renderer-native-Separate-offscreen-and-shadowfb.patch

# Handle lack of RANDR (#1776530)
Patch250: 0001-monitor-manager-xrandr-Move-dpms-state-and-screen-si.patch
Patch251: 0002-monitor-manager-xrandr-Create-dummy-screen-sized-mon.patch

# Fix build due to egl.pc provider change
Patch260: 0001-EGL-Include-EGL-eglmesaext.h.patch

# Fix popups with styli
Patch261: 0001-wayland-Check-stylus-serials-on-meta_wayland_seat_ca.patch

# Fix led-less pad mode switch buttons
Patch262: 0001-x11-Check-wacom-button-flags-to-determine-whether-bu.patch

# Wacom fixes
Patch263: 0001-backends-Consider-pen-eraser-devices-when-looking-fo.patch
Patch264: 0001-backends-Always-enable-tap-to-click-drag-on-opaque-W.patch
Patch265: 0001-backends-x11-Observe-multiple-pad-mode-switch-button.patch
Patch266: 0001-backends-Check-both-input-settings-and-mapper-for-ta.patch
Patch267: 0001-core-Let-pad-mode-switch-events-always-go-through-Me.patch
Patch268: 0001-Create-explicit-WacomDevices-for-tablet-touchpad-dev.patch
Patch269: 0001-Skip-wacom-touchpads-when-updating-setting.patch

# Revert stored-config behavior for VMs (#1365717)
Patch280: 0001-Revert-MetaMonitorManager-ignore-hotplug_mode_update.patch

# Respect xrandr --panning (#1690170)
Patch281: 0001-crtc-xrandr-Respect-configured-RANDR-panning.patch

# gnome-shell core dump after connection to docking station (#1809079)
Patch282: handle-hotplug-better.patch

# Improve performance under load (#1820760)
Patch290: 0001-clutter-avoid-redundant-_clutter_paint_node_init_typ.patch
Patch291: 0002-clutter-avoid-g_signal_emit_by_name-from-ClutterActo.patch
Patch292: 0003-clutter-fix-hole-in-ClutterPaintNode.patch

# Fix corrupted background after suspend (#1828162)
Patch300: 0001-background-Reload-when-GPU-memory-is-invalidated.patch

# Backport screen cast and remote desktop improvements (#1837381)
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/623
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/752
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/976
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1022
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1062
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/687
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1086
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1115
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1106
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1129
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1251
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1174
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1258
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1212
Patch400: screen-cast-remote-desktop-improvements.patch
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1283
Patch401: 0001-screen-cast-src-Destroy-hash-dmabuf-table-after-stre.patch
Patch402: 0002-renderer-native-Don-t-leak-DMA-buffer-CoglFramebuffe.patch
Patch403: 0001-renderer-Add-API-to-check-whether-renderer-is-hardwa.patch
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1318 (#1847062)
Patch404: 0001-backend-Add-getter-for-MetaScreenCast.patch
Patch405: 0002-renderer-native-Add-API-to-get-primary-GPU.patch
Patch406: 0003-screen-cast-Move-DMA-buffer-allocation-to-MetaScreen.patch
Patch407: 0004-screen-cast-Disable-DMA-buffer-based-screen-casting-.patch
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1351
# https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/1365
Patch408: cursor-move-only-screen-cast-fixes.patch
Patch409: mutter-bump-screencast-api-version.patch

# Only treat WM_PROTOCOLS messages as WM_PROTOCOL messages (#1847203)
Patch500: 0001-stage-x11-Check-that-message-is-WM_PROTOCOLS-before-.patch

# Don't show widow actor until explictly shown (#1719937)
Patch501: 0001-window-actor-Don-t-show-actor-until-meta_window_acto.patch

# Handle GPU unplug gracefully (#1846191)
Patch502: 0001-monitor-manager-kms-Trigger-hotplug-processing-on-gp.patch
Patch503: 0002-gpu-kms-Reset-CRTC-mode-and-output-list-if-no-resour.patch

# Add tile based shadow buffer damage tracking (#1670273)
Patch504: shadow-buffer-tile-damage.patch

# Add PING_TIMEOUT_DELAY to mutter MetaPreferences (#1886034)
Patch505: 0001-display-Make-check-alive-timeout-configureable.patch

# Polyinstantiation (#1861769)
Patch506: 0001-xwayland-Don-t-spew-warnings-when-looking-for-X11-di.patch
Patch507: 0002-xwayland-Make-sure-tmp-.X11-unix-exists.patch

# Mitigate nouveau misidentifying connectors (#1786496)
Patch508: 0001-monitor-config-manager-Handle-multiple-builtin-panel.patch

# Don't ever enable double buffered shadowfb and fix software rendering
# detection (#1921151)
Patch509: 0001-clutter-stage-view-Hide-double-buffered-shadowfb-beh.patch
Patch510: 0002-cogl-gpu-info-Fix-software-acceleration-detection.patch

# Backport of geometric picking, improving performance and fixing picking
# 10bpc pixel formats (#1919467)
Patch511: geometric-picking.patch

Patch520: 0001-clutter-Backport-of-touch-mode.patch

# Backport passing -xauth and adding local user to xhost (#1949176)
Patch521: xwayland-xauth-xhost-user.patch

# Backport fixes avoiding frozen partly off-screen clients (#1989035)
Patch522: wayland-frame-callback-rework.patch
# Backport fix avoiding regression due to the above changes (#1999120)
Patch523: 0001-wayland-Move-check-for-present-window-out-of-the-act.patch
Patch524: 0002-wayland-dnd-surface-Propagate-commit-to-parent-class.patch

# Backport monitor configuration policy feature (#2001655)
Patch525: monitor-config-policy.patch

# Backport EGLStream overview fixes (#1977721)
Patch526: eglstream-overview-fixes.patch

# Backport fix for stuck _NET_WM_FRAME_DRAWN handling (#2060305)
Patch527: 0001-compositor-Make-sure-_NET_WM_FRAME_DRAWN-timestamp-h.patch

# Fix race condition causing stuck pointer grabs (#2090168)
Patch528: 0001-events-Pass-CurrentTime-to-XIAllowEvents-when-unfree.patch

# Downgrade assert to warning (#2089311)
Patch529: 0001-workspace-Downgrade-assert-to-warning-when-adding-wi.patch

# Don't add common modes if panel already has (#2125031)
Patch530: 0001-output-kms-Add-more-heuristics-to-decide-when-to-off.patch

# Queue fail safe page flip callbacks (#2172057)
Patch531: 0001-renderer-native-Queue-fail-safe-callbacks-when-mode-.patch

Patch532: 0001-core-Change-MetaWaylandTextInput-event-forwarding-to.patch

BuildRequires: chrpath
BuildRequires: pango-devel
BuildRequires: startup-notification-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: glib2-devel >= %{glib_version}
BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: pkgconfig
BuildRequires: gobject-introspection-devel >= 1.41.0
BuildRequires: libSM-devel
BuildRequires: libwacom-devel
BuildRequires: libX11-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXtst-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: pam-devel
BuildRequires: pipewire-devel >= %{pipewire_version}
BuildRequires: systemd-devel
BuildRequires: upower-devel
BuildRequires: xorg-x11-server-Xorg
BuildRequires: xkeyboard-config-devel
BuildRequires: zenity
BuildRequires: desktop-file-utils
# Bootstrap requirements
BuildRequires: gtk-doc gnome-common gettext-devel git
BuildRequires: libcanberra-devel
BuildRequires: gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires: gnome-settings-daemon-devel
BuildRequires: meson
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-eglstream)

BuildRequires: json-glib-devel >= %{json_glib_version}
BuildRequires: libgudev1-devel
BuildRequires: libinput-devel >= %{libinput_version}
BuildRequires: xorg-x11-server-Xwayland

Obsoletes: mutter-wayland < 3.13.0
Obsoletes: mutter-wayland-devel < 3.13.0

# Make sure yum updates gnome-shell as well; otherwise we might end up with
# broken gnome-shell installations due to mutter ABI changes.
Conflicts: gnome-shell < 3.21.1

Requires: control-center-filesystem
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: pipewire%{_isa} >= %{pipewire_version}
Requires: startup-notification
Requires: dbus
Requires: zenity

Requires:      json-glib%{?_isa} >= %{json_glib_version}
Requires:      libinput%{?_isa} >= %{libinput_version}

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.

%package  tests
Summary:  Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -S git

%build
%meson -Degl_device=true -Dwayland_eglstream=true
%meson_build

%install
%meson_install

%find_lang %{name}

# Mutter contains a .desktop file so we just need to validate it
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/mutter
%{_datadir}/applications/*.desktop
%{_libdir}/lib*.so.*
%{_libdir}/mutter-%{mutter_api_version}/
%{_libexecdir}/mutter-restart-helper
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_mandir}/man1/mutter.1*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files tests
%{_libexecdir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/mutter-%{mutter_api_version}/tests

%changelog
* Thu Jun 08 2023 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-70
- Fix ordering of keyboard modifiers relative to other keyboard events
  Resolves: #2170830

* Tue May 23 2023 Jonas Ådahl <jadahl@redhat.com>) - 3.32.2-69
- Queue fail safe page flip callbacks
  Resolves: #2209025

* Wed Dec 21 2022 Olivier Fourdan <ofourdan@redhat.com> - 3.32.2-68
- Fix downstream synaptics patches breaking xdmcp
  Resolves: #2092450

* Thu Oct 20 2022 Jonas Ådahl <jadahl@redhat.com>) - 3.32.2-67
- Don't add common modes if panel already has
  Resolves: #2125031

* Mon Aug 29 2022 Jonas Ådahl <jadahl@redhat.com>) - 3.32.2-66
- Downgrade assert to warning
  Resolves: #2089311

* Mon Jun 27 2022 Jonas Ådahl <jadahl@redhat.com>) - 3.32.2-65
- Fix race condition causing stuck pointer grabs
  Resolves: #2090168

* Fri Mar 18 2022 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-64
- Backport fix for stuck _NET_WM_FRAME_DRAWN handling
  Resolves: #2060305

* Thu Feb 24 2022 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-63
- Fix EGLStream overview fixes backport
  Related: #1977721

* Mon Feb 21 2022 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-62
- Backport EGLStream overview fixes
  Resolves: #1977721

* Fri Feb 04 2022 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-61
- Backport monitor configuration policy feature
  Resolves: #2001655

* Mon Aug 30 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-60
- Backport fix avoiding DND regression
  Resolves: #2000905

* Fri Aug 06 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-59
- Backport fixes avoiding frozen partly off-screen clients
  Resolves: #1989035

* Mon Jul 05 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-58
- Backport xauth and xhost patches
  Resolves: #1949176

* Mon Feb 22 2021 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-57
- Backport touch-mode
  Resolves: #1833787

* Tue Feb 09 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-56
- Backport geometric picking patches
  Resolves: #1919467

* Tue Feb 09 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-55
- Fix slow nouveau with llvmpipe
  Resolves: #1921151

* Tue Jan 12 2021 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-54
- Fix polyinstantiation patch backport
  Resolves: #1861769

* Thu Dec 17 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-53
- Fix test case backport
  Related: #1786496

* Thu Dec 17 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-52
- Support polyinstantiation
  Resolves: #1861769
- Mitigate nouveau misidentifying connectors
  Resolves: #1786496

* Mon Dec 07 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-51
- Add PING_TIMEOUT_DELAY to mutter MetaPreferences
  Resolves: #1886034

* Thu Nov 26 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-50
- Fix GLX stereo buffer rebase error
  Resolves: #1889528

* Tue Nov 10 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-49
- Add tile based shadow buffer damage tracking
  Resolves: #1670273

* Thu Sep 03 2020 Florian Müllner <fmuellner@redhat.com> - 3.32.2-47
- Fix screen sharing on wayland
  Resolves: #1873963

* Wed Jul 15 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-46
- Handle cursor only screen cast frames better
  Related: #1837381

* Thu Jul 02 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-45
- Handle GPU unplug gracefully
  Resolves: #1846191

* Thu Jun 25 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-44
- Don't show widow actor until explictly shown
  Resolves: #1719937

* Thu Jun 25 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-43
- Only treat WM_PROTOCOLS messages as WM_PROTOCOL messages
  Resolves: #1847203

* Tue Jun 16 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-42
- Don't pass DMA buffers if they can't be mmap():ed
  Related: #1847062

* Wed Jun 10 2020 Florian Müllner <fmuellner@redhat.com> - 3.32.2-41
- Backport is_rendering_hardware_acclerated() API
  Related: #1837381

* Wed Jun 03 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-40
- Fix DMA buffer memory leak
  Related: #1837381

* Mon May 25 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-39
- Fix incorrect pipewire dependency version
  Related: #1837381

* Mon May 25 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-38
- Backport screen cast and remote desktop improvements
  Resolves: #1837381

* Tue May 19 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-37
- Fix corrupted background after suspend
  Resolves: #1828162

* Wed Apr 08 2020 Florian Müllner <fmuellner@redhat.com> - 3.32.2-36
- Improve performance under IO load
  Resolves: #1820760

* Mon Mar 23 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-35
- Drop EGLStream robustness patches
  Resolves: #1815430

* Thu Mar 05 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-34
- gnome-shell core dump after connection to docking station
  Resolves: #1809079

* Mon Feb 24 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-33
- Respect xrandr --panning
  Resolves: #1690170

* Mon Feb 24 2020 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-32
- Revert stored-config behavior for VMs
  Resolves: #1365717

* Mon Feb 24 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-31
- Fixup detection of multiple mode switch buttons
  Resolves: #1687979

* Fri Feb 21 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-30
- Avoid toggling wacom touchpads on tap-to-click/drag setting updates
  Resolves: #1716754

* Thu Feb 13 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-29
- Fixup Wacom pad OSD so it appears on the right monitor
  Resolves: #1777556

* Thu Feb 13 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-28
- Fixup automatic enabling of wacom touchpad tapping
  Resolves: #1716754

* Thu Feb 13 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-27
- Fixup handling of multiple mode switch buttons in pads
  Resolves: #1687979

* Mon Dec 16 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-26
- Let pad OSD update on mode switching
  Resolves: #1716774

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-25
- Fix Wacom OSDs so they appear on the right monitor
  Resolves: #1777556

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-24
- Handle multiple mode switch buttons in Cintiq 27QHD
  Resolves: #1687979

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-23
- Enable tapping features by default on standalone Wacom tablets
  Resolves: #1716754

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-22
- Fix detection of Wacom tablet features on X11
  Resolves: #1759619

* Wed Dec 04 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-21
- Fix mode switch pad buttons without LEDs
  Resolves: #1666070

* Mon Dec 02 2019 Tomas Pelka <tpelka@redhat.com> - 3.32.2-20
- Need rebuild in correct build target
  Resolves: #1730891

* Fri Nov 29 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-19
- Fix pop ups with stylus input
  Resolves: #1730891

* Wed Nov 27 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-18
- Revert memory leak fix
  Resolves: #1777911

* Wed Nov 27 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.2-17
- Fix some memory leaks
  Resolves: #1719819

* Wed Nov 27 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-16
- Fix build due to egl.pc provider change
  Related: #1776530

* Wed Nov 27 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-15
- Handle lack of RANDR
  Resolves: #1776530

* Mon Nov  4 2019 Olivier Fourdan <ofourdan@redhat.com> - 3.32.2-14
- Backports shadow FB improvements on llvmpipe
  Resolves: #1737553

* Wed Oct 30 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-13
- Fix invalid read in idle monitor
  Resolves: #1766695

* Wed Oct 30 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-12
- Don't freeze if input happens after many days of inactivity
  Resolves: #1766649

* Fri Oct 25 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-11
- Don't freeze on rapid input
  Resolves: #1759525

* Fri Aug 16 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-10
- Don't focus or activate unmanaging windows
  Resolves: #1741547

* Mon Aug 05 2019 Ray Strode <rstrode@redhat.com> - 3.32.2-9
- Another 16bpp graphics card crash
  Related: #1735382
  Resolves: #1737326

* Fri Aug 02 2019 Ray Strode <rstrode@redhat.com> - 3.32.2-8
- Fix crash in window icon handling on 16bpp graphics cards
  Resolves: #1735382

* Tue Jul 23 2019 Ray Strode <rstrode@redhat.com> - 3.32.2-7
- Fix bug leading to 100% cpu usage on suspend/resume
  Resolves: #1724551

* Mon Jul 15 2019 Jonas Ådahl <jadahl@redhat.com> - 3.32.2-6
- Don't ignore current mode when deriving current config
  Resolves: #1690506

* Thu Jun 20 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.32.2-5
- Ensure pad XDevices do not get buttons remapped
  Resolves: #1687949

* Wed Jun 12 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.2-4
- Expose workspace layout as properties
  Related: #1704360

* Thu May 30 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.2-3
- Avoid arch-specific bits in header comments
  Related: #1698884
* Tue May 28 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.2-2
- Fix a couple of issues pointed out by covscan
  Resolves: #1698884

* Thu May 23 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.2-1
- Update to 3.32.2
  Resolves: #1698884

* Tue Apr 02 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.3-19
- Fix synaptics/evdev driver support forward port to not break tablet pads
  Resolves: #1687949

* Thu Feb 21 2019 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-18
- Remove patch enabling monitor framebuffer scaling
  Related: #1668883

* Mon Feb 11 2019 Ray Strode <rstrode@redhat.com> - 3.28.3-17
- Fix bug in suspend/resume corruption patch leading to inhibit fd
  not getting fetched
  Related: #1663440

* Mon Feb 11 2019 Florian Müllner <fmuellner@redhat.com> - 3.28.3-16
- Backport forward_key() method
  Related: #1668979

* Mon Feb 11 2019 Florian Müllner <fmuellner@redhat.com> - 3.28.3-15
- Re-add dropped downstream patches (rhbz#1668883)

* Tue Feb 05 2019 Olivier Fourdan <jadahl@redhat.com> - 3.28.3-14
- Restore update monitor fix (rhbz#1635123)

* Fri Feb 01 2019 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-13
- Fix screen recording on HiDPI monitor (rhbz#1670287)

* Thu Jan 31 2019 Ray Strode <rstrode@redhat.com> - 3.28.3-12
- Drop "Always update monitor for non user op" patch. It's already
  in tree and getting misapplied
  Related: #1663440
- Fix suspend and resume corruption on NVidia
  Resolves: #1663440

* Tue Jan 22 2019 Olivier Fourdan <ofourdan@redhat.com> - 3.28.3-11
- Fix a new crash in recordwindow related to behavior changes in
  recent backport additions (rhbz#1657661)

* Fri Jan 11 2019 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-10
- Backport screen cast cursor side channel patches (rhbz#1658971)

* Fri Jan 11 2019 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-9
- Avoid EGLStream backend deadlock (rhbz#1656905)

* Fri Jan 11 2019 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-8
- Get texture pixels via offscreen for EGLStreams (rhbz#1656926)

* Mon Jan 07 2019 Olivier Fourdan <ofourdan@redhat.com> - 3.28.3-7
- Backport the RecordWindow screencast mode (rhbz#1657661)

* Fri Jan 04 2019 Ray Strode <rstrode@redhat.com> - 3.28.3-6
- Add shadow framebuffer for server cards to fix blending
  performance
  Resolves: #1591250

* Fri Oct 26 2018 Olivier Fourdan <ofourdan@redhat.com> - 3.28.3-5
- Allow Xwayland grabs on a selected set of X11 applications.
  (rhbz#1500399)

* Tue Oct 23 2018 Olivier Fourdan <ofourdan@redhat.com> - 3.28.3-4
- More backport fixes from upstream "gnome-3-28" branch
- enable eglstream support (rhbz#1639782)

* Mon Oct 15 2018 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-3
- Fix garbled window titles (rhbz#1639194)

* Thu Oct 04 2018 Olivier Fourdan <ofourdan@redhat.com> - 3.28.3-2
- Backport fixes from upstream "gnome-3-28" branch:
- [wayland] laptop with lid closed and external monitor can't log in to
  wayland session (rhbz#1635106)
- [Wayland] Crash with Xwayland grabs enabled in mutter (rhbz#1635110)
- [Wayland] Crash on monitor hotplug (rhbz#1635123)
- [wayland] mutter crashes if drmModeSetCrtc() failed (rhbz#1635155)
- mutter crashes if a modal window closes whilst being dragged (rhbz#1635159)
- gnome-shell crashed with SIGSEGV in meta_monitor_mode_get_resolution()
  (rhbz#1635164)
- [wayland] crash when drmModeGetResources() fails (rhbz#1635167)
- [wayland] Can't create new back buffer on Intel i915 (rhbz#1635170)
- [wayland] keyboard: Create a separate keymap shm file per resource
  (rhbz#1635235)
- Crash in gnome-shell/mutter after a window is destroyed (rhbz#1635237)
- [x11] Using a cursor theme missing cursors can crash mutter (rhbz#1635241)
- [wayland] Warning messages when starting mutter (rhbz#1635248)
- [wayland] mutter/gnome-shell crash after failed DnD in nautilus
  (rhbz#1635718)

* Thu Aug 09 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3
- Apply HW cursor on-demand patches
- Apply monitor transform regression patch

* Wed Aug 08 2018 Jonas Ådahl <jadahl@redhat.com> - 3.28.1-4
- Backport remote-access controller API patch

* Tue Aug 07 2018 Jonas Ådahl <jadahl@redhat.com> - 3.28.1-3
- Backport remote desktop related patches

* Wed Aug 01 2018 Jan Grulich <jgrulich@redhat.com> - 3.28.1-2
- Support PipeWire 0.2.2+

* Fri Apr 13 2018 Florian Müllner <fmuellner@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Florian Müllner <fmuellner@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Florian Müllner <fmuellner@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 28 2018 Adam Williamson <awilliam@redhat.com> - 3.27.91-2
- Backport MR#36 to fix RHBZ #1547691 (GGO #2), mouse issues

* Wed Feb 21 2018 Florian Müllner <fmuellner@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 3.27.1-4
- Rebuild against newer gnome-desktop3 package
- Add patch for adjustments to pipewire 0.1.8 API

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.1-2
- Remove obsolete scriptlets

* Mon Oct 30 2017 Florian Müllner <fmuellner@redhat.com> - 3.27.1-1
- Include 32-bit build fixes

* Tue Oct 17 2017 Florian Müllner <fmuellner@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Fri Oct 06 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.1-2
- Fix screencasts

* Wed Oct 04 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Sep 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.0-5
- Adjust to pipewire API break

* Wed Sep 20 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.0-5
- Enable tablet support

* Tue Sep 12 2017 Adam Williamson <awilliam@redhat.com> - 3.26.0-4
- Also backport BGO #787570 fix from upstream

* Tue Sep 12 2017 Adam Williamson <awilliam@redhat.com> - 3.26.0-3
- Backport upstream fixes for crasher bug BGO #787568

* Tue Sep 12 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.0-2
- Enable remote desktop support

* Tue Sep 12 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Thu Aug 24 2017 Bastien Nocera <bnocera@redhat.com> - 3.25.91-2
+ mutter-3.25.91-2
- Fix inverted red and blue channels with newer Mesa

* Tue Aug 22 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Thu Aug 10 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Florian Müllner <fmuellner@redhat.con> - 3.25.4-1
- Update to 3.25.4

* Wed Jun 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Wed May 24 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Thu May 18 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.1-2
- Fix copy+paste of UTF8 strings between X11 and wayland

* Thu Apr 27 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.1-1
- Update to 3.25.1

* Tue Apr 11 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Mon Mar 20 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Fri Mar 10 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.91-4
- Apply startup-notification hack again

* Tue Mar 07 2017 Adam Williamson <awilliam@redhat.com> - 3.23.91-3
- Backport more color fixes, should really fix BGO #779234, RHBZ #1428559

* Thu Mar 02 2017 Adam Williamson <awilliam@redhat.com> - 3.23.91-2
- Backport fix for a color issue in 3.23.91 (BGO #779234, RHBZ #1428559)

* Wed Mar 01 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Thu Feb 16 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Florian Müllner <fmuellner@redhat.com> - 3.23.3-1
- Update to 3.23.3

* Fri Dec 02 2016 Florian Müllner <fmuellner@redhat.com> - 3.23.2-2
- Fix build error on 32-bit platforms

* Thu Nov 24 2016 Kevin Fenzi <kevin@scrye.com> - 3.23.2-2
- Some fixes to get building. Still needs patch1 rebased.

* Wed Nov 23 2016 Florian Müllner <fmuellner@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Tue Nov  8 2016 Matthias Clasen <mclasen@redhat.com> - 3.23.1-2
- Fix 1376471

* Sun Oct 30 2016 Florian Müllner <fmuellner@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Tue Oct 18 2016 Kalev Lember <klember@redhat.com> - 3.22.1-3
- Backport a fix to make gnome-screenshot --area work

* Tue Oct 11 2016 Adam Jackson <ajax@redhat.com> - 3.22.1-2
- Prefer eglGetPlatformDisplay() to eglGetDisplay()

* Tue Oct 11 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Wed Sep 28 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.0-2
- Include fix for crash on VT switch

* Mon Sep 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Thu Sep 08 2016 Kalev Lember <klember@redhat.com> - 3.21.91-2
- wayland/cursor-role: Increase buffer use count on construction (#1373372)

* Tue Aug 30 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 3.21.90-3
- clutter/evdev: Fix absolute pointer motion events (#1369492)

* Sat Aug 20 2016 Kalev Lember <klember@redhat.com> - 3.21.90-2
- Update minimum dep versions

* Fri Aug 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Jul 20 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.4-1
- Update to 3.21.4
- Drop downstream patch
- Fix build error on 32-bit

* Tue Jun 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Fri May 27 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Fri Apr 29 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Wed Apr 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Florian Müllner <fmuellner@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 16 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Thu Mar 03 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.91-2
- Include fix for invalid cursor wl_buffer access

* Thu Mar 03 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Fri Feb 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Thu Dec 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Nov 25 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Tue Nov 10 2015 Ray Strode <rstrode@redhat.com> 3.19.1-5.20151110git049f1556d
- Update to git snapshot

* Thu Oct 29 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Wed Oct 21 2015 Ray Strode <rstrode@redhat.com> 3.18.1-4
- Force the cursor visible on vt switches after setting
  the crtc to workaround that qxl bug from before in a
  different situation
  Related: #1273247

* Wed Oct 21 2015 Kalev Lember <klember@redhat.com> - 3.18.1-3
- Backport a fix for a common Wayland crash (#1266486)

* Thu Oct 15 2015 Kalev Lember <klember@redhat.com> - 3.18.1-2
- Bump gnome-shell conflicts version

* Thu Oct 15 2015 Florian Müllner <fmuellner@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Sep 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Thu Sep 03 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Thu Sep 03 2015 Ray Strode <rstrode@redhat.com> 3.17.90-2
- Add workaround for qxl cursor visibility wonkiness that we
  did for f22
  Related: #1200901

* Thu Aug 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Thu Jul 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Wed Jul 22 2015 David King <amigadave@amigadave.com> - 3.17.3-2
- Bump for new gnome-desktop3

* Thu Jul 02 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.2-1
- Update to 3.17.2

* Thu Apr 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.1-1
- Update to 3.17.1

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1.1-2
- Bump gnome-shell conflicts version

* Wed Apr 15 2015 Rui Matos <rmatos@redhat.com> - 3.16.1.1-1
- Update to 3.16.1.1

* Tue Apr 14 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-2
- Update minimum dep versions
- Use license macro for the COPYING file

* Tue Mar 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 10 2015 Peter Hutterer <peter.hutterer@redhat.com> - 3.15.91-2
- Rebuild for libinput soname bump

* Wed Mar 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.91-1
- Update to 3.15.91

* Fri Feb 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Mon Feb 02 2015 Adam Williamson <awilliam@redhat.com> - 3.15.4-2
- backport ad90b7dd to fix BGO #743412 / RHBZ #1185811

* Wed Jan 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Mon Jan 19 2015 Peter Hutterer <peter.hutterer@redhat.com> 3.15.3-3
- Rebuild for libinput soname bump

* Mon Jan 12 2015 Ray Strode <rstrode@redhat.com> 3.15.3-2
- Add specific BuildRequires for wayland bits, so we don't
  get wayland support by happenstance.
- Add BuildRequires for autogoo since ./autogen.sh is run as part of
  the build process

* Fri Dec 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.3-1
- Revert unsatisfiable wayland requirement

* Fri Dec 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Thu Nov 27 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.2-1
- Update to 3.15.2

* Wed Nov 12 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 3.15.1-2
- Build installed tests

* Thu Oct 30 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Tue Oct 21 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.1-2
- Fix regression in handling raise-on-click option (rhbz#1151918)

* Tue Oct 14 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.1-1
- Update to 3.14.1

* Fri Oct 03 2014 Adam Williamson <awilliam@redhat.com> - 3.14.0-3
- backport fix for BGO #737233 / RHBZ #1145952 (desktop right click broken)

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-2
- Bump gnome-shell conflicts version

* Mon Sep 22 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.0-1
- Update to 3.14.0

* Wed Sep 17 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.92-1
- Update to 3.13.92

* Fri Sep 12 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.13.91-2
- Rebuild for libinput soname bump

* Wed Sep 03 2014 Florian Müllner <fmuellner@redhat.com> - 3.31.91-1
- Update to 3.13.91, drop downstream patches

* Tue Aug 26 2014 Adel Gadllah <adel.gadllah@gmail.com> - 3.13.90-4
- Apply fix for RH #1133166

* Mon Aug 25 2014 Hans de Goede <hdegoede@redhat.com> - 3.13.90-3
- Add a patch from upstream fixing gnome-shell crashing non stop on
  multi monitor setups (rhbz#1103221)

* Fri Aug 22 2014 Kevin Fenzi <kevin@scrye.com> 3.13.90-2
- Rebuild for new wayland

* Wed Aug 20 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-3
- Rebuilt for upower 0.99.1 soname bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-2
- Rebuilt for gobject-introspection 1.41.4

* Fri Jun 27 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.3-1
- New gobject-introspection has been built, drop the last patch again

* Wed Jun 25 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.3-1
- Revert annotation updates until we get a new gobject-introspection build

* Wed Jun 25 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.3-1
- Update to 3.13.1

* Wed Jun 11 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.2-2
- Backport fix for legacy fullscreen check

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.2-1
- Update to 3.13.2, drop upstreamed patches

* Thu May  8 2014 Matthias Clasen <mclasen@redhat.com> - 3.13.1-5
- Fix shrinking terminals

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-4
- Backport an upstream fix for a Wayland session crash

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-3
- Install mutter-launch as setuid root

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-2
- Obsolete mutter-wayland

* Wed Apr 30 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Tue Apr 15 2014 Florian Müllner <fmuellner@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Update dep versions

* Tue Mar 25 2014 Florian Müllner <fmuellner@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Thu Mar 06 2014 Florian Müllner <fmuellner@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-2
- Rebuilt for cogl soname bump

* Wed Feb 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-4
- Rebuilt for gnome-desktop soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.11.5-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-2
- Rebuilt for cogl soname bump

* Wed Feb 05 2014 Florian Müllner <fmuellner@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Florian Müllner <fmuellner@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Fri Dec 20 2013 Florian Müllner <fmuellner@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Wed Nov 13 2013 Florian Müllner <fmuellner@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Oct 30 2013 Florian Müllner <fmuellner@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Tue Oct 15 2013 Florian Müllner <fmuellner@redhat.com> - 3.10.1.1-1
- Update to 3.10.1.1

* Mon Oct 14 2013 Florian Müllner <fmuellner@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Florian Müllner <fmuellner@redhat.com> - 3.10.0.1-1
- Update to 3.10.0.1

* Mon Sep 23 2013 Florian Müllner <fmuellner@redhat.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-2
- Update the description and URL
- Tighten -devel subpackage deps with _isa
- Use the make_install macro

* Mon Sep 16 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-2
- Rebuilt for libgnome-desktop soname bump

* Tue Sep 03 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.90-1
- Update to 3.9.90

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-2
- Rebuilt for cogl 1.15.4 soname bump

* Tue Jul 30 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.5-1
- Update to 3.9.5

* Wed Jul 10 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Tue Jun 18 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.3-1
- Update to 3.9.3

* Tue May 28 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.2-1
- Update to 3.9.2

* Wed May 01 2013 Florian Müllner <fmuellner@redhat.com> - 3.9.1-1
- Update to 3.9.1

* Tue Apr 23 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Mon Mar 04 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Tue Feb 05 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4-2
- Rebuild for new cogl

* Tue Jan 15 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Tue Dec 18 2012 Florian Müllner <fmuellner@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Mon Nov 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Mon Oct 15 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-2
- Rebuild against new cogl

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-2
- Rebuild against new cogl/clutter

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Fri Jun  8 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-3
- Make resize grip area larger

* Thu Jun 07 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-2
- Don't check for Xinerama anymore - it is now mandatory

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2
- Remove upstreamed patches

* Wed May 09 2012 Adam Jackson <ajax@redhat.com> 3.4.1-3
- mutter-never-slice-shape-mask.patch, mutter-use-cogl-texrect-api.patch:
  Fix window texturing on hardware without ARB_texture_non_power_of_two
  (#813648)

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas scriplets

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1
- Conflict with gnome-shell versions older than 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-2
- Rebuild against new cogl

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Fri Jan 20 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-2
- Rebuild against new cogl

* Thu Jan  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-2
- Rebuild against new clutter

* Tue Nov 22 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Owen Taylor <otaylor@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Wed Sep 14 2011 Owen Taylor <otaylor@redhat.com> - 3.1.91.1-1
- Update to 3.1.91.1

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90.1-1
- Update to 3.1.90.1

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3.1-3
- Rebuild

* Mon Jul  4 2011 Peter Robinson <pbrobinson@gmail.com> - 3.1.3.1-2
- rebuild against new clutter/cogl

* Mon Jul 04 2011 Adam Williamson <awilliam@redhat.com> - 3.1.3.1-1
- Update to 3.1.3.1

* Thu Jun 30 2011 Owen Taylor <otaylor@redhat.com> - 3.1.3-1
- Update to 3.1.3

* Wed May 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.2.1-1
- Update to 3.0.2.1

* Fri Apr 29 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-3
- Actually apply the patch for #700276

* Thu Apr 28 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-2
- Make session saving of gnome-shell work

* Mon Apr 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Owen Taylor <otaylor@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Wed Mar 23 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Mon Mar  7 2011 Owen Taylor <otaylor@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Mar  1 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-2
- Build against libcanberra, to enable AccessX feedback features

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-2
- Rebuild against newer gtk

* Tue Feb  1 2011 Owen Taylor <otaylor@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.4-1
- Update to 2.91.4

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-2
- Rebuild against new gtk
- Drop no longer needed %%clean etc

* Mon Nov 29 2010 Owen Taylor <otaylor@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Tue Nov  9 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Tue Nov  2 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.1-2
- Rebuild against newer gtk3

* Fri Oct 29 2010 Owen Taylor <otaylor@redhat.com> - 2.91.1-1
- Update to 2.91.1

* Mon Oct  4 2010 Owen Taylor <otaylor@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-4
- Rebuild against newer gobject-introspection

* Wed Jul 14 2010 Colin Walters <walters@verbum.org> - 2.31.5-3
- Rebuild for new gobject-introspection

* Tue Jul 13 2010 Adel Gadllah <adel.gadllah@gmail.com> - 2.31.5-2
- Build against gtk3

* Mon Jul 12 2010 Colin Walters <walters@pocket> - 2.31.5-1
- New upstream version

* Mon Jul 12 2010 Colin Walters <walters@verbum.org> - 2.31.2-5
- Rebuild against new gobject-introspection

* Tue Jul  6 2010 Colin Walters <walters@verbum.org> - 2.31.2-4
- Changes to support snapshot builds

* Fri Jun 25 2010 Colin Walters <walters@megatron> - 2.31.2-3
- drop gir-repository-devel dep

* Wed May 26 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-2
- removed "--with-clutter" as configure is claiming it to be an unknown option

* Wed May 26 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-1
- New upstream 2.31.2 release

* Thu Mar 25 2010 Peter Robinson <pbrobinson@gmail.com> 2.29.1-1
- New upstream 2.29.1 release

* Wed Mar 17 2010 Peter Robinson <pbrobinson@gmail.com> 2.29.0-1
- New upstream 2.29.0 release

* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 2.28.1-0.2
- mutter-2.28.1-add-needed.patch: Fix FTBFS from --no-add-needed

* Thu Feb  4 2010 Peter Robinson <pbrobinson@gmail.com> 2.28.1-0.1
- Move to git snapshot

* Wed Oct  7 2009 Owen Taylor <otaylor@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Sep 15 2009 Owen Taylor <otaylor@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Fri Sep  4 2009 Owen Taylor <otaylor@redhat.com> - 2.27.4-1
- Remove workaround for #520209
- Update to 2.27.4

* Sat Aug 29 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-3
- Fix %%preun GConf script to properly be for package removal

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-2
- Add a workaround for Red Hat bug #520209

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-1
- Update to 2.27.3, remove mutter-metawindow.patch

* Fri Aug 21 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.2-2
- Add upstream patch needed by latest mutter-moblin

* Tue Aug 11 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.2-1
- New upstream 2.27.2 release. Drop upstreamed patches.

* Wed Jul 29 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-5
- Add upstream patches for clutter 1.0

* Wed Jul 29 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-4
- Add patch to fix mutter --replace

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-2
- Updates from review request

* Fri Jul 17 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.1-1
- Update to official 2.27.1 and review updates

* Thu Jun 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.0-0.2
- Updates from initial reviews

* Thu Jun 18 2009 Peter Robinson <pbrobinson@gmail.com> 2.27.0-0.1
- Initial packaging
