titl git-push(1)

text Update remote refs along with associated objects, i.e. send your local changes to a remote
item Either it just succeeds and you are done, or ...
item it forces you to update your local branch first by invoking either, git pull or git fetch, git merge FETCH\_HEAD
item You must have write permissions on the remote!
item Example:
	ite2
		code git push <remote> <branch>
	ite2
		code git push origin master
