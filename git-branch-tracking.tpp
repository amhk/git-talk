titl git-branch(1) - tracking

item Make git automatically follow the branch based on where you started from
	ite2
		code git branch -t <new_branch>

item Enable tracking of branches on an existing local branch
	ite2
		code git branch --set-upstream <local> <remote>

item Using checkout
	ite2
		code git checkout -t origin/master
item Using checkout, but another name than the remote name
	ite2
		code git checkout -t -b anothername origin/master
