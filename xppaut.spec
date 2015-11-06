Name: xppaut
Version: 6.00
Release: 1%{?dist}
Summary: XPPAUT the differential equations tool
License: Distributable (check README)
Source0: ftp://ftp.math.pitt.edu/pub/bardware/xppaut%{version}.tar.gz
Patch0: xppaut6.00-fixes2.patch
URL: http://www.math.pitt.edu/~bard/xpp/xpp.html
BuildRequires: gcc-c++ libX11-devel xorg-x11-xbitmaps

%description
XPPAUT is a tool for solving differential equations, 
difference equations, delay equations, functional 
equations, boundary value problems, and stochastic 
equations.

%prep
%setup -c
%patch0 -p1 -b .fixes2

%build
make
cd mkavi
make mkavi
cd ../ode
rm -f *dylib *so

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/xppaut
cp ode/* *.bitmap *.opt xppaut mkavi/mkavi $RPM_BUILD_ROOT/usr/share/xppaut
ln -fs %{_prefix}/share/xppaut/xppaut $RPM_BUILD_ROOT/usr/bin/xppaut
cat > $RPM_BUILD_ROOT/usr/bin/xpp <<ENDSCRIPT
#!/bin/sh
echo "Launching xppaut..."
echo "Please note that *.ode configuration files reside in /usr/share/xppaut directory and documentation is in %{_docdir}/%{name}-%{version} directory."
/usr//bin/xppaut "\$@"
ENDSCRIPT
chmod a+rx $RPM_BUILD_ROOT/usr/bin/xpp

chmod a+rx `find $RPM_BUILD_ROOT/usr/share/ -type d -print`

%files
%defattr(-,root,root)
%doc README
%doc *.ps
%doc *.pdf
%doc *.tex
%doc help/*
/usr/bin/xpp*
/usr/share/xppaut

%changelog
* Fri Nov  6 2015 Adrian Alves <alvesadrian@fedoraproject.org> 6.00-1
- Initial build
