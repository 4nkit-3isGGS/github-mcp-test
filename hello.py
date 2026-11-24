def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to the GitHub MCP Server."


def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)


def find_even_numbers(numbers):
    """Return all even numbers from the given list."""
    return [number for number in numbers if number % 2 == 0]


def main():
    name = "Ankit"
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(greet(name))
    print(f"Numbers: {numbers}")
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Even numbers: {find_even_numbers(numbers)}")


if __name__ == "__main__":
    main()
