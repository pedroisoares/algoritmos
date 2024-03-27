def inss(salario):
    if salario <= 1412:
        inss = salario * 0.075
    else:
        if salario <= 2666.68:
            inss = salario * 0.09 - 21.18
        else:
            if salario <= 4000.03:
                inss = salario * 0.12 - 101.18
            else:
                if salario <= 7786.02:
                    inss = salario * 0.14 - 181.18
                else:
                    inss = 908.86
    
    return inss

def ir(bcir):
    if bcir <= 2112:
        ir = 0.0
    else:
        if bcir <= 2826.65:
            ir = bcir * 0.075 - 158.4
        else:
            if bcir <= 3751.05:
                ir = bcir * 0.15 - 370.4
            else:
                if bcir <= 4664.68:
                    ir = bcir * 0.225 - 651.73
                else:
                    ir = bcir * 0.275 - 884.96
    
    return ir

def vr(salario):
    vr = salario * 0.01
    
    return vr

def vt(salario):
    vt = salario * 0.06
    
    return vt

# Main
aNome = [""] * (5)
aSalario = [0] * (5)
aDiasTrab = [0] * (5)
aINSS = [0] * (5)
aIR = [0] * (5)
aVT = [0] * (5)
aVR = [0] * (5)
aSalLiq = [0] * (5)

for i in range(0, 4 + 1, 1):
    aNome[i] = input()
    aSalario[i] = float(input())
    aDiasTrab[i] = int(input())
    aSalario[i] = float(int(int(aSalario[i] / 30 * aDiasTrab[i] * 1000) + 1) * 100) / 100
    print(aSalario[i])
    aVT[i] = vt(aSalario[i])
    aVR[i] = vr(aSalario[i])
    aINSS[i] = inss(aSalario[i])
    bcir = aSalario[i] - aINSS[i]
    aIR[i] = ir(bcir)
    aSalLiq[i] = aSalario[i] - aINSS[i] - aIR[i] - aVT[i] - aVR[i]
print("   *************  FOLHA DE PAGAMENTO  EMPRESA: XXXXXXXX   *********** ")
print("NOME                 SALARIO       Dias Trab.       INSS     IR        VT          VR            SAL.LIQ. ")
for i in range(0, 4 + 1, 1):
    print(aNome[i] + "   ", end='', flush=True)
    print(str(aSalario[i]) + "   ", end='', flush=True)
    print(str(aDiasTrab[i]) + "   ", end='', flush=True)
    print(str(aINSS[i]) + "   ", end='', flush=True)
    print(str(aIR[i]) + "   ", end='', flush=True)
    print(str(aVT[i]) + "   ", end='', flush=True)
    print(str(aVR[i]) + "   ", end='', flush=True)
    print(aSalLiq[i])
