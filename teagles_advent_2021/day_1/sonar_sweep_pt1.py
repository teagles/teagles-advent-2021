import sys

from .sonar_sweep_lib import find_depth_increments, stream_to_ints


def main():
    print(str(find_depth_increments(stream_to_ints(sys.stdin))))


if __name__ == '__main__':
    main()
