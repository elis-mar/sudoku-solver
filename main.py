import sudoku_api
import sudoku_solver

NUMBERS = [number for number in range(1, 10)]

def main():
    puzzle, solution = sudoku_api.fetch_sudoku()
    if puzzle != None:
        sudoku_solver.solve(puzzle, NUMBERS)
    
    if puzzle == solution:
        print('Sudoku puzzle solved successfully')
        print('you da man, man')
    else:
        print('you not da man')

if __name__ == '__main__':
    main()
