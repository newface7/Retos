def factura_energia(numeroDeSuscriptor: str, cargoBasico: int, kwSubsidiados: int, cargoPorkwExtra: int, kwConsumidos: int) -> str:

    totalFactura = (cargoBasico + (kwConsumidos-kwSubsidiados)*cargoPorkwExtra)*1.19

    totalFactura = round(totalFactura, 1)
    
    return f"El cliente {numeroDeSuscriptor} debe cancelar: {totalFactura} pesos"

print(factura_energia("YFC321", 30000, 200, 400, 400))

print(factura_energia("ACJ547", 40000, 100, 200, 250))


