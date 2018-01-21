sample1='''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1'''

def display(width, height, points):
    for i in range(height):
        row = ''
        for j in range(width):
            if (i,j) in points:
                row = row + '#'
            else:
                row = row + '.'
        print row
    print ""
    return

def rectangle(width, height, points):
    for i in range(height):
        for j in range(width):
            if (i,j) not in points:
                points.append((i,j))
    return

def rotate_column(column, rotations, points, height):
    newpoints = list(points)
    for point in points:
        if (point[1] == column):
            newpoints.remove(point)
            newrow = (point[0]+rotations) % height
            #print "from", point, "to", (newrow,point[1])
            newpoints.append((newrow,point[1]))
    return newpoints

def rotate_row(row, rotations, points, width):
    newpoints = list(points)
    for point in points:
        if (point[0] == row):
            newpoints.remove(point)
            newcolumn = (point[1]+rotations) % width
            newpoints.append((point[0],newcolumn))
    return newpoints

def sample():
    width = 7
    height = 3
    points = [(1,1),(0,0)]
    display(width,height,points) 
    rectangle(3,2,points)
    display(width,height,points)
    points = rotate_column(1, 1, points, height)
    display(width,height,points)
    points = rotate_row(0, 4, points, width)
    display(width,height,points)
    points = rotate_column(1, 1, points, height)
    display(width,height,points)
    return len(points)

def solve1(intext):
    width = 50
    height = 6
    points = []
    display(width,height,points) 
    for line in intext:
        print line
        line = line.split()
        if line[0] == "rect":
            dimensions = line[1].split('x')
            rectangle((int)(dimensions[0]),(int)(dimensions[1]), points)
        elif line[1] == "column":
            rotations = (int)(line[4])
            column = (int)(line[2].split('=')[1])
            points = rotate_column(column, rotations, points, height)
        elif line[1] == "row":
            rotations = (int)(line[4])
            row = (int)(line[2].split('=')[1])
            #print row, rotations
            points = rotate_row(row, rotations, points, width)
        #print points    
        display(width,height,points) 
    return len(points)


with open('inputs/08in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
#print sample()
print solve1(tests)
