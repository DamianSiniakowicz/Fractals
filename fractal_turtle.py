import turtle, math, numpy, time

def draw_polygon(number_sides,side_length):
	damian = turtle.Turtle()
	damian.speed(9)
	damian.st()
	for i in range(number_sides):
		damian.forward(side_length)
		damian.right(360/number_sides)
	return None

def draw_spiral(sides,angle,start_length,length_increase):
	damian = turtle.Turtle() # draw_spiral(700,72,10,1) gives a beautiful hexagonal spiral
	damian.speed(0)
	damian.ht()
	red = 0.0
	blue = 1.0
	for i in range(sides):
		damian.forward(start_length + length_increase*i)
		damian.right(angle)
		blue -= 1.0/sides
		red += 1.0/sides 
		damian.color(red,0.0,blue)
	return None

def draw_koch_curve(length,depth):
	# draw_spiral(700,72,10,1) gives a beautiful hexagonal spiral
	damian.speed(5)
	damian.ht()
	length = float(length)
	if depth == 1:
		damian.forward(length)
	else:
		draw_koch_curve(length/4,depth-1)
	damian.right(60)
	if depth == 1:
		damian.forward(length)
	else:
		draw_koch_curve(length/4,depth-1)
	damian.left(120)
	if depth == 1:
		damian.forward(length)
	else:
		draw_koch_curve(length/4,depth-1)
	damian.right(60)
	if depth == 1:
		damian.forward(length)
	else:
		draw_koch_curve(length/4,depth-1)
	return None

def draw_snowflake(length,depth):
	damian.penup()
	damian.setpos(-200,-150)
	damian.pendown()
	damian.speed(9)
	damian.ht()
	draw_koch_curve(length,depth-1)
	damian.left(120)
	draw_koch_curve(length,depth-1)
	damian.left(120)
	draw_koch_curve(length,depth-1)
	damian.left(120)
	return None

def draw_tree(length,depth):
	damian.speed(9)
	damian.ht()
	damian.forward(length)
	if depth > 1:
		damian.left(45)
		draw_tree(length/2,depth-1)
		damian.left(90)
		draw_tree(length/2,depth-1)
		damian.right(135)
	damian.right(180)
	damian.forward(length)
	return None
 

def circle_circle(radius,number):
	damian.speed(9)
	damian.ht()
	x_pairs = [[radius*(point/float(number)), -radius*(point/float(number))] for point in range(1,number)]
	x_coordinates = [] 
	for x_pair in x_pairs: x_coordinates.extend(x_pair)
	center_pairs = [[(x_coord,math.sqrt(radius**2-x_coord**2)),(x_coord,-math.sqrt(radius**2-x_coord**2))] for x_coord in x_coordinates]
	center_tuples = [] 
	for center_pair in center_pairs: center_tuples.extend(center_pair)
	red = 0.0
	blue = 1.0
	for circle_center in center_tuples:
		red += 1.0 / (4*(number-1))
		blue -= 1.0 / (4*(number-1))
		damian.color(red,0.0,blue)
		damian.penup()
		damian.setpos(circle_center[0]+radius,circle_center[1])
		damian.pendown()
		damian.circle(radius)
		# draw circle with radius "radius"

def quad_circle(radius,depth):
	radius = float(radius)
	damian.speed(9)
	damian.ht()
	damian.circle(radius)
	if depth > 1: # x's are a radius too positive, y's are radius/2 too negative
		damian.penup()
		x,y = damian.position()
		damian.setpos(x-radius,y+radius/2)
		damian.pendown()		
		quad_circle(radius/2,depth-1)
		damian.penup()
		# works up here
		damian.setpos(x+radius,y+radius/2)
		damian.pendown()
		quad_circle(radius/2,depth-1)
		damian.penup()
		damian.setpos(x,y-radius/2)
		damian.pendown()
		quad_circle(radius/2,depth-1)
		damian.penup()
		damian.setpos(x,y+(3/2.0)*radius)
		damian.pendown()
		quad_circle(radius/2,depth-1)
		damian.penup()
		damian.setpos(x-radius,y+radius)
		damian.pendown()

def concentric(depth,radius):
	for i in range(depth):
		damian.circle((i+1)*radius)
		damian.right(90)
		damian.penup()
		damian.forward(radius)
		damian.right(270)
		damian.pendown()

