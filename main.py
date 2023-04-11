from cars import get_cars, write_cars

if __name__ == "__main__":
    DROM_URL = "https://auto.drom.ru"
    cars = get_cars(DROM_URL)
    with open("cars.txt", "wt") as cars_file:
        write_cars(cars, cars_file)