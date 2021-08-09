from helpers import _clear,_setTitle,_printText,_readFile,_getCurrentTime,colors

class Combiner:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [Combiner]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                                  ╔═╗╔═╗╔╦╗╔╗ ╦╔╗╔╔═╗╦═╗
                                                  ║  ║ ║║║║╠╩╗║║║║║╣ ╠╦╝
                                                  ╚═╝╚═╝╩ ╩╚═╝╩╝╚╝╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combos = combos

    def _combine(self):
        user_email_path = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}User/email list path:{colors["lpurple"]} '))
        password_path = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Password list path:{colors["lpurple"]} '))
        print('')

        user_email_list = _readFile(user_email_path,'r')
        password_list = _readFile(password_path,'r')

        for i in range(len(user_email_list)):
            for j in range(len(password_list)):
                if len(user_email_list[i]) == 0 or len(password_list[j]) == 0:
                    _printText(colors['red'],colors['lpurple'],'ERROR','User/email list or password list empty!')
                    break
                else:
                    new_line = f'{user_email_list[i]}:{password_list[j]}'
                    with open(f'[Combiner]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                        f.write(f'{new_line}\n')

        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _start(self):
        self._combine()