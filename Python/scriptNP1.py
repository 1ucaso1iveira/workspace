from tkinter import N
import numpy as np
import matplotlib.pyplot as plt

plt.grid(True)
plt.axis('on')

plt.title("Lucas Oliveira - F31JJA8", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 10},
                    loc='left')

plt.title("lucas.oliveira247@aluno.unip.br", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 10},
                    loc='right')

# chart size
plt.axis([-10, 250, 90, 0])

# colored square
plt.plot([40,40],[50,80],linewidth=3,color='pink')
plt.plot([0,0],[50,80],linewidth=3,color='blue')
plt.plot([0,40],[50,50],linewidth=3,color='red')
plt.plot([0,40],[80,80],linewidth=3,color='green')

plt.scatter([20,20],[65,65],s=100,color='k')


# dotted square
plt.plot([60,100], [80,80], linewidth=3, color='black', linestyle=':')
plt.plot([60,100], [50,50], linewidth=3, color='black', linestyle=':')
plt.plot([60,60], [50,80], linewidth=3, color='black', linestyle=':')
plt.plot([100,100], [50,80], linewidth=3, color='black', linestyle=':')


# arrow
plt.arrow(150,65, 60, 0, linewidth=1, color='m', head_length=5, head_width=3)



plt.show()