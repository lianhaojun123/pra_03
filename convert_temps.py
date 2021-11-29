

def main():
    INPUT_FILE = 'temps_input.txt'
    OUTPUT_FILE = 'temps_output.txt'
    input_file = open(INPUT_FILE, 'r')
    output_file = open(OUTPUT_FILE, 'w')
    for line in input_file:
        number = convert_temps(float(line))
        print(format(number), file=output_file)
    input_file.close()
    output_file.close()


def convert_temps(number):
    return (number + 32) / 1.8


main()
