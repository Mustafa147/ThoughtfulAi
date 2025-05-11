def sort(width, height, length, mass)->str:
    if width <= 0 or height <= 0 or length <= 0 or mass < 0:
        raise ValueError("Invalid package dimensions or mass")
    volume = width*height*length
    bulky = volume >= 1000000 or max(width,height,length) >= 150
    heavy = mass >= 20

    if heavy and bulky:
        return "REJECTED"
    elif heavy or bulky:
        return "SPECIAL"
    else:
        return "STANDARD"

