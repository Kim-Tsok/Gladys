def instructions():
    from colorama import init, Fore, Style

    init()

    print("")
    print(f"📘 {Fore.BLUE}Instructions: {Style.RESET_ALL}")
    input(
        "This is a text-based choose-your-own-adventure game made with Python.\n"
        f"Press {Fore.GREEN}ENTER{Style.RESET_ALL} to continue after reading each line."
    )
    input(
        "Most of the time, you do not need to type anything.\n"
        "Just press ENTER to move forward."
    )
    input(
        f"The only time you should type something is when you see a prompt like {Fore.GREEN}(y/n){Style.RESET_ALL}."
    )
    input(
        "Besides prompts, there is also combat.\n"
        "You will always be warned before entering a combat situation."
    )
    input(
        "During combat:\n"
        f"{Fore.GREEN}(a){Style.RESET_ALL} = ATTACK\n"
        f"{Fore.GREEN}(d){Style.RESET_ALL} = DEFEND\n"
        f"{Fore.GREEN}(r){Style.RESET_ALL} = RUN\n"
        "Most battles follow these rules."
    )
    input(
        "Some battles may work differently.\n"
        "Any changes will be explained when they happen."
    )
    input(
        f"Choices are usually shown in brackets, like this {Fore.GREEN}(y/n){Style.RESET_ALL}."
    )
    print("")
    input(f"{Fore.MAGENTA}Enjoy the journey, Gladys. 💀⚔️ {Style.RESET_ALL}")
    print("")
    print("=" * 10)
    print("")
    input("Press Enter to start... ")
    print("")
