from collections import namedtuple

SubPosition = namedtuple('SubPosition', ['horizontal', 'depth'])
SubPosition2 = namedtuple('SubPosition', ['horizontal', 'depth', 'aim'])
Instruction = namedtuple('Instruction', ['direction', 'degree'])


def sub_u(position, degree):
    return SubPosition(position.horizontal, position.depth - degree)


def sub_d(position, degree):
    return SubPosition(position.horizontal, position.depth + degree)


def sub_f(position, degree):
    return SubPosition(position.horizontal + degree, position.depth)


def sub_u2(position, degree):
    return SubPosition2(position.horizontal, position.depth, position.aim - degree)


def sub_d2(position, degree):
    return SubPosition2(position.horizontal, position.depth, position.aim + degree)


def sub_f2(position, degree):
    return SubPosition2(position.horizontal + degree, position.depth + position.aim * degree, position.aim)


def move_sub(position, instruction):
    return instruction.direction(position, instruction.degree)


def instruction_tuples(stream):
    for line in stream:
        direction, degree = line.split(' ')
        if direction == 'down':
            yield Instruction(sub_d, int(degree))
        elif direction == 'up':
            yield Instruction(sub_u, int(degree))
        elif direction == 'forward':
            yield Instruction(sub_f, int(degree))
        else:
            raise ValueError(f'{direction} is an invalid direction.')


def instruction_tuples2(stream):
    for line in stream:
        direction, degree = line.split(' ')
        if direction == 'down':
            yield Instruction(sub_d2, int(degree))
        elif direction == 'up':
            yield Instruction(sub_u2, int(degree))
        elif direction == 'forward':
            yield Instruction(sub_f2, int(degree))
        else:
            raise ValueError(f'{direction} is an invalid direction.')
