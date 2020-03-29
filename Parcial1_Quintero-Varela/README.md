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

![Configuración máquinas virtuales](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/1ConfiguracionMaquinasVirtuales.png)

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

EL siguiente paso es aprovisionar la máquina broker con RabbitMQ. 

EL proceso es el siguiente:

1. En orden de usar el repositorio de RabbitMQ primero se debe agregar la clave de firma RabbitMQ a apt-key. Esto instruirá a apt para confiar en los paquetes firmados por esa clave.

2. Al igual que con todos los repositorios apt de terceros, se debe colocar un archivo que describa el repositorio en el directorio /etc/apt/sources.list.d/.

Los repositorios estándar de Debian y Ubuntu tienden a proporcionar versiones desactualizadas de Erlang/OTP. Team RabbitMQ mantiene un repositorio apto que incluye paquetes de versiones modernas de Erlang/OTP para una serie de distribuciones Debian y Ubuntu de uso común.

3. Por esto, se agrega prime la clave y después, se agregar el repositorio.

4. Se instala RabbitMQ.

![Aprovisionamiento broker](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/7Broker_ansible.png)

5. Se inicia RabbitMQ.

6. El complemento de administración RabbitMQ proporciona una API basada en HTTP para la administración y supervisión de nodos y clústeres RabbitMQ, junto con una interfaz de usuario basada en navegador y una herramienta de línea de comandos, rabbitmqadmin.Para ello, se habilita el plugin.

7. Luego se agrega un nuevo usuario administrador y elimina el usuario predeterminado de RabbitMQ.

8. Por último, se reinicia el servidor de RabbitMQ.

![Más aprovisionamiento RabbitMQ](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/8Broker_ansible.png)

Fuentes:
[1] https://www.rabbitmq.com/install-debian.html#erlang-repositories

### Evidencias del funcionamiento

Una vez se ejecuta el comando  `{vagrant up broker}`, accedemos por ssh:

![Broker SSH](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/9Broker_ssh.png)

Validamos que se haya realizado un correcto aprovisionamiento y se encuentre el servicio de RabbitMQ:

![Broker status](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/10Broker_rabbit_satus4.png)

Por último, verificamos, accediendo desde el navegador a la dirección IP: `{192.168.56.2.15672}`
![Broker plugin](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/11Broker_plugin_management5.png)

## Documentación del procedimiento para el aprovisionamiento de los consumidores

Los consumidores son la aplicación que recibe los mensajes desde la cola de RabbitMQ. Para esto, se han definido previamente en Vagrant dos máquinas virtuales: ConsumidorA y ConsumidorB.

El proceso de aprovisionamiento de estas máquinas es el siguiente:

1. Se instala "pip", una aplicación que permite instalar paquetes de Python.

2. Se instala "pika" haciendo uso de pip, ésta es necesaria para hacer uso del protocolo de RabbitMQ.

3. Se instala tambien git, con el objetivo de hacer clonación del repositorio dentro de la máquina.

