
def Verify_Cuit(cuit):
    if (not cuit): 
        return False
    if (len(cuit) != 13): 
        return False
    rv = False
    resultado = 0
    cuit_nro = cuit.replace("-", "")
    codes = "6789456789"
    cuit_long = int(cuit_nro)
    verificador = int(cuit_nro[len(cuit_nro)-1])
    x = 0
    while x < 10:
        digitoValidador = codes[x]
        digito = cuit_nro[x]
        if digitoValidador and digito:
            digitoValidacion = int(digitoValidador) * int(digito)
            resultado += digitoValidacion
        x = x + 1
    resultado = resultado % 11
    rv = (resultado == verificador)
    return rv