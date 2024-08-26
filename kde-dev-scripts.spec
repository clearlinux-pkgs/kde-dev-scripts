#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kde-dev-scripts
Version  : 24.08.0
Release  : 70
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kde-dev-scripts-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kde-dev-scripts-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kde-dev-scripts-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GFDL-1.2 GPL-2.0
Requires: kde-dev-scripts-bin = %{version}-%{release}
Requires: kde-dev-scripts-data = %{version}-%{release}
Requires: kde-dev-scripts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kdoctools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kde-dev-scripts-24.08.0
cd %{_builddir}/kde-dev-scripts-24.08.0
pushd ..
cp -a kde-dev-scripts-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724645630
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724645630
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-dev-scripts
cp %{_builddir}/kde-dev-scripts-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kde-dev-scripts/a21ac62aee75f8fcb26b1de6fc90e5eea271854c || :
cp %{_builddir}/kde-dev-scripts-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kde-dev-scripts/fcbf818f92ef8679a88f3778b12b4c8b5810545b || :
cp %{_builddir}/kde-dev-scripts-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kde-dev-scripts/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/adddebug
/usr/bin/addmocincludes
/usr/bin/build-progress.sh
/usr/bin/c++-copy-class-and-file
/usr/bin/c++-rename-class-and-file
/usr/bin/cheatmake
/usr/bin/clean-forward-declaration.sh
/usr/bin/clean-includes.sh
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
/usr/bin/port_new_gitlab_ci_template.sh
/usr/bin/pruneemptydirs
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
/usr/share/package-licenses/kde-dev-scripts/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kde-dev-scripts/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
/usr/share/package-licenses/kde-dev-scripts/fcbf818f92ef8679a88f3778b12b4c8b5810545b
