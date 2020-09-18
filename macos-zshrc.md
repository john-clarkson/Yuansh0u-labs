# macOS zshrc
```sh 
## If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/hi1ler/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes

# powerlevel9k THEME:agnoster or robbyrussell
ZSH_THEME="powerlevel9k/powerlevel9k"
# hide (user@hostname)
DEFAULT_USER=`id -un`
# icon fonts
POWERLEVEL9K_MODE='nerdfont-complete'
# command line 
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir dir_writable vcs) 
# <= left prompt setting to "dir"
# command line 
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status time)


POWERLEVEL9K_PROMPT_ON_NEWLINE=true
# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh" || true

# Add Visual Studio Code (code) and golang
export PATH="/Applications/Visual Studio Code.app/Contents/Resources/app/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin"

# POWERLEVEL9K_MODE='awesome-fontconfig'
# POWERLEVEL9K_PROMPT_ON_NEWLINE=true
# POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="%{%F{249}%}\u250f"
# POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="%{%F{249}%}\u2517%{%F{default}%} "
# POWERLEVEL9K_SHORTEN_DIR_LENGTH=4
# POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
# POWERLEVEL9K_OS_ICON_BACKGROUND="white"
# POWERLEVEL9K_OS_ICON_FOREGROUND="red"
# POWERLEVEL9K_TODO_BACKGROUND="black"
# POWERLEVEL9K_TODO_FOREGROUND="249"
# POWERLEVEL9K_DIR_HOME_BACKGROUND="black"
# POWERLEVEL9K_DIR_HOME_FOREGROUND="green"
# POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND="black"
# POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="249"
# POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="black"
# POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="249"
# POWERLEVEL9K_STATUS_OK_BACKGROUND="black"
# POWERLEVEL9K_STATUS_OK_FOREGROUND="green"
# POWERLEVEL9K_STATUS_ERROR_BACKGROUND="black"
# POWERLEVEL9K_STATUS_ERROR_FOREGROUND="red"
# POWERLEVEL9K_NVM_BACKGROUND="black"
# POWERLEVEL9K_NVM_FOREGROUND="249"
# POWERLEVEL9K_NVM_VISUAL_IDENTIFIER_COLOR="green"
# POWERLEVEL9K_RVM_BACKGROUND="black"
# POWERLEVEL9K_RVM_FOREGROUND="249"
# POWERLEVEL9K_RVM_VISUAL_IDENTIFIER_COLOR="red"
# POWERLEVEL9K_LOAD_CRITICAL_BACKGROUND="black"
# POWERLEVEL9K_LOAD_WARNING_BACKGROUND="black"
# POWERLEVEL9K_LOAD_NORMAL_BACKGROUND="black"
# POWERLEVEL9K_LOAD_CRITICAL_FOREGROUND="249"
# POWERLEVEL9K_LOAD_WARNING_FOREGROUND="249"
# POWERLEVEL9K_LOAD_NORMAL_FOREGROUND="249"
# POWERLEVEL9K_LOAD_CRITICAL_VISUAL_IDENTIFIER_COLOR="red"
# POWERLEVEL9K_LOAD_WARNING_VISUAL_IDENTIFIER_COLOR="yellow"
# POWERLEVEL9K_LOAD_NORMAL_VISUAL_IDENTIFIER_COLOR="green"
# POWERLEVEL9K_RAM_BACKGROUND="black"
# POWERLEVEL9K_RAM_FOREGROUND="249"
# POWERLEVEL9K_RAM_ELEMENTS=(ram_free)
# POWERLEVEL9K_BATTERY_LOW_BACKGROUND="black"
# POWERLEVEL9K_BATTERY_CHARGING_BACKGROUND="black"
# POWERLEVEL9K_BATTERY_CHARGED_BACKGROUND="black"
# POWERLEVEL9K_BATTERY_DISCONNECTED_BACKGROUND="black"
# POWERLEVEL9K_BATTERY_LOW_FOREGROUND="249"
# POWERLEVEL9K_BATTERY_CHARGING_FOREGROUND="249"
# POWERLEVEL9K_BATTERY_CHARGED_FOREGROUND="249"
# POWERLEVEL9K_BATTERY_DISCONNECTED_FOREGROUND="249"
# POWERLEVEL9K_BATTERY_LOW_VISUAL_IDENTIFIER_COLOR="red"
# POWERLEVEL9K_BATTERY_CHARGING_VISUAL_IDENTIFIER_COLOR="yellow"
# POWERLEVEL9K_BATTERY_CHARGED_VISUAL_IDENTIFIER_COLOR="green"
# POWERLEVEL9K_BATTERY_DISCONNECTED_VISUAL_IDENTIFIER_COLOR="249"
# POWERLEVEL9K_TIME_BACKGROUND="black"
# POWERLEVEL9K_TIME_FOREGROUND="249"
# POWERLEVEL9K_TIME_FORMAT="%D{%H:%M:%S} \UE12E"
# POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=('status' 'os_icon' 'todo' 'context' 'dir' 'vcs')
# POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=('nvm' 'rvm' 'load' 'ram_joined' 'battery' 'time')
# 

```
## Watch this
![](https://i.imgur.com/Ub0ruaw.png)

### Have coding fun!