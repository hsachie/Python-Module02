class GardenError (Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError (GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError (GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def gardenerror_test() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print("Caught PlantError:", err)
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print("Caught WaterError:", err)

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as err:
        print("Caught GardenError: ", err)
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as err:
        print("Caught GardenError: ", err)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    gardenerror_test()
