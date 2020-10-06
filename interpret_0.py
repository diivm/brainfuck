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


def interpret_0(input_buffer: str):
    """
    Converts brainfuck `input_buffer` to a python code.

    Parameters:
        - input_buffer (str)
    Returns:
        - python_code (str)
    """
    python_code = f"output_buffer = [0] * {MAX_SIZE}; ptr=0\n"
    no_of_tabs = 0
    for c in input_buffer:
        for _ in range(no_of_tabs):
            python_code += "\t"
        if c == ">":
            python_code += "ptr += 1\n"
        elif c == "<":
            python_code += "ptr -= 1\n"
        elif c == "+":
            python_code += "output_buffer[ptr] += 1\n"
        elif c == "-":
            python_code += "output_buffer[ptr] -= 1\n"
        elif c == ",":
            python_code += "output_buffer[ptr] = input()[0]\n"
        elif c == ".":
            python_code += "print(chr(output_buffer[ptr]), end='')\n"
        elif c == "[":
            python_code += "while output_buffer[ptr] != 0:\n"
            no_of_tabs += 1
        elif c == "]":
            python_code += "\n"
            no_of_tabs -= 1

    return python_code
