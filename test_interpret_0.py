import interpret_0

import pytest
import io
from contextlib import redirect_stdout


def test_hello_world():
    input_buffer = open("input/hello_world.bf").read()

    python_code = interpret_0.interpret_0(input_buffer)

    # Capture stdout from exec
    f = io.StringIO()
    with redirect_stdout(f):
        exec(python_code)
    out = f.getvalue()[:-1]  # out has '\n' at the end, remove that

    assert out == "Hello World!"
