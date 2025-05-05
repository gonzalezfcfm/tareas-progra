# Gimnasia de vacas
# Abrimos el archivo de entrada
with open("gymnastics.in", "r") as f:
    K, N = map(int, f.readline().split())  # Número de sesiones y vacas
    sessions = [list(map(int, f.readline().split())) for _ in range(K)]  # Leemos todas las sesiones

# rankings guarda la posición de cada vaca en cada sesión
rankings = []
for session in sessions:
    rank = {}
    for idx, cow in enumerate(session):
        rank[cow] = idx  # Guardamos la posición (mientras más cerca del inicio, mejor)
    rankings.append(rank)

# Contamos los pares consistentes
consistent_pairs = 0
for a in range(1, N + 1):         # Por cada vaca A
    for b in range(1, N + 1):     # Por cada vaca B
        if a == b:
            continue              # No comparamos la vaca consigo misma
        # Verificamos si A siempre estuvo antes que B
        if all(rank[a] < rank[b] for rank in rankings):
            consistent_pairs += 1

# Escribimos la salida
with open("gymnastics.out", "w") as f:
    f.write(f"{consistent_pairs}\n")
