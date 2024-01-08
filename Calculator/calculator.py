# from typing import Optional
from math import fsum
from numpy import format_float_positional as ffp


class Calculator:
    def __init__(self, starting_value: float = 0, verbose: bool = False):
        """
        Initiates an instance of the Calculator class with the following variables:
        * result_in_memory - starting value of the calculator.
            Default set to 0.
        * operation_counter - number of operations made with the current
            run of the calculator. Default set to 0.
        * previous_value_in_memory - value of the result_in_memory before an
            operation. Default set to None.
        * verbose - boolean variable defining return type of operations from
            text to float values.

        Methods: 
        add(*args)
        subtract(*args)
        multiply(*args)
        divide(*args)
        floor_divide(*args)
        root(*args)
        """

        self.result_in_memory: float | int = starting_value
        self.operation_counter: int = 0
        self.__previous_value_in_memory: float | None = None
        self.__verbose: bool = verbose

    @staticmethod
    def check_input_types(*args: float | int):
        """Asserts that all input values are numbers (floats or integers)."""
        assert all(
            [isinstance(argument, float | int) for argument in [*args]]
        ), "All inputs have to be of type Numeric."

    @staticmethod
    def find_decimal_point(*args: float | int) -> int:
        """
        Finds the largest number of decimal points for inputs to
        determine the number of decimal points in the return.
        """

        if any([isinstance(argument, float) for argument in [*args]]):
            return max(
                [len(str(ffp(a)).split(".")[1]) for a in [*args] if not isinstance(a, int)]
            )
        else:
            return 0

    def store_memory(self) -> None:
        """Stores the previous value that was created by previous calculations."""
        self.__previous_value_in_memory = self.result_in_memory

    def count_operations(self, nr_of_operations: int = 1) -> None:
        self.operation_counter += nr_of_operations

    def change_return_type(self) -> None:
        """Changes the return type of instance methods to the opposite type."""
        self.__verbose = not self.__verbose

    def reset(self):
        """
        Resets the memory of operation results to 0 & the result of operations back to 0.
        """

        if self.__verbose:
            print(
                f"You've previously made {self.operation_counter} operations with the end result being {self.result_in_memory}."
            )    
        self.result_in_memory = 0
        self.operation_counter = 0
        self.__previous_value_in_memory = None
        if self.__verbose:
            print("Your Calculator has been reset. Now the Current Memory is 0.")

    def add(self, *args: float | int) -> float | str:
        """
        Returns the sum of all provided arguments added to the value in memory.
        """
        self.check_input_types(*args)
        self.store_memory()
        self.result_in_memory += fsum([*args])
        self.count_operations(len([*args]))
        decimal_point = self.find_decimal_point(*args)

        if self.__verbose:
            return f"""You have added {fsum([*args]):.{decimal_point}f} to {self.__previous_value_in_memory:.{decimal_point}f} to get: {self.result_in_memory:.{decimal_point}f}."""
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point
            else self.result_in_memory
        )

    def subtract(self, *args: float | int) -> float | str:
        """
        Returns the result of subtracting the sum of all provided arguments from the value in memory.
        """
        self.check_input_types(*args)
        self.store_memory()
        self.result_in_memory -= fsum([*args])
        self.count_operations(len([*args]))
        decimal_point = self.find_decimal_point(*args)
        if self.__verbose:
            return f"You have subtracted {fsum([*args]):.{decimal_point}f} from {self.__previous_value_in_memory:.{decimal_point}f} to get: {self.result_in_memory:.{decimal_point}f}."
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point
            else self.result_in_memory
        )

    def multiply(self, *args: float | int) -> float | str:
        """
        Returns the result of multiplying the value in memory with all provided arguments.
        """

        self.check_input_types(*args)
        self.store_memory()
        decimal_point = self.find_decimal_point(*args)

        for multiplier in [*args]:
            self.result_in_memory *= multiplier

        self.count_operations(len([*args]))
        if self.__verbose:
            return f"""You have timed {(self.result_in_memory / self.__previous_value_in_memory)
                                    if self.__previous_value_in_memory != 0
                                    and self.__previous_value_in_memory is not None
                                    else 0} with {self.__previous_value_in_memory:.{decimal_point}f} to get: {self.result_in_memory:.{decimal_point}f}"""
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point
            else self.result_in_memory
        )

    def divide(self, *args: float | int) -> float | str:
        """
        Returns the result of dividing the value in memory with all provided arguments. 
        """

        self.check_input_types(*args)
        decimal_point = self.find_decimal_point(*args)
        assert all([*args]), """In order to be able to dive the result in memory with a number,
                                that number must be non-zero."""

        self.store_memory()
        decimal_point = self.find_decimal_point(*args)

        for diviser in [*args]:
            self.result_in_memory /= diviser

        if self.__verbose:
            return f"""You have divided {self.__previous_value_in_memory:.{decimal_point}f} by {self.result_in_memory
                                                                            / self.__previous_value_in_memory
                                                                            if self.__previous_value_in_memory != 0
                                                                            and self.__previous_value_in_memory is not None
                                                                            else 0} to get: {self.result_in_memory:.{decimal_point}f}."""
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point != 0
            else self.result_in_memory
        )
    
    def floor_divide(self, *args: float | int) -> float | str:
        """
        Returns the result of floor dividing the value in memory with all provided arguments.
        """

        self.check_input_types(*args)
        decimal_point = self.find_decimal_point(*args)
        assert all([*args]), """In order to be able to dive the resultin memory with a number,
                                that number must be non-zero."""

        self.store_memory()
        decimal_point = self.find_decimal_point(*args)

        for diviser in [*args]:
            self.result_in_memory //= diviser

        if self.__verbose:
            return f"""You have floor divided {self.__previous_value_in_memory:.{decimal_point}f} by {self.result_in_memory
                                                                            / self.__previous_value_in_memory
                                                                            if self.__previous_value_in_memory != 0
                                                                            and self.__previous_value_in_memory is not None
                                                                            else 0} to get: {self.result_in_memory:.{decimal_point}f}."""
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point
            else self.result_in_memory
        )

    def root(self, *args: float | int) -> float | str:
        """
        Returns the result of taking the nth root of the value in memory with
        all provided arguments for n. n is equivalent to root_number.
        """

        self.check_input_types(*args)
        assert (self.result_in_memory > 0), "In order to be able to take a root of a number, it must be non-negative."
        assert all([*args]), "In order to be able to take a root of a number, the root number has to be non-zero."

        self.store_memory()
        decimal_point = self.find_decimal_point(*args)

        for root in [*args]:
            self.result_in_memory **= 1 / root

        if self.__verbose:
            return f"""You have taken {len([*args]):.{decimal_point}f} consecutive roots of {self.__previous_value_in_memory
                                 if self.__previous_value_in_memory is not None
                                 else 0} with the root numbers being {", ".join(map(str, [*args]))} to get: {self.result_in_memory:.{decimal_point}f}."""
        return (
            round(self.result_in_memory, decimal_point)
            if decimal_point
            else self.result_in_memory
        )


if __name__ == "__main__":
    calc = Calculator(700, True)
    calc.find_decimal_point(0.4444, 0.222, 0, 5.55555)
    calc.add(4.28, 2.25, 2, 2.61, -9.84)
    calc.subtract(4.28, 2.25, 2, 2.61, -9.84555)
    calc.divide(25, 10, 5)
    calc.operation_counter
    calc.result_in_memory
    calc.reset()
