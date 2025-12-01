# Sistema de Gestión de Tienda de Electrónica

Sistema integral de gestión de inventario y ventas para una tienda de productos electrónicos desarrollado en Python con menú interactivo completo.

---

## Descripción del Proyecto

Sistema completo de gestión comercial que permite administrar el **inventario** de productos electrónicos, procesar **ventas** con descuentos según tipo de cliente, y generar **reportes analíticos** detallados del desempeño del negocio.
**Características principales:**
- **Gestión completa de inventario (CRUD)**
- Sistema de ventas con **descuentos por tipo de cliente**
- Generación de **reportes y análisis** de rendimiento
- **Validaciones exhaustivas** de datos
- Interfaz de usuario intuitiva
- Sistema de **caché** para optimizar reportes

---

## Funcionalidades del Sistema

### GESTIÓN DE INVENTARIO

#### 1. Agregar Producto
Registra nuevos productos en el inventario con: **ID único**, Nombre, Marca, Categoría, Precio unitario, Stock disponible y Meses de Garantía.

**Validaciones:**
- ID único (no duplicados)
- Campos obligatorios no vacíos
- Precio mayor a cero
- Stock no negativo
- Garantía no negativa

#### 2. Ver Todos los Productos
Muestra tabla formateada con: ID, nombre, marca, categoría, precio, stock disponible, garantía, el total de productos y el valor total del inventario.

#### 3. Actualizar Producto
Modifica información de productos existentes mediante **búsqueda por ID**. Ofrece la opción de mantener valores actuales (presionando Enter).

#### 4. Eliminar Producto
Elimina productos del inventario, requiriendo **confirmación explícita (SI)** para prevenir borrados accidentales.

### GESTIÓN DE VENTAS

#### 5. Registrar Venta
Procesa ventas completas con: Datos del cliente, selección de tipo de cliente, selección de producto y cantidad a vender.

* **Validación de stock** disponible.
* Cálculo automático de descuentos y total.
* **Actualización automática de inventario**.
* Generación de un ticket detallado de venta.

**Tipos de Cliente y Descuentos:**
| Tipo | Descuento |
| :--- | :--- |
| Regular | 0% |
| Miembro | 5% |
| VIP | 10% |
| Corporativo | 15% |

#### 6. Ver Historial de Ventas
Muestra tabla con todas las ventas registradas, incluyendo fecha, cliente, producto, cantidad, total de la venta e **ingresos totales generados**.

### REPORTES Y ANÁLISIS

#### 7. Top 3 Productos Más Vendidos
Ranking de productos por unidades vendidas, mostrando ingresos generados y **participación porcentual** sobre el total.

#### 8. Ventas por Marca
Reporte consolidado por marca, mostrando unidades, ingresos y **porcentaje de participación**, ordenado por ingresos (mayor a menor).

#### 9. Reporte Financiero
Análisis financiero completo, incluyendo:

* **Métricas Generales:** Total de transacciones, Ingreso bruto, Total descuentos aplicados, **Ingreso neto**, Ticket promedio y Tasa de descuento efectiva.
* **Análisis por Tipo de Cliente:** Número de transacciones, ingresos y Ticket promedio por tipo.

## Estructura de Datos

El sistema utiliza las siguientes estructuras de datos en Python para almacenar la información:

### Producto
```python
{
    'id': str,          # Ej: "PROD001" (Identificador único)
    'nombre': str,      # Ej: "Mouse Gamer Inalámbrico"
    'marca': str,       # Ej: "Logitech"
    'categoria': str,   # Ej: "Periféricos"
    'precio': float,    # Ej: 79.99 (Valor unitario)
    'stock': int,       # Ej: 45 (Cantidad disponible)
    'garantia': int     # Ej: 24 (Meses de cobertura)
}

##  Persistencia de Datos

**IMPORTANTE:** El sistema está diseñado solo para demostración.

* **Los datos son volátiles:** Al cerrar el programa (Opción 0), **toda la información** (libros añadidos y ventas registradas) se **pierde** permanentemente.
* **No hay archivos:** No existe conexión a base de datos, ni uso de archivos (CSV, JSON, etc.) para guardar la información.
