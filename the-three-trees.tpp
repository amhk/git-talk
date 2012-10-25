titl git's three trees

text \hfil
	\begin{pspicture}[xunit=1.2cm, yunit=1.2cm](6, 4)%\psgrid
	\pnode(1, 4){wdtop}
	\pnode(1, 0){wdbottom}
	\ncline{-}{wdtop}{wdbottom}
	\pnode(3, 4){itop}
	\pnode(3, 0){ibottom}
	\ncline{-}{itop}{ibottom}
	\pnode(5, 4){gdtop}
	\pnode(5, 0){gdbottom}
	\ncline{-}{gdtop}{gdbottom}
	\pnode(1, 3){addsrc}
	\pnode(3, 3){adddest}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{addsrc}{adddest}
	\psframe[fillstyle=solid, fillcolor=white, linecolor=white](2.8, 0.5)(3.2, 1.2)
	\naput{\small{git add}}
	\pnode(3, 2){commitsrc}
	\pnode(5, 2){commitdest}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{commitsrc}{commitdest}
	\naput{\small{git commit}}
	\pnode(5, 1){checkoutsrc}
	\pnode(1, 1){checkoutdest}
	\ncline[nodesep=6mm, linestyle=dotted]{->}{checkoutsrc}{checkoutdest}
	\naput{\small{git checkout}}
	\rput[B](1, 4){\psframebox[fillstyle=solid, fillcolor=gitdefault]{working dir}}
	\rput[B](3, 4){\psframebox[fillstyle=solid, fillcolor=gitdefault]{index}}
	\rput[B](5, 4){\psframebox[fillstyle=solid, fillcolor=gitdefault]{git database}}
	\end{pspicture}
	\hfil
