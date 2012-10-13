#!/bin/bash
set -eu

NO_CURL=1 make -j8
(cd t && ./t0030-stripspace.sh)
