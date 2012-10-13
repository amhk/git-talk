titl git-blame(1)

syno git blame [-Ln,m] path

item In which commit was a line introduced?

item
	code -L
	: limit output to a range of lines

ite2 number, /regex/, +offset, -offset
ite2
	code git blame -L128,+10 foo.c
