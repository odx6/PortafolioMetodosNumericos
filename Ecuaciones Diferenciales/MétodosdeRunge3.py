# PROGRAMA PRUEBA

# prueba y'-y-x+(x**2)-1 =0, y(0)=1

# INGRESO
# d1y = y' = f, d2y = y'' = f'
d1y = lambda x,y: y -x**2 + x + 1
x0 = 0
y0 = 1
h  = 0.1
muestras = 5

# PROCEDIMIENTO
puntosRK2 = rungekutta2(d1y,x0,y0,h,muestras)
xi = puntosRK2[:,0]
yiRK2 = puntosRK2[:,1]

# SALIDA
print('estimado[xi,yi]')
print(puntosRK2)

# ERROR vs solución conocida
y_sol = lambda x: ((np.e)**x) + x + x**2

yi_psol  = y_sol(xi)
errores  = yi_psol - yiRK2
errormax = np.max(np.abs(errores))

# SALIDA
print('Error máximo estimado: ',errormax)
print('entre puntos: ')
print(errores)

# GRAFICA [a,b+2*h]
a = x0
b = h*muestras+2*h
muestreo = 10*muestras+2
xis = np.linspace(a,b,muestreo)
yis = y_sol(xis)

# Gráfica
import matplotlib.pyplot as plt

plt.plot(xis,yis, label='y conocida')
plt.plot(xi[0],yiRK2[0],
         'o',color='r', label ='[x0,y0]')
plt.plot(xi[1:],yiRK2[1:],
         'o',color='m',
         label ='y Runge-Kutta 2 Orden')

plt.title('EDO: Solución con Runge-Kutta 2do Orden')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()