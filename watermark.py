from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class Watermark:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [Watermark]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                               ╦ ╦╔═╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╦═╗╦╔═
                                               ║║║╠═╣ ║ ║╣ ╠╦╝║║║╠═╣╠╦╝╠╩╗
                                               ╚╩╝╩ ╩ ╩ ╚═╝╩╚═╩ ╩╩ ╩╩╚═╩ ╩
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.added = 0

        self.combos = combos
        
    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Watermark] ^| ADDED: {self.added}')
            sleep(0.4)

    def _watermark(self):
        separator = str(input(f'{colors["white"]}[>] {colors["yellow"]}Enter the custom separator:{colors["white"]} '))
        author = str(input(f'{colors["white"]}[>] {colors["yellow"]}Author:{colors["white"]} '))
        print('')

        for line in self.combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                new_line = f'{line} {separator} Author: {author}'
                with open(f'[Watermark]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.added += 1

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._watermark()