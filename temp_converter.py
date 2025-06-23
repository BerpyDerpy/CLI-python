import argparse

def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-c", "--celsius",
        type=float,
    )
    group.add_argument(
        "-f", "--fahrenheit",
        type=float,
    )

    args = parser.parse_args()

    if args.celsius is not None:
        f_val = args.celsius
        c_val = f_to_c(f_val)
        print(f"{f_val}°F is {c_val:.2f}°C")
    else:
        c_val = args.fahrenheit
        f_val = c_to_f(c_val)
        print(f"{c_val}°C is {f_val:.2f}°F")

if __name__ == "__main__":
    main()