4. Haciendo uso de git, se clona el repositorio de github {https://github.com/dvlopez9811/Rabbitmqtest.git}, teniendo en cuenta que esta acción debe realizarse solo una vez haya sido instalado git.

5. Para permitir la ejecución de estos scripts, se le otorgan estos permisos al archivo en la carpeta ya clonada.

El aprovisionamiento de la primera de estas máquinas se define de la siguiente forma en el archivo servers.yml dentro de los playbooks de Ansible:

![Aprovisionamiento ConsumidorA](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/12ConsumidorA_ansible.png)

Asi mismo, se realiza el aprovisionamiento del segundo consumidor, ConsumidorB:

![Aprovisionamiento ConsumidorB](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/13ConsumidorB_ansible.png)

Como puede observarse, en el aprovisionamiento se hace la clonación de este repositorio mediante git dentro de estas máquinas. Esto con el objetivo de añadir en ellas los scripts que crean los bindings y reciben los mensajes o exchanges.

Estos archivos contienen la siguiente estructura: 

1. Primero, se importa el paquete pika `{ import pika }`

2. Se establecen las credenciales para acceder al servidor de RabbitMQ, en este caso mediante el usuario 'deploy' y la contraseña 'password': 

`{ credentials = pika.PlainCredentials('deploy', 'password') }`

3. Se establecen los parametros para la conexión al servidor haciendo uso de pika, con la respectiva dirección IP y credenciales.
A partir de estos se establece la conexión y posteriormente el canal:

`parameters = pika.ConnectionParameters('192.168.56.2',5672,'/', credentials)`

`connection = pika.BlockingConnection(parameters)`

`channel = connection.channel()`

Es importante establecer el tipo de exchanges que se realizaran, para esta conexión serán de tipo directo:

`channel.exchange_declare(exchange='direct_logs', exchange_type='direct')`

`result = channel.queue_declare(queue='', exclusive=True)`

`queue_name = result.method.queue`

4. Se establecen las severities, las cuales definen las colas a las cuales escuchará el consumidor:

`for severity in severities:`

    `channel.queue_bind(`
    
        `exchange='direct_logs', queue=queue_name, routing_key=severity)`

5. Finalmente, se pone en funcionamiento el consumidor, imprimiendo en consola los mensajes recibidos:

`def callback(ch, method, properties, body):`

   `print(" [x] %r:%r" % (method.routing_key, body)) `  

`channel.basic_consume(`

   ` queue=queue_name, on_message_callback=callback, auto_ack=True)`

`channel.start_consuming()`

A continuación se muestra el script completo de Consumidor A, con severities definidas como ["Grupo 01","General]:

![Script ConsumidorA](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/14ConsumidorA_py.png)

En el caso del ConsumidorB, las severities son  ["Grupo 02","General]:

![Script ConsumidorB](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/15ConsumidorB_py.png)

### Evidencias del funcionamiento

Una vez se ejecuta en cada máquina de consumidores el comando {python /src/Parcial1_Quintero-Varela/src/consumidorA.py} o {python /src/Parcial1_Quintero-Varela/src/consumidorB.py} según sea el caso, se establece un "listener" que actúa esperando los mensajes, los que llegan son imprimidos en consola:

![Ejecucion ConsumidorA](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/16ConsumidorA_ejecutar_py.png)

![Ejecucion ConsumidorB](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/17ConsumidorB_ejectuar_py.png)

En la interfaz del servidor de RabbitMQ, puede verificarse que ambos consumidores han sido agregados como queue:

![Verificacion consumidores](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/18Consumidores_verificacion.png)

Por último, también se verifica que el consumidor A se encuentra escuchando los bindings del "Grupo 01" y "General" como se establece en las severities:

![Binding consumidorA](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/20ConsumidorA_binding.png)

Y a su vez, el consumidor B escucha el "Grupo 02" y "General":

![Binding consumidorB](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/19ConsumidorB_binding.png)

## Documentación del procedimiento para el aprovisionamiento del productor

De parte del productor, se ejecuta el siguiente script

Primero, se crea un objeto de credenciales para la metodología de autenticación predeterminada con RabbitMQ.

Si no se pasa las credenciales al objeto ConnectionParameters, creará credenciales para "guest" con la contraseña de "guest".

Después de pasar los parámetros necesarios, primero se crea un intercambio con el comando: 
`{channel.exchange_declare(exchange='direct_logs', exchange_type='direct')}`

Ahora, se puede enviar un mensaje:
`{channel.basic_publish(exchange='direct_logs',routing_key=severity, body=message)}`

El script recibe dos argumento, primero, recibe el nombre del "binding" y luego el mensaje que se quiera mandar. Por ejemplo, si se quiere mandar un "Hola" al grupo "General", se debe ejecutar así:
- `{python productor.py "General" " Hola"}`

El script se realiza de tal forma que, si no recibe ningún parámetro, al ejectuarse en envíe por defecto al grupo "General" un "Mensaje por defecto".

A continuación se muestra el script completo:

![Python productor](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/21Productor_py.png)

Después, se realiza el aprovisionamiento, para ello, se instalan las mismas depedencias que los consumidores y se clona el repositorio donde se encuentra el script a ejecutar.

![Provisionamiento productor](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/22Productor_ansible.png)

### Evidencias del funcionamiento

Una vez se realiza el `{vagrant up}`, se ejecuta el comando, esta vez, teniendo un consumidor (Consumidor A) ejecutándose para poder verificar que está mandando el mensaje:

![Ejecutar script por defecto](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/23Productor_ejecutando_script.png)

Y el mensaje llega al Consumidor A que está vinculado al binding General.
![Verificando en un consumidor](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/24Productor_verificando.png)

## Documentación de las tareas de integración

La primera tarea de integración fue realizar el `{vagrant up}` para ejecutar todas las máquinas virtuales.

![Vagrant status](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/25Integracion_status.png)

### Evidencias de la integración

Ahora, para probarlo, se realiza el envío de los siguentes mensajes, verificando que para cada consumidor lleguen los mensajes que debería recibir.
![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/26Integracion_enviando_mensajes.png)

Efectivamente, se verfifica:
- Consumidor A: <br>
![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/27Integracion_consumidorA.png)

- Consumidor B: <br>
![](https://github.com/dvlopez9811/Rabbitmqtest/blob/master/Parcial1_Quintero-Varela/imagenes/28Integracion_consumidorB.png)

## Problemas encontrados y las acciones efectuadas para su solución al aprovisionar la infraestructura y aplicaciones

- Al ejectuar de forma local los scripts, todo funcionó. En el momento de provisionar las máquinas virtuales y tener todo separado, se presentó el problema de acceder remotamente a RabbitMQ. La forma de solucionar esto fue, primero, en el broker eliminar el usuario por defecto (solo podía ser accedido de forma local) y crear un nuevo usuario. Después, en cada uno de los scripts tanto de los consumidores como en el del prodcutor, crear unos parámetros para la autenticación y se puede acceder remotamente al servidor.

- Con el objetivo de realizar una implementación más práctica y automatizada de la aplicación, se propuso, desde el equipo de trabajo, ejecutar el script de consumidores y de productor directamente desde el aprovisionamiento en Ansible. Sin embargo, no se consiguió realizar esto en segundo plano para que la aplicación escuchara los mensajes y se guardaran en un archivo de texto de manera persistente. Por esta razón, se decidió mantener la implementación por medio de ejecuciones manuales de los scripts en cada una de las máquinas virtuales.
