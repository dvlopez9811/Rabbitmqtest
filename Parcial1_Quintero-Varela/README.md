# Primer examen parcial

## Estudiantes
### Juan Sebastián Quintero Yoshioka - A00310448
### Andrés David Varela López - A00049016 

## Descripción del parcial

Implemente una arquitectura que contenga:

- Un productor de mensajes (puede ser en la máquina física o en una máquina virtual)
- Un broker de RabbitMQ (puede ser en la máquina física o en una máquina virtual)
- Dos consumidores de mensajes (pueden ser en una máquina virtual o contenedores)
    - El primer consumidor recibirá los mensajes de la cola "Grupo 01"
    - El segundo consumidor recibirá los mensajes de la cola "Grupo 02"
    - Ambos consumidores recibirán los mensajes enviados al grupo "General"

## Prerequisitos
- Virtualbox
- Vagrant
- Ansible

## Instalación y configuración de las máquinas virtuales

Lo primero que se debe realizar es la instalación y configuración de las máquinas virtuales, para ello utilizamos Vagrant, una herramienta que nos permite crear nuestro entorno de desarrollo de máquinas virtuales.

Como se detalla a continuación, para cumplir con la arquitectura deseada, se crean cuatro (4) máquinas virtuales:
- Broker
- Consumidor A
- Consumidor B
- Productor

![COnfiguración máquinas virtuales](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/1ConfiguracionMaquinasVirtuales.png)

Además, se utiliza Ansible para realizar el aprovisionamiento de las máquinas. Para ello, se define la estructura:

![Estructura aprovisionamiento](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/2ConfiguracionAnsible.png)

Después, se crean los archivos necesarios para realizar el aprovisionamiento:

![Archivos Ansible](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/3ArchivosAnsible.png)

- Archivo de configuración:<br>
![Archivo de configuración](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/4Ansible_cfg.png)

- Archivo de los hosts:<br>
![Archivo de los hosts](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/5Hosts.png)

- Por último, se deja el esquema para realizar el aprovisionamiento de las máquinas virtuales:
![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/6Servers_yml.png)

## Documentación del procedimiento para el aprovisionamiento del broker

![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/7Broker_ansible.png)

![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/8Broker_ansible.png)

### Evidencias del funcionamiento

![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/9Broker_ssh.png)

![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/10Broker_rabbit_satus4.png)

![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/11Broker_plugin_management5.png)

## Documentación del procedimiento para el aprovisionamiento de los consumidores

### Evidencias del funcionamiento

## Documentación del procedimiento para el aprovisionamiento del productor

### Evidencias del funcionamiento

## Documentación de las tareas de integración

### Evidencias de la integración

## Problemas encontrados y las acciones efectuadas para su solución al aprovisionar la infraestructura y aplicaciones
