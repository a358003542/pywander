from pywander.file.utils import gen_bigfile_read

import pytest

@pytest.mark.skip('i have test it')
def test_gen_bigfile_read():
    result = []
    for line in gen_bigfile_read('README.md', line_start=2, line_count=6):
        result.append(line)

    assert len(result) == 6

@pytest.mark.skip('i have test it')
def test_gen_bigfile_read2():
    result = []
    for line in gen_bigfile_read('README.md', line_start=2, line_count=-1):
        result.append(line)

    assert len(result) > 0