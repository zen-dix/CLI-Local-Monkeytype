import time
from ui import TUIContext


def run_loop():
    with TUIContext() as term:
        with term.cbreak():
            wasted_time = 0.0
            output_line = 4
            while True:
                key = term.inkey(timeout=0.05)

                if key:
                    print(
                        term.move_xy(0, output_line)
                        + term.clear_eol
                        + f"Pressed: {key}",
                        end="",
                        flush=True,
                    )
                    if key.name == "KEY_ESCAPE":
                        break
                else:
                    wasted_time += 0.05
                    print(
                        term.move_xy(0, 2) + f"Waiting... Time: {wasted_time:.2f}s",
                        end="",
                        flush=True,
                    )


if __name__ == "__main__":
    run_loop()
