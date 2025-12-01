"""
Sistema Integral de Gestión de Inventario y Ventas con Reportes Dinámicos
Caso: Sistema de gestión del área digital de librería nacional
"""

from datetime import datetime

# ============================================================================
# DATOS INICIALES - 5 LIBROS PRE-CARGADOS
# ============================================================================

libros = [
    {
        "titulo": "sol y luna",
        "autor": "marcus",
        "categoria": "amor",
        "precio": 100,
        "existencias": 10
    },
    {
        "titulo": "fuego",
        "autor": "thiago",
        "categoria": "accion",
        "precio": 200,
        "existencias": 10
    },
    {
        "titulo": "el frio",
        "autor": "juan",
        "categoria": "ficcion",
        "precio": 300,
        "existencias": 10
    },
    {
        "titulo": "los colores",
        "autor": "stiven",
        "categoria": "suspenso",
        "precio": 400,
        "existencias": 10
    },
    {
        "titulo": "en la noche",
        "autor": "arturo",
        "categoria": "fantasia",
        "precio": 500,
        "existencias": 10
    }
]

ventas = []

# ============================================================================
# FUNCIONES DE IMPRESIÓN REUTILIZABLES
# ============================================================================

def imprimir_encabezado(titulo):
    """Imprime un encabezado formateado"""
    print(f"\n{'=' * 60}\n{titulo.center(60)}\n{'=' * 60}")

def imprimir_separador():
    """Imprime una línea separadora"""
    print("-" * 60)

def imprimir_info_libro(libro, mostrar_numero=None):
    """Imprime información de un libro"""
    prefijo = f"{mostrar_numero}. " if mostrar_numero else ""
    print(f"""{prefijo}Titulo: {libro['titulo']}
Autor: {libro['autor']}
Categoria: {libro['categoria']}
Precio: ${libro['precio']}
Existencias: {libro['existencias']}
""")

def imprimir_detalle_venta(venta):
    """Imprime detalle completo de una venta"""
    print(f"""
ID Venta: {venta['id']}
Cliente: {venta['cliente']}
Libro: {venta['titulo_libro']}
Autor: {venta['autor']}
Cantidad: {venta['cantidad']}
Precio unitario: ${venta['precio_unitario']}
Subtotal: ${venta['subtotal']:.2f}
Descuento: {venta['descuento']}% (-${venta['monto_descuento']:.2f})
TOTAL: ${venta['total']:.2f}
Fecha: {venta['fecha']}
""")
    imprimir_separador()

def imprimir_mensaje(mensaje):
    """Imprime un mensaje"""
    print(f"\n{mensaje}\n")

# ============================================================================
# FUNCIONES DE VALIDACIÓN (MANEJO DE EXCEPCIONES)
# ============================================================================

def obtener_texto_valido(mensaje, permitir_vacio=False):
    """Obtiene un texto no vacío con manejo de excepciones"""
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor and not permitir_vacio:
                print("Error: Este campo no puede estar vacio.")
                continue
            return valor
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

def obtener_decimal_valido(mensaje):
    """Obtiene un decimal positivo válido con manejo de excepciones"""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingrese un numero valido.")
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

def obtener_entero_valido(mensaje):
    """Obtiene un entero positivo válido con manejo de excepciones"""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingrese un numero entero valido.")
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

# ============================================================================
# FUNCIONES DE GESTIÓN DE LIBROS
# ============================================================================

def buscar_libro(titulo_busqueda):
    """Función auxiliar para buscar un libro por título"""
    for libro in libros:
        if libro["titulo"].lower() == titulo_busqueda.lower():
            return libro
    return None

