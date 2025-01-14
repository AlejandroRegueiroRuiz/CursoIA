import argparse

def convertir_de_C_a_F(temp):
    return f"{temp}º Celsius son equivalentes a {(temp * 1.8 + 32)}º Fahrenheit"

convertir_de_F_a_C = lambda temp: (f"{temp}º Fahrenheit son equivalentes a {(temp - 32) * 5/9}º Celsius")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Conversor de temperatura')
    parser.add_argument('--temp', type=float, required=True, help='Valor de temperatura a convertir.')
    parser.add_argument('--scale', type=str, choices=['C', 'F'], default='C', help='Escala de la temperatura de entrada (C o F). Opcional - Valor por defecto: C')

    args = parser.parse_args()

    if args.scale == 'C':
        print(convertir_de_C_a_F(args.temp))
    else:
        print(convertir_de_F_a_C(args.temp))  
