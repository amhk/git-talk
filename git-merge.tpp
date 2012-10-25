titl git-merge(1)

syno git merge their-branch

item Bring changes from another branch into the current branch
item
	code git branch && git merge dev

text What is something goes wrong? Conflicts?
item Markers will be put in the conflicting file(s)
text \begin{lstlisting}[tagsize=2]
	context
	<<<<<
    ours
    =====
    theirs
    >>>>>
    context
    \end{lstlisting}