def registrar_producto():
    """Función para registrar un producto"""
    try:
        imprimir_encabezado("REGISTRAR LIBRO")
        
        titulo = obtener_texto_valido("Ingrese el titulo del libro: ")
        if not titulo: return
        
        # Verificar si el libro ya existe
        if buscar_libro(titulo):
            imprimir_mensaje(f"El libro '{titulo}' ya existe.")
            return
        
        autor = obtener_texto_valido("Ingrese el autor del libro: ")
        if not autor: return
        
        categoria = obtener_texto_valido("Ingrese la categoria del libro: ")
        if not categoria: return
        
        precio = obtener_decimal_valido("Ingrese el precio del libro: ")
        if precio is None: return
        
        existencias = obtener_entero_valido("Ingrese la cantidad del libro: ")
        if existencias is None: return

        libros.append({
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "precio": precio,
            "existencias": existencias
        })
        
        imprimir_mensaje("Libro registrado exitosamente!")
        
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def consultar_producto():
    """Función para consultar un producto"""
    try:
        imprimir_encabezado("CONSULTAR LIBRO")
        
        titulo_busqueda = obtener_texto_valido("Ingrese el titulo del libro que desea buscar: ")
        if not titulo_busqueda: return
        
        libro = buscar_libro(titulo_busqueda)

        if libro:
            print(f"\nEste libro: '{titulo_busqueda}' existe.\n")
            imprimir_info_libro(libro)
        else:
            imprimir_mensaje(f"Este libro: '{titulo_busqueda}' no fue encontrado.")
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def actualizar_producto():
    """Función para actualizar un producto"""
    try:
        imprimir_encabezado("ACTUALIZAR LIBRO")
        
        titulo_busqueda = obtener_texto_valido("Ingrese el nombre del libro que desea actualizar: ")
        if not titulo_busqueda: return
        
        libro = buscar_libro(titulo_busqueda)
        
        if libro:
            print(f"\nLibro encontrado: {titulo_busqueda}\n")
            print("""¿Que desea actualizar?

1. Autor
2. Categoria
3. Precio
4. Existencias
""")
            
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                nuevo_autor = obtener_texto_valido("Ingrese el nuevo autor: ")
                if nuevo_autor:
                    libro["autor"] = nuevo_autor
                    imprimir_mensaje("Autor actualizado correctamente.")

            elif opcion == "2":
                nueva_categoria = obtener_texto_valido("Ingrese la nueva categoria: ")
                if nueva_categoria:
                    libro["categoria"] = nueva_categoria
                    imprimir_mensaje("Categoria actualizada correctamente.")

            elif opcion == "3":
                nuevo_precio = obtener_decimal_valido("Ingrese el nuevo precio: ")
                if nuevo_precio is not None:
                    libro["precio"] = nuevo_precio
                    imprimir_mensaje("Precio actualizado correctamente.")

            elif opcion == "4":
                nuevas_existencias = obtener_entero_valido("Ingrese las nuevas existencias: ")
                if nuevas_existencias is not None:
                    libro["existencias"] = nuevas_existencias
                    imprimir_mensaje("Existencias actualizadas correctamente.")

            else:
                imprimir_mensaje("Opcion invalida.")
        else:
            imprimir_mensaje(f"El libro '{titulo_busqueda}' no fue encontrado.")
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def eliminar_productos():
    """Función para eliminar un producto de la lista"""
    try:
        imprimir_encabezado("ELIMINAR LIBRO")
        
        titulo_busqueda = obtener_texto_valido("Ingrese el titulo del libro que desea eliminar: ")
        if not titulo_busqueda: return
        
        libro = buscar_libro(titulo_busqueda)
        
        if libro:
            print(f"\nLibro encontrado: {titulo_busqueda}\n")
            imprimir_info_libro(libro)
            
            confirmacion = input("¿Esta seguro de eliminar este libro? (si/no): ")
            
            if confirmacion.lower() == "si":
                libros.remove(libro)
                imprimir_mensaje(f"El libro '{titulo_busqueda}' ha sido eliminado correctamente.")
            else:
                imprimir_mensaje("Eliminacion cancelada.")
        else:
            imprimir_mensaje(f"El libro '{titulo_busqueda}' no fue encontrado.")
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def imprimir_todos_libros():
    """Imprime todos los libros en la lista"""
    if not libros:
        imprimir_mensaje("No hay libros registrados.")
        return
    
    imprimir_encabezado("LISTA DE LIBROS")
    for i, libro in enumerate(libros, 1):
        imprimir_info_libro(libro, mostrar_numero=i)

# ============================================================================
# FUNCIONES DE GESTIÓN DE VENTAS
# ============================================================================

