#!/bin/bash

echo "installazione nvim/curl"
sudo apt update && sudo apt install -y neovim curl

echo "creazione albero ~/.config"
mkdir -p ~/.config/nvim 
mkdir -p ~/.config/nvim/plugged
mkdir -p ~/.config/nvim/autoload

echo "copio init.vim in ~/.config/nvim"
cp init.vim ~/.config/nvim/init.vim

echo "scarico vim-plug da github e sposto plug.vim nella directoy autoload"
sh -c 'curl -fLo ~/.config/nvim/autoload/plug.vim  \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

echo "installazione di tutti i plugin"
nvim --headless +PlugInstall +qa

echo "Setup NeoVim completato!"
