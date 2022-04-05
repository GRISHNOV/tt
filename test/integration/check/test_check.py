import os
import re
import shutil

from utils import run_command_and_get_output


def test_check_unset_arg(tt_cmd, tmpdir):
    # Testing with unset application file.
    cmd = [tt_cmd, "check"]
    rc, output = run_command_and_get_output(cmd, cwd=tmpdir)
    assert rc == 1
    assert re.search(r"Currently, you can specify only one instance at a time.", output)


def test_check_too_many_args(tt_cmd, tmpdir):
    # Testing with more than one specified files.
    cmd = [tt_cmd, "check", "file1", "file2"]
    rc, output = run_command_and_get_output(cmd, cwd=tmpdir)
    assert rc == 1
    assert re.search(r"Currently, you can specify only one instance at a time.", output)


def test_check_non_existent_file(tt_cmd, tmpdir):
    # Testing with non-existent application file.
    cmd = [tt_cmd, "check", "path-to-non-existent-file"]
    rc, output = run_command_and_get_output(cmd, cwd=tmpdir)
    print(rc)
    print(output)
    assert rc == 1
    assert re.search(r"no such file or directory", output)


def test_check_incorrect_syntax_file(tt_cmd, tmpdir):
    # Copy the application file with incorrect syntax to the "run" directory.
    test_app_path = os.path.join(os.path.dirname(__file__), "test_app", "incorrect_syntax.lua")
    shutil.copy(test_app_path, tmpdir)

    # Testing application file with incorrect syntax.
    cmd = [tt_cmd, "check", 'incorrect_syntax']
    rc, output = run_command_and_get_output(cmd, cwd=tmpdir)
    assert rc == 0
    assert re.search(r"Syntax errors detected:", output)


def test_check_correct_syntax_file(tt_cmd, tmpdir):
    # Copy the application file with incorrect syntax to the "run" directory.
    test_app_path = os.path.join(os.path.dirname(__file__), "test_app", "correct_syntax.lua")
    shutil.copy(test_app_path, tmpdir)

    # Testing application file with correct syntax.
    cmd = [tt_cmd, "check", 'correct_syntax']
    rc, output = run_command_and_get_output(cmd, cwd=tmpdir)
    assert rc == 0
    assert re.search(r"is OK", output)
