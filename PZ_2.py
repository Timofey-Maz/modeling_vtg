import numpy as np
import matplotlib.pyplot as plt
k = 2
mu = 10.0
A = 1.0
t_end = 10.0
dt = 0.01
t = np.arange(0, t_end, dt)
Omega = np.zeros_like(t)
Omega[t < 3] = 2.0; Omega[(t >= 3) & (t < 7)] = 1.0
Omega[t >= 7] = 0
psi = np.cumsum(Omega) * dt
phi_beam = -(2 / (k**2 + 1)) * psi

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, Omega, 'b-', linewidth=2)
plt.title('Угловая скорость omega(t)', fontsize=14)
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('omega, рад/с', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, t_end)
plt.subplot(2, 1, 2)
plt.plot(t, psi, 'r-', linewidth=2, label='psi (угол поворота основания)')
plt.plot(t, phi_beam, 'g--', linewidth=2, label='phi_пуч (угол отставания волновой картины)')
plt.title('Углы поворота основания и отставания волновой картины', fontsize=14)
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('Угол, рад', fontsize=12)
plt.legend(loc='best', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, t_end)
plt.tight_layout()
plt.show()
psi_from_beam = -((k**2 + 1) / 2) * phi_beam
plt.figure(figsize=(10, 6))
plt.plot(t, psi, 'b-', linewidth=2, label='psi (интегрирование omega)')
plt.plot(t, psi_from_beam, 'r--', linewidth=2, label='psi (из волновой картины)')
plt.title('Сравнение углов: интегрирование omega и волновая картина', fontsize=14)
plt.xlabel('Время t, с', fontsize=12)
plt.ylabel('Угол psi, рад', fontsize=12)
plt.legend(loc='best', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, t_end)
plt.tight_layout()
plt.show()