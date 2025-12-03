def find_total_area(**areas):
    print("Rooms in the property:")
    for room in areas.keys():
        print(room)
    
    return f"The total square meter of the property is {sum(areas.values())} meters squared"

find_total_area(
                    Bathroom = 10,
                    Bedroom = 20,
                    Living = 20,
                    Kitchen = 15
                )