Summary:	Linux PCI Utilities
Summary(es):	Utilitarios Linux para PCI
Summary(pl):	Narz�dzia do manipulacji ustawieniami urz�dze� PCI
Summary(pt_BR):	Utilit�rios para PCI do Linux
Summary(uk):	���̦�� ������ � PCI ����������
Summary(ru):	������� ������ � PCI ������������
Name:		pciutils
Version:	2.1.10
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Source2:	http://pciids.sourceforge.net/pci.ids
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-bufsiz.patch
Patch2:		%{name}-devel.patch
Patch4:		%{name}-man.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/lib
%define		_datadir	%{_prefix}/share/misc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l es
Utilitarios Linux para PCI.

%description -l pl
Pakiet zawiera narz�dzia do ustawiania i odczytywania informacji o
urz�dzeniach pod��czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udost�pniaj�cego odpowiednie informacje
poprzez /proc/bus/pci).

%description -l pt_BR
Este pacote cont�m v�rios utilit�rios para inspe��o e configura��o de
dispositivos conectados ao barramento PCI do seu computador.

%description -l ru
����� pciutils �������� ������� ��� ��������������� � ����������������
���������, ������������ � PCI ����.

��� ������ ���� �������� ���������� ������� ���������� /proc/bus/pci.

%description -l uk
����� pciutils ͦ����� ���̦�� ��� ������������� �� ���Ʀ���������
������ϧ�, Ц�'������� �� PCI ����.

��� ������ æ ���̦�� ���������� �������Ԧ ���������� /proc/bus/pci.

%package devel
Summary:	pciutils development files (for PLD-installer)
Summary(es):	Biblioteca de desarrollo para aplicaciones que trabajan con el bus PCI en Linux
Summary(pl):	pliki developerskie pciutils
Summary(pt_BR):	Biblioteca de desenvolvimentos para aplica��es que trabalhem com o barramento PCI no Linux
Summary(ru):	������ � ������ ����� ��� ���������� ��������, ���������� � ����� PCI
Summary(uk):	������ �� ��ۦ ����� ��� �������� �������, �� �������� � ����� PCI
Group:		Development/Libraries

%description devel
You need this package if (and probably only if) you are going to build
PLD-installer.

%description devel -l es
Biblioteca de desarrollo para aplicaciones que trabajen con el bus PCI
en Linux.

%description devel -l pl
Prawdopodobnie jedynym powodem dla kt�rego mo�esz potrzebowa� tego
pakietu jest kompilacja instalatora PLD.

%description devel -l pt_BR
Biblioteca de desenvolvimentos para aplica��es que trabalhem com o
barramento PCI no Linux.

%description devel -l ru
���� ����� �������� ������ � ������ ����� ��� ���������� ��������
�������������� � ��������������� ����������, ������������ � ���� PCI.

%description devel -l uk
��� ����� ͦ����� ������ �� ��ۦ ����� ��� �������� �������, ��
����������� �� ���Ʀ������� ������ϧ, Ц�'����Φ �� ���� PCI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
# paranoid check whether pci.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE2}`" -lt "`wc -l < pci.ids`" ] ; then
	echo "pci.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE2} .
%{__make} OPT="%{rpmcflags} -fomit-frame-pointer"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci	$RPM_BUILD_ROOT%{_sbindir}
install *.h lib/[ch]*.h	$RPM_BUILD_ROOT%{_includedir}/pci
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids		$RPM_BUILD_ROOT%{_datadir}
install lib/libpci.a	$RPM_BUILD_ROOT%{_libdir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_datadir}/pci.ids
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%lang(ja) %{_mandir}/ja/man8/*
%lang(pl) %{_mandir}/pl/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpci.a
%dir %{_includedir}/pci
%{_includedir}/pci/*.h
