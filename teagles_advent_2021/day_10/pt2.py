import sys


from .lib import validate, score_autocomplete, Bracket


def main():
    scores = list(sorted(filter(None, map(lambda b: score_autocomplete(b) if type(b) != Bracket else None,
                                          map(validate, sys.stdin)))))
    print(scores[len(scores) // 2])


if __name__ == '__main__':
    main()
