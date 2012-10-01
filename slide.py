import re

TOKEN_ERR_ = -1
TOKEN_CONT = 0 # continuation
TOKEN_BLAN = 1 # blank line
TOKEN_COMM = 2 # comment
TOKEN_BEGI = 3 # file begin
TOKEN_END_ = 4 # file end
TOKEN_TITL = 5
TOKEN_TEXT = 6
TOKEN_ITEM = 7
TOKEN_ITE2 = 8
TOKEN_CODE = 9
TOKEN_GRAP = 10
TOKEN_BLIS = 11 # begin list
TOKEN_ELIS = 12 # end list
TOKEN_COL_ = 13 # split into columns, beginning of column 2
TOKEN_BCOL = 14 # begin columns
TOKEN_ECOL = 15 # end columns
TOKEN_BASH = 16
TOKEN_PART = 17

LEFT_COLUMN_PERCENTAGE = 0.6

enable_bash = False

class Context:
	def __init__(self):
		self.out = []
		self.prev_func = None

def get_data(token):
	return token[2]

def parse_begi(context, not_used):
	context.out.append("\\begin{frame}[fragile]")

def parse_end_(context, not_used):
	context.out.append("\\end{frame}")

def parse_blis(context, not_used):
	context.out.append("\\begin{itemize}")

def parse_elis(context, not_used):
	context.out.append("\\end{itemize}")

def parse_titl(context, token):
	#context.out.append("\\subsection{%s}" % get_data(token))
	context.out.append("\\frametitle{%s}" % get_data(token))

def parse_bash(context, token):
	if enable_bash:
		data = get_data(token).split("#", 1)
		if len(data) == 1:
			context.out.append("$ %s" % data[0])
		elif len(data[0]) == 0:
			context.out.append("# %s" % data[1])
		elif data[1][0] == "#":
			context.out.append("$ %s%s" % (data[0], data[1]))
		else:
			context.out.append("$ %s %%\\hfill%% # %s" % (data[0], data[1]))

def parse_text(context, token):
	context.out.append("%s" % get_data(token))

def parse_item(context, token):
	context.out.append("\\item %s" % get_data(token))

def parse_ite2(context, token):
	context.out.append("\\item %s" % get_data(token))

def parse_part(context, token):
	context.out.append("\\begin{center}")
	context.out.append("\\Huge\\textcolor{black}{%s}" % get_data(token))
	context.out.append("\\end{center}")

def parse_code(context, token):
	if context.prev_func == None:
		raise Exception("code not top-level element")
	context.out.append("\\code{%s}" % get_data(token))

def parse_grap(context, token):
	raise Exception("grap not implemented")

def parse_col_(context, token):
	width = 1 - LEFT_COLUMN_PERCENTAGE
	context.out.append("\\column{%.2f\\textwidth}" % width)

def parse_bcol(context, token):
	context.out.append("\\begin{columns}")
	context.out.append("\\column{%.2f\\textwidth}" % LEFT_COLUMN_PERCENTAGE)

def parse_ecol(context, token):
	context.out.append("\\end{columns}")

patterns = []
patterns.append((TOKEN_BLAN, None, re.compile("^(\s*)$")))
patterns.append((TOKEN_COMM, None, re.compile("^\s*#\s*(.*)$")))
patterns.append((TOKEN_TITL, parse_titl, re.compile("^\s*titl\s*(.*)\s*$")))
patterns.append((TOKEN_BASH, parse_bash, re.compile("^\s*bash\s*(.*)\s*$")))
patterns.append((TOKEN_TEXT, parse_text, re.compile("^\s*text\s*(.*)\s*$")))
patterns.append((TOKEN_ITEM, parse_item, re.compile("^\s*item\s*(.*)\s*$")))
patterns.append((TOKEN_ITE2, parse_ite2, re.compile("^\s*ite2\s*(.*)\s*$")))
patterns.append((TOKEN_PART, parse_part, re.compile("^\s*part\s*(.*)\s*$")))
patterns.append((TOKEN_CODE, parse_code, re.compile("^\s*code\s*(.*)\s*$")))
patterns.append((TOKEN_GRAP, parse_grap, re.compile("^\s*grap\s*(.*)\s*$")))
patterns.append((TOKEN_COL_, parse_col_, re.compile("^\s*col\s*(.*)\s*$")))
#patterns.append((TOKEN_ERR_, None, re.compile("(.*)")))

def match_token(data):
	for p in patterns:
		(type, func, regex) = p
		m = regex.match(data)
		if m:
			return (type, func, m.group(1))
	# a leading > may be inserted to force leading whitespace
	# (useful for listings environment)
	m = re.match("^\s*[>]?(.*?)\s*$", data)
	return (TOKEN_CONT, func, m.group(1))

