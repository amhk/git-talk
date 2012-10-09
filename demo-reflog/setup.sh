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

cat > factorial.c << EOF
#include <stdio.h>

static unsigned int factorial(unsigned int n)
{
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

int main()
{
    unsigned int i;
    for (i = 0; i < 10; ++i)
        printf("factorial(%d) = %d\n", i, factorial(i));
    return 0;
}
EOF

git add factorial.c
git commit -m 'Added factorial.c'

cat << EOF
--------------------------------
1. hack, hack, hack...
2. git add -u
3. git commit --amend
4. git reflog
5. 'git show HEAD@{1}' vs 'git show'
-> original commit still reachable
EOF
