def main():
    cars = ['Toyota', 'Lambo', 'Ferrari', 'Kia', 'Bentley']
    print(cars)
    print(cars[1])
    cars.append('Honda')
    print(cars)
    print(len(cars))
    cars.pop(1)
    cars.insert(1, 'Lambo')
    print(cars)

    for i in cars:
        print(i)
    points = [[2, 4], [2, 3], [5, 5]]
    print(points)



if __name__ == "__main__":
            main ()