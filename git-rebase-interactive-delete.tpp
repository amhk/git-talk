titl git-rebase(1) --- interactive --- delete

item Delete lines in the rebase editor

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
	\gitcommit[C']{3}{5}{BC}
	\gitparent{BA}{BC}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
