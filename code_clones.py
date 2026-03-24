import os

def read_file(file_path: str) -> str:
    """
    Read the contents of a file.

    :param file_path: The path to the file to read.
    :return: The contents of the file.
    """

    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a file.")

    with open(file_path, 'r') as file:
        return file.read()

def compute_jaccard_similarity(a: str, b: str) -> float:
    """
    Compute the Jaccard similarity between two programs.

    :param a: The first program to compare.
    :param b: The second program to compare.
    :return: The Jaccard similarity between the two programs.
    """

    a_content = read_file(a).splitlines()
    b_content = read_file(b).splitlines()

    # TODO: Implement the rest of this function
    # Jaccard similarity does not consider the order of statements

    a_unique = []
    for line in a_content:
        if line not in a_unique:
            a_unique.append(line)

    b_unique = []
    for line in b_content:
        if line not in b_unique:
            b_unique.append(line)

    intersection = 0
    for line in a_unique:
        if line in b_unique:
            intersection += 1

    union = len(a_unique) + len(b_unique) - intersection

    return 1 if union == 0 else intersection / union

def visualise_dot_plot(a: str, b: str) -> str:
    a_content = read_file(a).splitlines()
    b_content = read_file(b).splitlines()

    plot = '-' * 80 + '\n'
    for i in range(len(a_content)):
        plot += f'x{i}: {a_content[i]}\n'
    plot += '-' * 80 + '\n'
    for j in range(len(b_content)):
        plot += f'y{j}: {b_content[j]}\n'
    plot += '-' * 80 + '\n'

    # TODO: Implement the rest to return the dot plot for the two given programs (a: x-axis, b: y-axis)
    plot += '\t'
    for i in range(len(a_content)):
        plot += f'x{i}\t'

    plot += '\n'
    for j in range(len(b_content)):
        plot += f'y{j}'
        for i in range(len(a_content)):
            if b_content[j] == a_content[i]:
                plot += '\t*'
            else:
                plot += '\t '

        plot += '\t\n'
    # Below is a sample output:
    '''
    --------------------------------------------------------------------------------
    x0: def calculate_total(values: list):
    x1:     total = 0
    x2:     for value in values:
    x3:         if value < 0:
    x4:             continue
    x5:         total += value
    x6:     return total
    --------------------------------------------------------------------------------
    y0: def calculate_total(values: list):
    y1:     total = 0
    y2:     for value in values:
    y3:         if value < 0:
    y4:             print("Negative value!")
    y5:             continue
    y6:         total += value
    y7:     return total
    --------------------------------------------------------------------------------
        x0	x1	x2	x3	x4	x5	x6	
    y0	*	 	 	 	 	 	 	
    y1	 	*	 	 	 	 	 	
    y2	 	 	*	 	 	 	 	
    y3	 	 	 	*	 	 	 	
    y4	 	 	 	 	 	 	 	
    y5	 	 	 	 	*	 	 	
    y6	 	 	 	 	 	*	 	
    y7	 	 	 	 	 	 	*	
    --------------------------------------------------------------------------------
    '''

    # plot += '\t'
    plot += '-' * 80

    return plot.strip()