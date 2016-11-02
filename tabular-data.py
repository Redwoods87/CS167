# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/tabular-data.py

# Run with ipython for access to matplotlib
import matplotlib.pyplot as pyplot
import urllib.request as web

def plotQuakes():
    """Plot the locations of all earthquakes in the past month.
    Parameters: None.
    Produces: Nothing. Called for its side effects.
    Provenance: Havill (2016), _Discovering Computer Science, P. 387-8.
    """

    url = \
     "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
    quakeFile = web.urlopen(url)
    header = quakeFile.readline() # Discard first line of the file

    longitudes = []
    latitudes = []
    depths = []
    magnitudes = []

    for line in quakeFile:
        line = line.decode('utf-8')
        row = line.split(',')
        latitudes.append(float(row[1]))
        longitudes.append(float(row[2]))
        depths.append(float(row[3]))
        magnitudes.append(row[4]) #THIS NEEDS TO CONVERT TO FLOAT, BUT IT'S NOT WORKING!
    quakeFile.close()

    colors = []
    for depth in depths:
        if depth < 10:
            colors.append('yellow')
        elif depth < 50:
            colors.append('red')
        else:
            colors.append('blue')
            
    sizes = []
    for mag in magnitudes:
        if mag < 3:
            sizes.append(10)
        elif mag < 6:
            sizes.append(20)
        else:
            sizes.append(30)
            
            
            

    pyplot.scatter(longitudes, latitudes, sizes, color=colors)
    pyplot.show()

if __name__=='__main__':
    plotQuakes()
