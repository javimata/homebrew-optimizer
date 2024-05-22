# Optimizer

Optimizer es una herramienta que optimiza las imágenes en la carpeta actual.

## Instalación

Primero, necesitas instalar Pillow (PIL). Puedes hacerlo con el siguiente comando:

```
pip install pillow
```

> Nota: Si tienes problemas para instalar Pillow, puedes encontrar más información en la [documentación oficial de Pillow](https://pillow.readthedocs.io/en/stable/installation.html). el comando puede ser **pip3** o algún otro dependiendo de tu sistema.

Luego, puedes instalar Optimizer con Homebrew usando los siguientes comandos:

```
brew tap javimata/optimizr https://github.com/javimata/optimizr
brew install optimizer
```

## Uso

Puedes ejecutar Optimizer con el siguiente comando:

```
optimizer
```

Este comando optimizará todas las imágenes en la carpeta actual.

## Argumentos

| Argumento | Descripción | Valor por defecto |
|-----------|-------------|-------------------|
| `-h` o `--help` | Muestra el mensaje de ayuda y termina el programa. | N/A |
| `-v` o `--version` | Muestra la versión del programa y termina. | N/A |
| `-o` o `--output_dir` | Directorio de salida para guardar las imágenes optimizadas. | `out` |
| `-f` o `--format` | Formato para guardar las imágenes (por ejemplo, 'JPEG', 'PNG'). | N/A |
| `-w` o `--width` | Ancho para redimensionar las imágenes. | N/A |
| `-t` o `--height` | Altura para redimensionar las imágenes. | N/A |
| `-q` o `--quality` | Calidad de las imágenes optimizadas (1-100). | `85` |
| `-r` o `--report` | Muestra el informe de optimización. | `True` |
| `-n` o `--nooverwrite` | No sobrescribir los archivos existentes. | `False` |

## Licencia

Optimizer está licenciado bajo la licencia MIT. Para más detalles, por favor vea el archivo LICENSE en este repositorio.