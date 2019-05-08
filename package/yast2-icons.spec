#
# spec file for package yast2-icons
#
# Copyright (c) 2019 Stasiek Michalski <hellcp@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           yast2-icons
Version:        4.2.0
Release:        0
Summary:        YaST2 - Icons
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-icons

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  yast2-devtools
BuildRequires:  rubygem(yast-rake)
Supplements:    (yast2-theme and hicolor-icon-theme)

Requires:       hicolor-icon-theme
Provides:       yast2-icons = %{version}
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}

BuildArch:      noarch

%description
Contains base icon theme for YaST2.

%if 0%{?is_opensuse}
%package oxygen
Summary:        YaST2 - Oxygen icon theme
Group:          System/YaST
Supplements:    (yast2-theme and oxygen5-icon-theme)
PreReq:         yast2-branding = %{version}
BuildRequires:  oxygen5-icon-theme
Requires:       oxygen5-icon-theme
Provides:       yast2-theme-oxygen = %{version}
Obsoletes:      yast2-theme-oxygen < %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}

%description oxygen
Contains icons in KDE Oxygen style (from KDE Plasma 4).

%package breeze
Summary:        YaST2 - Breeze icon theme
Group:          System/YaST
Supplements:    (yast2-theme and breeze5-icons)
PreReq:         yast2-branding = %{version}
BuildRequires:  breeze5-icons
Requires:       breeze5-icons
Provides:       yast2-theme-breeze = %{version}
Obsoletes:      yast2-theme-breeze < %{version}

%description breeze
Contains icons in KDE Breeze style (from KDE Plasma 5).
%endif

%prep
%autosetup -q

%build
mkdir -p %{buildroot}%{_datadir}/icons/breeze/apps/32
mkdir -p %{buildroot}%{_datadir}/icons/breeze/apps/48
mkdir -p %{buildroot}%{_datadir}/icons/breeze-dark/apps/32
mkdir -p %{buildroot}%{_datadir}/icons/breeze-dark/apps/48
cd icons/breeze/
sh make-symlinks.sh %{buildroot}%{_datadir}/icons/breeze
sh make-symlinks.sh %{buildroot}%{_datadir}/icons/breeze-dark

%install
%{yast_install}

%if !0%{?is_opensuse}
# SLE doesn't have those icon themes:
rm -rf %{buildroot}%{yast_icondir}/oxygen
rm -rf %{buildroot}%{yast_icondir}/breeze
rm -rf %{buildroot}%{yast_icondir}/breeze-dark
%endif

%fdupes %{buildroot}%{yast_icondir}

%files
%license COPYING
%doc %{yast_docdir}
%{yast_icondir}/hicolor/*

%if 0%{?is_opensuse}
%files oxygen
%{yast_icondir}/oxygen/*

%files breeze
%{yast_icondir}/breeze/*
%{yast_icondir}/breeze-dark/*
%endif

%changelog