def registrar_venta():
    """Función para registrar una venta"""
    try:
        imprimir_encabezado("REGISTRAR VENTA")
        
        nombre_cliente = obtener_texto_valido("Nombre del cliente: ")
        if not nombre_cliente: return
        
        titulo_busqueda = obtener_texto_valido("Titulo del libro a vender: ")
        if not titulo_busqueda: return
        
        libro = buscar_libro(titulo_busqueda)
        
        if not libro:
            imprimir_mensaje(f"El libro '{titulo_busqueda}' no fue encontrado.")
            return
        
        print("\nLibro encontrado:\n")
        imprimir_info_libro(libro)
        
        cantidad = obtener_entero_valido("Cantidad a vender: ")
        if cantidad is None: return
        
        if cantidad > libro['existencias']:
            imprimir_mensaje(f"Error: Solo hay {libro['existencias']} unidades disponibles.")
            return
        
        descuento = obtener_decimal_valido("Descuento en % (0 si no aplica): ")
        if descuento is None: return
        
        # Calcular totales usando funciones lambda
        calcular_subtotal = lambda precio, cant: precio * cant
        calcular_monto_descuento = lambda subtotal, desc: subtotal * (desc / 100)
        calcular_total = lambda subtotal, monto_desc: subtotal - monto_desc
        
        subtotal = calcular_subtotal(libro['precio'], cantidad)
        monto_descuento = calcular_monto_descuento(subtotal, descuento)
        total = calcular_total(subtotal, monto_descuento)
        
        # Actualizar existencias
        libro['existencias'] -= cantidad
        
        # Registrar venta
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        venta = {
            "id": len(ventas) + 1,
            "cliente": nombre_cliente,
            "titulo_libro": libro['titulo'],
            "autor": libro['autor'],
            "cantidad": cantidad,
            "precio_unitario": libro['precio'],
            "subtotal": subtotal,
            "descuento": descuento,
            "monto_descuento": monto_descuento,
            "total": total,
            "fecha": fecha
        }
        
        ventas.append(venta)
        
        imprimir_encabezado("VENTA REGISTRADA")
        print(f"""Cliente: {nombre_cliente}
Libro: {libro['titulo']}
Cantidad: {cantidad}
Precio unitario: ${libro['precio']}
Subtotal: ${subtotal:.2f}
Descuento ({descuento}%): -${monto_descuento:.2f}
TOTAL: ${total:.2f}
Fecha: {fecha}
Existencias restantes: {libro['existencias']}
""")
        imprimir_separador()
        
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def consultar_ventas():
    """Función para consultar ventas"""
    if not ventas:
        imprimir_mensaje("No hay ventas registradas.")
        return
    
    imprimir_encabezado("VENTAS REGISTRADAS")

    for venta in ventas:
        imprimir_detalle_venta(venta)
    
    # Calcular totales usando lambda
    total_ventas = sum(map(lambda v: v['total'], ventas))
    total_libros_vendidos = sum(map(lambda v: v['cantidad'], ventas))
    
    imprimir_encabezado("RESUMEN DE VENTAS")
    print(f"""Total de ventas: {len(ventas)}
Libros vendidos: {total_libros_vendidos}
Ingresos totales: ${total_ventas:.2f}
""")

def buscar_venta_por_cliente():
    """Buscar ventas por cliente"""
    try:
        imprimir_encabezado("BUSCAR VENTAS POR CLIENTE")
        
        nombre_cliente = obtener_texto_valido("Nombre del cliente: ")
        if not nombre_cliente: return
        
        # Usando lambda para filtrar
        filtrar_cliente = lambda venta: nombre_cliente.lower() in venta['cliente'].lower()
        ventas_cliente = list(filter(filtrar_cliente, ventas))
        
        if not ventas_cliente:
            imprimir_mensaje(f"No se encontraron ventas para el cliente '{nombre_cliente}'.")
            return
        
        imprimir_encabezado(f"VENTAS DE {nombre_cliente.upper()}")
        
        for venta in ventas_cliente:
            print(f"""ID: {venta['id']} | Cliente: {venta['cliente']} | Libro: {venta['titulo_libro']} | Cantidad: {venta['cantidad']} | Total: ${venta['total']:.2f}
Fecha: {venta['fecha']}
""")
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

# ============================================================================
# MÓDULO DE REPORTES
# ============================================================================

def top_3_mas_vendidos():
    """Muestra los 3 productos más vendidos"""
    try:
        imprimir_encabezado("TOP 3 LIBROS MAS VENDIDOS")
        
        if not ventas:
            imprimir_mensaje("No hay datos de ventas disponibles.")
            return
        
        # Agrupar ventas por libro usando lambda
        ventas_libro = {}
        for venta in ventas:
            titulo = venta['titulo_libro']
            if titulo not in ventas_libro:
                ventas_libro[titulo] = {'cantidad': 0, 'ingresos': 0}
            ventas_libro[titulo]['cantidad'] += venta['cantidad']
            ventas_libro[titulo]['ingresos'] += venta['total']
        
        # Ordenar por cantidad usando lambda
        libros_ordenados = sorted(ventas_libro.items(), key=lambda x: x[1]['cantidad'], reverse=True)
        
        print("\nRANKING POR CANTIDAD VENDIDA:\n")
        for i, (titulo, datos) in enumerate(libros_ordenados[:3], 1):
            print(f"{i}. {titulo}")
            print(f"   Unidades vendidas: {datos['cantidad']}")
            print(f"   Ingresos: ${datos['ingresos']:.2f}\n")
        
        imprimir_separador()
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def ventas_por_autor():
    """Muestra ventas agrupadas por autor"""
    try:
        imprimir_encabezado("VENTAS POR AUTOR")
        
        if not ventas:
            imprimir_mensaje("No hay datos de ventas disponibles.")
            return
        
        # Agrupar por autor usando lambda
        ventas_autor = {}
        for venta in ventas:
            autor = venta['autor']
            if autor not in ventas_autor:
                ventas_autor[autor] = {'cantidad': 0, 'ingresos': 0, 'libros': set()}
            ventas_autor[autor]['cantidad'] += venta['cantidad']
            ventas_autor[autor]['ingresos'] += venta['total']
            ventas_autor[autor]['libros'].add(venta['titulo_libro'])
        
        # Calcular ingresos totales usando lambda
        ingresos_totales = sum(map(lambda x: x['ingresos'], ventas_autor.values()))
        
        print("\nRENDIMIENTO POR AUTOR:\n")
        for autor, datos in sorted(ventas_autor.items(), key=lambda x: x[1]['ingresos'], reverse=True):
            porcentaje = (datos['ingresos'] / ingresos_totales * 100) if ingresos_totales > 0 else 0
            print(f"Autor: {autor.upper()}")
            print(f"   Libros vendidos: {', '.join(datos['libros'])}")
            print(f"   Unidades: {datos['cantidad']}")
            print(f"   Ingresos: ${datos['ingresos']:.2f} ({porcentaje:.1f}% del total)")
            print()
        
        imprimir_separador()
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

