nmap <space> :source tpp.vim<cr>:w<cr>:make preview<cr>

syn match basicLanguageKeywords "^[ \t]*grap[ \t]"
syn match basicLanguageKeywords "^[ \t]*item[ \t]"
syn match basicLanguageKeywords "^[ \t]*ite2[ \t]"
syn match basicLanguageKeywords "^[ \t]*text[ \t]"
syn match basicLanguageKeywords "^[ \t]*part[ \t]"
syn match basicLanguageKeywords "^[ \t]*bash[ \t]"
hi def link basicLanguageKeywords Statement

"syn region slidesCode start="code" end="$"
"hi def link slidesCode Constant

syn region slidesCode matchgroup=basicLanguageKeywords start="^[ \t]*code[ \t]" end="$"
syn region slidesCode matchgroup=basicLanguageKeywords start="^[ \t]*titl[ \t]" end="$"
syn region slidesCode matchgroup=basicLanguageKeywords start="^[ \t]*bash[ \t]" end="$"
hi def link slidesCode Constant

syn match slidesColumn "^[ \t]*col[ \t]*"
hi def link slidesColumn PreProc
"syn region slidesColumn matchgroup=basicLanguageKeywords start="^[ \t]*col[ \t]*$" end="\%$"
"hi def link slidesColumn Error

syn match slidesComment "^[ \t]*#.*"
hi def link slidesComment Comment

set noexpandtab
set sw=5
set ts=5

"au BufNewFile,BufRead *.tpp so tpp.vim
