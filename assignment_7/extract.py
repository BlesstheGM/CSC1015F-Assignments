# program to extract useful data from a raw data
# Blessing Hlongwane
# HLNBLE002
# 12 April 2023

def location(block):
    e = -(block[-1::-1].find("DNE") + 1) # find position of E
    comma = block.find(",")
    space = block[comma:].find(" ") + comma
    site_name = block[e-4:space:-1]
    return site_name.title()
    
def temperature(block):
    space = block.find(" ")
    under_score = block.find("_") # Find position of an underscore
    temperature = eval(block[space+1:under_score])
    return temperature
    
def x_coordinate(block):
    colon = block.find(":")
    comma = block.find(",")
    Xcoordinate = block[colon+1:comma]
    return Xcoordinate

def y_coordinate(block):
    comma = block.find(",")
    space = block[comma:].find(" ") + comma
    Ycoordinate = block[comma+1:space]
    return Ycoordinate

def pressure(block):
    under_score = block.find("_") 
    colon = block.find(":")
    pressure = float(block[under_score+1:colon])
    return pressure    
    
def get_block(data):
    b = data.find("BEGIN") # start the sentence on Begin
    e = -(data[-1::-1].find("DNE") + 1) # End the sentence on End
    our_sentence = data[b:e+1] 
    return our_sentence

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block).title())
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
