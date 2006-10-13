%define		_decoration Alphacube
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/32099-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	e5213ead2810f8b9f7cfde80f11035fa
URL:		http://www.kde-look.org/content/show.php?content=32099
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_decoration} is an port of GNOME metacity theme, originating
in one of Mac OS X theme.

%description -l pl
%{_decoration} to port motywu z GNOME, maj±cego swoje korzenie
w jednym z motywów Mac OS X.

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
#%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
