cmd = input()

match cmd:
    case "top" | "Top" | "TOP" | "bottom" | "Bottom" | "BOTTOM" | "right" | "Right" | "RIGHT" | "left" | "Left" | "LEFT":
        print(f"Команда {cmd.lower()}")
    case _:
        print("Неверная команда")
