


def is_dream_flower(n):
    dream_flower = ""
    for a in range(n):
        music = ""
        for i in range (13):
            if i <= 8:
                music += "とんで"
            elif 8 < i <= 11:
                music += "まわって"
            else:
                music += "まわる"
        dream_flower += music + "\n"
    return dream_flower

print(is_dream_flower(3))