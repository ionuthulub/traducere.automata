import re
import sys


def load_file(filename):
    d = {}
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            line = line.strip()
            if not line:
                continue
            k, v = line.split('=')
            d[k] = v
    return d


def apply_rules(s):
    pos = load_file(sys.argv[2])
    tokens = re.split('([^a-zA-Z])', s)
    for i in range(len(tokens) - 2):
        if tokens[i] in pos and pos[tokens[i]] == 'N':
            if tokens[i+2] in pos and pos[tokens[i+2]] == 'ADJ':
                tokens[i], tokens[i+2] = tokens[i+2], tokens[i]
    return ''.join(tokens)


def replace_words(s):
    dictionary = load_file(sys.argv[1])
    tokens = re.split('([^a-zA-Z])', s)
    tokens = [dictionary[t] if t in dictionary else t for t in tokens]
    return ''.join(tokens)


def translate(s):
    s = apply_rules(s)
    s = replace_words(s)
    return s

def main():
    with open(sys.argv[3], 'r') as fin:
        sentences = [s.strip() for s in fin.readlines() if s.strip()]

    for s in sentences:
        print '{0}\n{1}\n'.format(s, translate(s))


if __name__ == '__main__':
    main()

