def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
		int("abc")

	elif operation_number == 1:
		operation_number / 0

	elif operation_number == 2:
		open("/non/existent/file")

	elif operation_number == 3:
		"abc" + 123
	else:
		print("Operation completed successfully")

def test_error_types() -> None:
	print("=== Garden Error Types Demo ===")

	print("Testing operation 0...")
	try:
		garden_operations(0)
	except ValueError as err:
		print("Caught ValueError: ", err)

	print("Testing operation 1...")
	try:
		garden_operations(1)
	except ZeroDivisionError as err:
		print("Caught ZeroDivisionError: ", err)

	print("Testing operation 2...")
	try:
		garden_operations(2)
	except FileNotFoundError as err:
		print("Caught FileNotFoundError: ", err)

	print("Testing operation 3...")
	try:
		garden_operations(3)
	except TypeError as err:
		print("Caught TypeError: ", err)

	print("Testing operation 4...")
	garden_operations(4)

	print("Testing multiple errors...")
	try:
		garden_operations(0)
	except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as err:
		print("Caught an error:", err)

	print("All error types tested successfully!")

if __name__ == "__main__":
	test_error_types()
