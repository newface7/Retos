def factura_energia(informacion:dict)->dict:
    numeroDeSuscriptor = informacion["numeroSuscriptor"]
    cargoBasico = informacion["cargoBasico"]
    kwSubsidiados = informacion["kwSubsidiados"]
    kwExtra = informacion["cargoPorKwExtra"]
    kwConsumidos = informacion["kwConsumidos"]
    Estrato = informacion["estrato"]

    if kwConsumidos <= kwSubsidiados:
        consumo = 0
    else:
        consumo = kwConsumidos-kwSubsidiados

    subtotal = (cargoBasico + (consumo)*kwExtra)    
    
    total = 0
    iva = 0
    seguro = 0

    if subtotal >= 30000:
        iva = 0.2 * subtotal
        if Estrato <= 3:
            seguro = 7500
        elif Estrato >=3:
            seguro = 8500
                
    elif subtotal < 30000:
        iva = 0 * subtotal
        if Estrato <= 3:
           seguro = 5500
        if Estrato >=3:
           seguro = 6500
                
    iva = round(iva, 1)
    subtotal = subtotal + iva + seguro
    total = round(subtotal, 1)
    total = float(total)
    
    diccionario_respuesta = {
        "numeroSuscriptor" : numeroDeSuscriptor,
        "valorImpuesto" : iva,
        "valorSeguro" : seguro,
        "totalFactura" : total
    }
    return diccionario_respuesta

usuariosFactura = {
    "numeroSuscriptor" : "ABC123",
    "cargoBasico" : 17000,
    "kwSubsidiados" : 173,
    "cargoPorKwExtra" : 5000,
    "kwConsumidos" : 172,
    "estrato" : 2,
}

print (factura_energia(usuariosFactura))



