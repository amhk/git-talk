titl git-bisect(1) --- demo

text	\vfill\hfil
	\begin{pspicture}[xunit=1.2cm, yunit=1.2cm](6, 5)%\psgrid
	%
	% ITERATON 0
	%
	\rput(-0.5, 5){\Rnode{itera}{$i_0$}}
	\gitcommitshaded[A]{0}{5}{AA}
	\gitcommit[B]{1}{5}{AB}
	\gitcommit[C]{2}{5}{AC}
	\gitcommit[D]{3}{5}{AD}
	\gitcommit[E]{4}{5}{AE}
	\gitcommit[F]{5}{5}{AF}
	\gitcommitshaded[G]{6}{5}{AG}
	\gitparentshaded{AA}{AB}
	\gitparent{AB}{AC}
	\gitparent{AC}{AD}
	\gitparent{AD}{AE}
	\gitparent{AE}{AF}
	\gitparentshaded{AF}{AG}
	\gittag{0}{4.2}{good}{AA}
	\gittag{3}{4.2}{HEAD}{AD}
	\gittag{6}{4.2}{bad}{AG}
	%
	% ITERATON 1
	%
	\rput(-0.5, 3){\Rnode{iterb}{$i_1$}}
	\gitcommitshaded[A]{0}{3}{BA}
	\gitcommitshaded[B]{1}{3}{BB}
	\gitcommitshaded[C]{2}{3}{BC}
	\gitcommitshaded[D]{3}{3}{BD}
	\gitcommit[E]{4}{3}{BE}
	\gitcommit[F]{5}{3}{BF}
	\gitcommitshaded[G]{6}{3}{BG}
	\gitparentshaded{BA}{BB}
	\gitparentshaded{BB}{BC}
	\gitparentshaded{BC}{BD}
	\gitparentshaded{BD}{BE}
	\gitparent{BE}{BF}
	\gitparentshaded{BF}{BG}
	\gittag{3}{2.2}{good}{BD}
	\gittag{5}{2.2}{HEAD}{BF}
	\gittag{6}{2.2}{bad}{BG}
	%
	% ITERATON 2
	%
	\rput(-0.5, 1){\Rnode{iterc}{$i_2$}}
	\gitcommitshaded[A]{0}{1}{CA}
	\gitcommitshaded[B]{1}{1}{CB}
	\gitcommitshaded[C]{2}{1}{CC}
	\gitcommitshaded[D]{3}{1}{CD}
	\gitcommit[E]{4}{1}{CE}
	\gitcommitshaded[F]{5}{1}{CF}
	\gitcommitshaded[G]{6}{1}{CG}
	\gitparentshaded{CA}{CB}
	\gitparentshaded{CB}{CC}
	\gitparentshaded{CC}{CD}
	\gitparentshaded{CD}{CE}
	\gitparentshaded{CE}{CF}
	\gitparentshaded{CF}{CG}
	\gittag{2.8}{0.2}{good}{CD}
	\gittag{4}{0.2}{HEAD}{CE}
	\gittag{5.2}{0.2}{bad}{CF}
	%
	% GIT COMMANDS
	%
	\psset{nrot=:U}
	\ncarc[nodesep=4pt, arcangle=-20]{->}{itera}{iterb}
	\nbput{\tiny{git bisect good}}
	\ncarc[nodesep=4pt, arcangle=-20]{->}{iterb}{iterc}
	\nbput{\tiny{git bisect bad}}
	\end{pspicture}
	\hfil
