from math import gcd
from typing import Union, Literal, Self, List


## TODO: chưa hỗ trợ biến đổi float sang Fraction
class Fraction:
    def __init__(
        self,
        numerator: Union[int, float, str] = 0,
        denominator: Union[int, float, Literal[1]] = 1,
    ) -> None:
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, str):
            try:
                temp: List[str] = numerator.split("/")
                match len(temp):
                    case 1:
                        self.numerator = int(temp[0])
                        self.denominator = denominator
                    case 2:
                        if temp[0] == "":
                            self.numerator = 0
                            self.denominator = int(temp[1])
                        elif temp[1] == "":
                            self.numerator = int(temp[0])
                            self.denominator = denominator
                        else:
                            self.numerator = int(temp[0])
                            self.denominator = int(temp[1])
                    case _:
                        raise ValueError
            except Exception as err:
                raise ValueError from err

    def zero_den(self) -> None:
        if self.denominator in [0, 0.0]:
            print("INVALID fraction")
            quit()

    def mixed(self) -> str:
        return (
            f"{self.numerator // self.denominator} {self.numerator % self.denominator}/{self.denominator}"
            if self.numerator % self.denominator != 0
            else f"{self.numerator//self.denominator}"
        )

    def to_float(self) -> float:
        return self.numerator / self.denominator

    def simplify(self) -> Self:
        temp: int = gcd(self.numerator, self.denominator)
        self.numerator //= temp
        self.denominator //= temp
        return self

    def __abs__(self) -> "Fraction":
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __add__(self, other) -> "Fraction":
        Fraction.zero_den(self)
        Fraction.zero_den(other)
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        ).simplify()

    def __sub__(self, other) -> "Fraction":
        Fraction.zero_den(self)
        Fraction.zero_den(other)
        return Fraction(
            self.numerator * other.denominator - self.denominator * other.numerator,
            self.denominator * other.denominator,
        ).simplify()

    def __mul__(self, other) -> "Fraction":
        Fraction.zero_den(self)
        Fraction.zero_den(other)
        return Fraction(
            self.numerator * other.numerator, self.denominator * other.denominator
        ).simplify()

    def __truediv__(self, other) -> "Fraction":
        Fraction.zero_den(self)
        Fraction.zero_den(other)
        return Fraction(
            self.numerator * other.denominator, self.denominator * other.numerator
        ).simplify()

    def __pow__(self, integer: int) -> "Fraction":
        Fraction.zero_den(self)
        return Fraction(
            self.numerator**integer,
            self.denominator**integer,
        ).simplify()
        # * ch pow được phân số vs phân số, chỉ pow đc với số nguyên
        ...

    def __radd__(self, other) -> "Fraction":
        return self.__add__(other)

    def __rsub__(self, other) -> "Fraction":
        return self.__sub__(other)

    def __rmul__(self, other) -> "Fraction":
        return self.__mul__(other)

    def __rtruediv__(self, other) -> "Fraction":
        return self.__truediv__(other)

    def __rpow__(self, other) -> "Fraction":
        return self.__pow__(other)

    def __str__(self) -> str:
        if self.numerator % self.denominator == 0:
            return f"{self.numerator//self.denominator}"
        return (
            f"{self.numerator}/{self.denominator}"
            if self.denominator > 0
            else f"{-self.numerator}/{-self.denominator}"
        )

    def __eq__(self, other) -> bool:
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __ne__(self, other) -> bool:
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __lt__(self, other) -> bool:
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __gt__(self, other) -> bool:
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __le__(self, other) -> bool:
        return self.numerator / self.denominator <= other.numerator / other.denominator

    def __ge__(self, other) -> bool:
        return self.numerator / self.denominator >= other.numerator / other.denominator


a = Fraction(-4, -6)
print(Fraction(1) + a)
