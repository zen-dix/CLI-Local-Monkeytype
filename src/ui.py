from blessed import Terminal


class TUIContext:
    def __init__(self):
        self.term = Terminal()

    def __enter__(self):
        print(self.term.enter_fullscreen + self.term.hide_cursor, end="", flush=True)
        return self.term

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.term.normal_cursor + self.term.exit_fullscreen, end="", flush=True)
        if exc_type is KeyboardInterrupt:
            print("\nExit...")
            return True


if __name__ == "__main__":
    # Импортируем time только для теста
    import time

    print("Это обычный экран терминала.")
    time.sleep(1)

    try:
        with TUIContext() as term:
            # Проверяем центрирование текста (из теории)
            test_text = "TUI работает! Ждем 3 секунды..."
            x = (term.width - len(test_text)) // 2
            y = term.height // 2

            print(term.move_xy(x, y) + test_text, flush=True)
            time.sleep(3)

            # Проверяем, что будет при Ctrl+C внутри контекста
            print(
                term.move_xy(x, y + 2) + "А теперь нажми Ctrl+C для теста проверки!",
                flush=True,
            )
            while True:
                time.sleep(0.1)

    except Exception as e:
        print(f"Какая-то другая ошибка: {e}")

    print("Мы успешно вернулись в обычный терминал! История очищена, курсор на месте.")
