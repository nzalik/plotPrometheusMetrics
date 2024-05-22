import matplotlib.pyplot as plt

# Vos données existantes
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# Créer la figure avec deux sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Tracer le premier graphique
ax1.plot(x1, y1)
ax1.set_ylabel('cores per second')
ax1.set_title('CPU usage')
ax1.grid(True)

# Tracer le deuxième graphique
ax2.plot(x2, y2)
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('cores per second')
ax2.grid(True)

# Aligner les tiques de l'axe des x
ax1.set_xticks(x1)
ax1.set_xticklabels([str(x) for x in x1], rotation=45)
ax2.set_xticks(x2)
ax2.set_xticklabels([str(x) for x in x2], rotation=45)

# Ajuster l'espacement entre les sous-graphiques
plt.subplots_adjust(hspace=0.5)

# Ajouter la légende
ax1.legend()
ax2.legend()

plt.show()