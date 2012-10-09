titl gitrevisions(7) --- ranges

item
	code A
	: (parent) commits reachable from A

item
	code ^A
	: exclude commits reachable from A

item
	code ^A B
	$\equiv$
	code A..B
	: commits reachable from B, excluding commits reachable from A

ite2
	code git log HEAD~5..HEAD

item
	code A...B
	: commits reachable from A or B, but not from both (XOR)
