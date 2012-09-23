#!/usr/bin/python
from slide import convert
import os
import optparse

def verbatim(filename):
	fin = open(filename, "r")
	data = fin.readlines()
	fin.close()
	return data

def latest_file(files):
	(filename, mtime) = (None, 0)
	for f in files:
		st_mtime = os.stat(f).st_mtime
		if st_mtime > mtime:
			(filename, mtime) = (f, st_mtime)
	return filename

parser = optparse.OptionParser("tpp.py FIXME")
parser.add_option("-P", "--preview", action="store_true", dest="preview",
		help="preview mode (only generate slide for latest modified input file")
parser.add_option("-d", "--development", action="store_true", dest="development",
		help="development mode (use alternate set of input files, geared for development of tpp)")
parser.add_option("-b", "--bash", action="store_true", dest="bash",
		help="bash prints enabled (generate slides with bash commands)")
parser.add_option("-p", "--part", action="store", type="string", dest="part", default=None,
		help="limit output to specific part (1, 2 or 3)")
(options, args) = parser.parse_args()

if options.development:
	from index import dev_files
	files = dev_files
elif options.part == "1":
	from index import files_part1
	files = files_part1
elif options.part == "2":
	from index import files_part2
	files = files_part2
elif options.part == "3":
	from index import files_part3
	files = files_part3
else:
	from index import files

only_this_file = None
if options.preview:
	only_this_file = latest_file(files)

for f in files:
	if f.endswith(".tex"):
		print "".join(verbatim(f))
	else:
		if only_this_file == None:
			print "\n".join(convert(f, options.bash))
		elif only_this_file == f:
			print "\n".join(convert(f, options.bash))

# vi: noexpandtab ts=4 sw=4
