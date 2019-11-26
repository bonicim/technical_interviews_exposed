[![Build Status](https://travis-ci.org/bonicim/technical_interviews_exposed.svg?branch=master)](https://travis-ci.org/bonicim/technical_interviews_exposed)

# Summary

Simple and clean solutions for typical technical interview questions. The solutions are written in Python3.

This repo is a resource for the Technical Interviews Workshops at Northeastern University Seattle campus. Feel free to join the slack channel for this workshop. Note, you must have a husky.neu.edu email address to join the channel:

[https://join.slack.com/t/neu-tech-intv-wkshp/signup](https://join.slack.com/t/neu-tech-intv-wkshp/signup?x=x-p383132105155-382689801953-645529769844)

## Prerequisites

You must have the following installed on your machine:

* Python 3.7
* [Pytest](https://docs.pytest.org/en/latest/index.html)

## How to run the tests

### Running the test on the command line

To run a single test file, `cd` into the `tst` directory. Then run any test file. For example, to run the `test_two_sum.py` tests, enter the following command:

```bash
$ pytest test_two_sum.py --verbose
```

To run all tests:

```bash
$ pytest
```

Or if you want to invoke pytest via python, try **one** of the following:

```bash
python -m pytest
```

```bash
python3 -m pytest
```

You should see the following output:

```bash
============================================================ test session starts ============================================================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0 -- /Users/markbonicillo/Python-Virtual-Environments/ipython_env/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/markbonicillo/Workplace/technical_interviews_exposed/tst/.hypothesis/examples')
rootdir: /Users/markbonicillo/Workplace/technical_interviews_exposed
plugins: hypothesis-4.36.2
collected 11 items

test_two_sum.py::test_empty_list PASSED                                                                                               [  9%]
test_two_sum.py::test_example PASSED                                                                                                  [ 18%]
test_two_sum.py::test_empty PASSED                                                                                                    [ 27%]
test_two_sum.py::test_single PASSED                                                                                                   [ 36%]
test_two_sum.py::test_duplicate PASSED                                                                                                [ 45%]
test_two_sum.py::test_negative_integers_included PASSED                                                                               [ 54%]
test_two_sum.py::test_half_target_included PASSED                                                                                     [ 63%]
test_two_sum.py::test_sorted_ascending PASSED                                                                                         [ 72%]
test_two_sum.py::test_sorted_descending PASSED                                                                                        [ 81%]
test_two_sum.py::test_only_neg PASSED                                                                                                 [ 90%]
test_two_sum.py::test_zero_only PASSED                                                                                                [100%]

============================================================ 11 passed in 0.11s =============================================================
```

## Extra
See my blog post: [A Shortish Guide to Preparing For a Technical Interview](https://markbonicillo.com/2019/11/20/a-shortish-guide-to-preparing-for-a-technical-interview.html)
