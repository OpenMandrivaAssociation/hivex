# Make ocaml happy
%global _disable_ld_no_undefined 1

%define libname %mklibname hivex 0
%define devname %mklibname -d hivex

Name: hivex
Version: 1.3.18
Release: 1
Source0: http://download.libguestfs.org/hivex/hivex-%{version}.tar.gz
Summary: Tool for editing the Registry in Windows guest images
Group: System/Libraries
URL: http://libguestfs.org/
License: GPL
BuildRequires: ocaml ocaml-findlib perl(Pod::Html)
BuildRequires: pkgconfig(python3)
BuildRequires: make
Requires: %{libname} = %{EVRD}

%description
Hivex is a library for extracting the contents of Windows Registry "hive"
files.

It is designed to be secure against buggy or malicious registry files.

Unlike other tools in this area, it doesn't use the textual .REG
format, because parsing that is as much trouble as parsing the original
binary format.

Instead it makes the file available through a C API, and then wraps this
API in higher level scripting and GUI tools.

%package -n %{libname}
Summary: Library for editing the Registry in Windows guest images
Group: System/Libraries

%description -n %{libname}
Library for editing the Registry in Windows guest images

%package -n %{devname}
Summary: Development files for the Hivex Windows registry reader
Group: Development/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the Hivex Windows registry reader

%package -n python-%{name}
Summary: Python bindings for the Hivex Windows registry reader
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n python-%{name}
Python bindings for the Hivex Windows registry reader

%package -n ocaml-%{name}
Summary: OCaml bindings for the Hivex Windows registry reader
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n ocaml-%{name}
OCaml bindings for the Hivex Windows registry reader

%prep
%autosetup -p1
%configure

%build
%make

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/hivexget
%{_bindir}/hivexml
%{_bindir}/hivexsh
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/libhivex.so.0*

%files -n %{devname}
%{_includedir}/hivex.h
%{_libdir}/pkgconfig/hivex.pc
%{_libdir}/libhivex.so
%{_mandir}/man3/*.3*

%files -n ocaml-%{name}
%{_libdir}/ocaml/hivex
%{_libdir}/ocaml/stublibs/dllmlhivex.so*

%files -n python-%{name}
%{py_platsitedir}/hivex
%{py_platsitedir}/*.so
