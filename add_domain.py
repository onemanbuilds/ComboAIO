from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors
from threading import Thread
from time import sleep

class AddDomain:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [AddDomain]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                                ╔═╗╔╦╗╔╦╗╔╦╗╔═╗╔╦╗╔═╗╦╔╗╔
                                                ╠═╣ ║║ ║║ ║║║ ║║║║╠═╣║║║║
                                                ╩ ╩═╩╝═╩╝═╩╝╚═╝╩ ╩╩ ╩╩╝╚╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.added = 0

        self.combos = combos
        
    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [AddDomain] ^| ADDED: {self.added}')
            sleep(0.4)

    def _domain(self):
        domain = str(input(f'{colors["lpurple"]}[>] {colors["yellow"]}Domain:{colors["lpurple"]} '))

        if '@' in domain:
            domain = domain
        else:
            domain = '@'+domain

        for line in self.combos:
            new_line = line.split(':')[0]+domain+':'+line.split(':')[1]
            with open(f'[AddDomain]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')
            self.added += 1

        print('')
        _printText(colors['yellow'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self._domain()