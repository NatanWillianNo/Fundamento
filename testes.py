import numpy as np
import matplotlib.pyplot as plt

def draw_heart():
    # Definir a equação do coração
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Plotando o coração
    plt.figure(figsize=(6, 5))
    plt.plot(x, y, 'r')
    plt.fill_between(x, y, color='red')
    
    # Adicionando o texto "I love you Python"
    plt.text(0, 0, "I love you Python", fontsize=15, ha='center', color='white')
    
    # Removendo os eixos
    plt.axis('off')
    
    # Mostrando o gráfico
    plt.show()

draw_heart()
