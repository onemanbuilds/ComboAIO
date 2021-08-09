from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class EmailExtractor:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [EmailExtractor]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                        ╔═╗╔╦╗╔═╗╦╦  ╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                                        ║╣ ║║║╠═╣║║  ║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
                                        ╚═╝╩ ╩╩ ╩╩╩═╝╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)


        self.extracted = 0

        self.combos = combos

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [EmailExtractor] ^| EXTRACTED: {self.extracted}')
            sleep(0.4)

    def _emailExtract(self):
        for line in self.combos:
            new_line = line.split(':')[0]
            with open(f'[EmailExtractor]/email_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')
            self.extracted += 1

        print('')
        _printText(colors['yellow'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._emailExtract()