#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gspell
Version  : 1.6.1
Release  : 6
URL      : https://download.gnome.org/sources/gspell/1.6/gspell-1.6.1.tar.xz
Source0  : https://download.gnome.org/sources/gspell/1.6/gspell-1.6.1.tar.xz
Summary  : Spell checking for GTK+
Group    : Development/Tools
License  : LGPL-2.1
Requires: gspell-bin
Requires: gspell-lib
Requires: gspell-doc
Requires: gspell-locales
Requires: gspell-data
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libc6-locale
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : valgrind

%description
gspell - a spell-checking library for GTK+ applications
=======================================================

%package bin
Summary: bin components for the gspell package.
Group: Binaries
Requires: gspell-data

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
Requires: gspell-lib
Requires: gspell-bin
Requires: gspell-data
Provides: gspell-devel

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
Requires: gspell-data

%description lib
lib components for the gspell package.


%package locales
Summary: locales components for the gspell package.
Group: Default

%description locales
locales components for the gspell package.


%prep
%setup -q -n gspell-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524079575
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1524079575
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
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
/usr/lib64/libgspell-1.so.1
/usr/lib64/libgspell-1.so.1.3.0

%files locales -f gspell-1.lang
%defattr(-,root,root,-)

