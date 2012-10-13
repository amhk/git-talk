# -- BASICS = 30 min (Bech from here)
part1 = [
	"part-basics.tpp",
	"intro.tpp", # reason for this course
	# INTRO
	# goal: overview of git for daily usage
	# will re-iterate and explain same concepts using
	# different angles over and over again

	"distributed.tpp",
	# DISTRIBUTED
	# local copy -> free to mess around locally

	# INIT/CLONE
	"git-init.tpp",
	"git-clone.tpp",
	# git init && ls -d .git
	# everything stored in top-level .git directory
	# git clone <url> <dir>

	# HELP/MAN
	"git-help-man.tpp",
	# git help cmd
	# man git-cmd

	# ADD
	"git-add.tpp",
	# fortune >> foo.txt && git add foo.txt
	# don't explain in detail what's happening, not yet

	# COMMIT
	# git commit
	"git-commit.tpp",
	# manually write commit msg in EDITOR
	# still don't explain what's happening

	# LOG
	# git log
	# git log -p
	# git log --graph ? "there are GUIs..."
	# re-do add, commit, log to add one more commit

	# THE BIG PICTURE
	# [working directory] ---- [index] ---- [.git version]
	# "animated" image: git add move to index, git commit move to .git

# -- BRANCHES AND MERGES 30-45 min
#
# STATUS
# status
# status -s
#
# DIFF
# show work in progress: git diff && git diff --cached
# also show diff between range of commits: git diff HEAD~5..HEAD
# also, diff --stat, diff --word-diff
#
# MV/RM
# use them
#
# SHOW
# git show <any commit>
#
# WHAT'S A PATCH
# Inspect git show output.
# Explain hunk header, that it's all text, old well-known format not intrinsict to git.
# Possible to store a patch as a plain text file!
#
# BRANCH
# git branch b && git checkout b
# git checkout -b b
# # checkout is a Swizz army knife, used for anything...
#
# BRANCH, CONT
# add commits on branch, run log
# switch branch to master, add commits, run log
#
# BRANCH, NO BRANCH
# possible to git checkout <sha1> -> will get no branch state
#
# MERGE
# git branch # -> standing on master
# git merge dev # -> merge branch dev into master
#
# MERGE, CONFLICT
# set up brances with conflicting changes
# git merge -> get conflict
# git status
# display <<<< ==== >>>> markers
# manually resolve
# git add to mark file as resolved
# git commit to finish merge
#
# MERGETOOL
# just mention mergetool, difftool
#
#
# MERGE, FAST FORWARD
# merge by default creates a merge commit
# fast-forward: dest branch not changed
# --no-commit, --ff-only, etc
#
# -- COMMUNICATING WITH THE REST OF THE WORLD = 15 min
#
# REMOTE
# explain how to set up list of remote branches
# add
# rename
# -v
#
# FETCH, PULL
# git clone revisited, implicit origin remote
# git fetch -> download commits to FETCH_HEAD
# git pull -> git fetch and merge
#
# PUSH
# upload changes
# either successeds, or makes you do conflict resolution locally
# requires write permission
#
# GIT PROTOCOLS
# git, ssh, http, https
#
# BRACHES, TRACKING
# git branch -t
#
# REBASE
# (plain rebase, not interactive)
# run example
#
# -- FLUID WORKFLOW (Kongstad from here and below) = 30-45 min
#
	"part-fluid-workflow.tpp",
	"git-config.tpp",
	"git-config-alias.tpp", # [alias] in git-config
	"gitignore.tpp",
	"githooks.tpp",
	"gitrevisions.tpp",
	"gitrevisions-ranges.tpp",
	"gitrevisions-demo.tpp",
	"git-tag.tpp",
	"git-reflog.tpp",
	"trick-find-commits.tpp",
#
# -- REBASE AND FRIENDS = 30 min
#
	"part-interactive-rebase-and-friends.tpp",
	"git-stash.tpp",
	"git-merge-squash.tpp",
	"trick-topic-branches.tpp",
	"git-rebase-interactive.tpp",
	"git-rebase-interactive-amend.tpp",
	"git-rebase-interactive-reorder.tpp",
	"git-rebase-interactive-delete.tpp",
	"git-rebase-interactive-squash.tpp",
	"git-rebase-interactive-split.tpp",
	"git-add-interactive.tpp",
	"git-rerere.tpp",
#
# SHOW commitish:path
# display file 'path' as it were at commit 'commitish'
#
# -- MORE PATCHES = 10 min
	"part-patches-explained.tpp",
#
# AUTHOR VS COMITTER
# git show --format=fuller on a commit
#
# CHERRY-PICK
# use git cherry-pick -x
#
# FORMAT-PATCH, AM
# git format-patch && mail someone && git am
# this is how patches are submitted to the kernel
#
# APPLY
# apply raw patch
#
# -- MISCELLANEOUS = 30 min
	"part-miscellaneous.tpp",
#
# RESET AND CHECKOUT
# to reset files in working directory
#
# CLEAN
# clean -n
# clean -fxd
# git reset --hard
#
	"git-blame.tpp",
	"git-bisect.tpp",
	"git-bisect-demo.tpp",
#
# -- INTERNAL REPRESENTATION = 15 min
	"part-git-internals.tpp",
# fsck
# gc
# visualize-git.sh
# init --bare
# remove object from history: filter-branch, won't work if published
#
# SECURITY/ATOMICITY
# git tag vs git tag -a (save for later)
]

files = ["head.tex", "cover.tpp"] + part1 + ["foot.tex"]

dev_files = [
	"head.tex",
	"dev-part.tpp",
	"dev-text.tpp",
	"dev-item.tpp",
	"dev-column.tpp",
	"dev-pstricks.tpp",
	"dev-listings.tpp",
	"dev-bash.tpp",
	"dev-git.tpp",
	"dev-torture.tpp",
	"foot.tex",
]

# vi: noexpandtab ts=4 sw=4
