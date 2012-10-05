titl gitrevisions(7) --- ranges

item A..B: commits reachable from B, excluding commits reachable from A

ite2
	code git log HEAD~5..HEAD

item A...B: commits reachable from A or B, but not from both (XOR)
