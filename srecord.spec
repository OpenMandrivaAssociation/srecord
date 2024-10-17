%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Manipulate EPROM load files
Name:		srecord
Version:	1.62
Release:	2
License:	GPLv3+ and LGPLv3+
Group:		Development/Other
Url:		https://srecord.sourceforge.net/
Source0:	http://downloads.sourceforge.net/srecord/srecord-%{version}.tar.gz
BuildRequires:	diffutils
BuildRequires:	ghostscript-common
BuildRequires:	groff
BuildRequires:	libtool
BuildRequires:	sharutils
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libgcrypt)

%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary.  These file formats may be read
  and written.  Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add checksums
  to the data, crop to keep address ranges, exclude to remove address
  ranges, fill to plug holes in the data, length to insert the data
  length, maximum to insert the data address maximum, minimum to insert
  the data address minimum, offset to adjust addresses, and split for
  wide data buses and memory striping.

More than one filter may be applied to each input file.  Different filters
may be applied to each input file.  All filters may be applied to all
file formats.

%files
%doc LICENSE BUILDING README
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for SRecord
Group:		System/Libraries
Conflicts:	%{name} < 1.62

%description -n %{libname}
Shared library for SRecord.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development headers and libraries for SRecord
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name}-devel < 1.62
Obsoletes:	%{name}-devel < 1.62
Conflicts:	%{name} < 1.62

%description -n %{devname}
Development headers and libraries for developing applications against SRecord.

%files -n %{devname}
%{_includedir}/srecord/
%{_libdir}/libsrecord.so
%{_libdir}/pkgconfig/srecord.pc
%{_mandir}/man3/*.3*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
mkdir -p %{buildroot}%{_libdir}
%makeinstall_std

%check
# Test scripts requirements: cmp, diff, uudecode
make sure

