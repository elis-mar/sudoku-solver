import sudoku_api

def main():
    puzzle, solution = sudoku_api.fetch_sudoku()
    if puzzle and solution:
        print('Sudoku puzzle')
        sudoku_api.display_grid(puzzle)
        print('Sudoku puzzle solution')
        sudoku_api.display_grid(solution)

if __name__ == '__main__':
    main()
