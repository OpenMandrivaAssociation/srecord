Name:		srecord
Version:	1.59
Release:	1
Summary:	Manipulate EPROM load files
Group:		Development/Other
License:	GPLv3+ and LGPLv3+
URL:		http://srecord.sourceforge.net/
Source0:	http://downloads.sourceforge.net/srecord/srecord-%{version}.tar.gz
BuildRequires:	diffutils, sharutils, groff, boost-devel, libgcrypt-devel, libtool

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

%package devel
Summary:	Development headers and libraries for srecord
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for developing applications against
srecord.

%prep
%setup -q

%build
%configure
# Fails to build in SMP machines using "make %{?_smp_mflags}"
%make

%install
mkdir -p %{buildroot}%{_libdir}
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la
chmod +x %{buildroot}%{_libdir}/libsrecord.so.*

%check
# Test scripts requirements: cmp, diff, uudecode
make sure

%files
%doc LICENSE BUILDING README
%{_bindir}/*
%{_libdir}/libsrecord.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man5/*.5*

%files devel
%{_includedir}/srecord/
%{_libdir}/libsrecord.so
%{_libdir}/pkgconfig/srecord.pc
