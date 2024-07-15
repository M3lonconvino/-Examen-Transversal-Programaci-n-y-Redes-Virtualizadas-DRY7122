def verificar_vlan(numero_vlan):
    if 1 <= numero_vlan <= 4094:
        return "VLAN del rango normal."
    elif 4095 <= numero_vlan <= 4096:
        return "VLAN del rango extendido."
    else:
        return "Número de VLAN fuera de los rangos normal y extendido."

def main():
    numero_vlan = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(numero_vlan)
    print(resultado)

if __name__ == "__main__":
    main()