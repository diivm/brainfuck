import interpret_0, interpret_1

import io, os
from contextlib import redirect_stdout

output = {"add.bf": "7", "hello_world.bf": "Hello World!"}

in_out = {}  # entry: input_buffer
for entry in os.listdir(basepath := "input/"):
    if os.path.isfile(filename := os.path.join(basepath, entry)):
        in_out[open(filename).read()] = output[entry]


def test_interpret_0():
    for input_buffer, printing_value in in_out.items():
        python_code = interpret_0.interpret_0(input_buffer)

        # Capture stdout from exec
        f = io.StringIO()
        with redirect_stdout(f):
            exec(python_code)
        out = f.getvalue()
        if "\n" in out:
            out = out[:-1]

        assert out == printing_value


def test_interpret_1():
    for input_buffer, printing_value in in_out.items():
        out = interpret_1.interpret_1(input_buffer)
        if "\n" in out:
            out = out[:-1]
        assert out == printing_value
