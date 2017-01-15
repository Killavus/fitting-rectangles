from rectangle import Rectangle 

def read_rectangles():
    try:
        rectangles = []
        while True:
            w, h = map(float, raw_input().split())
            rectangles.append(Rectangle(w, h))  
    except EOFError:
        return rectangles
