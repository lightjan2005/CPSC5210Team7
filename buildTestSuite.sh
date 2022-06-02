#!/bin/bash
# shellcheck disable=SC2164
cd /Users/anthonypinza/Desktop/CPSC5210Team7
python3 test_basketball.py > output.txt
pytest -cov >> output.txt
# shellcheck disable=SC2086
# shellcheck disable=SC2259
# shellcheck disable=SC2259

