
# Matriz de inventario: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [101, "Teclado", 3, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 2, 5],
    [104, "USB", 20, 15],
    [105, "Impresora", 0, 3]
]

def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad a pedir según stock actual y mínimo requerido.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

print("=== Informe de pedidos ===")
for codigo, nombre, stock_actual, stock_minimo in inventario:
    cantidad = calcular_pedido(stock_actual, stock_minimo)
    print(f"Artículo: {nombre} | Pedido: {cantidad}")
