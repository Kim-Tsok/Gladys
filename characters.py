from colorama import init, Fore, Style

init()

# This is to make sure the character names are colored and to not clutter the main file
characters = {
    "player" :f"{Fore.GREEN}You:{Style.RESET_ALL}",
    "-player": "     ",
    "unknown" : f"{Fore.RED}Unknown:{Style.RESET_ALL}",
    "-unknown": "         ",
    "person01" : f"{Fore.BLUE}Person01:{Style.RESET_ALL}",
    "-person01" : "          "
}
