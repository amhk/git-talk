titl git-merge(1) --- squash

syno git merge --squash commitish

item Create a single commit out of all commits which are being merged

col

text \begin{pspicture}(4, 6)%\psgrid
	% before
	\gitcommit[A]{0.5}{1}{AA}
	\gitcommit[B]{0.5}{2}{AB}
	\gitcommit[C]{0.5}{3}{AC}
	\gitcommit[D]{0.5}{4}{AD}
	\gitcommit[E]{1.5}{4}{AE}
	\gitcommit[F]{1.5}{5}{AF}
	\gitparent{AA}{AB}
	\gitparent{AB}{AC}
	\gitbranch{AC}{AE}
	\gitparent{AC}{AD}
	\gitparent{AE}{AF}
	% after
	\gitcommit[A]{3}{1}{BA}
	\gitcommit[B]{3}{2}{BB}
	\gitcommit[C]{3}{3}{BC}
	\gitcommit[D]{3}{4}{BD}
	\gitcommit[\scriptsize EF]{3}{5}{BEF}
	\gitcommit[E]{4}{4}{BE}
	\gitcommit[F]{4}{5}{BF}
	\gitparent{BA}{BB}
	\gitparent{BB}{BC}
	\gitparent{BC}{BD}
	\gitparent{BD}{BEF}
	\gitbranch{BC}{BE}
	\gitparent{BE}{BF}
	% before -> after arrow
	\pnode(1,3){before}
	\pnode(3,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
