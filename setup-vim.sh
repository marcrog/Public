#!/bin/bash

# 1. Installa Vim e Git se non presenti (utile per VM nuove)
echo "Aggiornamento pacchetti e installazione Vim/Git..."
sudo apt update && sudo apt install -y vim git curl

# 2. Crea le directory necessarie per Vundle
echo "Configurazione directory per Vundle..."
mkdir -p ~/.vim/bundle

# 3. Scarica Vundle se non esiste giÃ 
if [ ! -d "$HOME/.vim/bundle/Vundle.vim" ]; then
    echo "Clonazione di Vundle..."
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim [cite: 1]
else
    echo "Vundle giÃ  presente."
fi

# 4. Copia il tuo file vimrc nella Home
# Nota: Assicurati che il file si chiami 'vimrc' nella cartella corrente
cp vimrc ~/.vimrc

# 5. Installa i plugin specificati nel vimrc in modalitÃ  "silent"
echo "Installazione dei plugin di Vim (NERDTree, Gruvbox, ecc.)..."
vim +PluginInstall +qall 

echo "Setup completato! Ora puoi aprire Vim."
