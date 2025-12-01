"""
Comprehensive Inventory and Sales Management System with Dynamic Reports
Case: National bookstore digital area management system
"""

from datetime import datetime

# ============================================================================
# INITIAL DATA - 5 PRE-LOADED BOOKS
# ============================================================================

books = [
    {
        "title": "sun and moon",
        "author": "marcus",
        "category": "love",
        "price": 100,
        "stock": 10
    },
    {
        "title": "fire",
        "author": "thiago",
        "category": "action",
        "price": 200,
        "stock": 10
    },
    {
        "title": "the cold",
        "author": "juan",
        "category": "fiction",
        "price": 300,
        "stock": 10
    },
    {
        "title": "the colors",
        "author": "stiven",
        "category": "suspense",
        "price": 400,
        "stock": 10
    },
    {
        "title": "at night",
        "author": "arturo",
        "category": "fancy",
        "price": 500,
        "stock": 10
    }
]

sales = []

# ============================================================================
# REUSABLE PRINT FUNCTIONS
# ============================================================================

def print_header(title):
    """Prints a formatted header"""
    print(f"\n{'=' * 60}\n{title.center(60)}\n{'=' * 60}")

def print_separator():                                   
    """Prints a separator line"""
    print("-" * 60)

def print_book_info(book, show_number=None):  
    """Prints book information"""
    prefix = f"{show_number}. " if show_number else ""
    print(f"""{prefix}Titulo: {book['title']}
Autor: {book['author']}
Categoria: {book['category']}
Precio: ${book['price']}
Stock: {book['stock']}
""")

def print_sale_detail(sale):
    """Prints complete sale detail"""
    print(f"""
ID Venta: {sale['id']}
Cliente: {sale['customer']}
Libro: {sale['book_title']}
Autor: {sale['author']}
Cantidad: {sale['quantity']}
Precio unitario: ${sale['unit_price']}
Subtotal: ${sale['subtotal']:.2f}
Descuento: {sale['discount']}% (-${sale['discount_amount']:.2f})
TOTAL: ${sale['total']:.2f}
Fecha: {sale['date']}
""")
    print_separator()

def print_message(message):
    """Prints a message"""
    print(f"\n{message}\n")

# ============================================================================
# VALIDATION FUNCTIONS (NEW - EXCEPTION HANDLING)
# ============================================================================

def get_valid_string(prompt, allow_empty=False):
    """Gets a non-empty string with exception handling"""
    while True:
        try:
            value = input(prompt).strip()
            if not value and not allow_empty:
                print("Error: Este campo no puede estar vacio.")
                continue
            return value
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None


