from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class Watermark:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [Watermark]')
        _clear()
        title = colors['lpurple']+"""
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
        separator = str(input(f'{colors["lpurple"]}[>] {colors["yellow"]}Enter the custom separator:{colors["lpurple"]} '))
        author = str(input(f'{colors["lpurple"]}[>] {colors["yellow"]}Author:{colors["lpurple"]} '))
        print('')

        for line in self.combos:
            new_line = f'{line} {separator} Author: {author}'
            with open(f'[Watermark]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')
            self.added += 1

        print('')
        _printText(colors['yellow'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._watermark()