titl git-merge(1) - fast forward

text ``fast forward'' means that destination branch hasn't changed.
item Refuse to merge if a fast forward isn't possible
	ite2
		code git merge --ff-only
item Just merge the code, but don't actually commit it
	ite2
		code git merge --no-commit
