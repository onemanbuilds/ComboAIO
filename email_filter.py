from helpers import _clear,_setTitle,_printText,_readFile,colors
from threading import Thread,active_count
from time import sleep
from os import path,mkdir

class EmailFilter:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [EmailFilter]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                               ╔═╗╔╦╗╔═╗╦╦  ╔═╗╦╦ ╔╦╗╔═╗╦═╗
                                               ║╣ ║║║╠═╣║║  ╠╣ ║║  ║ ║╣ ╠╦╝
                                               ╚═╝╩ ╩╩ ╩╩╩═╝╚  ╩╩═╝╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combos = combos

        self.providers = _readFile('[EmailFilter]/providers.txt','r')
        self.threads = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Threads:{colors["lpurple"]} '))
        print('')

    def _createFolder(self,foldername):
        try:
            if not path.exists(foldername):
                mkdir(foldername)
        except FileExistsError:
            pass
        

    def _emailFilter(self,combo:str):
        email = combo.split(':')[0]
        if '@' in email:
            for provider in self.providers:
                if provider in email:
                    self._createFolder(f'[EmailFilter]/[{provider}]')
                    with open(f'[EmailFilter]/[{provider}]/{provider}.txt','a',encoding='utf8') as f:
                        f.write(f'{combo}\n')
        else:
            _printText(colors['red'],colors['lpurple'],'ERROR',f'Invalid format {email}!')

    def _start(self):
        threads = []
        for combo in self.combos:
            run = True
            while run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._emailFilter,args=(combo,))
                    threads.append(thread)
                    thread.start()
                    run = False

        for x in threads:
            x.join()

        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')