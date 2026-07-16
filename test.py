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


class TUIRenderer:
    def __init__(self, term):
        self.term = term

    def _get_center_coords(self, text_len: int) -> tuple:
        return ((self.term.width - text_len) // 2, self.term.height // 2)

    def draw_stats(self, wpm, accuracy) -> None:
        print(
            self.term.move_xy(0, 0) + f"WPM: {wpm} Accuracy: {accuracy}",
            end="",
            flush=True,
        )

    def draw_typing_screen(self, target_text: str, user_input: str) -> None:
        output_str = ""
        # Выносим расчет координат из цикла для производительности
        x, y = self._get_center_coords(len(target_text))

        for i in range(len(target_text)):
            if i < len(user_input):
                if target_text[i] == user_input[i]:
                    output_str += self.term.green(target_text[i])
                else:
                    if target_text[i] == " ":
                        symb = "_"
                    else:
                        symb = target_text[i]
                    output_str += self.term.red(symb)
            elif i == len(user_input):
                output_str += self.term.reverse(target_text[i])
            else:
                output_str += self.term.dim(target_text[i])

        # Сначала "затираем" старую строку пробелами, затем пишем новую поверх
        wipe_str = " " * len(target_text)
        print(
            self.term.move_xy(x, y) + wipe_str + self.term.move_xy(x, y) + output_str,
            end="",
            flush=True,
        )


if __name__ == "__main__":
    import time

    print("Starting Interactive UI test...")
    time.sleep(1)

    try:
        with TUIContext() as term:
            # Входим в режим cbreak, чтобы перехватывать ввод без эха в консоль
            with term.cbreak():
                renderer = TUIRenderer(term)

                # Чистим экран один раз перед циклом
                print(term.clear, end="")

                target = "hello world"
                typed = ""

                while True:
                    # Рисуем актуальное состояние
                    renderer.draw_stats(wpm=72.5, accuracy=96.4)
                    renderer.draw_typing_screen(target, typed)

                    # Ждем нажатия клавиши
                    key = term.inkey()

                    # 1. Выход по кнопке ESC
                    if key.name == "KEY_ESCAPE":
                        break

                    # 2. Обработка Backspace (разные терминалы шлют разные коды, проверяем все)
                    elif key.name in ("KEY_BACKSPACE", "KEY_DELETE") or key == "\x7f":
                        if len(typed) > 0:
                            typed = typed[:-1]

                    # 3. Если это обычный символ и мы еще не заполнили всю строку
                    elif not key.is_sequence and key != "" and len(typed) < len(target):
                        typed += key

    except Exception as e:
        print(f"Test crashed with error: {e}")

    print("Returned to normal shell. Terminal state restored successfully!")
