# main.py

# Function to calculate the sum of two numbers
def sum(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of the two integers.
    """
    return a + b

# Example usage
if __name__ == "__main__":
    result = sum(3, 5)
    print(f"The sum of 3 and 5 is {result}")