#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gspell
Version  : 1.11.1
Release  : 21
URL      : https://download.gnome.org/sources/gspell/1.11/gspell-1.11.1.tar.xz
Source0  : https://download.gnome.org/sources/gspell/1.11/gspell-1.11.1.tar.xz
Summary  : Spell-checking for GTK applications
Group    : Development/Tools
License  : LGPL-2.1
Requires: gspell-bin = %{version}-%{release}
Requires: gspell-data = %{version}-%{release}
Requires: gspell-lib = %{version}-%{release}
Requires: gspell-license = %{version}-%{release}
Requires: gspell-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libc6-locale
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(enchant-2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)

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
%setup -q -n gspell-1.11.1
cd %{_builddir}/gspell-1.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664152535
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1664152535
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gspell
cp %{_builddir}/gspell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gspell/5013d109e2fe11116d2b062bb46114a398276501 || :
%make_install
%find_lang gspell-1

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/include/gspell-1/gspell/gspell-version.h
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
/usr/lib64/libgspell-1.so.2
/usr/lib64/libgspell-1.so.2.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gspell/5013d109e2fe11116d2b062bb46114a398276501

%files locales -f gspell-1.lang
%defattr(-,root,root,-)

