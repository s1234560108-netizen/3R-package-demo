from three_r_package.process import process


def test_process():
    assert process("  hello  ") == "hello"
