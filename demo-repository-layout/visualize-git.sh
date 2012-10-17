#!/bin/bash

function handle_tree()
{
    local sha1=$1
    local short=$2

    echo "\"${sha1}\" [label=\"${short}\ntree\" fillcolor=\"#66bb66\"];"

    for pair in $(git cat-file -p $sha1 | awk '{ printf("%s:%s\n", $3, $4); }'); do
        obj=$(echo $pair | cut -d: -f1)
        path=$(echo $pair | cut -d: -f2)
        echo "\"${sha1}\" -> \"${obj}\" [label=\"$path\"];"
    done
}

function handle_commit()
{
    local sha1=$1
    local short=$2
    local tree=$(git cat-file -p $sha1 | awk '/^tree / { print $2; }')

    echo "\"${sha1}\" [label=\"${short}\ncommit\" fillcolor=\"#ee8866\"];"
    echo "\"${sha1}\" -> \"${tree}\";"

    for obj in $(git cat-file -p $sha1 | awk '/^parent / { print $2; }'); do
        echo "\"${sha1}\" -> \"${obj}\" [style=\"dotted\"];"
    done
}

function handle_blob()
{
	local sha1=$1
	local short=$2
	echo "\"${sha1}\" [label=\"${short}\nblob\" fillcolor=\"#88bbbb\"];";
}

function handle_object()
{
    local sha1=$1

    short=$(git rev-parse --short $sha1)
    type=$(git cat-file -t $sha1)

    case ${type} in
        tree) handle_tree $sha1 $short; ;;
        commit) handle_commit $sha1 $short; ;;
        blob) handle_blob $sha1 $short ;;
    esac
}

function handle_ref()
{
	local path=$1

	short=${path:5}
	sha1=$(cat $path)
	echo "\"$path\" [label=\"${short}\" shape=\"box\"];"
	echo "\"$path\" -> \"$sha1\";"
}

function main()
{
	echo "digraph G" {
	echo "node [style=\"filled\"];"

	# loose objects
	for path in $(find .git/objects -type d -name 'pack' -prune -or -type d -name 'info' -prune -or -type f -print); do
		sha1=$(echo $path | sed 's+.git/objects/++' | sed 's+/++')
		handle_object $sha1
	done

	# pack files
	cluster_id=0
	for path in $(find .git/objects/pack -type f -name '*.idx'); do
		short=${path:18:12}
		sha1s=$(git show-index < $path | awk '{ print $2; }')
		cluster_id=$(($cluster_id + 1))
		echo "subgraph cluster_$cluster_id {"
		echo "label=\"$short\";"
		for sha1 in $sha1s; do
			handle_object $sha1
		done
		echo "}"
	done

	# tags
	for path in $(find .git/refs/tags -type f); do
		handle_ref $path
	done

	# branches
	for path in $(find .git/refs/heads -type f); do
		handle_ref $path
	done

	## info/refs
	#if [ -e '.git/info/refs' ]; then
	#	for pair in $(awk '{ printf("%s:%s\n", $1, $2); }' .git/info/refs); do
	#		sha1=$(echo $pair | cut -d: -f1)
	#		name=$(echo $pair | cut -d: -f2)
	#		echo "\"$name\" [label=\"${name}\" shape=\"box\"];"
	#		echo "\"$name\" -> \"$sha1\";"
	#	done
	#fi

	echo "}"
}

echo "Scanning git tree"
main > /tmp/git.dot

echo "Generating graph"
dot -Tpng /tmp/git.dot > /tmp/git.png
