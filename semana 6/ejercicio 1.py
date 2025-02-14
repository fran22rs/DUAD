def impuesto_de_producto(precio):
    return precio*0.13


def monto_total_del_producto(precio):
    impuesto= impuesto_de_producto(precio)
    total= precio + impuesto
    return total

precio=230
print(monto_total_del_producto(precio))    
