# 🔐 MCRACK

**MCRACK** es una herramienta que permite realizar ataques de diccionario para recuperar contraseñas de archivos ofimáticos (Microsoft Office) y documentos PDF.

---

## 🚀 Características

* **Formatos:**
    * 📄 **PDF:**.
    * 📊 **Office Moderno:** `.docx`, `.xlsx`, `.pptx`.
    * 🗄️ **Office Legacy:** `.accdb`, `.mdb`.
* **Anti-Falso Positivo:** Implementa verificación de cabeceras ZIP (`PK`) en archivos Office modernos para asegurar que la contraseña es correcta antes de reportarla.
* **Monitorización en Vivo:** Muestra el tiempo transcurrido, tiempo restante estimado (ETA) y velocidad de prueba.
* **Cross-Platform:** Compatible con Windows y Linux.

---

## 📋 Requisitos

* Python 3.8 o superior.

---

## 🛠️ Instalación y Configuración

### 1. Clonar o descargar el proyecto

### 2. Crear un entorno virtual

### 3. Crear entorno
```bash
python -m venv mcrack
```

### 4. Activar entorno
**Windows:** 
```bash
.\mcrack\Scripts\Activate.ps1
```
**Linux / macOS:** 
```bash
source mcrack/bin/activate
```

### 5. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 6. Uso

```bash
python mcrack.py -w <ruta_al_diccionario> -f <archivo_a_crackear>
```
Argumentos:

- -w, --wordlist: Ruta al archivo de texto con la lista de contraseñas.

- -f, --file: Ruta al archivo PDF u Office protegido.

---

## 🧪 Tests Unitarios

El proyecto incluye 4 tests unitarios. Se pueden ejecutar con:

```bash
python test_mcrack.py
```

### Descripción de los Tests:

1.  **`test_time_format`**: Verifica que la función auxiliar de formateo de tiempo convierte correctamente los segundos en formato `HH:MM:SS`.(ej. 3661s -> 01:01:01)

2.  **`test_get_total_lines`**: Asegura que el conteo de líneas del diccionario (wordlist) es preciso. Se crea un archivo temporal con 3 líneas y se valida que la función retorne 3. También se prueba el manejo de archivos inexistentes.

3.  **`test_try_pdf_mock`**: Valida el manejo de errores en la función de cracking de PDF. Se intenta abrir un archivo que no es un PDF válido para confirmar que la función captura la excepción y retorna `False` en lugar de romper la ejecución.

4.  **`test_try_office_mock`**: Valida el manejo de errores en la función de cracking de Office. Similar al anterior, se pasa un archivo inválido para asegurar que la librería `msoffcrypto` y el código manejan la excepción correctamente retornando `False`.