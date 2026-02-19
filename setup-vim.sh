#!/bin/bash

echo "installazione vim/git/curl"
sudo apt update && sudo apt install -y vim git curl

echo "creazione cartella ~/.vim/bundle"
mkdir -p ~/.vim/bundle

echo "git clone Vundle.vim in ~/.vim/bundle/Vundle.vim"
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

echo "copio vimrc in .vimrc"
cp .vimrc ~/.vimrc

echo "installazione di tutti i plugin"
vim +PluginInstall +qall

echo "Setup Vim completato!"
