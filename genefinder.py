# Skeleton code for Project 6.2
# Havill (2016), _Discovering Computer Science_

import turtle

width = 1440			# width of the window
cols = width // 6		# number of columns of text
height = 600			# height of the window
rows = height // 100	# number of rows of text

def plot(tortoise, index, value, window):
	"""Plot GC fraction value for window ending at position index."""
	
	if (index == window) or (index - window + 1) // cols != (index - window) // cols:
		tortoise.up()	
		tortoise.goto((index - window + 1) % cols, \
		              (index - window + 1) // cols + 0.7 + value * 0.25)
		tortoise.down()
	else:
		tortoise.goto((index - window + 1) % cols, \
		              (index - window + 1) // cols + 0.7 + value * 0.25)
		
def bar(tortoise, index, rf):
	"""Draw a colored bar over codon starting at position index in
	   reading frame rf.  Put the turtle's tail up and down to
	   handle line breaks properly."""
	   
	tortoise.up()
	tortoise.goto(index % cols, index // cols + (rf + 1) / 5)
	tortoise.down()
	tortoise.forward(1)
	tortoise.up()
	tortoise.goto((index + 1) % cols, (index + 1) // cols + (rf + 1) / 5)
	tortoise.down()
	tortoise.forward(1)
	tortoise.up()
	tortoise.goto((index + 2) % cols, (index + 2) // cols + (rf + 1) / 5)
	tortoise.down()
	tortoise.forward(1)

def gcFreq(dna, window, tortoise):
	"""Plot GC frequency over a sliding window."""
	
	# draw red lines at 0.5 above the sequence
	
	tortoise.pencolor('red')
	for index in range(len(dna) // cols + 1):
		tortoise.up()
		tortoise.goto(0, index + 0.825)
		tortoise.down()
		if index < len(dna) // cols:
			tortoise.goto(cols - 1, index + 0.825)
		else:
			tortoise.goto((len(dna) - window) % cols, index + 0.825)
	tortoise.up()
	tortoise.pencolor('blue')
	
	# YOUR CODE GOES HERE
	
	# get initial window count
	
	# get subsequent window counts and plot them
	# to plot a fraction for the window ending at position index,
	# call plot(tortoise, index, fraction, window)
		
def orf1(dna, rf, tortoise):
	inORF = False	
	for index in range(rf, len(dna)-1, 3):
		codon = dna[index:index+3]	
		if codon == "ATG":
			inORF = True
		elif codon == 'TAT' or codon == 'TGA' or codon == 'TAG':
			inORF = False
		
		if inORF == True:
			tortoise.pencolor('blue')
			bar(tortoise, index, rf)
		elif inORF == False:
			tortoise.pencolor('red')
			bar(tortoise, index, rf)    

	# YOUR CODE GOES HERE
	
	# to place a bar in the current color over the codon starting at 
	# position index in reading frame rf, call
	# bar(tortoise, index, rf)

def viewer(dna):
	"""Display GC content and ORFs in 3 forward reading frames."""
	
	dna = dna.upper()	   # make everything upper case

	tortoise = turtle.Turtle()
	screen = tortoise.getscreen()
	screen.setup(width, height)					# make a long, thin window
	screen.setworldcoordinates(0, 0, cols, rows) # scale coord system so 1 char fits at each point
	screen.tracer(100)
	tortoise.hideturtle()
	tortoise.speed(0)
	tortoise.up()
	
	# Draw DNA string in window.
	
	for index in range(len(dna)):
		tortoise.goto(index % cols, index // cols)
		tortoise.write(dna[index], font = ('Courier', 9, 'normal'))
		
	# Find ORFs in forward reading frames 0, 1, 2.
	
	tortoise.width(5)
	for index in range(3):
		orf1(dna, index, tortoise)
		
	# Plot GC frequency.
	
	tortoise.width(1)
	gcFreq(dna, 5, tortoise)

	screen.update()
	screen.exitonclick()
			
def main():
	# Read DNA from a file and find ORFs
	
	inputFile = open('Eco536-1K.txt', 'r')
	dna = inputFile.read()
	viewer(dna)

main()
