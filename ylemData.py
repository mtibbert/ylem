from temporencUtils.temporencUtils import TemporencUtils
from temporencUtils.types.typeD import TypeD


def main():
    print_type_d()


def print_type_d():
    data = "["
    for x in range(1983, 1989):
        if (x % 3) == 0:
            data += "\n    "
        obj = TypeD(TemporencUtils.packb(year=x))
        data += obj.asJson(True) + ", "
    data = data[:-2] + "\n]"
    print data


if __name__ == "__main__":
    main()
