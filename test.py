from blessed import Terminal

term = Terminal()
with term.fullscreen(), term.cbreak():
    print("Нажимай любые клавиши. Esc для выхода.")
    # Курсор пользователя находится где-то в центре экрана
    # Курсор временно переместился в левый верхний угол
    # При выходе из контекста курсор автоматически возвращается на свое исходное место!

    while True:
        # Ждем клавишу 50 мс
        val = term.inkey(timeout=0.05)

        long_text = (
            "Очень длинный текст, который мы хотим красиво отобразить на экране..."
        )
        wrapped_lines = term.wrap(
            long_text, width=40
        )  # Заворачиваем в колонку шириной 40
        for line in wrapped_lines:
            print(line)
        if val:
            if val.is_sequence:
                print(f"Системная клавиша: {val.name}")
                if val.name == "KEY_ESCAPE":
                    break
            else:
                print(f"Обычный символ: {val}")
            with term.location(140, 0):
                print("WPM: 70 | ACC: 98%")
