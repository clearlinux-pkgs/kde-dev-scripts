#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kde-dev-scripts
Version  : 19.08.0
Release  : 11
URL      : https://download.kde.org/stable/applications/19.08.0/src/kde-dev-scripts-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/kde-dev-scripts-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/kde-dev-scripts-19.08.0.tar.xz.sig
Summary  : Scripts and setting files useful during development of KDE software
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kde-dev-scripts-bin = %{version}-%{release}
Requires: kde-dev-scripts-data = %{version}-%{release}
Requires: kde-dev-scripts-license = %{version}-%{release}
Requires: kde-dev-scripts-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
Stuff in this directory:
=== DEBUGGING SUPPORT
adddebug        Modifies the Makefile to add debug info (-g)

%package bin
Summary: bin components for the kde-dev-scripts package.
Group: Binaries
Requires: kde-dev-scripts-data = %{version}-%{release}
Requires: kde-dev-scripts-license = %{version}-%{release}

%description bin
bin components for the kde-dev-scripts package.


%package data
Summary: data components for the kde-dev-scripts package.
Group: Data

%description data
data components for the kde-dev-scripts package.


%package license
Summary: license components for the kde-dev-scripts package.
Group: Default

%description license
license components for the kde-dev-scripts package.


%package man
Summary: man components for the kde-dev-scripts package.
Group: Default

%description man
man components for the kde-dev-scripts package.


%prep
%setup -q -n kde-dev-scripts-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565896570
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565896570
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-dev-scripts
cp COPYING %{buildroot}/usr/share/package-licenses/kde-dev-scripts/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kde-dev-scripts/COPYING.DOC
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/adddebug
/usr/bin/build-progress.sh
/usr/bin/c++-copy-class-and-file
/usr/bin/c++-rename-class-and-file
/usr/bin/cheatmake
/usr/bin/colorsvn
/usr/bin/create_cvsignore
/usr/bin/create_makefile
/usr/bin/create_makefiles
/usr/bin/create_svnignore
/usr/bin/cvs-clean
/usr/bin/cvsaddcurrentdir
/usr/bin/cvsbackport
/usr/bin/cvsblame
/usr/bin/cvscheck
/usr/bin/cvsforwardport
/usr/bin/cvslastchange
/usr/bin/cvslastlog
/usr/bin/cvsrevertlast
/usr/bin/cvsversion
/usr/bin/cxxmetric
/usr/bin/draw_lib_dependencies
/usr/bin/extend_dmalloc
/usr/bin/extractattr
/usr/bin/extractrc
/usr/bin/findmissingcrystal
/usr/bin/fix-include.sh
/usr/bin/fixkdeincludes
/usr/bin/fixuifiles
/usr/bin/grantlee_strings_extractor.py
/usr/bin/includemocs
/usr/bin/kde-systemsettings-tree.py
/usr/bin/kde_generate_export_header
/usr/bin/kdedoc
/usr/bin/kdekillall
/usr/bin/kdelnk2desktop.py
/usr/bin/kdemangen.pl
/usr/bin/krazy-licensecheck
/usr/bin/makeobj
/usr/bin/noncvslist
/usr/bin/nonsvnlist
/usr/bin/optimizegraphics
/usr/bin/package_crystalsvg
/usr/bin/png2mng.pl
/usr/bin/pruneemptydirs
/usr/bin/qtdoc
/usr/bin/reviewboard-am
/usr/bin/svn-clean
/usr/bin/svnbackport
/usr/bin/svnchangesince
/usr/bin/svnforwardport
/usr/bin/svngettags
/usr/bin/svnintegrate
/usr/bin/svnlastchange
/usr/bin/svnlastlog
/usr/bin/svnrevertlast
/usr/bin/svnversions
/usr/bin/uncrustify-kf5
/usr/bin/wcgrep
/usr/bin/zonetab2pot.py

