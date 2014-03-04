#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2014 Research Compendia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import datetime
import json
from os.path import abspath, join, curdir
import subprocess


CHOICES = ['amd_demo', 'amd_demo2', 'amd_simple', 'amd_f77demo', 'amd_f77simple']


def run(demo):
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    results_file = join(abspath(curdir), 'Data', '%s_%s_results.txt' % (demo, timestamp))
    cmd = join(abspath(curdir), 'Demo', demo)
    with open(results_file, 'w+') as fh:
        subprocess.call(cmd, stdout=fh, stderr=subprocess.PIPE)


def setup():
    subprocess.call(['make', 'lib', 'fortran'])


def cleanup():
    subprocess.call(['make', 'clean'])


def build_parser():
    parser = argparse.ArgumentParser(description="""

    Runs the AMD C and Fortran 77 demos from AMD Version 1.1 (Jan. 21, 2004)
    http://www.cise.ufl.edu/research/sparse/amd

    AMD is a set of routines for pre-ordering sparse matrices prior to Cholesky
    or LU factorization, using the approximate minimum degree ordering
    algorithm.  Written in ANSI/ISO C with a MATLAB interface, and in
    Fortran 77.

    """)
    parser.add_argument('-s', '--setup', action='store_true', help='compiles demos')
    parser.add_argument('-c', '--cleanup', action='store_true', help='cleans compiled files')
    parser.add_argument('params', default='default.json', nargs='?',
        help='json file with parameters: { "demos": %s' % CHOICES)
    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.setup:
        setup()

    with open(args.params) as fh:
        params = json.load(fh)
        assert 'demos' in params, "missing 'demos' parameter."

    for demo in params['demos']:
        assert demo in CHOICES, "invalid demo, choose from %s" % CHOICES
        result = run(demo)
