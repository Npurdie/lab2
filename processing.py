def to_bin(fractional):
    fraction = float('0.' + fractional)
    binary = ''
    while(fraction != 0.0):
        fraction = fraction * 2
        if (fraction < 1):
            binary = binary + '0'
        else:
            binary = binary + '1'
            fraction = fraction - 1
    return binary

def to_twos_comp(word, word_precision, fractional, fractional_precision):
    p = '0' + str(word_precision) + 'b'
    converted = bin(int(word) % (1 << word_precision))
    binary = format(int(converted, 2), p)

    while (len(fractional) < fractional_precision):
        fractional = fractional + '0'
    return binary + fractional

def calculatePrecision(values):
    word_precision = 1
    fractional_precision = 0
    for i in range(len(values)):
        word = len(bin(int(values[i][2]))) - 1  # precision of decimal
        fractional = len(to_bin(values[i][3]))  # precision of fraction
        if (word > word_precision): word_precision = word
        if (fractional > fractional_precision): fractional_precision = fractional
    return word_precision, fractional_precision

def calculateTwosComplements(values, word_precision, fractional_precision):
    output = []
    for i in range(len(values)):
        output.append(to_twos_comp(values[i][1] + values[i][2], word_precision, to_bin(values[i][3]), fractional_precision))
    return output

def writeOutput(output_values, filename):
    output = ''
    for i in range(len(output_values)):
        output = output + output_values[i] + '\n'
    writer = open(filename, 'w')
    writer.write(output)

def vectorize(values, string):
    for i in range(0, len(string)-1):
        value = string[i]
        vector = ['1', '', '0', '0']
        vector[0] = value
        if (value[0] == '-'):
            value = value.replace('-', '')
            vector[1] = '-'
        split = value.split('.')
        vector[2] = split[0]
        if (len(split) == 2):
            vector[3] = split[1]
        values.append(vector)

x_values = []
y_values = []

vectorize(x_values, open('lab2-x.txt', 'r').readlines()[0].split(' '))
vectorize(y_values, open('lab2-y.txt', 'r').readlines()[0].split(' '))

w_x, f_x = calculatePrecision(x_values)
w_y, f_y = calculatePrecision(y_values)

print('Word Precision x : ' + str(w_x))
print('Fractional Precision x: ' + str(f_x))
print('Word Precision y : ' + str(w_y))
print('Fractional Precision y : ' + str(f_y))

writeOutput(calculateTwosComplements(x_values, w_x, f_x), 'lab2-x-fixed-point.txt')
writeOutput(calculateTwosComplements(y_values, w_y, f_y), 'lab2-y-fixed-point.txt')
