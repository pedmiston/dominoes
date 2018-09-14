
def find_next(head, dominoes):
    """Find the domino in dominoes that is next to head."""
    for left, right in dominoes:
        if head[1] == left:
            return (left, right)
    return None


def make_chain(output, rest):
    last = output[-1]
    next = find_next(last, rest)
    if next:
        output.append(next)
        rest.remove(next)
        return make_chain(output, rest)
    return output


def chain(dominoes):
    for first in dominoes:
        rest = dominoes[:]
        rest.remove(first)
        output_chain = make_chain([first], rest)
        if len(output_chain) == len(dominoes) and output_chain[0][0] == output_chain[-1][1]:
            return output_chain
