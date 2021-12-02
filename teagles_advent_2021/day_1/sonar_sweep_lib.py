def stream_to_ints(stream):
    for line in stream:
        yield int(line)


def find_depth_increments(ints):
    last = None
    increments = 0
    for current_int in ints:
        if not last:
            pass
        elif current_int > last:
            increments += 1
        last = current_int
    return increments
