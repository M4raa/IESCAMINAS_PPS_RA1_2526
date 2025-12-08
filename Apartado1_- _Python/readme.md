# pywdGenerator

Este proyecto es una aplicación gráfica sencilla que permite generar contraseñas seguras según las opciones seleccionadas por el usuario.  Incluye opciones para usar mayúsculas, minúsculas, números y símbolos, además de elegir la longitud de la contraseña.


<image src="../imagenes/pywdGenerator.png">

## requisitos

Para ejecutar esta aplicación necesitas unicamenete:

### python 3.8 o superior  

El programa usa unica y exclusivamente librerías incluidas en python por defecto:
- `tkinter` → para la interfaz gráfica (viene con Python)
- `string` → para los conjuntos de caracteres
- `random` → para la generación aleatoria

No hace falta instalar dependencias externas.


## ejecución

1. Descarga el script `pywdGenerator.py`
2. Ejecuta el script en la terminal:

```bash
python3 pywdGenerator.py
```

## cómo usar la aplicación

Cuando se abra la ventana verás:

### opciones de caracteres
- **Mayúsculas (A-Z)**  
- **Minúsculas (a-z)**  
- **Números (0-9)**  
- **Símbolos (!@#$%...)**

Marca las casillas que quieras incluir en la contraseña.

---

### selector de longitud
Un deslizador permite elegir entre **4 y 50 caracteres**.  
Por defecto, está ajustado a **12 caracteres**, una longitud recomendada.

---

### generar contraseña
al pulsar el botón **“Generar”**, se creará una contraseña aleatoria cumpliendo todos los criterios seleccionados.

la contraseña aparecerá en el cuadro de texto inferior.

si no seleccionas ninguna opción, se mostrará un aviso indicando que debes elegir al menos una categoría.

---

## ¿cómo funciona?

la función principal utiliza:

```python
password = "".join(random.choice(caracteres) for _ in range(longitud))
```

esto significa:

1. Toma la longitud seleccionada.
2. En cada posición, elige un carácter aleatorio del conjunto permitido.
3. Junta todos los caracteres generados para formar la contraseña final.
