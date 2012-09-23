all:
	./tpp.py > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi

preview:
	./tpp.py --preview > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi

development:
	./tpp.py --development --bash > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi

handout:
	./tpp.py --bash > a.tex
	echo X | latex '\def\MODE{handout} \input{a.tex}'
	dvips a.dvi
	psnup -4 -W128mm -H96mm a.ps handout.ps
	ps2pdf handout.ps
	rm handout.ps

part1:
	./tpp.py --part=1 > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi
	./tpp.py --part=1 --bash > a.tex
	echo X | latex '\def\MODE{handout} \input{a.tex}'
	dvips a.dvi
	psnup -4 -W128mm -H96mm a.ps handout.ps
	ps2pdf handout.ps
	rm handout.ps
	mv a.pdf part1.pdf
	mv handout.pdf part1-handout.pdf

part2:
	./tpp.py --part=2 > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi
	./tpp.py --part=2 --bash > a.tex
	echo X | latex '\def\MODE{handout} \input{a.tex}'
	dvips a.dvi
	psnup -4 -W128mm -H96mm a.ps handout.ps
	ps2pdf handout.ps
	rm handout.ps
	mv a.pdf part2.pdf
	mv handout.pdf part2-handout.pdf

part3:
	./tpp.py --part=3 > a.tex
	echo X | latex '\def\MODE{} \input{a.tex}'
	dvipdf a.dvi
	./tpp.py --part=3 --bash > a.tex
	echo X | latex '\def\MODE{handout} \input{a.tex}'
	dvips a.dvi
	psnup -4 -W128mm -H96mm a.ps handout.ps
	ps2pdf handout.ps
	rm handout.ps
	mv a.pdf part3.pdf
	mv handout.pdf part3-handout.pdf
