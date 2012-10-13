titl git-rebase(1) --- interactive --- reorder

item Reorder the lines in the rebase editor

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
	\gitcommit[C']{3}{3}{BC}
	\gitcommit[B']{3}{5}{BB}
	\gitparent{BA}{BC}
	\gitparent{BC}{BB}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
