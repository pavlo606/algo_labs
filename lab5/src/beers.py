def read_file_and_parse(path: str = "src/input.txt") -> tuple[int, int, list[str]]:
    """Read data from file and parse it for beers problem"""
    with open(path, "r") as file:
        n, b = file.readline().split(" ")
        beers = file.readline().split(" ")

        return int(n), int(b), beers

def write_file(string: str, path: str = "src/output.txt", mode: str = "w") -> None:
    """Write data to file"""
    with open(path, mode) as file:
        file.write(str(string))

def min_beer_types(N: int, B: int, preferences: list[str], debug: bool = False) -> int:
    """
    Finds minimum number of beer sorts that we need to buy, while all employees are satisfied
    
    Arguments:
        * N (int) -- number of employee;
        * B (int) -- number of beer sorts;
        * preferences (list[str]) -- preferences of each employee like ["YNY", "NYY"]
        * debug (bool) -- If true then fucntion will print in-between results (default False)
    
    Returns:
        One number: minimum number of beer sorts that we need to buy
    """
    beers_graph = {}                 # Graph with employees preferences in format: { beer_sort: [emplyees] }
    beer_sorts = list(range(B))      # Beer sorts that we need to buy
    employees_preferences = [preference.count("Y") for preference in preferences]  # How much beer sorts each employee likes

#   Filling the beers_graph
    for beer in range(B):
        beers_graph[beer] = []
        for employee in range(N):
            if preferences[employee][beer] == "Y":
                beers_graph[beer] += [employee]

    if debug:
        print(f"beers_graph = {beers_graph}")
        print(f"start employees_preferences = {employees_preferences}")

    sorted_beers_graph = sorted(beers_graph.items(), key=lambda x: len(x[1]))  # Sorting graph by length of employees
#   Finding the beer sort in which everyone who likes it likes at least one more sort
    for beer, employees in sorted_beers_graph:
#       Checking if everyone who likes this beer likes one more, if not then we break the loop
        for employee in employees:
            if employees_preferences[employee] <= 1:
                break
        else:   # if previous loop wasn't breaked then we don't need to buy this sort
            beer_sorts.remove(beer)
            for employee in employees:
                employees_preferences[employee] -= 1

    if debug:
        print(f"final employees_preferences = {employees_preferences}")
        print(f"final beer_sorts = {beer_sorts}")

    return len(beer_sorts)

if __name__ == "__main__":
    result = min_beer_types(*read_file_and_parse(), debug=True)
    write_file(result)
    print(f"\nresult = {result}")