titl git-rebase(1) --- interactive --- split

item Mark a commit as
	code edit

item
	code git reset HEAD^

item Add first part, commit

item Add second part, commit

item
	code git rebase --continue

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
	\gitcommit[B']{3}{2.3}{BB}
	\gitcommit[\small B'']{3}{3.7}{BC}
	\gitcommit[C']{3}{5}{BD}
	\gitparent{BA}{BB}
	\gitparent{BB}{BC}
	\gitparent{BC}{BD}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
