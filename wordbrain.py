#!/usr/bin/env python3
#Wordbrain search solver using word lists in the English language

import argparse

def make_letter_files(filename):
    letters = []

    with open(filename, "r") as words:
        for i in range(3000):
            try:
                word = words.readline()
                print(word)
                with open("Letters/{}.txt".format(word[0].lower()), 'a+') as letter_file:
                    letter_file.write("{}".format(word))

            except Exception:
                print(Exception)
                continue

    for letter_file in letters:
        letters_file.close()

def get_grid(num_rows, num_cols, letter_string):
    grid = [['' for j in range(num_cols)] for i in range(num_rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = letter_string[count]
            count += 1
    return grid

def get_boolean_grid(num_rows, num_cols):
    visited = [[True for j in range(num_cols)] for i in range(num_rows)]
    return visited

def is_valid(row, col):
    return (row > -1) and (row < rows) and (col > -1) and (col < cols) and visited[row][col]

def search(fd, length, word, curr_row, curr_col):
    global word_list
    if length == 1:
        word_list = set([word.strip() for word in list(open(word[0] + ".txt"))])
    if length > max_length:
        visited[curr_row][curr_col] = True
        return
    if length in word_sizes:
        if not (word in words):
            if word in word_list:
                print(word)
                fd.write("{}\n".format(word))
                words.append(word)
    for move in moves:
        row = curr_row + move[0]
        col = curr_col + move[1]
        if is_valid(row, col):
            visited[curr_row][curr_col] = False
            search(fd, length + 1, word + grid[row][col], row, col)
            visited[curr_row][curr_col] = True

def print_grid(matrix):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print() 

def setup(sizes, letter_string, num_rows, num_cols):
    global grid
    global visited
    global rows
    global cols
    global words
    global word_sizes
    global moves
    global max_length

    words = []
    moves = [(0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0)]
    word_sizes = sizes
    rows = num_rows
    cols = num_cols
    grid = get_grid(rows, cols, letter_string)
    visited = get_boolean_grid(rows, cols)
    max_length = max(word_sizes)

    sol_file = "words_found.txt"
    sols = open(sol_file, 'w+')
     
    print_grid(grid)

    for i in range(rows):
        for j in range(cols):
            print("\nPos: {} {}\n".format(i, j))
            search(sols, 1, grid[i][j], i, j)

    sols.close()

    words.sort()
    words.sort(key=len) 

    print()
    print("Words found: ")
    print()

    for word in words:
        print(str(len(word)) + ": " + word)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wordbrain Solver')
    parser.add_argument('-f', metavar='Word List', type=str, nargs='+', help='The word list file')
    parser.add_argument('-p', metavar='Puzzle File', type=str, nargs='+', help='The puzzle file')

    args = parser.parse_args()

    letter_string = ""
    num_rows = 0
    num_cols = 0
    sizes = []

    try:
        word_list = args.f[0]
        print(word_list)
        make_files(word_list)
    except:
        print("No word list. Assuming existence of letter files.")

    try:
        puzzle_file = args.p[0]
        puzzle_file = open(puzzle_file, 'r')
        file_data = puzzle_file.readlines()
        num_rows, num_cols = [int(i) for i in file_data[0].rstrip().split()]

        for i in range(1, num_rows + 1):
            letter_string += file_data[i].rstrip()

        sizes = [int(i) for i in file_data[num_rows + 1].rstrip().split()]
    except Exception as e:
        print("Could not open puzzle file...\n")
        print(e)
        exit(1)

    sizes = list(dict.fromkeys(sizes))

    sorted(sizes)
    setup(sizes, letter_string, num_rows, num_cols) 
