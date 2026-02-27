#/ IMPOSTAZION DI SISTEMA

# Forza i colori per i comandi di base
alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Disegna il prompt a colori (Verde per utente@host, Blu per il percorso)
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '


#/  MY ALIAS ---------
alias ..='cd ..'
alias bprofile='vi ~/.bash_profile'
alias uni='cd /Users/simonecudia/Uni/'
alias juni='cd /Users/simonecudia/Uni/FI_2/'
alias py='python3'
alias .='cd /Users/simonecudia/Rabbit'
alias p='.; cd Programs/'
alias compileJavaFX='javac --module-path $PATH_TO_FX --add-modules javafx.controls'
alias runJavaFX='java --module-path $PATH_TO_FX --add-modules javafx.controls'
alias oll='cd /Users/simonecudia/Rabbit/eclipse/eclipse-workspace/.Ollare/src'
alias ls='ls -G'
alias run='/Users/simonecudia/Rabbit/Programs/C++/Physics/Physics/build/debug/main'
#Programs
alias tree='py /Users/simonecudia/Rabbit/Programs/Python/tree/tree.py'
alias snake='py /Users/simonecudia/Rabbit/Programs/Python/snake/snake.py'
alias cerca='py /Users/simonecudia/Rabbit/Programs/Python/cerca/cerca.py'
alias op='open'

#/  MY PATH ---------

export PATH=/opt/homebrew/bin:$PATH
export PATH_TO_FX=/Library/Java/JavaVirtualMachines/myjdk16_with_fx/lib
export PATH=/Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin:$PATH
export PATH=/Users/simonecudia/Rabbit/Programs/Graphic/Processing/Processing.app/Contents/MacOS:$PATH
export PATH="/usr/local/opt/llvm/bin:$PATH"
export IMPORT=/Users/simonecudia/Rabbit/Programs/C++/box/OpenVX-sample-impl/include
export JAVA_HOME=/Library/Java/JavaVirtualMachines/myjdk16_with_fx
