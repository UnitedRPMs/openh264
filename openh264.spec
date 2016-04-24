# globals for openh264-1.5.0-20160419-2610ab1.tar.xz
%global gitdate 20160419
%global gitversion 2610ab1
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}

Name:         	openh264
Summary:      	Open Source H.264 Codec
URL:          	http://www.openh264.org/
Group:        	System/Libraries
License:      	BSD
Version:      	1.5.0
Release:        1%{?gver}%{dist}
Source0:	%{name}-%{version}-%{snapshot}.tar.xz
Source1: 	%{name}-snapshot.sh
Patch:		fix_path.patch
BuildRequires: 	nasm git

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -n openh264

%ifarch x86_64
%patch -p0
%else
sed -i 's/PREFIX=\/usr\/local/PREFIX=\/usr/g' Makefile
%endif

%build
make %{_smp_mflags} PREFIX=/usr

%install
%make_install PREFIX=/usr
%ifarch x86_64
sed -i 's|${prefix}/lib|${prefix}/lib64|g' %{buildroot}/%{_libdir}/pkgconfig/openh264.pc
%endif

%files
%doc README.md LICENSE CONTRIBUTORS
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/wels
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.5.0-20160419-2610ab1-1
- Initial build rpm
