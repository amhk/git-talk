titl git-branch(1)

item A branch in git is simply a file that contains the 40 character SHA-1 of the commit it points to (41 bytes), i.e. very cheap!
item Create e new branch
	ite2
		code git branch <branchname>
item Switch/go to another branch
	ite2
		code git checkout <branchname>
item Create e new branch using git checkout
	ite2
		code git checkout -b <branchname>
item git checkout is like a Swizz army knife, create branch, select branch, undo changes \ldots
