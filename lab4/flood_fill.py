from collections import deque

def read_file(filename = "input.txt") -> tuple:
    input_matrix = []

    with open(filename, "r") as file:
        width, height = list(map(int, file.readline().split(",")))
        x, y = list(map(int, file.readline().split(",")))
        color = file.readline().replace("\n", "")
        for _ in range(height):
            input_matrix.append(file.readline().replace("\n", "").split(" "))

    return input_matrix, width, height, x, y, color

def write_file(matrix, filename = "output.txt") -> None:
    with open(filename, "w") as file:
        for i in matrix:
            file.write(" ".join(map(str, i)) + "\n")

def isValid(matrix, width, height, x, y, prev_color) -> bool:
    if 0 <= x < width and 0 <= y < height \
        and matrix[x][y] == prev_color:
            return True
    return False

def flood_fill(matrix, width, height, x, y, color) -> list:
    queue = deque()
    queue.append([x, y])

    visited = []

    prev_color = matrix[x][y]
    if prev_color == color:
        return matrix
    matrix[x][y] = color

    while queue:
        currSize = len(queue)
        while currSize > 0:
            currNode = queue.popleft()
            currSize -= 1

            currX = currNode[0]
            currY = currNode[1]

            matrix[currX][currY] = color

            if isValid(matrix, width, height, currX, currY - 1, prev_color): #Go up
                if [currX, currY - 1] not in visited:
                    queue.append([currX, currY - 1])
                    visited.append([currX, currY - 1])
            if isValid(matrix, width, height, currX + 1, currY, prev_color): #Go right
                if [currX + 1, currY] not in visited:
                    queue.append([currX + 1, currY])
                    visited.append([currX + 1, currY])
            if isValid(matrix, width, height, currX, currY + 1, prev_color): #Go down
                if [currX, currY + 1] not in visited:
                    queue.append([currX, currY + 1])
                    visited.append([currX, currY + 1])
            if isValid(matrix, width, height, currX - 1, currY, prev_color): #Go left
                if [currX - 1, currY] not in visited:
                    queue.append([currX - 1, currY])
                    visited.append([currX - 1, currY])

    write_file(matrix)

    return matrix

if __name__ == "__main__":
    output = flood_fill(*read_file())

    for i in output:
        print(i)