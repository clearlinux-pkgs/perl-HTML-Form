#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-HTML-Form
Version  : 6.12
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Form-6.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Form-6.12.tar.gz
Summary  : 'Class that represents an HTML form element'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Form-license = %{version}-%{release}
Requires: perl-HTML-Form-perl = %{version}-%{release}
Requires: perl(HTML::Tagset)
Requires: perl(HTML::TokeParser)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Request::Common)
Requires: perl(HTTP::Response)
Requires: perl(LWP::MediaTypes)
Requires: perl(URI)
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Tagset)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-HTML-Form package.
Group: Development
Provides: perl-HTML-Form-devel = %{version}-%{release}
Requires: perl-HTML-Form = %{version}-%{release}

%description dev
dev components for the perl-HTML-Form package.


%package license
Summary: license components for the perl-HTML-Form package.
Group: Default

%description license
license components for the perl-HTML-Form package.


%package perl
Summary: perl components for the perl-HTML-Form package.
Group: Default
Requires: perl-HTML-Form = %{version}-%{release}

%description perl
perl components for the perl-HTML-Form package.


%prep
%setup -q -n HTML-Form-6.12
cd %{_builddir}/HTML-Form-6.12
pushd ..
cp -a HTML-Form-6.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Form
cp %{_builddir}/HTML-Form-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-Form/46f8922a53eef3bc16b11460b9091e42c3351881 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Form.3
/usr/share/man/man3/HTML::Form::FileInput.3
/usr/share/man/man3/HTML::Form::IgnoreInput.3
/usr/share/man/man3/HTML::Form::ImageInput.3
/usr/share/man/man3/HTML::Form::Input.3
/usr/share/man/man3/HTML::Form::KeygenInput.3
/usr/share/man/man3/HTML::Form::ListInput.3
/usr/share/man/man3/HTML::Form::SubmitInput.3
/usr/share/man/man3/HTML::Form::TextInput.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Form/46f8922a53eef3bc16b11460b9091e42c3351881

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
