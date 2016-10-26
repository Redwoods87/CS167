def windChill(temp, wind):
    """
    Preconditions: temp is positive integer or double equal or lesser than 10
    Postconditions: wind is a integer equal to or greater than 4.8, lower than or equal to temperature
    """
    
    chill = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * wind ** 0.16
    return round(chill)