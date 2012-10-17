titl git-reset(1)

syno git reset [--soft|--mixed|--hard] c

item
	code git checkout
	: change to branch

item
	code git reset
	: change branch itself

col

text \begin{pspicture}(4, 6)%\psgrid
	% before
	\gitcommit[A]{0.5}{1}{AA}
	\gitcommit[B]{0.5}{3}{AB}
	\gitcommit[C]{0.5}{5}{AC}
	\gitparent{AA}{AB}
	\gitparent{AB}{AC}
	\gittag{1.5}{6}{master}{AC}
	% after
	\gitcommit[A]{2.5}{1}{BA}
	\gitcommit[B]{2.5}{3}{BB}
	\gitcommitshaded[C]{2.5}{5}{BC}
	\gitparent{BA}{BB}
	\gitparentshaded{BB}{BC}
	\gittag{3.5}{4}{master}{BB}
	% before -> after arrow
	\pnode(0.5,3){before}
	\pnode(2.5,3){after}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{before}{after}
	\end{pspicture}
