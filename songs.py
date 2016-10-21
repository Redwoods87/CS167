def songs(capacity, bitrate):
    """
    Returns the number of 4-minute songls someone can fit on his/her device, given the capacity in gigabytles and the bitrate in kbps.
    CURRENTLY BUGGY -- variable names screwed up
    
    """
        
    songLengthInMinutes = 4
    bitsPerGigabyte = 8 * (2**30)
    bitsPerKilobit = 2**10
    capacityInBits = songLengthInMinutes * bitrate * bitsPerKilobit
    numberOfSongs = capacityInBits // songLengthInBits
    return numberOfSongs

def main():
    capacity = float(input("What is the capacity of your device in gigabytes? : "))
    bitrate = float(input("What is the bitrate? : "))
    songs (capacity, bitrate)
    print = int(numberOfSongs)
    
main()