def get_valid_float(prompt):
    """Gets a valid positive float with exception handling"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return value
        except ValueError:
            print("Error: Por favor ingrese un numero valido.")
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

def get_valid_int(prompt):
    """Gets a valid positive integer with exception handling"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return value
        except ValueError:
            print("Error: Por favor ingrese un numero entero valido.")
        except KeyboardInterrupt:
            print("\nOperacion cancelada.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

# ============================================================================
# BOOK MANAGEMENT FUNCTIONS
# ============================================================================

def find_book(title_search):
    """Auxiliary function to find a book by title"""
    for book in books:
        if book["title"].lower() == title_search.lower():
            return book
    return None

def register_product():
    """Function to register a product"""
    try:
        print_header("REGISTRAR LIBRO")
        
        title = get_valid_string("Ingrese el titulo del libro: ")
        if not title: return
        
        # Check if book already exists
        if find_book(title):
            print_message(f"El libro '{title}' ya existe.")
            return
        
        author = get_valid_string("Ingrese el autor del libro: ")
        if not author: return
        
        category = get_valid_string("Ingrese la categoria del libro: ")
        if not category: return
        
        price = get_valid_float("Ingrese el precio del libro: ")
        if price is None: return
        
        stock = get_valid_int("Ingrese la cantidad del libro: ")
        if stock is None: return

        books.append({
            "title": title,
            "author": author,
            "category": category,
            "price": price,
            "stock": stock
        })
        
        print_message("Libro registrado exitosamente!")
        
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def consult_product():
    """Function to consult a product"""
    try:
        print_header("CONSULTAR LIBRO")
        
        title_search = get_valid_string("Ingrese el titulo del libro que desea buscar: ")
        if not title_search: return
        
        book = find_book(title_search)

        if book:
            print(f"\nEste libro: '{title_search}' existe.\n")
            print_book_info(book)
        else:
            print_message(f"Este libro: '{title_search}' no fue encontrado.")
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def update_product():
    """Function to update a product"""
    try:
        print_header("ACTUALIZAR LIBRO")
        
        title_search = get_valid_string("Ingrese el nombre del libro que desea actualizar: ")
        if not title_search: return
        
        book = find_book(title_search)
        
        if book:
            print(f"\nLibro encontrado: {title_search}\n")
            print("""¿Que desea actualizar?

1. Autor
2. Categoria
3. Precio
4. Stock
""")
            
            option = input("Seleccione una opcion: ")
            
            if option == "1":
                new_author = get_valid_string("Ingrese el nuevo autor: ")
                if new_author:
                    book["author"] = new_author
                    print_message("Autor actualizado correctamente.")

            elif option == "2":
                new_category = get_valid_string("Ingrese la nueva categoria: ")
                if new_category:
                    book["category"] = new_category
                    print_message("Categoria actualizada correctamente.")

            elif option == "3":
                new_price = get_valid_float("Ingrese el nuevo precio: ")
                if new_price is not None:
                    book["price"] = new_price
                    print_message("Precio actualizado correctamente.")

            elif option == "4":
                new_stock = get_valid_int("Ingrese el nuevo stock: ")
                if new_stock is not None:
                    book["stock"] = new_stock
                    print_message("Stock actualizado correctamente.")

            else:
                print_message("Opcion invalida.")
        else:
            print_message(f"El libro '{title_search}' no fue encontrado.")
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def delete_products():
    """Function to delete a product from the list"""
    try:
        print_header("ELIMINAR LIBRO")
        
        title_search = get_valid_string("Ingrese el titulo del libro que desea eliminar: ")
        if not title_search: return
        
        book = find_book(title_search)
        
        if book:
            print(f"\nLibro encontrado: {title_search}\n")
            print_book_info(book)
            
            confirmation = input("¿Esta seguro de eliminar este libro? (si/no): ")
            
            if confirmation.lower() == "si":
                books.remove(book)
                print_message(f"El libro '{title_search}' ha sido eliminado correctamente.")
            else:
                print_message("Eliminacion cancelada.")
        else:
            print_message(f"El libro '{title_search}' no fue encontrado.")
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def print_all_books():
    """Prints all books in the list"""
    if not books:
        print_message("No hay libros registrados.")
        return
    
    print_header("LISTA DE LIBROS")
    for i, book in enumerate(books, 1):
        print_book_info(book, show_number=i)

# ============================================================================
# SALES MANAGEMENT FUNCTIONS
# ============================================================================

def register_sale():
    """Function to register a sale"""
    try:
        print_header("REGISTRAR VENTA")
        
        customer_name = get_valid_string("Nombre del cliente: ")
        if not customer_name: return
        
        title_search = get_valid_string("Titulo del libro a vender: ")
        if not title_search: return
        
        book = find_book(title_search)
        
        if not book:
            print_message(f"El libro '{title_search}' no fue encontrado.")
            return
        
        print("\nLibro encontrado:\n")
        print_book_info(book)
        
        quantity = get_valid_int("Cantidad a vender: ")
        if quantity is None: return
        
        if quantity > book['stock']:
            print_message(f"Error: Solo hay {book['stock']} unidades disponibles.")
            return
        
        discount = get_valid_float("Descuento en % (0 si no aplica): ")
        if discount is None: return
        
        # Calculate totals using lambda functions
        calculate_subtotal = lambda price, qty: price * qty
        calculate_discount_amount = lambda subtotal, disc: subtotal * (disc / 100)
        calculate_total = lambda subtotal, disc_amount: subtotal - disc_amount
        
        subtotal = calculate_subtotal(book['price'], quantity)
        discount_amount = calculate_discount_amount(subtotal, discount)
        total = calculate_total(subtotal, discount_amount)
        
        # Update stock
        book['stock'] -= quantity
        
        # Register sale
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        sale = {
            "id": len(sales) + 1,
            "customer": customer_name,
            "book_title": book['title'],
            "author": book['author'],
            "quantity": quantity,
            "unit_price": book['price'],
            "subtotal": subtotal,
            "discount": discount,
            "discount_amount": discount_amount,
            "total": total,
            "date": date
        }
        
        sales.append(sale)
        
        print_header("VENTA REGISTRADA")
        print(f"""Cliente: {customer_name}
Libro: {book['title']}
Cantidad: {quantity}
Precio unitario: ${book['price']}
Subtotal: ${subtotal:.2f}
Descuento ({discount}%): -${discount_amount:.2f}
TOTAL: ${total:.2f}
Fecha: {date}
Stock restante: {book['stock']}
""")
        print_separator()
        
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def consult_sales():
    """Function to consult sales"""
    if not sales:
        print_message("No hay ventas registradas.")
        return
    
    print_header("VENTAS REGISTRADAS")

    for sale in sales:
        print_sale_detail(sale)
    
    # Calculate totals using lambda
    total_sales = sum(map(lambda s: s['total'], sales))
    total_books_sold = sum(map(lambda s: s['quantity'], sales))
    
    print_header("RESUMEN DE VENTAS")
    print(f"""Total de ventas: {len(sales)}
Libros vendidos: {total_books_sold}
Ingresos totales: ${total_sales:.2f}
""")

def search_sale_by_customer():
    """Search sales by customer"""
    try:
        print_header("BUSCAR VENTAS POR CLIENTE")
        
        customer_name = get_valid_string("Nombre del cliente: ")
        if not customer_name: return
        
        # Using lambda for filtering
        filter_customer = lambda sale: customer_name.lower() in sale['customer'].lower()
        customer_sales = list(filter(filter_customer, sales))
        
        if not customer_sales:
            print_message(f"No se encontraron ventas para el cliente '{customer_name}'.")
            return
        
        print_header(f"VENTAS DE {customer_name.upper()}")
        
        for sale in customer_sales:
            print(f"""ID: {sale['id']} | Cliente: {sale['customer']} | Libro: {sale['book_title']} | Cantidad: {sale['quantity']} | Total: ${sale['total']:.2f}
Fecha: {sale['date']}
""")
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")




# ============================================================================
# REPORTS MODULE (NEW - REQUIRED FUNCTIONALITY)
# ============================================================================

def top_3_best_selling():
    """Shows top 3 best-selling products"""
    try:
        print_header("TOP 3 LIBROS MAS VENDIDOS")
        
        if not sales:
            print_message("No hay datos de ventas disponibles.")
            return
        
        # Group sales by book using lambda
        book_sales = {}
        for sale in sales:
            title = sale['book_title']
            if title not in book_sales:
                book_sales[title] = {'quantity': 0, 'revenue': 0}
            book_sales[title]['quantity'] += sale['quantity']
            book_sales[title]['revenue'] += sale['total']
        
        # Sort by quantity using lambda
        sorted_books = sorted(book_sales.items(), key=lambda x: x[1]['quantity'], reverse=True)
        
        print("\nRANKING POR CANTIDAD VENDIDA:\n")
        for i, (title, data) in enumerate(sorted_books[:3], 1):
            print(f"{i}. {title}")
            print(f"   Unidades vendidas: {data['quantity']}")
            print(f"   Ingresos: ${data['revenue']:.2f}\n")
        
        print_separator()
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def sales_by_author():
    """Shows sales grouped by author"""
    try:
        print_header("VENTAS POR AUTOR")
        
        if not sales:
            print_message("No hay datos de ventas disponibles.")
            return
        
        # Group by author using lambda
        author_sales = {}
        for sale in sales:
            author = sale['author']
            if author not in author_sales:
                author_sales[author] = {'quantity': 0, 'revenue': 0, 'books': set()}
            author_sales[author]['quantity'] += sale['quantity']
            author_sales[author]['revenue'] += sale['total']
            author_sales[author]['books'].add(sale['book_title'])
        
        # Calculate total revenue using lambda
        total_revenue = sum(map(lambda x: x['revenue'], author_sales.values()))
        
        print("\nRENDIMIENTO POR AUTOR:\n")
        for author, data in sorted(author_sales.items(), key=lambda x: x[1]['revenue'], reverse=True):
            percentage = (data['revenue'] / total_revenue * 100) if total_revenue > 0 else 0
            print(f"Autor: {author.upper()}")
            print(f"   Libros vendidos: {', '.join(data['books'])}")
            print(f"   Unidades: {data['quantity']}")
            print(f"   Ingresos: ${data['revenue']:.2f} ({percentage:.1f}% del total)")
            print()
        
        print_separator()
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

def financial_report():
    """Shows net and gross income report"""
    try:
        print_header("REPORTE FINANCIERO")
        
        if not sales:
            print_message("No hay datos de ventas disponibles.")
            return
        
        # Calculate gross income (without discounts) using lambda
        calculate_gross = lambda sale: sale['subtotal']
        gross_income = sum(map(calculate_gross, sales))
        
        # Calculate total discounts using lambda
        calculate_discount = lambda sale: sale['discount_amount']
        total_discounts = sum(map(calculate_discount, sales))
        
        # Calculate net income (with discounts) using lambda
        calculate_net = lambda sale: sale['total']
        net_income = sum(map(calculate_net, sales))
        
        # Calculate metrics
        avg_ticket = net_income / len(sales) if sales else 0
        discount_rate = (total_discounts / gross_income * 100) if gross_income > 0 else 0
        
        print(f"""
RESUMEN:
--------
Total de ventas: {len(sales)}
Unidades vendidas: {sum(map(lambda s: s['quantity'], sales))}

INGRESOS:
---------
Ingreso bruto (sin descuentos): ${gross_income:.2f}
Descuentos aplicados: -${total_discounts:.2f}
Ingreso neto (con descuentos): ${net_income:.2f}

METRICAS:
---------
Ticket promedio: ${avg_ticket:.2f}
Descuento promedio por venta: ${total_discounts/len(sales):.2f}
Tasa de descuento: {discount_rate:.1f}%
""")
        
        print_separator()
    
    except Exception as e:
        print_message(f"Error inesperado: {e}")

# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main function with system menu"""
    print_header("SISTEMA INTEGRAL DE GESTION DE INVENTARIO Y VENTAS")
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
            
            option = input("Seleccione una opcion: ").strip()
            
            if option == "1":
                register_product()
                
            elif option == "2":
                consult_product()
                
            elif option == "3":
                update_product()
                
            elif option == "4":
                delete_products()
                
            elif option == "5":
                print_all_books()
            
            elif option == "6":
                register_sale()
            
            elif option == "7":
                consult_sales()
            
            elif option == "8":
                search_sale_by_customer()
            
            elif option == "9":
                top_3_best_selling()
            
            elif option == "10":
                sales_by_author()
            
            elif option == "11":
                financial_report()
            
            elif option == "0":
                print_message("Gracias por usar el sistema. Hasta luego!")
                break
                
            else:
                print_message("Opcion invalida. Por favor intente de nuevo.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print_message(f"Error inesperado: {e}\nEl programa continuara funcionando.")

if __name__ == "__main__":
    main()