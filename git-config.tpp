titl git-config(1)

syno git config [--global] key value

text Configure git options

item user name, email, \ldots
item which colors to use, what tools to use
item git commit template
item \ldots

text Three levels, each shadowing the former

item system:
	code $(prefix)/etc/gitconfig
item user:
	code $HOME/.gitconfig
item repository
	code $GIT_DIR/config