def four_square(length,depth):
	damian.speed(9)
	damian.ht()
	damian.forward(length)
	damian.left(90)
	damian.forward(length)
	damian.left(90)
	damian.forward(length)
	damian.left(90)
	damian.forward(length)
	damian.left(90)
	damian.forward(length/2)
	damian.left(90)
	damian.forward(length)
	damian.left(90)
	damian.forward(length/2)
	damian.left(90)
	damian.forward(length/2)
	damian.left(90)
	damian.forward(length)
	damian.right(90)
	damian.forward(length/2)
	damian.right(90)
	damian.forward(length)
	damian.right(180)
	if depth > 1:
		x,y = damian.position()
		damian.penup()
		damian.setpos(x+length/2,y+length/2)
		damian.pendown()
		four_square(length/2,depth-1)
		damian.penup()
		damian.setpos(x,y)
		damian.pendown()
		four_square(length/2,depth-1)
		damian.penup()
		damian.setpos(x+length/2,y)
		damian.pendown()
		four_square(length/2,depth-1)
		damian.penup()
		damian.setpos(x,y+length/2)
		damian.pendown()
		four_square(length/2,depth-1)

def triforce(length, depth):
	damian.speed(9)
	damian.ht()
	damian.forward(length)
	damian.left(120)
	damian.forward(length)
	damian.left(120)
	damian.forward(length)
	damian.left(120)
	if depth > 1:
		x,y = damian.position()
		triforce(length/2,depth-1)
		damian.penup()
		damian.forward(length/2)
		damian.pendown()	
		triforce(length/2,depth-1)
		damian.penup()
		damian.left(180)
		damian.forward(length/2)
		damian.right(120)
		damian.forward(length/2)
		damian.right(60)
		damian.pendown()
		triforce(length/2,depth-1)
		damian.penup()
		damian.right(120)
		damian.forward(length/2)
		damian.left(120)
		damian.pendown()

def I_fractal(length,depth):
	damian.speed(9)
	damian.ht()
	damian.forward(length/2)
	damian.left(180)
	damian.forward(length)
	damian.left(180)
	damian.forward(length/2)
	if depth > 1:
		damian.forward(length/2)
		damian.left(90)
		I_fractal(length/2,depth-1)
		damian.left(90)
		damian.forward(length)
		damian.right(90)
		I_fractal(length/2,depth-1)
		damian.right(90)
		damian.forward(length/2)

def cantor_set(length,depth,spacing):
	print depth 
	length = float(length)
	damian.speed(9)
	damian.ht()
	damian.pendown()
	damian.forward(length)
	damian.penup()
	damian.right(180)
	damian.forward(length)
	damian.right(180)
	damian.pendown()
	if depth > 1:
		damian.left(90)
		damian.penup()
		damian.forward(spacing)
		damian.right(90)
		damian.pendown()
		cantor_set(length/3,depth-1,spacing)
		damian.penup()
		damian.forward(length*(2/3.0))
		damian.pendown()
		cantor_set(length/3,depth-1,spacing)
		damian.penup()
		damian.left(180)
		damian.forward(length*(2/3.0))
		damian.left(90)
		damian.forward(spacing)
		damian.left(90)
		damian.pendown()

def fern(branch_angle, num_branch, bend_angle, trunk_length, depth):
	# try : floor (length1/3)-(i/2) and 1
	# and : floor length2-i and 1
	# len1 : number branches 
	# ang1 : child to parent branch angle 
	# len2 : length between two recursive branches on a parent branch
	# ang2 : single branch bend angle
	flip = 1
	ratio = num_branch / float(num_branch + 1)
	trunk_sizes = [trunk_length * ratio**(float(segment)/8) for segment in range(num_branch)]
	for branch in range(num_branch):
		damian.left(bend_angle)
		#shrink_ratio = 1 - (branch+1)/(num_branch+1)
		damian.forward(trunk_sizes[branch]) # trunk length needs to decrease with each iteration

		if depth > 1:
			damian.left(flip*branch_angle)
			recursion_ratio = depth / float(depth + 1)
			loop_ratio = 1 - (float(branch + 1) / num_branch)
			new_trunk_length = trunk_length * recursion_ratio * loop_ratio
			fern(branch_angle,num_branch,bend_angle,new_trunk_length,depth-1) # trunk length needs to decrease with each recurse
			damian.right(flip*branch_angle)

		flip *= -1

	damian.right(180)
	for branch in range(num_branch-1,-1,-1): # need to reverse trunk length shrinkage
		damian.forward(trunk_sizes[branch])
		damian.right(bend_angle)

	damian.right(180)
	