def scan(filename):
	tokens = []

	fin = open(filename, "r")
	data = fin.readlines()
	fin.close()

	for d in data:
		tokens.append(match_token(d))
		if tokens[-1][0] == TOKEN_ERR_:
			raise Exception("failed to match token: %s" % tokens[-1][2])

	return tokens

def massage(tokens):
	# insert begin, end tokens
	tokens.insert(0, (TOKEN_BEGI, parse_begi, None))
	tokens.append((TOKEN_END_, parse_end_, None))

	# fix item list
	item_depth = 0
	i = 0
	while tokens[i][0] != TOKEN_END_:
		type = tokens[i][0]
		if type == TOKEN_ITEM:
			if item_depth == 0:
				item_depth = 1
				tokens.insert(i, (TOKEN_BLIS, parse_blis, None))
				i += 1
			elif item_depth == 1:
				pass
			elif item_depth == 2:
				item_depth = 1
				tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
				i += 1
			else:
				raise Exception("unexpected list")
		elif type == TOKEN_ITE2:
			if item_depth == 1:
				item_depth = 2
				tokens.insert(i, (TOKEN_BLIS, parse_blis, None))
				i += 1
			elif item_depth == 2:
				pass
			else:
				raise Exception("unexpected list")
		elif type != TOKEN_CODE and type != TOKEN_BLAN and type != TOKEN_COMM and type != TOKEN_CONT:
			if item_depth == 1:
				item_depth = 0
				tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
				i += 1
			if item_depth == 2:
				item_depth = 0
				tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
				tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
				i += 2
		i += 1
	if item_depth == 1:
		tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
	if item_depth == 2:
		tokens.insert(i, (TOKEN_ELIS, parse_elis, None))
		tokens.insert(i, (TOKEN_ELIS, parse_elis, None))

	# fix columns
	i = 0
	ncols = 0
	while tokens[i][0] != TOKEN_END_:
		type = tokens[i][0]
		if type == TOKEN_COL_ and ncols == 0:
			tokens.insert(2, (TOKEN_BCOL, parse_bcol, None))
			tokens.insert(-1, (TOKEN_ECOL, parse_ecol, None))
			i += 1
			ncols += 1
		elif type == TOKEN_COL_:
			raise Exception("multiple columns not supported")
		i += 1

	# fix bash commands
	if enable_bash:
		title = None
		i = 0
		while tokens[i][0] != TOKEN_END_:
			type = tokens[i][0]
			if type == TOKEN_TITL:
				title = get_data(tokens[i])
	
			if type == TOKEN_BASH:
				tokens.insert(i, (TOKEN_END_, parse_end_, None))
				tokens.insert(i + 1, (TOKEN_BEGI, parse_begi, None))
				tokens.insert(i + 2, (TOKEN_TITL, parse_titl,
					"Bash commands (%s)" % title))
				tokens.insert(i + 3, (TOKEN_TEXT, parse_text,
					"\\begin{lstlisting}"))
				i += 4
				while (type == TOKEN_BASH or type == TOKEN_BLAN or type == TOKEN_CONT) and type != TOKEN_END_:
					i += 1
					type = tokens[i][0]
				tokens.insert(i, (TOKEN_TEXT, parse_text, "\\end{lstlisting}"))
			else:
				i += 1

	part = False
	for t in tokens:
		if t[0] == TOKEN_PART:
			part = True
	if part:
		tokens.insert(0, (TOKEN_TEXT, parse_text, "{\\usebackgroundtemplate{\includegraphics[totalheight=0.8\\paperheight, trim=20 0 0 2, clip=true]{background-part}}"))
		tokens.append((TOKEN_TEXT, parse_text, "}"))

	return tokens

def parse(tokens):
	context = Context()
	for t in tokens:
		(type, func, data) = t
		if type == TOKEN_BLAN or type == TOKEN_COMM:
			context.prev_func = None
			continue
		if type == TOKEN_CONT:
			if context.prev_func == None:
				raise Exception("unexpected cont after blank or comment")
			this_func = context.prev_func
		else:
			this_func = func
		this_func(context, t)
		if (this_func != parse_code):
			context.prev_func = this_func
		else:
			context.prev_func = parse_text

	return context.out


def convert(filename, b):
	global enable_bash

	enable_bash = b
	tokens = scan(filename)
	tokens = massage(tokens)
	return parse(tokens)

# vi: noexpandtab ts=4 sw=4
