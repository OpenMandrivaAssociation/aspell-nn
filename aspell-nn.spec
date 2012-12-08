%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50.1-1
%define languageenglazy Nynorsk
%define languagecode nn
%define lc_ctype nn_NO

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.1
Release:       %mkrel 13
Group:         System/Internationalization
Source:	       http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-11mdv2011.0
+ Revision: 662857
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-10mdv2011.0
+ Revision: 603449
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-9mdv2010.1
+ Revision: 518950
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-8mdv2010.0
+ Revision: 413092
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.1-7mdv2009.1
+ Revision: 350082
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.1-6mdv2009.0
+ Revision: 220434
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.1-5mdv2008.1
+ Revision: 182507
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.1-4mdv2008.1
+ Revision: 148837
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-3mdv2007.0
+ Revision: 123341
- Import aspell-nn

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.1-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.1-1mdk
- first version

