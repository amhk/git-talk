titl git-rebase(1) --- interactive --- amend

item Mark a commit as
	code reword
	(commit message)

item Mark a commit as
	code edit
	(patch:
	code git commit --amend
	)

item Note: subsequent commits are changed wrt parent sha1

col

text \begin{pspicture}(4, 6)%\psgrid
	% before
	\gitcommit[A]{1}{1}{AA}
	\gitcommit[B]{1}{3}{AB}
	\gitcommit[C]{1}{5}{AC}
	\gitparent{AA}{AB}
	\gitparent{AB}{AC}
	% after
	\gitcommit[A]{3}{1}{BA}
	\gitcommit[B']{3}{3}{BB}
	\gitcommit[C']{3}{5}{BC}
	\gitparent{BA}{BB}
	\gitparent{BB}{BC}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
