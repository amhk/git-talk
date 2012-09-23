# intro hook: pid-to-pname script, this course will help write such tools

# intersperse with slides of examples, for me to show
# interactively, and for handouts? (record bash session with "script")

# ssh, tmux, screen
# mmv, mcp
# watch
# diff, patch (hunks, etc), summary only, in depth when speaking about git
# jobs: background, foreground, bg, fg, &
# several commands together, cd /foo && rm -rf (or just rm -rf /foo)

part1 = [
	"goals.tpp", # reason for this course

	"part-system.tpp", # overview of Linux system
	"agenda.tpp",
	"init.tpp",
	"leaving-the-kernel.tpp",
	"processes.tpp",
	"process-types.tpp",
	"process-cmds.tpp", # user process interaction (top, pstree, ps, kill)
	"signals.tpp", # signal sending in general
	"users-and-groups.tpp", # users (yourself, root, daemon users)
	"file-permissions.tpp", # file permissions (-wrxwr-wr-)
	"file-systems.tpp", # file system in general, mount
	"root-dirs.tpp", # root dirs (/boot, /home, etc), ~ for $HOME
	"types-of-files.tpp", # types of files
	"symlinks.tpp", # symbolic links
	"proc.tpp", # /proc
	"syscalls.tpp", # system calls, strace
]

part2 = [
	"part-commands.tpp", # common commands, basic bash usage
	"man-pages.tpp", # man pages, there exist options, some optional
	"man-pages-nav.tpp", # man pages, how to navigate
	#"what-is-bash.tpp", # FIXME: intro to bash?
	#"shells.tpp", # FIXME: reuse shells.tpp here?
	"dir-traversal.tpp", # ls, cd, pushd, popd, pwd
	"find.tpp", # find
	"unix-philosophy.tpp", # intermission, unix philosophy
	"cp-and-friends.tpp", # cp, rm, mkdir, rmdir, touch, mv (rsync)
	"globbing.tpp", # globbing (* and ?, foo{,bar})
	"view-text.tpp", # cat, less, tail -f
	"simple-grep.tpp", # "search-text.tpp", # grep (no regex)
	"regex.tpp", # introduction to regex
	"regex-cont.tpp", # regex, cont
	"wc-and-friends.tpp", # wc, uniq, sort (best in combination with pipe)
	"stdio.tpp", # stdin, stdout, stderr
	"pipes.tpp", # pipes FIXME: examples: sort | uniq, tail -f | grep
	"stream-redirection.tpp", # a > b, a 2>&1, etc
	"stream-editors.tpp", # sed, tr
	"xargs.tpp", # xargs
	"bash-tricks.tpp", # history (ctrl-r), tab expansion
]

part3 = [
	"part-scripting.tpp", # scripting (scripts and on cmd line)
	# sliding scale of what is a script?
	"scripts-intro.tpp", # introduction to scripts
	"how-to-run-scripts.tpp", # source vs #!, # is comment
	"crunch-bang.tpp", # #! at head of file
	"shells.tpp", # different types of shells (bash)
	"variables.tpp", # variable names, leading $ when referencing
	"variables-arrays.tpp", # arrays
	"special-variables.tpp", # implicit variables, $1, $2, $*, $?
	"quotes.tpp", # quotes, "" vs '' FIXME: example, variable expanded in ""
	"bash-arithmetic.tpp", # bash arithmetic $((expr))
	"bash-conditionals.tpp", # [[ expr ]]
	"bash-conditionals-cont.tpp", # !, &&, || FIXME: example of shortcut: cd foo && rm -rf
	"if-else-fi.tpp", # if statements
	"for.tpp", # for loop FIXME: (push many files via adb)
	"while.tpp", #mention while, case, etc, refer to man bash
	"functions.tpp", # functions, parameters, recommend local name="$1"
	"mktemp.tpp", # temporary files, mktemp
	"trap.tpp", # trap signals, ERR, EXIT
	"trap-cont.tpp", # example of at_exit
	"command-substitution.tpp", # $(...)
	"demo-shell.tpp",

	# repetition and comparison with android
	"part-android.tpp",
	"adb-shell.tpp", # adb shell vs adb shell command
	"adb-shell-ps.tpp", # adb shell ps, zygote (why: fork keeps parent data)
	"adb-shell-kill.tpp", # adb shell kill
	"adb-shell-pipe.tpp", # adb shell script on target, tr -d '\r'
	"demo-shell-android.tpp",
]

files = ["head.tex", "part-intro.tpp"] + part1 + part2 + part3 + ["part-intro.tpp", "foot.tex"]
files_part1 = ["head.tex", "part-intro.tpp"] + part1 + ["part-intro.tpp", "foot.tex"]
files_part2 = ["head.tex", "part-intro.tpp"] + part2 + ["part-intro.tpp", "foot.tex"]
files_part3 = ["head.tex", "part-intro.tpp"] + part3 + ["part-intro.tpp", "foot.tex"]

	# example program to illustrate fork
	# example program to illustrate fork and exec
	# example program to illustrate signals
	# example implementation of syscall
	#    Android's bionic:
	#        ./libc/bionic/fork.c
	#        ./libc/arch-x86/syscalls/__fork.S
	#        ./libc/arch-arm/syscalls/__fork.S
	#        ./libc/include/sys/linux-syscalls.h
	# strace
	# fg, bg, & (perhaps in part two)
	# <, > and >> (perhaps in part two)



	# /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state
	# lists time spent at different CPU frequencies; couple with watch!
	# 
	# demo phone in sleep vs awake with input
	# watch -n0.5 adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state

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
