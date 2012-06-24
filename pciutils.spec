Summary:	Linux PCI utilities
Summary(cs):	Linuxov� utility pro PCI
Summary(da):	PCI-bus-relaterede v�rkt�jer
Summary(de):	PCI-Bus verwandte Dienstprogramme
Summary(es):	Utilitarios Linux para PCI
Summary(fr):	Utilitaires relatifs au bus PCI
Summary(it):	Utility correlate al bus PCI
Summary(ja):	PCI �Х���Ϣ�桼�ƥ���ƥ�
Summary(ko):	PCI ���� ���� ��ƿ��Ƽ��
Summary(nb):	PCI-buss-relaterte verkt�y
Summary(pl):	Narz�dzia do manipulacji ustawieniami urz�dze� PCI
Summary(pt):	Utilit�rios relacionados com o 'bus' PCI
Summary(pt_BR):	Utilit�rios para PCI do Linux
Summary(ru):	������� ������ � PCI ������������
Summary(sv):	PCI-bussrelaterade verktyg
Summary(uk):	���̦�� ������ � PCI ����������
Summary(zh_CN):	PCI ������صĹ��ߡ�
Name:		pciutils
Version:	2.1.11
Release:	9
License:	GPL
Group:		Applications/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
# Source0-md5:	1d40f90aaae69594790bdb8ff90b4a41
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/pciutils-non-english-man-pages.tar.bz2
# Source1-md5:	1ac48f433b1995044e14c24513992211
Source2:	http://pciids.sourceforge.net/pci.ids
# NoSource2-md5:	3db20d38b4d78f46ee9c478293a75350
Patch0:		%{name}-bufsiz.patch
Patch1:		%{name}-devel.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-segv.patch
Patch4:		%{name}-pci_h.patch
Patch5:		%{name}-pcimodules.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/%{_lib}
%define		_datadir	/etc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l cs
Bal��ek pciutils obsahuje r�zn� programy pro prohl�en� a nastavov�n�
za��zen� p�ipojen�ch na sb�rnici PCI. Obsa�en� programy vy�aduj� j�dro
verze 2.1.82 nebo nov�j�� (podporuj�c� rozhran� /proc/bus/pci).

%description -l da
Pakken pciutils indeholder forskellige v�rkt�jer for at undres�ge og
ops�tte enheder koplet til PCI-bussen. V�rkt�jet kr�ver kerneversion
2.1.82 eller senere (som underst�tter gr�nsefladen /proc/bus/pci).

%description -l de
Das pciutils Paket enth�lt verschiedene Dienstprogramme f�r das
�berpr�fen und Konfigurieren von Ger�ten, die an den PCI-Bus
angeschlossen sind. Die bereitgestellten Dienstprogramme erfordern
Kernel Version 2.1.82 oder neuer (und die darin implementierte
Unterst�tzung der Schnittstelle /proc/bus/pci).

%description -l es
Este paquete contiene varias utilidades para controlar y configurar
los dispositivos conectados al bus PCI. Las utilidades ofrecidas en
este paquete requieren la versi�n 2.1.82 o una posterior del kernel
(necesita del soporte para la interfaz /proc/bus/pci).

