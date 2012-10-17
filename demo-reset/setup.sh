#!/bin/bash
set -eu

if [ $# -ne 1 ]; then
	echo "usage: $(basename $0) dir"
	exit 1
fi
root="$1"

mkdir "${root}"
cd "${root}"

git init

echo "first" > a.txt
echo "will never be changed" > b.txt
git add a.txt b.txt
git commit -m 'First commit'
git tag first

echo "second" > a.txt
git add a.txt
git commit -m 'Second commit'
git tag second

echo "third" > a.txt
git add a.txt
git commit -m 'Third commit'
git tag third

cat << EOF
--------------------------------
Three commits created. Feel free
to experiment with git reset.

End by adding a new commit to
'third', in which both a.txt
and b.txt are changed.
EOF
