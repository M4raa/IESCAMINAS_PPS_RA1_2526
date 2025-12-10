# PC Info Fetch Script

este script en Bash obtiene información básica sobre tu PC, como la dirección MAC, la dirección IP, el sistema operativo, la versión del kernel, y el nombre del equipo junto con el usuario actual.

## funciones

- **dirección MAC**: Muestra la dirección MAC de la primera interfaz de red.
- **sistema operativo**: Determina si el sistema es Windows (WSL) o Linux.
- **versión del kernel**: Muestra la versión actual del kernel.
- **nombre del equipo y usuario**: Muestra el nombre del equipo y el usuario actual en el sistema.

## requisitos

este script está diseñado para funcionar en sistemas basados en Linux o Windows (WSL).

Asegúrate de tener acceso a la terminal con privilegios de usuario estándar.

## instrucciones

1. bajate el script `pc-info.sh`.
2. asegúrate de que el archivo tenga permisos de ejecución:
   
   ```bash
   chmod +x pc_info.sh
   ```

3. ejecuta el script:
    ```bash
    ./pc_info.sh
    ```

## ejemplo de salida

```bash
    ================== -- PC Info Fetch -- ==================
        nombre del equipo y usuario: <hostname> - <user>
        dirección MAC: <mac_address>
        sistema Operativo: <os>, <kernel_version>
    ========================================================
```