from ui import TUIContext, TUIRenderer
from engine import StatsTracker, WordGenerator


def run_loop():
    word_gen = WordGenerator()
    stats = StatsTracker()

    target = word_gen.generate_text_block("en_1000", 10)
    typed = ""
    all_time = 0
    with TUIContext() as term:
        print(term.clear, end="", flush=True)
        renderer = TUIRenderer(term)

        with term.cbreak():
            while True:
                renderer.draw_stats(wpm=stats.wpm, accuracy=stats.accuracy)
                renderer.draw_typing_screen(target, typed)

                if len(typed) == len(target):
                    stats.stop()

                    print(term.clear, end="", flush=True)
                    renderer.draw_final_stats(
                        wpm=stats.wpm, accuracy=stats.accuracy, time=round(all_time, 2)
                    )
                    while True:
                        key = term.inkey()
                        if key == "KEY_ESCAPE":
                            break
                    break
                key = term.inkey(timeout=0.05)
                all_time += 0.05
                if not key:
                    continue

                if key.name == "KEY_ESCAPE":
                    break

                elif key.name in ("KEY_BACKSPACE", "KEY_DELETE") or key == "\x7f":
                    if len(typed) > 0:
                        typed = typed[:-1]

                elif not key.is_sequence and key != "":
                    try:
                        target_char = target[len(typed)]
                    except IndexError:
                        pass
                    stats.register_keystroke(target_char, key)

                    typed += key


if __name__ == "__main__":
    run_loop()
