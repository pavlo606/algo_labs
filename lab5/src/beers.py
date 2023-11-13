def read_file_and_parse(path: str = "src/input.txt") -> tuple[int, int, list[str]]:
    """Read data from file and parse it for beers problem"""
    with open(path, "r") as file:
        n, b = file.readline().split(" ")
        n = int(n)
        b = int(b)
        beers = file.readline().split(" ")

        return n, b, beers

def write_file(string: str, path: str = "src/output.txt", mode: str = "w") -> None:
    """Write data to file"""
    with open(path, mode) as file:
        file.write(string)

def min_beer_types(N: int, B: int, preferences: list[str], debug: bool = False) -> int:
    """Finds minimum number of beer sorts that we need to buy, while all employees are satisfied
    
    Arguments:
        * N (int) -- number of employee;
        * B (int) -- number of beer sorts;
        * preferences (list[str]) -- preferences of each employee like ["YNY", "NYY"]
        * debug (bool) -- If true then fucntion will print in-between results (default False)
    
    Returns:
        One number: minimum number of beer sorts that we need to buy
    """
    beer_count = []     # Here are preferences of employees but more comfortable
    beer_sorts = []     # Here are types of beer that we need to buy

#   Converting preferences like: preferences=["YNY", "NYY"] -> beer_count=[[0, 2],[1, 2]]
    for i in range(N):
        tmp_employee = []
        for j in range(B):
            if preferences[i][j] == "Y":
                tmp_employee.append(j)

#       If employee like only one sort of beer then we definitely have to buy this sort of beer
        if len(tmp_employee) == 1:
            if tmp_employee[0] not in beer_sorts:
                beer_sorts.append(tmp_employee[0])
        elif tmp_employee not in beer_count:
            beer_count.append(tmp_employee)

    if debug:
        print(f"primary beer_count:{beer_count}")
        print(f"primary beer_sorts:{beer_sorts}")

    while beer_count:
#       Deleting all employees that love any beer that we already heve to buy
        for i in beer_count.copy():
            for beer in beer_sorts:
                if beer in i:
                    beer_count.remove(i)
                    break

        if debug:
            print(f"\nbeer_count:{beer_count}")
            print(f"beer_sorts:{beer_sorts}")

#       If there are employees who doesn't like any of beer that we already heve to buy
#       Then we choose one sort that is most repeated
        if beer_count:
            joined_beers = []
            for i in beer_count:
                joined_beers += i
            new_beer_sort = max(set(joined_beers), key=joined_beers.count)
            beer_sorts.append(new_beer_sort)
            if debug:
                print(f"new beer sort:{new_beer_sort}")

    return len(beer_sorts)

if __name__ == "__main__":
    result = min_beer_types(*read_file_and_parse(), True)
    write_file(result)
    print(f"\nresult = {result}")