from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors

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

        self.combos = combos
        
    def _watermark(self):
        separator = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Enter the custom separator:{colors["lpurple"]} '))
        author = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Author:{colors["lpurple"]} '))
        print('')

        for line in self.combos:
            new_line = f'{line} {separator} Author: {author}'
            with open(f'[Watermark]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')

        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        self._watermark()