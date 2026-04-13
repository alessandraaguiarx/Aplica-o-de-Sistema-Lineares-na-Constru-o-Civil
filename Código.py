import numpy as np

print("Aplicação de Sistema Lineares")

try:
    # Entrada
    area_total = float(input("Digite a área total (m²): "))
    blocos_total = float(input("Digite a quantidade total de blocos: "))

    # Matriz do sistema
    A = np.array([[1, 1],
                  [13, 15]])
    B = np.array([area_total, blocos_total])

    # Determinante
    D = np.linalg.det(A)
    print("\nDeterminante:", D)

    # Classificação
    if D != 0:
        print("Sistema Possível e Determinado (SPD)")
        x, y = np.linalg.solve(A, B)

        # Materiais
        argamassa = 0.02 * x + 0.03 * y
        graute = 0.04 * y

        print("\nResultados")
        print(f"Convencional (x): {x:.2f} m²")
        print(f"Estrutural (y): {y:.2f} m²")
        print(f"Argamassa: {argamassa:.3f} m³")
        print(f"Graute: {graute:.3f} m³")
    else:
        # Verifica consistência do sistema estendido
        A_ext = np.array([[1, 1, area_total],
                          [13, 15, blocos_total]])
        posto_A = np.linalg.matrix_rank(A)
        posto_A_ext = np.linalg.matrix_rank(A_ext)

        if posto_A == posto_A_ext:
            print("Sistema Possível e Indeterminado (SPI)")
        else:
            print("Sistema Impossível (SI)")
except Exception as e:
    print("Erro:", e)