%description -l fr
Le paquetage pciutils contient divers utilitaires permettant
d'inspecter et de param�trer des p�riph�riques connect�s au bus PCI.
Les utilitaires fournis requi�rent un noyau version 2.1.82 ou plus
r�cent (prenant en charge l'interface /proc/bus/pci).

%description -l id
Paket ini berisi berbagai utilitas untuk mengamati dan mengeset device
yang terhubung ke bus PCI. Utilitas yang disediakan ini membutuhkan
kernel versi 2.1.82 atau yang lebih baru (yaitu yang mendukung
antarmuka /proc/bus/pci).

%description -l is
�essi pakki inniheldur �mis t�l til a� sko�a og setja t�ki tengd PCI
r�tunni. T�lin eru nau�synleg fyrir kjarna 2.1.82 e�a n�rri (sty�ja
/proc/bus/pci vi�m�ti�).

%description -l it
Il pacchetto pciutils contiene varie utility per controllare e
configurare i dispositivi collegati al bus PCI. L'utility fornita in
questo pacchetto richiede la versione 2.1.82 o successiva del kernel
(richiede il supporto per l'interfaccia /proc/bus/pci).

%description -l ja
���Υѥå������ˤϡ�PCI �Х�����³���줿�ǥХ�����Ĵ�������ꤹ�뤿
��γƼ�桼�ƥ���ƥ����ޤޤ�Ƥ��ޤ��������Υ桼�ƥ���ƥ��ϡ�����
�ͥ�С������ 2.1.82 �ʹ� (/proc/bus/pci ���󥿡��ե������򥵥ݡ���)
��ɬ�פȤ��ޤ���

%description -l pl
Pakiet zawiera narz�dzia do ustawiania i odczytywania informacji o
urz�dzeniach pod��czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udost�pniaj�cego odpowiednie informacje
poprzez /proc/bus/pci).

%description -l pt
Este pacote cont�m v�rios utilit�rios para inspeccionar e configurar
os dispositivos ligados ao bus PCI. Os utilit�rios fornecidos precisam
dum n�cleo ou 'kernel' vers�o 2.1.82 ou mais recente (que suporte a
interface /proc/bus/pci).

%description -l pt_BR
Este pacote cont�m v�rios utilit�rios para inspe��o e configura��o de
dispositivos conectados ao barramento PCI do seu computador.

%description -l ru
����� �������� ��������� ������� ��� �������� � ��������� ���������,
������������ � ���� PCI. ������� ������� ���� ������ 2.1.82 (��� �����
����� ������), ������������� ��������� /proc/bus/pci.

%description -l sk
Tento bal�k obsahuje rozli�n� pomocn� programy pre prehliadanie a
nastavovanie zariaden� pripojen�ch na PCI zbernicu. N�stroje vy�aduj�
jadro s ��slom verzie aspo� 2.1.82 (podporuj�ce rozhranie
/proc/bus/pci).

%description -l sv
Paketet pciutils inneh�ller olika verktyg f�r att inspektera och
st�lla in enheter kopplade till PCI-bussen. Verktygen kr�ver
k�rnversion 2.1.82 eller senare (som st�djer gr�nssnittet
/proc/bus/pci).

%description -l uk
����� pciutils ͦ����� ���̦�� ��� ������������� �� ���Ʀ���������
������ϧ�, Ц�'������� �� PCI ����. ��� ������ æ ���̦�� ����������
�������Ԧ ���������� /proc/bus/pci.

%package devel
Summary:	Linux PCI development library
Summary(cs):	Linuxov� v�vojov� knihovna pro PCI
Summary(da):	Linux PCI udviklingsbibliotek
Summary(de):	Linux PCI-Entwicklungsbibliothek
Summary(es):	Biblioteca de desarrollo para aplicaciones que trabajan con el bus PCI en Linux
Summary(fr):	Biblioth�que de d�veloppement PCI Linux
Summary(id):	Library pengembangan PCI Linux
Summary(is):	PCI �r�unara�ger�asafn fyrir Linux
Summary(it):	Libreria di sviluppo PCI per Linux
Summary(ja):	Linux PCI ��ȯ�饤�֥��
Summary(ko):	Linux PCI ���߿� ���̺귯��
Summary(nb):	Linux PCI utviklingsbibliotek
Summary(pl):	Pliki developerskie pciutils
Summary(pt):	Biblioteca de desenvolvimento para PCI do Linux
Summary(pt_BR):	Biblioteca de desenvolvimentos para aplica��es que trabalhem com o barramento PCI no Linux
Summary(ru):	������ � ������ ����� ��� ���������� ��������, ���������� � ����� PCI
Summary(sk):	Kni�nica pre v�voj PCI na Linuxe
Summary(sl):	Razvojna knji�nica za PCI v Linuxu
Summary(sv):	Linux PCI utvecklignsbibliotek
Summary(uk):	������ �� ��ۦ ����� ��� �������� �������, �� �������� � ����� PCI
Summary(zh_CN):	Linux PCI ��������⡣
Group:		Development/Libraries

%description devel
This package contains a library for inspecting and setting devices
connected to the PCI bus.

%description devel -l cs
Tento bal��ek obsahuje knihovny pro prohl�en� a nastavov�n� za��zen�
p�ipojen�ch k PCI sb�rnici.

%description devel -l da
Denne pakke indeholder et bibliotek for at inspektere og st�lla in
enheder kopplade til PCI-bussen.

%description devel -l de
Dieses Paket enth�lt eine Bibliothek f�r das �berpr�fen und
Konfigurieren von Ger�ten, die an den PCI-Bus angeschlossen sind.

%description devel -l es
Biblioteca de desarrollo para aplicaciones que trabajen con el bus PCI
en Linux.

%description devel -l fr
Ce paquetage contient une biblioth�que permettant d'inspecter et de
d�finir des p�riph�riques connect�s au bus PCI.

%description devel -l id
Paket ini berisi library untuk mengamati dan mengeset device yang
terhubung ke bus PCI.

%description devel -l is
�essi pakki inniheldur a�ger�asafn til a� sko�a og setja t�ki tengd
PCI r�tunni.

%description devel -l it
Questo pacchetto contiene una libreria per controllare e configurare i
dispositivi collegati al bus PCI.

%description devel -l ja
���Υѥå������ˤϡ�PCI �Х�����³���줿�ǥХ����򸡺�������
���뤿��Υ饤�֥�꤬�ޤޤ�Ƥ��ޤ���

%description devel -l ko
�� ��Ű���� PCI ������ ���ӵ� ��ġ���� �����ϰ� �����ϴµ� ���Ǵ�
���̺귯���� �����ϰ� �ֽ��ϴ�.

%description devel -l pl
Pakiet ten zawiera bibliotek� s�u��c� do badania i konfigurowania
urz�dze� przy��czonych do magistrali PCI.

%description devel -l pt
Este pacote cont�m uma biblioteca para inspeccionar e configurar
dispositivos ligados ao bus PCI.

%description devel -l pt_BR
Biblioteca de desenvolvimentos para aplica��es que trabalhem com o
barramento PCI no Linux.

%description devel -l ru
���� ����� �������� ������ � ������ ����� ��� ���������� ��������
�������������� � ��������������� ����������, ������������ � ���� PCI.

%description devel -l sk
Tento bal�k obsahuje kni�nicu pre prehliadanie a nastavovanie
zariaden� pripojen�ch na PCI zbernicu.

%description devel -l sv
Detta paket inneh�ller ett bibliotek f�r att inspektera och st�lla in
enheter kopplade till PCI-bussen.

%description devel -l uk
��� ����� ͦ����� ������ �� ��ۦ ����� ��� �������� �������,��
����������� �� ���Ʀ������� ������ϧ, Ц�'����Φ �� ���� PCI.

%description devel -l zh_CN
�����������һ������⣬���ڼ��������� PCI �������ӵ��豸��

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# paranoid check whether pci.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE2}`" -lt "`wc -l < pci.ids`" ] ; then
	echo "pci.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE2} .

cp -rf lib pci

%build
%{__make} lib/config.h pci/config.h \
	SHAREDIR=%{_datadir}

%{__make} -C lib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	SHAREDIR=/etc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci pcimodules	$RPM_BUILD_ROOT%{_sbindir}
install *.h lib/[ch]*.h	$RPM_BUILD_ROOT%{_includedir}/pci
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids		$RPM_BUILD_ROOT%{_datadir}
install lib/libpci.a	$RPM_BUILD_ROOT%{_libdir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
cp -f lib/pci.h		$RPM_BUILD_ROOT%{_includedir}/pci

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