def sierpinski_carpet(length,depth):
	damian.speed(9)
	damian.ht()
	damian.penup()
	damian.forward(length/3)
	damian.left(90)
	damian.forward(length/3)
	damian.pendown()
	damian.forward(length/3)
	damian.right(90)
	damian.forward(length/3)
	damian.right(90)
	damian.forward(length/3)
	damian.right(90)
	damian.forward(length/3)
	damian.penup()
	damian.forward(length/3)
	damian.left(90)
	damian.forward(length/3)
	damian.left(90)
	if depth > 1:
		sierpinski_carpet(length/3,depth-1)
		damian.forward(length/3)
		sierpinski_carpet(length/3,depth-1)
		damian.forward(length/3)
		sierpinski_carpet(length/3,depth-1)
		damian.left(90)
		damian.forward(length/3)
		damian.right(90)
		sierpinski_carpet(length/3,depth-1)
		damian.left(90)
		damian.forward(length/3)
		damian.right(90)
		sierpinski_carpet(length/3,depth-1)
		damian.right(180)
		damian.forward(length/3)
		damian.right(180)
		sierpinski_carpet(length/3,depth-1)
		damian.right(180)
		damian.forward(length/3)
		damian.right(180)
		sierpinski_carpet(length/3,depth-1)
		damian.right(90)
		damian.forward(length/3)
		damian.left(90)
		sierpinski_carpet(length/3,depth-1)
		damian.right(90)
		damian.forward(length/3)
		damian.left(90)


def christmas_tree(branch_angle,num_branch,length,depth):
	damian.speed(9)
	damian.ht()
	flip = 1
	if depth > 1:
		for branch in range(num_branch):
			damian.forward(length)
			damian.left(flip*branch_angle)
			christmas_tree(branch_angle, num_branch, length*(float(4)/5), depth-1)
			damian.right(flip*branch_angle)
			flip *= -1
		damian.forward(length/2.0)
		damian.right(180)
		damian.forward(length/2.0)
		for branch in range(num_branch):
			damian.forward(length)
		damian.right(180)
	else:
		damian.forward(2*length)
		damian.right(180)
		damian.forward(2*length)
		damian.right(180)

# pythag alphabet
cur_angle = 90.0
def pythag_L_tree(length,angle,depth,initial_pos):
	damian = turtle.Turtle()
	damian.speed(2)
	damian.st()
	current = "0" 
	pos_angle_stack = []
	global cur_angle
	cur_angle = 90.0
	x,y = initial_pos
	damian.penup()
	damian.setpos(x,y)
	damian.pendown()
	damian.left(90)
	def grow(current):
		new = ""
		for char in current:
			if char == "0":
				new += "1[0]0"
			elif char == "1":
				new += "11"
			else:
				new += char
		return new
	def draw(current): # would be better if you passed arg so forward dist was modified according to depth
		for char in current:
			if char == "0":
				damian.forward(length/4.0) # should be modified according to depth
			elif char == "1":
				damian.forward(length/(4.0)) # should be modified according to depth
			elif char == "[":
				pos_angle_stack.append((cur_angle,damian.pos()))
				if cur_angle + angle > 360.0:
					global cur_angle
					cur_angle = (cur_angle + angle) - 360.0
					damian.left(angle)
				else:
					global cur_angle
					cur_angle = cur_angle + angle
					damian.left(angle) 
			else:
				old_angle,old_pos = pos_angle_stack.pop(-1)
				damian.penup()
				damian.setpos(old_pos[0],old_pos[1])
				damian.pendown()
				# find val of angle we want to get to
				if old_angle - angle > 0.0:
					new_angle = old_angle - angle
				else:
					new_angle = 360.0 + (old_angle - angle)
				if cur_angle > new_angle:
					damian.right(cur_angle - new_angle)
					global cur_angle
					cur_angle = new_angle
				else:
					damian.left(new_angle - cur_angle)
					global cur_angle
					cur_angle = new_angle
	for gen in range(depth):
		current = grow(current)
	draw(current)

def koch_L_curve(length,depth):
	axiom = "F"
	def grow(current):
		new = ""
		for char in current:
			if char == "F":
				new += "FVF^FVF"
			else:
				new += char
		return new
	def draw(axiom,length,depth):
		length = length * (1/3.0)**depth
		for char in axiom:
			if char == "F":
				damian.forward(length)
			elif char == "V":
				damian.left(60)
			else:
				damian.right(120)
	for iter in range(depth):
		axiom = grow(axiom)
	draw(axiom,length,depth)