def reporte_financiero():
    """Muestra reporte de ingresos netos y brutos"""
    try:
        imprimir_encabezado("REPORTE FINANCIERO")
        
        if not ventas:
            imprimir_mensaje("No hay datos de ventas disponibles.")
            return
        
        # Calcular ingreso bruto (sin descuentos) usando lambda
        calcular_bruto = lambda venta: venta['subtotal']
        ingreso_bruto = sum(map(calcular_bruto, ventas))
        
        # Calcular descuentos totales usando lambda
        calcular_descuento = lambda venta: venta['monto_descuento']
        descuentos_totales = sum(map(calcular_descuento, ventas))
        
        # Calcular ingreso neto (con descuentos) usando lambda
        calcular_neto = lambda venta: venta['total']
        ingreso_neto = sum(map(calcular_neto, ventas))
        
        # Calcular métricas
        ticket_promedio = ingreso_neto / len(ventas) if ventas else 0
        tasa_descuento = (descuentos_totales / ingreso_bruto * 100) if ingreso_bruto > 0 else 0
        
        print(f"""
RESUMEN:
--------
Total de ventas: {len(ventas)}
Unidades vendidas: {sum(map(lambda v: v['cantidad'], ventas))}

INGRESOS:
---------
Ingreso bruto (sin descuentos): ${ingreso_bruto:.2f}
Descuentos aplicados: -${descuentos_totales:.2f}
Ingreso neto (con descuentos): ${ingreso_neto:.2f}

METRICAS:
---------
Ticket promedio: ${ticket_promedio:.2f}
Descuento promedio por venta: ${descuentos_totales/len(ventas):.2f}
Tasa de descuento: {tasa_descuento:.1f}%
""")
        
        imprimir_separador()
    
    except Exception as e:
        imprimir_mensaje(f"Error inesperado: {e}")

# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def principal():
    """Función principal con menú del sistema"""
    imprimir_encabezado("SISTEMA INTEGRAL DE GESTION DE INVENTARIO Y VENTAS")
    print("Sistema inicializado con 5 libros pre-cargados.\n")
    
    while True:
        try:
            print(f"""
{'=' * 60}
SISTEMA DE GESTION DE LIBROS
{'=' * 60}

GESTION DE INVENTARIO
1. Registrar libro
2. Consultar libro
3. Actualizar libro
4. Eliminar libro
5. Mostrar todos los libros

GESTION DE VENTAS
6. Registrar venta
7. Consultar ventas
8. Buscar ventas por cliente

MODULO DE REPORTES
9. Top 3 libros mas vendidos
10. Ventas por autor
11. Reporte financiero (neto vs bruto)

0. Salir

{'=' * 60}
""")
            
            opcion = input("Seleccione una opcion: ").strip()
            
            if opcion == "1":
                registrar_producto()
                
            elif opcion == "2":
                consultar_producto()
                
            elif opcion == "3":
                actualizar_producto()
                
            elif opcion == "4":
                eliminar_productos()
                
            elif opcion == "5":
                imprimir_todos_libros()
            
            elif opcion == "6":
                registrar_venta()
            
            elif opcion == "7":
                consultar_ventas()
            
            elif opcion == "8":
                buscar_venta_por_cliente()
            
            elif opcion == "9":
                top_3_mas_vendidos()
            
            elif opcion == "10":
                ventas_por_autor()
            
            elif opcion == "11":
                reporte_financiero()
            
            elif opcion == "0":
                imprimir_mensaje("Gracias por usar el sistema. Hasta luego!")
                break
                
            else:
                imprimir_mensaje("Opcion invalida. Por favor intente de nuevo.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            imprimir_mensaje(f"Error inesperado: {e}\nEl programa continuara funcionando.")

if __name__ == "__main__":
    principal()