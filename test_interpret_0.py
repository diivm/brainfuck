import pytest
import interpret_0


def test_hello_world():
    f = open("input/hello_world.bf")
    input_buffer = f.read()

    python_code = interpret_0.interpret_0(input_buffer)
    exec(python_code)
