Name: hunspell-ne
Summary: Nepali hunspell dictionaries
Version: 20080425
Release: 8%{?dist}
Source: http://nepalinux.org/downloads/ne_NP_dict.zip
Group: Applications/Text
URL: http://nepalinux.org/downloads
License: LGPLv2
BuildArch: noarch

Requires: hunspell

%description
Nepali hunspell dictionaries.

%prep
%setup -q -c -n ne_NP_dict
sed -i 's|चलन/चल्ती/15,22|चलनचल्ती/15,22|g' ne_NP.dic
sed -i 's|निजामती/I15,22|निजामती/15,22|g' ne_NP.dic

# Remove ^M and trailing whitespace characters
sed -i 's/\r//;s/[ \t]*$//' ne_NP.dic

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ne_NP_aliases="ne_IN"
for lang in $ne_NP_aliases; do
        ln -s ne_NP.aff $lang.aff
        ln -s ne_NP.dic $lang.dic
done
popd

%files
%doc README_ne_NP.txt 
%{_datadir}/myspell/*

%changelog
* Wed May 29 2013 Parag <pnemade AT redhat DOT com> - 20080425-8
- Removed BR:dos2unix and instead use sed (rh# 967638)

* Tue May 28 2013 Parag <pnemade AT redhat DOT com> - 20080425-7
- Resolves:rh#959987: Error message: “0 is wrong flag id” occurs when using hunspell-ne
- Resolves:rh#967638: ne_NP.dic contains both CRLF and LF line terminators

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080425-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080425-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20080425-4
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080425-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080425-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 20080425-1
- Update to next upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Parag <pnemade@redhat.com> - 20061217-3
- Resolves:rh#475982 - Perhaps hunspell-ne suffices for ne_IN as well as ne_NP 

* Mon Jan 21 2008 Parag <pnemade@redhat.com> - 20061217-2
- Corrected License tag.

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20061217-1
- Initial Fedora release
