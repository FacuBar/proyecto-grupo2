# proyecto-grupo2

Este proyecto de Python es para un administrador de un índice de documentos en un directorio del sistema.

## Instrucciones

Hay dos modos de usar la herramienta, uno es hacer la invocación directa del módulo (independientemente de la localización de este) usando la línea de comandos.

```sh
$ python3 personal_library/personal_library.py --help
```

Y el otro es por medio del sistema de Setuptools de Python. La instalacíon se hace corriendo los comandos a continuación.

```sh
$ python3 setup.py build
$ python3 setup.py install --root=<directorio de destino>
```

Para que luego se pueda invocar la utilidad si es que esta se haya en el `PATH` del sistema.

```sh
$ docmgr --help
```

La razón de las dos opciones fue porque durante el desarrollo se requirió uso de herramientas de formateado y resaltado, además de respetar las consignas de trabajo.
