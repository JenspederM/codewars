def solution(string: str, marker: list):
    lines = string.splitlines()
    n = len(lines)
    out = ''
    for i, line in enumerate(lines):
        res = ''
        for c in line:
            if c in marker:
                break
            res += c
        res = res.rstrip()
        if i < n - 1:
            res += "\n"
        out += res

    return out


def solution2(string, markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
