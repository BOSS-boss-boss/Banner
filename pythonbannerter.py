import os
import subprocess
import time
import random

# Define colors
COLORS = {
    "RED": "\033[1;91m",
    "GREEN": "\033[1;92m",
    "YELLOW": "\033[1;93m",
    "BLUE": "\033[1;94m",
    "MAGENTA": "\033[1;95m",
    "CYAN": "\033[1;96m",
    "WHITE": "\033[1;97m",
    "RESET": "\033[0m"
}

RANDOM_COLOR = random.choice(list(COLORS.values()))

# Display Banner
def show_banner():
    print(RANDOM_COLOR)
    print("   ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗")
    print("   ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗")
    print("   ██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝")
    print("   ██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗")
    print("   ██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║")
    print("   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
    print(COLORS["RESET"])

    print(f"{COLORS['MAGENTA']}      +----------------------------------------+")
    print(f"{COLORS['MAGENTA']}      |{COLORS['YELLOW']} Code   : ★ BOSS ★                   {COLORS['MAGENTA']}|")
    print(f"{COLORS['MAGENTA']}      |{COLORS['YELLOW']} Github : https://github.com/BOSS-boss-boss {COLORS['MAGENTA']}|")
    print(f"{COLORS['MAGENTA']}      |{COLORS['YELLOW']} YouTube: ?                             {COLORS['MAGENTA']}|")
    print(f"{COLORS['MAGENTA']}      +----------------------------------------+{COLORS['RESET']}")

# Function to execute shell commands
def run_command(command):
    subprocess.run(command, shell=True, check=True)

# Install Required Packages
def install_pkg(pkg):
    try:
        subprocess.run(f"command -v {pkg}", shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(f"{COLORS['BLUE']}[*]{COLORS['GREEN']} Installing {pkg}...{COLORS['RESET']}")
        run_command(f"pkg install {pkg} -y")

# Termux Setup
def setup_termux():
    print(f"{COLORS['BLUE']}[*]{COLORS['GREEN']} Updating Termux...{COLORS['RESET']}")
    run_command("pkg update -y && pkg upgrade -y")
    
    packages = ["ruby", "figlet", "toilet", "wget", "boxes", "zsh", "curl", "git"]
    for pkg in packages:
        install_pkg(pkg)
    
    run_command("gem install lolcat")
    print(f"{COLORS['GREEN']}Termux setup complete!{COLORS['RESET']}")

# Install Oh My Zsh
def setup_ohmyzsh():
    if os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
        run_command("rm -rf ~/.oh-my-zsh")

    print(f"{COLORS['BLUE']}[*]{COLORS['GREEN']} Installing Oh My Zsh...{COLORS['RESET']}")
    run_command("git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh")
    print(f"{COLORS['GREEN']}Oh My Zsh installation complete!{COLORS['RESET']}")

# Install Zsh Plugins
def install_plugin(plugin_name, repo_url):
    plugin_path = os.path.expanduser(f"~/.oh-my-zsh/custom/plugins/{plugin_name}")
    if os.path.exists(plugin_path):
        run_command(f"rm -rf {plugin_path}")
    
    print(f"{COLORS['BLUE']}[*]{COLORS['GREEN']} Installing {plugin_name}...{COLORS['RESET']}")
    run_command(f"git clone {repo_url} {plugin_path}")
    print(f"{COLORS['GREEN']}Installation complete!{COLORS['RESET']}")

# Install Figlet Font
def install_figlet():
    font_dir = os.path.expanduser("~/.figlet")
    os.makedirs(font_dir, exist_ok=True)
    os.chdir(font_dir)
    
    print(f"{COLORS['BLUE']}[*]{COLORS['GREEN']} Installing Custom Figlet Font...{COLORS['RESET']}")
    run_command("wget -q 'https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Shadow.flf'")
    
    os.chdir(os.path.expanduser("~"))
    print(f"{COLORS['GREEN']}Custom Figlet Installed!{COLORS['RESET']}")

# Setup Banner
def setup_banner():
    os.system("clear")
    os.system('figlet -f ~/.figlet/ANSI\\ Shadow.flf "BOSS" | boxes -d ansi-heavy | lolcat')
    
    banner_name = input("\033[1;4;95mEnter Banner Name ⟩ \033[0m")
    shell_name = input("\033[1;4;95mEnter Shell Name ⟩ \033[0m")
    
    print("\033[1;32m[✓] Successfully Set Up Banner 😁\033[0m")
    
    with open(os.path.expanduser("~/.zshrc"), "w") as f:
        f.write(f"""
clear
figlet -f ~/.figlet/ANSI\\ Shadow.flf "{banner_name}" | boxes -d ansi-heavy | lolcat
source $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source $HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
echo ""
PROMPT="%F{{green}}┌─[%F{{red}}{shell_name}👹localhost%F{{green}}]─[%F{{blue}}%~%F{{green}}]
%F{{green}}└──► %F{{blue}}❯❯❯ %F{{green}}"
""")

    run_command("chsh -s zsh")
    print(f"{COLORS['GREEN']}Banner Successfully Set Up! Restart Termux.{COLORS['RESET']}")

# Remove Banner
def remove_banner():
    run_command("rm -f ~/.zshrc ~/.bashrc")
    print(f"{COLORS['RED']}Banner Removed Successfully!{COLORS['RESET']}")

# Menu
while True:
    os.system("clear")
    show_banner()
    
    print(f"{RANDOM_COLOR}========================================{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[1] Termux Setup{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[2] Install Oh My Zsh{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[3] Install Autosuggestions{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[4] Install Syntax Highlighting{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[5] Install Figlet Font{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[6] Setup Banner{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[7] Remove Banner{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[8] Exit{COLORS['RESET']}")
    print(f"{RANDOM_COLOR}========================================{COLORS['RESET']}")

    choice = input("Choose an option: ")

    options = {
        "1": setup_termux,
        "2": setup_ohmyzsh,
        "3": lambda: install_plugin("zsh-autosuggestions", "https://github.com/zsh-users/zsh-autosuggestions"),
        "4": lambda: install_plugin("zsh-syntax-highlighting", "https://github.com/zsh-users/zsh-syntax-highlighting"),
        "5": install_figlet,
        "6": setup_banner,
        "7": remove_banner,
        "8": exit
    }

    if choice in options:
        options[choice]()
    else:
        print(f"{COLORS['RED']}Invalid Option!{COLORS['RESET']}")
        time.sleep(2)

