pos = "right"
dir = "left"
for avang in range(1, 20, 1):
    if pos == "right":
        print("right")
        pos = "center"
        dir = "left"
    elif pos == "center":
        print("center")
        pos = dir

    elif pos == "left":
        print("left")
        pos = "center"
        dir = "right"