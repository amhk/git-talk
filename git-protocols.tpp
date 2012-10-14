titl git protocols

text Git supports several protocols when it comes to communicating with remotes

item rsync
	ite2
		code rsync://host.xz/path/to/repo.git/
item http, https (ssl)
	ite2
		code http://host.xz[:port]/path/to/repo.git/
	ite2
		code https://host.xz[:port]/path/to/repo.git/
item git protocol
	ite2
		code git://host.xz[:port]/path/to/repo.git/
	ite2
		code git://host.xz[:port]/~user/path/to/repo.git/
item ssh
	ite2
		code ssh://[user@]host.xz[:port]/path/to/repo.git/
	ite2
		code ssh://[user@]host.xz/path/to/repo.git/
	ite2
		code ssh://[user@]host.xz/~user/path/to/repo.git/
	ite2
		code ssh://[user@]host.xz/~/path/to/repo.git
