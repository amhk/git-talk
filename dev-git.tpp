titl dev-git

syno This is the synopsis command.

text PSTricks for drawing git trees.

text \begin{pspicture}(8, 5)\psgrid
	\gitcommit{1}{2}{A}
	\gitcommit{2}{2}{B}
	\gitcommit{3}{2}{C}
	\gitcommit{4}{2}{D}
	\gitcommit{5}{2}{E}
	\gitparent{A}{B}
	\gitparent{B}{C}
	\gitparent{C}{D}
	\gitparent{D}{E}
	\gitcommitshaded[$\alpha$]{3}{3}{o1}
	\gitcommitshaded[$\beta$]{4}{3}{o2}
	\gitbranchshaded{B}{o1}
	\gitparentshaded{o1}{o2}
	\gitcommit[$\alpha'$]{6}{3}{n1}
	\gitcommit[$\beta'$]{7}{3}{n2}
	\gitbranch{E}{n1}
	\gitparent{n1}{n2}
	\gittag{7}{4}{dev}{n2}
	\gittagshaded{4}{4}{dev}{o2}
	\gittag{5}{1}{master}{E}
	\gittagshaded{2}{1}{master}{B}
	\end{pspicture}

# vi: sw=5 ts=5 noexpandtab
