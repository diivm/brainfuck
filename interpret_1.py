# uses walrus operator

MAX_SIZE = 30000

"""
> = increases memory pointer, or moves the pointer to the right 1 block.
< = decreases memory pointer, or moves the pointer to the left 1 block.
+ = increases value stored at the block pointed to by the memory pointer
- = decreases value stored at the block pointed to by the memory pointer
[ = like while(cur_block_value != 0) loop.
] = if block currently pointed to's value is not zero, jump back to [
, = input 1 character.
. = print 1 character to the console
"""


def find_matching_paranthesis(input_buffer: str, idx: int):
    bracket_stack = []
    for i in range(len(input_buffer)):
        c = input_buffer[i]
        if c == "[":
            bracket_stack.append(i)
        elif c == "]":
            if bracket_stack:
                bracket_stack.pop()
            else:
                return i


def printing_value(input_buffer: str, output_buffer: list, char_list: list):
    """
    Helper function
    """
    state = []
    ptr = 0
    i = 0
    while i < (buf_len := len(input_buffer)):
        c = input_buffer[i]
        if c == ">":
            if ptr == buf_len - 1:
                ptr = 0
            else:
                ptr += 1
        elif c == "<":
            if ptr == 0:
                ptr = buf_len - 1
            else:
                ptr -= 1
        elif c == "+":
            output_buffer[ptr] += 1
        elif c == "-":
            output_buffer[ptr] -= 1
        elif c == ",":
            output_buffer[ptr] = input()[0]
        elif c == ".":
            print(chr(output_buffer[ptr]), end="")
            char_list.append(chr(output_buffer[ptr]))
        elif c == "[":
            if output_buffer[ptr] != 0:
                state.append(i)
            else:
                if find_matching_paranthesis(input_buffer[i:], i):
                    i = find_matching_paranthesis(input_buffer[i:], i) + 1
                    continue
                else:
                    raise Exception("No closing matching paranthesis")
        elif c == "]":
            if output_buffer[ptr] != 0:
                if state:
                    i = state.pop()
                    continue
                else:
                    raise Exception("No opening matching paranthesis")
            else:
                state.pop()

        i += 1


def interpret_1(input_buffer: str):
    """
    Interprets brainfuck `input_buffer` and returns a printing value.

    Parameters:
        - input_buffer (str)
    Returns:
        Printing value
    """
    output_buffer = [0] * MAX_SIZE
    char_list = []
    printing_value(input_buffer, output_buffer, char_list)
    return "".join(char_list)
