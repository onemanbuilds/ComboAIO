from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class ComboExtractor:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [ComboExtractor]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                      ╔═╗╔═╗╔╦╗╔╗ ╔═╗╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                                      ║  ║ ║║║║╠╩╗║ ║║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
                                      ╚═╝╚═╝╩ ╩╚═╝╚═╝╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)


        self.extracted = 0
        self.combos = combos

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Extractor] ^| EXTRACTED: {self.extracted}')
            sleep(0.4)

    def _extract(self):
        for line in self.combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                new_line = line.split(':')[0]+':'+line.split(':')[1].split()[0]
                with open(f'[ComboExtractor]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.extracted += 1

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        t.join()
        self._extract()