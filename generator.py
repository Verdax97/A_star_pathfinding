import random
if __name__ == "__main__":
    width = int(input("how long can this go on?(width) "))
    height = int(input("how far can this go on?(height) "))
    p = float(input("probability of walls "))
    a = list()
    for y in range(0, int(height)):
        b = ""
        for x in range(0, int(width)):
            i = random.random()
            if i < p:
                b += "x"
            else:
                b += " "
        b += "\n"
        a.append(b)
        
    x,y = random.randrange(0, width - 1), random.randint(0, height - 1)
    while a[y][x] != " ":
        x,y = random.randrange(0, width - 1), random.randint(0, height - 1)
    a[y] = a[y][:x] + 's' + a[y][x:]
    x,y = random.randrange(0, width - 1), random.randint(0, height - 1)
    while a[y][x] != " ":
        x,y = random.randrange(0, width - 1), random.randint(0, height - 1)
    a[y] = a[y][:x] + 'f' + a[y][x:]
    text_file = open("inputs/" + input("file name ") + ".txt", "w")
    text_file.writelines(a)
    text_file.close()