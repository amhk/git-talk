titl dev-torture

text This is some text.
	And so is this.

item First list item.
item Second list item.

item Locate all files ending in~.c:
	code find . -name '*.c'
#foobar
item Find any directory called src:
	code find . -type d -name 'src'
ite2 2nd item

col

text This is a \LaTeX\ command.

text \begin{pspicture}(4,3)
		\psframe(0, 0)(4, 3)
		\rput(2, 1.5){pstricks}
	\end{pspicture}

text	\begin{lstlisting}
	>for (i = 0; i < N; ++i)
	>    listings();
	\end{lstlisting}

item 1st level
ite2 2nd level

# vi: sw=5 ts=5 noexpandtab
