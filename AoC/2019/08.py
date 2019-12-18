testinputa = "123456789012"
testinputb = "0222112222120000"


def print_layer(layer):
    for i in layer:
        for j in i:
            if j == "1":
                print("*", end = '')
            elif j == "2":
                print("2", end = '')
            else:
                print("_", end = '')
            
        print("")
    print("")


def deep_count(layer, counting):
    count = 0
    for i in layer:
        for j in i:
            if j == counting:
                count += 1
    return count


def a(inputs, w, h):
    layer_template = [["0"] * w] * h
    num_layers = (len(inputs) // (w * h))
    layers = []
    for _ in range(num_layers):
        new_layer = [x[:] for x in layer_template]
        layers.append(new_layer)
    
    #print(layers)
    for i in range(len(inputs)):
        layer = i // (w * h)
        x = i % (w)
        y = (i  % (w * h)) // w
        #print(inputs[i], i, layer, x, y)
        layers[layer][y][x] = inputs[i]

    min_zeroes = w*h
    min_zeroes_layer = layers[0]
    for layer in layers:
        zeroes = deep_count(layer, "0")
        if zeroes < min_zeroes:
            min_zeroes = zeroes
            min_zeroes_layer = layer
    
    #print_layer(min_zeroes_layer)

    return deep_count(min_zeroes_layer, "1") * deep_count(min_zeroes_layer, "2")


def add_layer(image, layer):
    #print_layer(layer)
    #print_layer(image)
    for i in range(len(layer)):
        for j in range(len(layer[i])):
            if layer[i][j] == "0":
                image[i][j] = "0"
            if layer[i][j] == "1":
                image[i][j] = "1"

def b(inputs, w, h):
    layer_template = [[0] * w] * h
    num_layers = (len(inputs) // (w * h))
    layers = []
    for _ in range(num_layers):
        new_layer = [x[:] for x in layer_template]
        layers.append(new_layer)
    
    #print(layers)
    for i in range(len(inputs)):
        layer = i // (w * h)
        x = i % (w)
        y = (i  % (w * h)) // w
        #print(inputs[i], i, layer, x, y)
        layers[layer][y][x] = inputs[i]
    
    image = layers[len(layers)-1]
    for layer in range(len(layers)-2, -1, -1):
        add_layer(image, layers[layer])

    return print_layer(image)



with open('inputs/08in.txt', 'r') as infile:
    inputs = infile.read()


#print(a(testinputa, 3, 2))
print(a(inputs, 25, 6))

#print(b(testinputb, 2, 2))
print(b(inputs, 25, 6))
