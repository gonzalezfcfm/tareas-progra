#La señal de la vaca
# Abrimos el archivo de entrada y leemos los datos
with open("cowsignal.in", "r") as fin:
    M, N, K = map(int, fin.readline().split())
    signal = [fin.readline().strip() for _ in range(M)]

# Creamos una nueva lista para almacenar la señal ampliada
amplified_signal = []

for row in signal:
    # Ampliamos horizontalmente
    expanded_row = ''.join(char * K for char in row)
    # Ampliamos verticalmente
    for _ in range(K):
        amplified_signal.append(expanded_row)

# Escribimos la señal ampliada en el archivo de salida
with open("cowsignal.out", "w") as fout:
    for row in amplified_signal:
        fout.write(row + "\n")
