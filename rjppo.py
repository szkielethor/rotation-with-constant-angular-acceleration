# -*- coding: cp1250 -*-
from visual import *

#custom window:
window = display(title = "Ruch jednostajnie przyspieszony po okregu",
               width = 720, height = 700, background = color.black)
dt = 0.001
rad_scale_factor = 7


r_val = 25 # circle radius
v_val = 10
a_val = v_val**2 / r_val
omega_val = v_val/r_val

r_vect = vector(r_val, 0, 0)
v_vect = vector(0, v_val, 0)
a_vect = vector(-a_val, 0 ,0) #uwzgledniam zwrot przeciwny do r
omega_vect = vector(0,0,omega_val)

body = sphere(pos = (r_val,0,0), radius = 0.2, color = color.yellow,
	make_trail = True, interval = 10)
r_vect_arrow = arrow(pos = (0,0,0), axis = body.pos, color = color.cyan,
	shaftwidth = 0.1)
a_vect_arrow = arrow(pos = body.pos, axis = -body.pos, length = mag(a_vect), 
 	shaftwidth = 0.25, color = color.red)
v_vect_arrow = arrow(pos = body.pos, axis = (0,1,0), length = v_val,
 	shaftwidth = 0.25, color = color.blue)
omega_vect_arrow = arrow(pos = (0,0,0), axis = (0,0,1), 
 	lenght = omega_val*rad_scale_factor, color = color.blue)
while True:
	rate(2500)
	body.pos = body.pos + v_vect*dt #przesuwam
	v_vect = v_vect + a_vect*dt #skrecam prędkość
	a_vect_direction = norm(vector(0,0,0)-body.pos)
	a_vect = a_val * a_vect_direction
	r_vect_arrow.axis = body.pos
	#aktualizacja strzałki przyśpieszenia
	a_vect_arrow.axis = -body.pos
	a_vect_arrow.length = mag(a_vect)
	a_vect_arrow.pos = body.pos
	#aktualizacja strzałki szybkości
	v_vect_arrow.pos = body.pos
	v_vect_arrow.axis = v_vect



# r_vect = (r,0,0)  # x axis direction
# v_vect = (0,v,0)
# a_vect = (-a,0,0) # direction oposite to x axis

# body = sphere(pos = (r_x_value,0,0), radius = 0.15, color = color.yellow,
# 	make_trail = True, interval = 10, retain = 75)
# r = arrow(pos = (0,0,0), axis = body.pos, color = color.cyan,
# 	shaftwidth = 0.1)
# a = arrow(pos = body.pos, axis = -body.pos, length = a_value, 
# 	shaftwidth = 0.25, color = color.red)
# v = arrow(pos = body.pos, axis = (0,1,0), length = v_y_value,
# 	shaftwidth = 0.25, color = color.blue)


# ball0 = sphere(pos = (0,0,0), radius = 0.3)
# ball1 = sphere(pos = (1,0,0), radius = 0.3, color = color.red)
# ball2 = sphere(pos = (0,1,0), radius = 0.3, color = color.green)
# ball3 = sphere(pos = (0,0,1), radius = 0.3, color = color.blue)

