"""
Author: John Paul Goodman
Course: ISyE 6644
Semester: Fall 2021
Project Group: 40
"""
from RV import RandomVariates
# from RV import RandomVariates as rv


def main():
    """
    Main
    """
    rv = RandomVariates()
    print(rv.uniform(n=5))


if __name__ == '__main__':
    main()
