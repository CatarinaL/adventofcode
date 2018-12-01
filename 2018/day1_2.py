def get_content(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content


def calculate_frequency(frequencies):
    #print(seen_freq)
    seen_freq = set()
    current_position = 0
    current_frequency = 0

    while(True):
        if current_frequency in seen_freq:
            return current_frequency
        else:
            seen_freq.add(current_frequency)
            current_frequency = current_frequency + frequencies[current_position]
            current_position = (current_position + 1) % len(frequencies)


if __name__ == '__main__':
    fname = 'day1_1_input.txt'
    values = get_content(fname)
    frequency = calculate_frequency(values)
    print(frequency)
