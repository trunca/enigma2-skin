import os
from shutil import rmtree, copytree
import urllib2

url = "http://linuxzone.online/addons/picon/picon.tar.gz"
backup = "/tmp/.piconbackup"
descarga = "/tmp/picon.tar.gz"

os.system("wget -P /tmp/ %s" % (url))

if os.path.exists(backup):
    rmtree(backup)

if os.path.ismount('/media/hdd'):
    folder = '/media/hdd/picon'
elif os.path.ismount('/media/usb'):
    folder = '/media/usb/picon'
elif os.path.exists('/usr/share/enigma2'):
    folder = '/usr/share/enigma2/picon'

if os.path.exists(folder):
    copytree(folder, backup)

print "Copia de picon creada en %s" % (backup)

if os.path.ismount('/media/hdd'):
    descomprimir = '/media/hdd'
elif os.path.ismount('/media/usb'):
    descomprimir = '/media/usb'
elif os.path.exists('/usr/share/enigma2'):
    descomprimir = '/usr/share/enigma2'

if os.path.exists(descomprimir):
    os.system("tar -zxf /tmp/picon.tar.gz -C %s" % (descomprimir))

os.system("rm -r %s" % (descarga))

f = urllib2.urlopen("http://www.salvametv.es/")
print f.read()
f.close()

print "Tu receptor ha sido con picon Movistar+ by linuxzone.tv"
