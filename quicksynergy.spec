Name:		quicksynergy
Version:	0.9.0
Release:	2
Summary:	Share keyboard and mouse between computers
Group:		System/Configuration/Hardware
License:	GPLv2+
URL:		http://code.google.com/p/quicksynergy/
Source0:	http://quicksynergy.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	synergy

%description
QuickSynergy is a graphical interface (GUI) for easily configuring Synergy2,
an application that allows the user to share his mouse and keyboard between
two or more computers.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=QuickSynergy
Comment=Share keyboard and mouse between computers
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=false
StartupNotify=true
Categories=System;Utility;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert src/logo/qslogo.png -resize ${N}x${N} $N.png;
install -D -m 0644 16.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING AUTHORS README
%{_bindir}/quicksynergy
%{_datadir}/applications/quicksynergy.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

