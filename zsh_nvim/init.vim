set encoding=utf-8
set fileencoding=utf-8
syntax on

set noerrorbells
set noswapfile
set nu
set nuw=4
set updatetime=50
set nohlsearch
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nowrap
set incsearch
set showcmd
set laststatus=2 

set number relativenumber

filetype plugin indent on   





"------ PLUGINS -------
" ... (tutte le tue impostazioni iniziali come set nu, set tabstop, ecc.) ...

if !exists('g:vscode')
    "------ PLUGINS -------"
    call plug#begin('~/.local/share/nvim/plugged')
    Plug 'preservim/NERDTree'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'morhetz/gruvbox',
    Plug 'machakann/vim-colorscheme-imas'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes' " Opzionale, per cambiare i colori
    Plug 'olimorris/onedarkpro.nvim'
    call plug#end()


endif

"---------------------------------------------------
" (Da qui in giù lasci tutte le tue mappature nnoremap, inoremap jk, ecc.)
" --- SCELTA TEMA IN BASE A MACOS ---
" Interroga il Mac per sapere se la Dark Mode è attiva

let s:macos_theme = system('defaults read -g AppleInterfaceStyle 2>/dev/null')

" Se la stringa restituita contiene la parola 'Dark'
if s:macos_theme =~? 'Dark'
    set background=dark
    colorscheme gruvbox
else
    " Altrimenti il Mac è in modalità chiara
    set background=light
    
    " Se usi gruvbox, impostare background=light cambierà i colori in automatico.
    " Oppure puoi scrivere il nome di un tema completamente diverso, es:
    " colorscheme vim-material
    colorscheme imas
endif
" -----------------------------------




"---------------------------------------------------
"
let mapleader = " "

" Disabilita il movimento in avanti dello spazio (No Operation)
nnoremap <Space> <Nop>
vnoremap <Space> <Nop>

if !exists('g:vscode')
    "---------------------------------------------------
    " --- 1. COMANDI DI "TAGLIA" ---

    nnoremap x "_x

    nnoremap dw "_dw

    nnoremap dd "_dd

    nnoremap D "_D

    " --- 1a. VERSIONI PER MODALITÀ VISUALE ---

    vnoremap x "_x

    vnoremap D "_D
    "---------------------------------------------------
    " --- 2. COMANDI DI CANCELLAZIONE 'PULITA' (Usando il Leader) ---

    nnoremap <leader>x +x

    nnoremap <leader>dw dw

    nnoremap <leader>dd dd

    nnoremap <leader>D D

    " --- 2a. VERSIONI PER MODALITÀ VISUALE ---
    " Se selezioni del testo e premi Leader + d, lo elimina senza sovrascrivere gli appunti
    vnoremap <leader>x x

    vnoremap <leader>D D
endif


"---------------------------------------------------
"------ INSERT MODE -----
inoremap jk <ESC>



"---------------------------------------------------
"------ NORMAL MODE -----
nnoremap <C-j> 3j
nnoremap <C-k> 3k

nnoremap <leader>w :w<CR>


"---------------------------------------------------
"------ NORMAL MODE -----
nnoremap <C-d> <C-d>zz


" Mantieni la selezione in Visual mode dopo aver indentato
vnoremap < <gv
vnoremap > >gv

"non dover digitare due volte < o >
nnoremap < <<
nnoremap > >>
