# Escáner de Equipos y Puertos Activos

Escáner de Equipos y Puertos Activos es un proyecto escolar desarrollado con Python 2.7 y Tkinter para Python, el cual nos permite conocer los equipos activos conectados dentro de nuestra red y a su vez los puertos lógicos activos de algún equipo que se desee, por medio de la interfaz gráfica de usuario. 
Es un programa multiplataforma disponible para Windows, Linux y macOS. Es un programa Open Source disponible para todo aquel que quiera hacer uso de él y realizar mejoras al sistema.
Para su uso e implementación se recomienda tener instalada una versión mínima de Python 2.7.9, ya que se necesita tener instalado Setuptools. También se requiere el uso e instalación previa de las bibliotecas ipaddress-1.0.18 y netifaces-0.10.5 pertenecientes a Python, las cuales se encuentran disponibles en:

  https://www.python.org/downloads/release/python-2713/
  
  https://pypi.python.org/pypi/netifaces
  
  https://pypi.python.org/pypi/ipaddress

Limitaciones.
	No detecta el nombre del servicio, solo el puerto.
  
	Solo se aplica el escaneo para puertos bien conocidos.
  
	No escanea los puertos abiertos en dispositivos móviles.
  
	No detecta a equipos que tengan restricción en el reply para ICMP.

