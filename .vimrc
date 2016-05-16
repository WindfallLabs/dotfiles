syntax on
set ff=dos
set fileformats=dos
set textwidth=79
set tabstop=8
set expandtab
set softtabstop=4
set shiftwidth=4
filetype indent on
set encoding=utf-8

" Copy the template text to clipboard; paste with P
autocmd VimEnter * !cat /h/templates/PY_TEMPLATE.txt > /dev/clipboard
nnoremap <silent> <F5> :!clear;python %<CR>
