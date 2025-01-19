def convert(mass):
    return mass * 300000000**2


def main():
    mass = int(input("Mass in kg: "))
    print(convert(mass))


main()
