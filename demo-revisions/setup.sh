#!/bin/bash
# Construct the following revision graph and print different ranges.
# Examples taken from the gitrevisions(7) man page.
#
#     root
#   / |  \ \
#  /  |   |  \
# G   H   I   J
#  \ /     \ /
#   D   E   F
#    \  |  / \
#     \ | /   |
#      \|/    |
#       B     C
#        \   /
#         \ /
#          A
#
set -eu

function create_commit()
{
	echo "$1" > $1.txt
	git add $1.txt
	git commit -m "$1"
	git tag $1
}

function create_child()
{
	local parent=$1
	local child=$2

	git checkout refs/tags/$parent
	create_commit $child
}

function create_child2()
{
	local parent_left=$1
	local parent_right=$2
	local child=$3

	git checkout $parent_left
	git merge --no-ff -m "$child" $parent_right
	git tag "$child"
}

function create_child3()
{
	local parent_left=$1
	local parent_middle=$2
	local parent_right=$3
	local child=$4

	git checkout $parent_left
	git merge --no-ff -m "$child" $parent_middle $parent_right
	git tag "$child"
}

function print_range()
{
	local range="$1"
	printf "%-10s : " "$range"
	git log --format="%s" $range | sort | xargs echo
}

if [ $# -ne 1 ]; then
	echo "usage: $(basename $0) dir"
	exit 1
fi
root="$1"

mkdir "${root}"
cd "${root}"

git init

create_commit root

create_child root H
create_child root G
create_child root E
create_child root I
create_child root J

create_child2 G H D
create_child2 I J F

create_child3 D E F B
create_child F C

create_child2 B C A

git log --format="%s" --graph

print_range "D"
print_range "D F"
print_range "B...C"
print_range "^D B C"
