import math

LENGTH_OF_COASTLINE_UNIT = 1   #Miles
LENGTH_OF_COASTLINE = 80   #Miles
WIDTH_OF_COASTLINE = 1 #Miles
HEIGHT = .2      #Miles.  We will get this from James/Ilana
FOCAL_LENGTH = 50   #mm.  We will get this from James/Ilana

def height_to_miles_per_mile():
    fov = height_to_fov()
    miles_per_mile = fov_to_miles_per_mile(fov)
    return miles_per_mile

def height_to_fov():
#    this will call the cam sim
#    for now we're just returning an arbitrary value, .2 miles diameter
    return 1

def fov_to_miles_per_mile(fov):
    l = LENGTH_OF_COASTLINE
    w = WIDTH_OF_COASTLINE
    f = fov

    total_coast_with_loops = (l-f) + (w-f) * math.ceil(l/f)
    return total_coast_with_loops/80

def range_of_plane():
    return 80 #estimate from multiple sources.  Needs verification

def miles_to_theta(miles):
    theta = miles/LENGTH_OF_COASTLINE * 360
    return theta

def theta_to_chord_length(theta):
    radius = LENGTH_OF_COASTLINE/(2* math.pi)
    theta = math.radians(theta)
    return radius * 2*(abs(math.sin(theta/2)))

def number_of_trips(bay_circumference):
    #Simulation that returns number of trips and total distance

    remaining_range = range_of_plane()
    plane_miles_per_coast_mile = height_to_miles_per_mile()
    position = 0  #degrees
    trips = 0

    step_size = .01  #miles of coastline

    while (position < 360):
        remaining_range = range_of_plane()
        remaining_range -= theta_to_chord_length(position)
        if (remaining_range < (.5 * range_of_plane())):
            raise NameError("it won't make it")
        while (remaining_range > theta_to_chord_length(position) and position < 360):
            remaining_range -= plane_miles_per_coast_mile * step_size #Update remaining range in miles
            position += miles_to_theta(step_size)                     #Update theta position
        trips += 1

    return(trips, trips * range_of_plane() - remaining_range)



print number_of_trips(80)