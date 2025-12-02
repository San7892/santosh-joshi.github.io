class Calculator:
    
    def __init__(self, a: float, b: float, operation: str):
        
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Convert to lowercase for case-insensitive matching

    def _add(self) -> float:
        """Performs addition: a + b"""
        return self.a + self.b

    def _subtract(self) -> float:
        """Performs subtraction: a - b"""
        return self.a - self.b

    def _multiply(self) -> float:
        """Performs multiplication: a * b"""
        return self.a * self.b

    def _divide(self) -> float | str:
        """Performs division: a / b. Handles division by zero."""
        if self.b == 0:
            return "Error: Cannot divide by zero."
        return self.a / self.b

    def perform_operation(self):
        """
        Executes the specified operation and returns the result.
        """
        match self.operation:
            case 'addition':
                return self._add()
            case 'subtraction':
                return self._subtract()
            case 'multiplication':
                return self._multiply()
            case 'division':
                return self._divide()
            case _:
                return f"Error: Invalid operation type '{self.operation}'. Please use 'addition', 'subtraction', 'multiplication', or 'division'."

