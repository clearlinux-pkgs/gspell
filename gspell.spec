#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
Name     : gspell
Version  : 1.12.2
Release  : 29
URL      : https://download.gnome.org/sources/gspell/1.12/gspell-1.12.2.tar.xz
Source0  : https://download.gnome.org/sources/gspell/1.12/gspell-1.12.2.tar.xz
Summary  : Spell-checking for GTK applications
Group    : Development/Tools
License  : LGPL-2.1
Requires: gspell-bin = %{version}-%{release}
Requires: gspell-data = %{version}-%{release}
Requires: gspell-lib = %{version}-%{release}
Requires: gspell-license = %{version}-%{release}
Requires: gspell-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libc6-locale
BuildRequires : libxslt-bin
BuildRequires : llvm
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(enchant-2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package bin
Summary: bin components for the gspell package.
Group: Binaries
Requires: gspell-data = %{version}-%{release}
Requires: gspell-license = %{version}-%{release}

%description bin
bin components for the gspell package.


%package data
Summary: data components for the gspell package.
Group: Data

%description data
data components for the gspell package.


%package dev
Summary: dev components for the gspell package.
Group: Development
Requires: gspell-lib = %{version}-%{release}
Requires: gspell-bin = %{version}-%{release}
Requires: gspell-data = %{version}-%{release}
Provides: gspell-devel = %{version}-%{release}
Requires: gspell = %{version}-%{release}

%description dev
dev components for the gspell package.


%package doc
Summary: doc components for the gspell package.
Group: Documentation

%description doc
doc components for the gspell package.


%package lib
Summary: lib components for the gspell package.
Group: Libraries
Requires: gspell-data = %{version}-%{release}
Requires: gspell-license = %{version}-%{release}

%description lib
lib components for the gspell package.


%package license
Summary: license components for the gspell package.
Group: Default

%description license
license components for the gspell package.


%package locales
Summary: locales components for the gspell package.
Group: Default

%description locales
locales components for the gspell package.


%prep
%setup -q -n gspell-1.12.2
cd %{_builddir}/gspell-1.12.2
pushd ..
cp -a gspell-1.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701964590
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
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

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
export SOURCE_DATE_EPOCH=1701964590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gspell
cp %{_builddir}/gspell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gspell/5013d109e2fe11116d2b062bb46114a398276501 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang gspell-1
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gspell-app1
/usr/bin/gspell-app1

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gspell-1.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gspell-1.deps
/usr/share/vala/vapi/gspell-1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gspell-1/gspell/gspell-checker-dialog.h
/usr/include/gspell-1/gspell/gspell-checker.h
/usr/include/gspell-1/gspell/gspell-entry-buffer.h
/usr/include/gspell-1/gspell/gspell-entry.h
/usr/include/gspell-1/gspell/gspell-enum-types.h
/usr/include/gspell-1/gspell/gspell-language-chooser-button.h
/usr/include/gspell-1/gspell/gspell-language-chooser-dialog.h
/usr/include/gspell-1/gspell/gspell-language-chooser.h
/usr/include/gspell-1/gspell/gspell-language.h
/usr/include/gspell-1/gspell/gspell-navigator-text-view.h
/usr/include/gspell-1/gspell/gspell-navigator.h
/usr/include/gspell-1/gspell/gspell-text-buffer.h
/usr/include/gspell-1/gspell/gspell-text-view.h
/usr/include/gspell-1/gspell/gspell.h
/usr/lib64/libgspell-1.so
/usr/lib64/pkgconfig/gspell-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gspell-1.0/GspellChecker.html
/usr/share/gtk-doc/html/gspell-1.0/GspellCheckerDialog.html
/usr/share/gtk-doc/html/gspell-1.0/GspellEntry.html
/usr/share/gtk-doc/html/gspell-1.0/GspellEntryBuffer.html
/usr/share/gtk-doc/html/gspell-1.0/GspellLanguage.html
/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooser.html
/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooserButton.html
/usr/share/gtk-doc/html/gspell-1.0/GspellLanguageChooserDialog.html
/usr/share/gtk-doc/html/gspell-1.0/GspellNavigator.html
/usr/share/gtk-doc/html/gspell-1.0/GspellNavigatorTextView.html
/usr/share/gtk-doc/html/gspell-1.0/GspellTextBuffer.html
/usr/share/gtk-doc/html/gspell-1.0/GspellTextView.html
/usr/share/gtk-doc/html/gspell-1.0/GtkEntry-support.html
/usr/share/gtk-doc/html/gspell-1.0/GtkTextView-support.html
/usr/share/gtk-doc/html/gspell-1.0/annexes.html
/usr/share/gtk-doc/html/gspell-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/gspell-1.0/api-index-1-2.html
/usr/share/gtk-doc/html/gspell-1.0/api-index-1-4.html
/usr/share/gtk-doc/html/gspell-1.0/api-index-1-6.html
/usr/share/gtk-doc/html/gspell-1.0/api-index-full.html
/usr/share/gtk-doc/html/gspell-1.0/api-reference.html
/usr/share/gtk-doc/html/gspell-1.0/core-classes.html
/usr/share/gtk-doc/html/gspell-1.0/gspell-1.0.devhelp2
/usr/share/gtk-doc/html/gspell-1.0/home.png
/usr/share/gtk-doc/html/gspell-1.0/index.html
/usr/share/gtk-doc/html/gspell-1.0/intro.html
/usr/share/gtk-doc/html/gspell-1.0/language-choosers.html
/usr/share/gtk-doc/html/gspell-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gspell-1.0/left.png
/usr/share/gtk-doc/html/gspell-1.0/object-tree.html
/usr/share/gtk-doc/html/gspell-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gspell-1.0/right.png
/usr/share/gtk-doc/html/gspell-1.0/spell-checker-dialog.html
/usr/share/gtk-doc/html/gspell-1.0/style.css
/usr/share/gtk-doc/html/gspell-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gspell-1.0/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgspell-1.so.2.3.2
/usr/lib64/libgspell-1.so.2
/usr/lib64/libgspell-1.so.2.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gspell/5013d109e2fe11116d2b062bb46114a398276501

%files locales -f gspell-1.lang
%defattr(-,root,root,-)

