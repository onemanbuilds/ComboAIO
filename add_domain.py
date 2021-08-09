from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors

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

        self.combos = combos
        
    def _domain(self):
        domain = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Domain:{colors["lpurple"]} '))

        if '@' in domain:
            domain = domain
        else:
            domain = '@'+domain

        for line in self.combos:
            new_line = line.split(':')[0]+domain+':'+line.split(':')[1]
            with open(f'[AddDomain]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{new_line}\n')

        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        self._domain()