#
Summary:	XSplash
Summary(pl.UTF-8):	XSplash
Name:		xsplash
Version:	0.8.5
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://launchpad.net/xsplash/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	9de23920734a54b6c9e04e347a84cba8
URL:		https://launchpad.net/xsplash/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSplash is a software project in the Ubuntu community that uses the X
Window System to replace the scrolling-text screens that appear while
booting a Linux-based computer with a graphical splash screen.

#%description -l pl.UTF-8

%prep
%setup -q

%build
%configure \
	--with-user=root \
	--with-dbus-sys=/etc/dbus-1/system.d/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(4755,root,root) %{_bindir}/xsplash
/etc/dbus-1/system.d/xsplash.conf
%dir %{_datadir}/images
%dir %{_datadir}/images/xsplash
%{_datadir}/images/xsplash/*
