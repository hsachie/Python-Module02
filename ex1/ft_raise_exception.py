def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as err:
        print(f"Caught input_temperature error: {err}")

    print()
    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as err:
        print(f"Caught input_temperature error: {err}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