%files data
%defattr(-,root,root,-)
/usr/share/uncrustify/uncrustify-kf5.cfg
/usr/share/uncrustify/uncrustify-qt.cfg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-dev-scripts/COPYING
/usr/share/package-licenses/kde-dev-scripts/COPYING.DOC

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/adddebug.1
/usr/share/man/ca/man1/cheatmake.1
/usr/share/man/ca/man1/create_cvsignore.1
/usr/share/man/ca/man1/create_makefile.1
/usr/share/man/ca/man1/create_makefiles.1
/usr/share/man/ca/man1/cvscheck.1
/usr/share/man/ca/man1/cvslastchange.1
/usr/share/man/ca/man1/cvslastlog.1
/usr/share/man/ca/man1/cvsrevertlast.1
/usr/share/man/ca/man1/cxxmetric.1
/usr/share/man/ca/man1/extend_dmalloc.1
/usr/share/man/ca/man1/extractrc.1
/usr/share/man/ca/man1/fixincludes.1
/usr/share/man/ca/man1/pruneemptydirs.1
/usr/share/man/ca/man1/qtdoc.1
/usr/share/man/ca/man1/reportview.1
/usr/share/man/ca/man1/transxx.1
/usr/share/man/ca/man1/zonetab2pot.py.1
/usr/share/man/da/man1/adddebug.1
/usr/share/man/da/man1/cheatmake.1
/usr/share/man/da/man1/create_cvsignore.1
/usr/share/man/da/man1/create_makefiles.1
/usr/share/man/da/man1/cvscheck.1
/usr/share/man/da/man1/cvslastchange.1
/usr/share/man/da/man1/cvslastlog.1
/usr/share/man/da/man1/cvsrevertlast.1
/usr/share/man/da/man1/cxxmetric.1
/usr/share/man/da/man1/extend_dmalloc.1
/usr/share/man/da/man1/extractrc.1
/usr/share/man/da/man1/fixincludes.1
/usr/share/man/da/man1/pruneemptydirs.1
/usr/share/man/da/man1/qtdoc.1
/usr/share/man/da/man1/reportview.1
/usr/share/man/da/man1/zonetab2pot.py.1
/usr/share/man/de/man1/adddebug.1
/usr/share/man/de/man1/cheatmake.1
/usr/share/man/de/man1/create_cvsignore.1
/usr/share/man/de/man1/create_makefile.1
/usr/share/man/de/man1/create_makefiles.1
/usr/share/man/de/man1/cvscheck.1
/usr/share/man/de/man1/cvslastchange.1
/usr/share/man/de/man1/cvslastlog.1
/usr/share/man/de/man1/cvsrevertlast.1
/usr/share/man/de/man1/cxxmetric.1
/usr/share/man/de/man1/extend_dmalloc.1
/usr/share/man/de/man1/extractrc.1
/usr/share/man/de/man1/fixincludes.1
/usr/share/man/de/man1/pruneemptydirs.1
/usr/share/man/de/man1/qtdoc.1
/usr/share/man/de/man1/reportview.1
/usr/share/man/de/man1/transxx.1
/usr/share/man/de/man1/zonetab2pot.py.1
/usr/share/man/es/man1/adddebug.1
/usr/share/man/es/man1/cheatmake.1
/usr/share/man/es/man1/create_cvsignore.1
/usr/share/man/es/man1/create_makefile.1
/usr/share/man/es/man1/create_makefiles.1
/usr/share/man/es/man1/cvscheck.1
/usr/share/man/es/man1/cvslastchange.1
/usr/share/man/es/man1/cvslastlog.1
/usr/share/man/es/man1/cvsrevertlast.1
/usr/share/man/es/man1/cxxmetric.1
/usr/share/man/es/man1/extend_dmalloc.1
/usr/share/man/es/man1/extractrc.1
/usr/share/man/es/man1/fixincludes.1
/usr/share/man/es/man1/pruneemptydirs.1
/usr/share/man/es/man1/qtdoc.1
/usr/share/man/es/man1/reportview.1
/usr/share/man/es/man1/transxx.1
/usr/share/man/es/man1/zonetab2pot.py.1
/usr/share/man/et/man1/qtdoc.1
/usr/share/man/fr/man1/adddebug.1
/usr/share/man/fr/man1/cheatmake.1
/usr/share/man/fr/man1/create_cvsignore.1
/usr/share/man/fr/man1/create_makefile.1
/usr/share/man/fr/man1/create_makefiles.1
/usr/share/man/fr/man1/cvscheck.1
/usr/share/man/fr/man1/cvslastchange.1
/usr/share/man/fr/man1/cvslastlog.1
/usr/share/man/fr/man1/cvsrevertlast.1
/usr/share/man/fr/man1/cxxmetric.1
/usr/share/man/fr/man1/extend_dmalloc.1
/usr/share/man/fr/man1/extractrc.1
/usr/share/man/fr/man1/fixincludes.1
/usr/share/man/fr/man1/pruneemptydirs.1
/usr/share/man/fr/man1/qtdoc.1
/usr/share/man/fr/man1/reportview.1
/usr/share/man/fr/man1/transxx.1
/usr/share/man/fr/man1/zonetab2pot.py.1
/usr/share/man/gl/man1/adddebug.1
/usr/share/man/gl/man1/cheatmake.1
/usr/share/man/gl/man1/create_cvsignore.1
/usr/share/man/gl/man1/create_makefiles.1
/usr/share/man/gl/man1/cvscheck.1
/usr/share/man/gl/man1/cvslastchange.1
/usr/share/man/gl/man1/cvslastlog.1
/usr/share/man/gl/man1/cvsrevertlast.1
/usr/share/man/gl/man1/cxxmetric.1
/usr/share/man/gl/man1/extend_dmalloc.1
/usr/share/man/gl/man1/extractrc.1
/usr/share/man/gl/man1/fixincludes.1
/usr/share/man/gl/man1/pruneemptydirs.1
/usr/share/man/gl/man1/qtdoc.1
/usr/share/man/gl/man1/reportview.1
/usr/share/man/gl/man1/transxx.1
/usr/share/man/gl/man1/zonetab2pot.py.1
/usr/share/man/it/man1/adddebug.1
/usr/share/man/it/man1/cheatmake.1
/usr/share/man/it/man1/create_cvsignore.1
/usr/share/man/it/man1/create_makefile.1
/usr/share/man/it/man1/create_makefiles.1
/usr/share/man/it/man1/cvscheck.1
/usr/share/man/it/man1/cvslastchange.1
/usr/share/man/it/man1/cvslastlog.1
/usr/share/man/it/man1/cvsrevertlast.1
/usr/share/man/it/man1/cxxmetric.1
/usr/share/man/it/man1/extend_dmalloc.1
/usr/share/man/it/man1/extractrc.1
/usr/share/man/it/man1/fixincludes.1
/usr/share/man/it/man1/pruneemptydirs.1
/usr/share/man/it/man1/qtdoc.1
/usr/share/man/it/man1/reportview.1
/usr/share/man/it/man1/transxx.1
/usr/share/man/it/man1/zonetab2pot.py.1
/usr/share/man/man1/adddebug.1
/usr/share/man/man1/cheatmake.1
/usr/share/man/man1/create_cvsignore.1
/usr/share/man/man1/create_makefile.1
/usr/share/man/man1/create_makefiles.1
/usr/share/man/man1/cvscheck.1
/usr/share/man/man1/cvslastchange.1
/usr/share/man/man1/cvslastlog.1
/usr/share/man/man1/cvsrevertlast.1
/usr/share/man/man1/cxxmetric.1
/usr/share/man/man1/extend_dmalloc.1
/usr/share/man/man1/extractrc.1
/usr/share/man/man1/fixincludes.1
/usr/share/man/man1/pruneemptydirs.1
/usr/share/man/man1/qtdoc.1
/usr/share/man/man1/reportview.1
/usr/share/man/man1/transxx.1
/usr/share/man/man1/zonetab2pot.py.1
/usr/share/man/nl/man1/adddebug.1
/usr/share/man/nl/man1/cheatmake.1
/usr/share/man/nl/man1/create_cvsignore.1
/usr/share/man/nl/man1/create_makefile.1
/usr/share/man/nl/man1/create_makefiles.1
/usr/share/man/nl/man1/cvscheck.1
/usr/share/man/nl/man1/cvslastchange.1
/usr/share/man/nl/man1/cvslastlog.1
/usr/share/man/nl/man1/cvsrevertlast.1
/usr/share/man/nl/man1/cxxmetric.1
/usr/share/man/nl/man1/extend_dmalloc.1
/usr/share/man/nl/man1/extractrc.1
/usr/share/man/nl/man1/fixincludes.1
/usr/share/man/nl/man1/pruneemptydirs.1
/usr/share/man/nl/man1/qtdoc.1
/usr/share/man/nl/man1/reportview.1
/usr/share/man/nl/man1/transxx.1
/usr/share/man/nl/man1/zonetab2pot.py.1
/usr/share/man/pt/man1/adddebug.1
/usr/share/man/pt/man1/cheatmake.1
/usr/share/man/pt/man1/create_cvsignore.1
/usr/share/man/pt/man1/create_makefile.1
/usr/share/man/pt/man1/create_makefiles.1
/usr/share/man/pt/man1/cvscheck.1
/usr/share/man/pt/man1/cvslastchange.1
/usr/share/man/pt/man1/cvslastlog.1
/usr/share/man/pt/man1/cvsrevertlast.1
/usr/share/man/pt/man1/cxxmetric.1
/usr/share/man/pt/man1/extend_dmalloc.1
/usr/share/man/pt/man1/extractrc.1
/usr/share/man/pt/man1/fixincludes.1
/usr/share/man/pt/man1/pruneemptydirs.1
/usr/share/man/pt/man1/qtdoc.1
/usr/share/man/pt/man1/reportview.1
/usr/share/man/pt/man1/transxx.1
/usr/share/man/pt/man1/zonetab2pot.py.1
/usr/share/man/pt_BR/man1/adddebug.1
/usr/share/man/pt_BR/man1/cheatmake.1
/usr/share/man/pt_BR/man1/create_cvsignore.1
/usr/share/man/pt_BR/man1/create_makefile.1
/usr/share/man/pt_BR/man1/create_makefiles.1
/usr/share/man/pt_BR/man1/cvscheck.1
/usr/share/man/pt_BR/man1/cvslastchange.1
/usr/share/man/pt_BR/man1/cvslastlog.1
/usr/share/man/pt_BR/man1/cvsrevertlast.1
/usr/share/man/pt_BR/man1/cxxmetric.1
/usr/share/man/pt_BR/man1/extend_dmalloc.1
/usr/share/man/pt_BR/man1/extractrc.1
/usr/share/man/pt_BR/man1/fixincludes.1
/usr/share/man/pt_BR/man1/pruneemptydirs.1
/usr/share/man/pt_BR/man1/qtdoc.1
/usr/share/man/pt_BR/man1/reportview.1
/usr/share/man/pt_BR/man1/transxx.1
/usr/share/man/pt_BR/man1/zonetab2pot.py.1
/usr/share/man/sv/man1/adddebug.1
/usr/share/man/sv/man1/cheatmake.1
/usr/share/man/sv/man1/create_cvsignore.1
/usr/share/man/sv/man1/create_makefile.1
/usr/share/man/sv/man1/create_makefiles.1
/usr/share/man/sv/man1/cvscheck.1
/usr/share/man/sv/man1/cvslastchange.1
/usr/share/man/sv/man1/cvslastlog.1
/usr/share/man/sv/man1/cvsrevertlast.1
/usr/share/man/sv/man1/cxxmetric.1
/usr/share/man/sv/man1/extend_dmalloc.1
/usr/share/man/sv/man1/extractrc.1
/usr/share/man/sv/man1/fixincludes.1
/usr/share/man/sv/man1/pruneemptydirs.1
/usr/share/man/sv/man1/qtdoc.1
/usr/share/man/sv/man1/reportview.1
/usr/share/man/sv/man1/transxx.1
/usr/share/man/sv/man1/zonetab2pot.py.1
/usr/share/man/uk/man1/adddebug.1
/usr/share/man/uk/man1/cheatmake.1
/usr/share/man/uk/man1/create_cvsignore.1
/usr/share/man/uk/man1/create_makefile.1
/usr/share/man/uk/man1/create_makefiles.1
/usr/share/man/uk/man1/cvscheck.1
/usr/share/man/uk/man1/cvslastchange.1
/usr/share/man/uk/man1/cvslastlog.1
/usr/share/man/uk/man1/cvsrevertlast.1
/usr/share/man/uk/man1/cxxmetric.1
/usr/share/man/uk/man1/extend_dmalloc.1
/usr/share/man/uk/man1/extractrc.1
/usr/share/man/uk/man1/fixincludes.1
/usr/share/man/uk/man1/pruneemptydirs.1
/usr/share/man/uk/man1/qtdoc.1
/usr/share/man/uk/man1/reportview.1
/usr/share/man/uk/man1/transxx.1
/usr/share/man/uk/man1/zonetab2pot.py.1
