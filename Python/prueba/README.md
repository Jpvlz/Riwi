# Electronic Store Management System

Comprehensive inventory and sales management system for an electronics store developed in Python with a full interactive menu.

---

## Project Description

Complete commercial management system that allows you to manage the **inventory** of electronic products, process **sales** with discounts depending on the customer type, and generate detailed **analytical reports** on business performance.

**Main Features:**
- **Full inventory management (CRUD)**
- Sales system with **customer-type discounts**
- Generation of **reports and analysis** of performance
- **Extensive data validations**
- Intuitive user interface
- **Cache system** to optimize reports

---

## System Features

### INVENTORY MANAGEMENT

#### 1. Add Product
Registers new products in the inventory with: **Unique ID**, Name, Brand, Category, Unit Price, Available Stock, and Warranty Months.

**Validations:**
- Unique ID (no duplicates)
- Required fields cannot be empty
- Price greater than zero
- Non-negative stock
- Non-negative warranty

#### 2. View All Products
Displays a formatted table with: ID, name, brand, category, price, available stock, warranty, the total number of products, and the total inventory value.

#### 3. Update Product
Modifies existing product information through **ID search**. Offers the option to keep current values (press Enter).

#### 4. Delete Product
Deletes products from the inventory, requiring **explicit confirmation (YES)** to prevent accidental deletions.

---

### SALES MANAGEMENT

#### 5. Register Sale
Processes complete sales with: Customer data, customer type selection, product selection, and quantity to sell.

* **Stock validation**
* Automatic calculation of discounts and total
* **Automatic inventory update**
* Generation of a detailed sales receipt

**Customer Types and Discounts:**
| Type | Discount |
| :--- | :--- |
| Regular | 0% |
| Member | 5% |
| VIP | 10% |
| Corporate | 15% |

#### 6. View Sales History
Displays a table with all registered sales, including date, customer, product, quantity, total sale amount, and **total generated revenue**.

---

### REPORTS AND ANALYSIS

#### 7. Top 3 Best-Selling Products
Ranking of products by units sold, showing generated revenue and **percentage contribution** over the total.

#### 8. Sales by Brand
Consolidated report by brand, showing units, revenue, and **percentage contribution**, ordered from highest to lowest revenue.

#### 9. Financial Report
Complete financial analysis, including:

* **General Metrics:** Total transactions, gross income, total discounts applied, **net income**, average ticket, and effective discount rate.
* **Analysis by Customer Type:** Number of transactions, revenue, and average ticket per type.

---

## Data Structure

The system uses the following Python data structures to store information:

### Product
```python
{
   'id': str,          # Eg: "PROD001" (Unique identifier)
   'nombre': str,      # Eg: "Wireless Gaming Mouse"
   'marca': str,       # Eg: "Logitech"
   'categoria': str,   # Eg: "Peripherals"
   'precio': float,    # Eg: 79.99 (Unit price)
   'stock': int,       # Eg: 45 (Available quantity)
   'garantia': int     # Eg: 24 (Months of coverage)
}
