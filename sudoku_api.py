import requests

def fetch_sudoku():
    url = "https://sudoku-api.vercel.app/api/dosuku"
    
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    if response.status_code != 200:
        print("Error: Failed to fetch Sudoku puzzle")
        return None, None

    try:
        data = response.json()
        puzzle = data["newboard"]["grids"][0]["value"]
        solution = data["newboard"]["grids"][0]["solution"]
        return puzzle, solution
    except requests.exceptions.JSONDecodeError as e:
        print("Error: JSONDecodeError:", e)
        return None, None

def display_grid(grid):
    for row in grid:
        print(' '.join(str(num) if num != 0 else '-' for num in row))

def main():
    puzzle, solution = fetch_sudoku()
    if puzzle and solution:
        print("\n Sudoku Puzzle:")
        display_grid(puzzle)
        print("\n Solution:")
        display_grid(solution)

if __name__ == '__main__':
    main()
