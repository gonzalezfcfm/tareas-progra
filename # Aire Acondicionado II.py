# Aire Acondicionado II
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])  # Número de vacas
    idx += 1
    M = int(data[idx])  # Número de aires acondicionados
    idx += 1
    
    vacas = []
    for _ in range(N):
        s = int(data[idx])    # Inicio del rango de la vaca
        idx += 1
        t = int(data[idx])    # Fin del rango de la vaca
        idx += 1
        c = int(data[idx])    # Necesidad de enfriamiento
        idx += 1
        vacas.append((s, t, c))
    
    aires = []
    for _ in range(M):
        a = int(data[idx])    # Inicio del rango del aire
        idx += 1
        b = int(data[idx])    # Fin del rango del aire
        idx += 1
        p = int(data[idx])    # Potencia de enfriamiento
        idx += 1
        m = int(data[idx])    # Costo
        idx += 1
        aires.append((a, b, p, m))
    
    mejor_costo = float('inf')  # Inicializamos con infinito

    # Probar todas las combinaciones de aires (bitmask de 0 a 2^M)
    for mascara in range(1 << M):
        enfriamiento = [0] * 101  # Enfriamiento total en cada puesto
        costo_total = 0
        
        for i in range(M):
            if (mascara >> i) & 1:
                a, b, p, m = aires[i]
                costo_total += m
                for j in range(a, b + 1):
                    enfriamiento[j] += p
        
        valido = True
        for s, t, c in vacas:
            for j in range(s, t + 1):
                if enfriamiento[j] < c:
                    valido = False
                    break
            if not valido:
                break
        
        if valido:
            mejor_costo = min(mejor_costo, costo_total)
    
    print(mejor_costo)