def dragon_L_curve(length,depth):
	damian.speed(9)
	damian.ht()
	damian.left(45)
	axiom = "FX"
	def grow(current):
		new = ""
		for char in current:
			if char == "X":
				new += "X+YF+"
			elif char == "Y":
				new += "-FX-Y"
			else:
				new += char
		return new
	def draw(length,axiom):
		for char in axiom:
			if char == "+":
				damian.right(90)
			elif char == "-":
				damian.left(90)
			elif char == "F":
				damian.forward(length)
			else:
				pass
	for iter in range(depth):		 
		axiom = grow(axiom)
	draw(length,axiom)

def hilbert_curve(length,depth):
	axiom = "A"
	def grow(old):
		new = ""
		for char in old:
			pass

def pyramid(length,depth):
	for side in range(depth,0,-1):
		this_side = length * (side/float(depth))
		damian.forward(this_side)
		damian.left(120)

def tri_spi(length,angle,depth):
	for side in range(depth,0,-1):
		this_side = length * (side/float(depth))
		damian.forward(this_side)
		damian.left(120-angle)

'''				
L-System
~ Alphabet : the symbols that encode stuff ex. "ABCD"
~ Axiom : the initial state of the system ex. "ADD"
~ Rules : a mapping from letters in the alphabet to sentences. ex. A -> ADD, B -> C, C -> D, D -> DD 
'''
'''
IFS
'''
'''
Chaos Game
'''



# python click package command line interface for drawing fractals
# def improved christmas tree / pine / manorah  
# peano_curve(): and other space filling curves ugh
# def stoch_fract():
# def arb_ang_tree_dif_thick():
# def stock_fractal():
# def sarpinski_carpet():
# general pattern : 
# 1.) do something
# 2.) get back to where you started
# 3.) do the same thing on a smaller scale at some positions defined relative to the starting position
# 3-D Fractals with PyCairo and OpenGL and then get VR in the picture

if __name__ == "__main__":
	'''
	draw_polygon(5,200)
	turtle.clearscreen()
	draw_spiral(300,72,15,1)
	turtle.clearscreen()

	damian = turtle.Turtle()
	draw_koch_curve(100,1)
	turtle.clearscreen()
	damian=turtle.Turtle()
	draw_koch_curve(100,2)
	turtle.clearscreen()
	damian=turtle.Turtle()
	draw_koch_curve(200,3)
	turtle.clearscreen()
	damian=turtle.Turtle()
	draw_snowflake(400,4)
	damian = turtle.Turtle()
	damian.right(90)
	damian.penup()
	damian.setpos(0,200)
	damian.pendown()
	draw_tree(300,6)
	damian = turtle.Turtle()
	circle_circle(120,16)
	damian=turtle.Turtle()
	concentric(5,25)
	damian=turtle.Turtle()
	damian.penup()
	damian.setpos(-100,-200)
	damian.pendown()
	quad_circle(200,5)
	damian=turtle.Turtle()
	four_square(256,4)
	damian = turtle.Turtle()
	damian.penup()
	damian.setpos(-200,-200)
	damian.pendown()
	time.sleep(5)
	triforce(640,5)
	damian = turtle.Turtle()
	time.sleep(5)
	I_fractal(896,7)
	damian=turtle.Turtle()
	time.sleep(5)
	damian.penup()
	damian.setpos(-400,-200)
	damian.pendown()
	cantor_set(976,7,15)
	damian=turtle.Turtle()
	damian.penup()
	damian.setpos(-100,-300)
	damian.pendown()
	damian.left(90)
	time.sleep(5)
	fern(50,4,10,150,4)
	damian=turtle.Turtle()
	damian.penup()
	damian.setpos(-400,-325)
	time.sleep(5)
	sierpinski_carpet(729,4)
	damian=turtle.Turtle()
	damian.penup()
	damian.setpos(-100,-250)
	damian.pendown()
	damian.left(90)
	christmas_tree(35,9,40,3)
	damian = turtle.Turtle()
	pythag_L_tree(105,65,5,(-100,-300))
	damian = turtle.Turtle()
	damian.penup()
	damian.setpos(-300,-250)
	damian.pendown()
	koch_L_curve(900,4)
	damian = turtle.Turtle()
	damian.penup()
	damian.setpos(-300,0)
	damian.pendown()
	dragon_L_curve(10,10)
	damian = turtle.Turtle()
	damian.speed(9)
	pyramid(350,100)
	damian = turtle.Turtle()
	damian.speed(9)
	damian.penup()
	damian.setpos(-200,-200)
	damian.pendown()
	tri_spi(600,.75,400)
	'''
	damian.bye()	
