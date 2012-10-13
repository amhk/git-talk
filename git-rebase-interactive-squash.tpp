titl git-rebase(1) --- interactive --- squash

item Reorder and mark commit
	code squash
	or
	code fixup

item
	code --autosquash
	: list of commits will be automatically reordered

ite2 Commit message: `fixup!~message~of~parent'

col

text \begin{pspicture}(4, 6)%\psgrid
	% before
	\gitcommit[A]{1}{1}{AA}
	\gitcommit[B]{1}{2.3}{AB}
	\gitcommit[C]{1}{3.7}{AC}
	\gitcommit[D]{1}{5}{AD}
	\gitparent{AA}{AB}
	\gitparent{AB}{AC}
	\gitparent{AC}{AD}
	% after
	\gitcommit[A]{3}{1}{BA}
	\gitcommit[\scriptsize BD]{3}{3}{BB}
	\gitcommit[C']{3}{5}{BC}
	\gitparent{BA}{BB}
	\gitparent{BB}{BC}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
