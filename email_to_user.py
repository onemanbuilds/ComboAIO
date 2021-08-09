from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class EmailToUser:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [EmailToUser]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                              ╔═╗╔╦╗╔═╗╦╦ ╔╦╗╔═╗╦ ╦╔═╗╔═╗╦═╗
                                              ║╣ ║║║╠═╣║║  ║ ║ ║║ ║╚═╗║╣ ╠╦╝
                                              ╚═╝╩ ╩╩ ╩╩╩═╝╩ ╚═╝╚═╝╚═╝╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)


        self.converted = 0

        self.combos = combos

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [EmailToUser] ^| CONVERTED: {self.converted}')
            sleep(0.4)

    def _emailToUser(self):
        for line in self.combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            elif '@' not in line.split(':')[0]:
                _printText(colors['red'],colors['white'],'ERROR','Please use email combo instead of user!')
                break
            else:
                new_line = line.split(':')[0].split('@')[0]+':'+line.split(':')[1]
                with open(f'[EmailToUser]/user_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.converted += 1

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._emailToUser()