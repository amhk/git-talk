titl githooks(5)

syno $GIT_DIR/hooks/*

item Collection of scripts that are run at pre-determined execution points

item A script return value of non-zero will (in most cases) abort encapsulating operation

item post-commit: trigger notification, start build, \ldots

item pre-commit: check for trailing whitespace, \ldots

item dev branches:
	code git commit --no-verify
