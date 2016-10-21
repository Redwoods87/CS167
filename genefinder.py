"""
Author username(s): watsonjr ; johnsoam
Date: 10/20/16
Assignment/problem number: Homework 10
Assignment/problem title: Genomics
"""

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
	"""Draw a colored bar over codon starting at position index in reading frame rf.  Put the turtle's tail up and down to handle line breaks properly."""
	   
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
	"""Plot GC frequency over a sliding window.

	Parameters:
		dna: a dna sequence as a string
		window: size of reading window, an integer
		tortoise: a turtle named tortoise

	Returns: None
	"""
	
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

	windowStart = dna[0:window+1]
	windowCount = 0	
	for char in windowStart:
		if char == "C" or char == "G":
			windowCount += 1
	fraction = windowCount/window
	plot (tortoise, window, fraction, window)

	for i in range(len(dna)-window):
		if dna[i] == "C" or dna[i] == "G":
			windowCount -= 1
		if dna[i+window] == "C" or dna[i+window] == "G":
			windowCount += 1
		fraction = windowCount/window
		plot (tortoise, window+i, fraction, window)
			
		
	# get initial window count
	
	# get subsequent window counts and plot them
	# to plot a fraction for the window ending at position index,
	# call plot(tortoise, index, fraction, window)
		
def orf1(dna, rf, tortoise):
	"""Displays open reading frames (ORF's) by calling the bar function to draw blue bars for ORF's and red bars for non-ORF's.
	
	Parameters:
		dna: a dna sequence as a string
		rf: the starting nucleotide of the first ORF (an integer between 0 and 2)
		tortoise: a turtle named tortoise

	Returns: None

	"""    

	# YOUR CODE GOES HERE	

	inORF = False	
	for index in range(rf, len(dna)-1, 3):
		codon = dna[index:index+3]	
		if codon == 'ATG':
			inORF = True
		elif codon == 'TAT' or codon == 'TGA' or codon == 'TAG':
			inORF = False
		
		if inORF == True:
			tortoise.pencolor('blue')
			bar(tortoise, index, rf)
		elif inORF == False:
			tortoise.pencolor('red')
			bar(tortoise, index, rf)    

	
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
	
	inputFile = open('eco536-1k.txt', 'r')	# change text file for different DNA sequences
	dna = inputFile.read()
	viewer(dna)

main()
