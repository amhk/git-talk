#!/bin/bash
GIT_ORG=$PWD/original
GIT_COPY=$PWD/copy_original

clear
echo "About to create two git repositories called original and copy_original."
echo "The git repositories will contain a file readme.txt"
read -n 1

mkdir -p $GIT_ORG

cd $GIT_ORG
git init

cat > readme.txt << EOF
I am the first line in readme.txt created in git "original".
EOF

git add readme.txt
git commit -a -m "Added first line in original"

git clone $GIT_ORG $GIT_COPY

cd $GIT_ORG
cat >> readme.txt << EOF
I am the second line in readme.txt created in git "original".
EOF
git commit -a -m "Added second line in original"

cd $GIT_COPY
cat >> readme.txt << EOF
I am the second line in readme.txt created in git "copy_original".
EOF
git commit -a -m "Added second line in copy_original"

clear
echo "Show the content of original"
echo "  cd $GIT_ORG"
echo "  cat readme.txt"
echo "  git log"
echo ""
echo "Show the content of copy_original"
echo "  cd $GIT_COPY"
echo "  cat readme.txt"
echo "  git log"
echo "Different 2nd lines in the readme.txt"
echo "Try to merge changes from origin -> copy_original"
echo "  git pull -> conflict!"
echo "  git status"
echo "  vim readme.txt"

read -n 1
unset PROMPT_COMMAND
gnome-terminal &
cd $GIT_ORG
gnome-terminal &
