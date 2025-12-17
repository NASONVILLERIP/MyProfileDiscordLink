github_profile = {
    "name": "Swiper",
    "discord_link": "https://discord.gg/your-discord-invite",
    "other_links": [
        "https://twitter.com/yourprofile",
        "https://linkedin.com/in/yourprofile",
        "https://yourblog.com",
        "https://portfolio.com",
        "https://stackoverflow.com/users/yourid"
    ],
    "friends": ["Alice", "Bob", "Charlie", "Diana"],
    "programming_language": "C++"
}

def print_line(char="=", length=60):
    print(char * length)

def display_profile(profile):
    print_line()
    print(f"Swipers Profile")
    print_line()
    print()
    
    print("About Me:")
    print(f"   Hello, I'm Swiper, I code on C++. Add my dc AKA M4tt3rz (only accepts on that acc)
    print("   I coded this all, welp")
    print()
    
    print_line("-")
    print("🔗 Connect with Me:")
    print(f"   🎮 Discord: {profile['discord_link']}")
    for i, link in enumerate(profile["other_links"], 1):
        print(f"   🌐 Link {i}: {link}")
    print_line("-")
    
    print()
    print("🤝 My Awesome Friends:")
    for friend in profile["friends"]:
        print(f"   ⭐ {friend}")
    print()
    
    print_line()
    print("Something random about me:")
    print("   I use C++ for coding, and I'm a gtag modder.")
    print()
    print_line()
    print("I love coding")
    print_line()

if __name__ == "__main__":
    display_profile(github_profile)
