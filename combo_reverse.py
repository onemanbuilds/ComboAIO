from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class ComboReverse:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [ComboReverse]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                          ╔═╗╔═╗╔╦╗╔╗ ╔═╗╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗
                                          ║  ║ ║║║║╠╩╗║ ║╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣ 
                                          ╚═╝╚═╝╩ ╩╚═╝╚═╝╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.reversed = 0
        self.combos = combos

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Reversed] ^| REVERSED: {self.reversed}')
            sleep(0.4)

    def _reverse(self):
        for line in self.combos:
            new_line = line.split(':')[1]+':'+line.split(':')[0]
            with open(f'[ComboReverse]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')
            self.reversed += 1

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._reverse()