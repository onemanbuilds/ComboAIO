from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors

class ComboExtractor:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [ComboExtractor]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                      ╔═╗╔═╗╔╦╗╔╗ ╔═╗╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                                      ║  ║ ║║║║╠╩╗║ ║║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
                                      ╚═╝╚═╝╩ ╩╚═╝╚═╝╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combos = combos

    def _extract(self):
        for line in self.combos:
            new_line = line.split(':')[0]+':'+line.split(':')[1].split()[0]
            with open(f'[ComboExtractor]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')

        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        self._extract()