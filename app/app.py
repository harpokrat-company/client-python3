
import sys
import signal

from cli import CLI


def signal_handler(sig, frame):
    print('Exit.')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    cli = CLI()
    cli.run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
