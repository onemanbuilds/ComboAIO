from helpers import _clear,_setTitle,_printText,_getCurrentTime,colors

class DuplicateRemover:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [DuplicateRemover]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                           ╔╦╗╦ ╦╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╦  ╦╔═╗╦═╗
                                            ║║║ ║╠═╝║╣ ╠╦╝║╣ ║║║║ ║╚╗╔╝║╣ ╠╦╝
                                           ═╩╝╚═╝╩  ╚═╝╩╚═╚═╝╩ ╩╚═╝ ╚╝ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combos = combos

    def _duplicateRemove(self):
        cleaned_file = set(self.combos)
        for line in cleaned_file:
            with open(f'[DuplicateRemover]/cleaned_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                f.write(f'{line}\n')
        
        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        self._duplicateRemove()

