
import sys

from cli import CLI


def main():
    cli = CLI()
    cli.run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
