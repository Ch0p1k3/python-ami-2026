import sys


def printer(
    *args,
    sep=" ",
    end="\n",
    **kwargs,
):
    print(*args, sep=sep, end=end)
    print(*((k, v) for k, v in kwargs.items()), sep=sep, end=end)


def main():
    exec(sys.stdin.read())


if __name__ == "__main__":
    main()
