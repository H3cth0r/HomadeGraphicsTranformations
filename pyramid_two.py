import transformations as tf
import math

x = 3.3
A = tf.Point((-1.812, -6.824 + (math.sqrt(3)/3)*x, 5.247))
B = tf.Point((-1.812 - (x/2), -6.824 - (math.sqrt(3)/6)*x, 5.247))
C = tf.Point((-1.812 + (x/2), -6.824 - (math.sqrt(3)/6)*x, 5.247))
D = tf.Point((-1.812, -6.824, 5.247 - math.sqrt(2/3)*x))
M = tf.Point((-1.812, -6.824, 5.247 - (math.sqrt(3)/6)*x))

A.debugModeOn = True
B.debugModeOn = True
C.debugModeOn = True
D.debugModeOn = True
D.debugModeOn = True
M.debugModeOn = True

print(A.coords)
print(B.coords)
print(C.coords)
print(D.coords)
print(M.coords)

res = [0, 0, 0]
for i in range(3):
	res[i] = A.coords[i] + B.coords[i] + C.coords[i] + D.coords[i]
for i in range(3):
	res[i] /= 4

centroid = tf.Point(tuple(res))
centroid.debugModeOn = True

print(f"CENTROID: {centroid.coords}")

pimid = tf.Objeto()
pimid.vertix.append(A)
pimid.vertix.append(B)
pimid.vertix.append(C)
pimid.vertix.append(D)

pimid.centroid = centroid

pimid.faces.append((2, 1, 0))
pimid.faces.append((2, 1, 3))
pimid.faces.append((2, 0, 3))
pimid.faces.append((0, 1, 3))


# Importing libraries for ploting result
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# function to plot the pyramid on the openGL-pygame screen
def draw_pyramid(vert, faces):
	glBegin(GL_TRIANGLES)   # We tell the program to draw triangles with vertices input
	
	clrs = [(0.2, 0.6, 0.3), (0.7, 0, 0.5), (1, 0.6, 0), (0.1, 0, 1)] # list of sides colors
	for i in range(len(faces)):
		glColor(*clrs[i])   # Select a color for the face
		for j in faces[i]:
			glVertex3f(*vert[j].coords) # add a vertex from the list of vertices of the pyramid obj
		
	glEnd()     # end drawing

# Method for printing the x, y, z axis 
def draw_axis_lines():
	glBegin(GL_LINES)
	
	# x axis red
	glColor3f(1.0,0.0,0.0)
	glVertex3f(-10.0, 0.0, 0.0)
	glVertex3f(10.0, 0.0, 0.0)

	# y axis green
	glColor3f(0.0,1.0,0.0)
	glVertex3f(0.0, -10.0, 0.0)
	glVertex3f(0.0, 10.0, 0.0)
	
	# z axis blue
	glColor3f(0.0,0.0,1.0)
	glVertex3f(0.0, 0.0, -10.0)
	glVertex3f(0.0, 0.0, 10.0)

	glEnd()

up_down_angle = 0.0 # variable to keep track of angle of visualization

# function to read user movements with keys
def read_user_movements():
	# Get keys
	keypress = pygame.key.get_pressed()
	#mouseMove = pygame.mouse.get_rel()
	
	# Up or down
	global up_down_angle
	if keypress[pygame.K_2]:
		up_down_angle = 0.1
		glRotatef(up_down_angle, 0.1, 0.0, 0.0)
	if keypress[pygame.K_1]:
		up_down_angle = 0.1
		glRotatef(up_down_angle, -0.1, 0.0, 0.0)
	
	# Movement ASDW
	if keypress[pygame.K_w]:
		glTranslatef(0,0,0.1)
	if keypress[pygame.K_s]:
		glTranslatef(0,0,-0.1)
	if keypress[pygame.K_d]:
		glTranslatef(-0.1,0,0)
	if keypress[pygame.K_a]:
		glTranslatef(0.1,0,0)
	
	# left or right
	
	if keypress[pygame.K_3]:
		glRotatef(0.11, 0.0, 1, 0.0)
	if keypress[pygame.K_4]:
		glRotatef(-0.11, 0.0, 1, 0.0)


pygame.init()       # init pygame screen
display = (800, 600) # create window with size
pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # display with opengl parameters
pygame.display.set_caption("3D Pyramid")    # screen title
gluPerspective(45, (display[0]/display[1]), 0.1, 50)    # visualization perspective
glTranslate(0, 0, 0-30)     # initial translate position for camera

forward = True
degs = 0

# loop for keeping drawign and listening for keys
while True:
    # if quiting
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	#glRotate(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Rotating the pyramid
	if forward == True:
		if degs == -15:
			forward = False
		else:
            # using custom function for rotating the points of a pivot
			pimid.rotateOnPivotY(pimid.centroid.coords, -1)
			degs -= 1
	#pimid.rotateOnPivotY(pimid.centroid.coords, 1)
	draw_pyramid(pimid.vertix, pimid.faces) # draw piramid with points changes
	draw_axis_lines()   # draw axis lines
	read_user_movements()  
	pygame.display.flip()
	pygame.time.wait(15)

