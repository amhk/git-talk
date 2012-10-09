titl gitrevisions(7) --- demo

text	\hfil
	\begin{pspicture}[xunit=1.2cm, yunit=1.2cm](6, 4)
	\gitcommit{3}{4}{.}
	\gitcommit{0}{3}{G}
	\gitcommit{2}{3}{H}
	\gitcommit{4}{3}{I}
	\gitcommit{6}{3}{J}
	\gitcommit{1}{2}{D}
	\gitcommit{3}{2}{E}
	\gitcommit{5}{2}{F}
	\gitcommit{3}{1}{B}
	\gitcommit{5}{1}{C}
	\gitcommit{4}{0}{A}
	\gitparent{.}{G}
	\gitparent{.}{H}
	\gitparent{.}{I}
	\gitparent{.}{J}
	\gitparent{.}{E}
	\gitparent{G}{D}
	\gitparent{H}{D}
	\gitparent{I}{F}
	\gitparent{J}{F}
	\gitparent{D}{B}
	\gitparent{E}{B}
	\gitparent{F}{B}
	\gitparent{F}{C}
	\gitparent{B}{A}
	\gitparent{C}{A}
	\end{pspicture}
	\hfil
