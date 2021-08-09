from helpers import _clear,_setTitle,_printText,_readFile,_getCurrentTime,colors
from threading import Thread
from time import sleep

class Combiner:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [Combiner]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                  ╔═╗╔═╗╔╦╗╔╗ ╦╔╗╔╔═╗╦═╗
                                                  ║  ║ ║║║║╠╩╗║║║║║╣ ╠╦╝
                                                  ╚═╝╚═╝╩ ╩╚═╝╩╝╚╝╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combined = 0
        self.combos = combos

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Combiner] ^| COMBINED: {self.combined}')
            sleep(0.4)

    def _combine(self):
        user_email_path = str(input(f'{colors["white"]}[>] {colors["yellow"]}User/email list path:{colors["white"]} '))
        password_path = str(input(f'{colors["white"]}[>] {colors["yellow"]}Password list path:{colors["white"]} '))
        print('')

        user_email_list = _readFile(user_email_path,'r')
        password_list = _readFile(password_path,'r')

        for i in range(len(user_email_list)):
            for j in range(len(password_list)):
                if len(user_email_list[i]) == 0 or len(password_list[j]) == 0:
                    _printText(colors['red'],colors['white'],'ERROR','User/email list or password list empty!')
                    break
                else:
                    new_line = f'{user_email_list[i]}:{password_list[j]}'
                    with open(f'[Combiner]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                        f.write(f'{new_line}\n')
                    self.combined += 1

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._combine()