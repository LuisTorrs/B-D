"""
Programa para convertir números binarios a decimales
"""

def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal.
    
    Args:
        binario (str): Número en formato binario
        
    Returns:
        int: Número en formato decimal
    """
    # Validar que solo contenga 0 y 1
    if any(bit not in "01" for bit in binario):
        raise ValueError("Error: introduce solo números binarios (0 y 1).")
    
    # Convertir binario a decimal
    decimal = int(binario, 2)
    return decimal


def main():
    """
    Función principal que pide al usuario un número binario y lo convierte a decimal.
    """
    print("=" * 50)
    print("CONVERTIDOR DE BINARIO A DECIMAL")
    print("=" * 50)
    
    while True:
        try:
            binario = input("\nIntroduce un número binario (o 'salir' para terminar): ").strip()
            
            if binario.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            if not binario:
                print("Error: por favor introduce un número binario.")
                continue
            
            decimal = binario_a_decimal(binario)
            print(f"✓ El número binario '{binario}' equivale a {decimal} en decimal.")
            
        except ValueError as e:
            print(f"✗ {e}")


if __name__ == "__main__":
    main()
