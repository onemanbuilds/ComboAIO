from helpers import _clear,_setTitle,_printText,_readFile,colors
from add_domain import AddDomain
from combiner import Combiner
from combo_extractor import ComboExtractor
from combo_reverse import ComboReverse
from dehash import Dehash
from duplicate import DuplicateRemover
from email_extractor import EmailExtractor
from email_filter import EmailFilter
from email_to_user import EmailToUser
from watermark import Watermark
from time import sleep

class Menu:
    def __init__(self) -> None:
        _setTitle('[ComboAIO]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                  ╔═╗╔═╗╔╦╗╔╗ ╔═╗╔═╗╦╔═╗
                                                  ║  ║ ║║║║╠╩╗║ ║╠═╣║║ ║
                                                  ╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩╩╚═╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

    def _menu(self):        
        _setTitle('[ComboAIO] ^| [Menu]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                      ╔╦╗╔═╗╔╗╔╦ ╦
                                                      ║║║║╣ ║║║║ ║
                                                      ╩ ╩╚═╝╝╚╝╚═╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.combos = _readFile('combos.txt','r')

        options = ['AddDomain','Combiner','ComboExtractor','ComboReverse','Dehash','DuplicateRemover','EmailExtractor','EmailFilter','EmailToUser','Watermark']
        counter = 0
        for option in options:
            counter+=1
            _printText(colors['green'],colors['white'],str(counter),option)
        print('')

        selected = int(input(f'{colors["white"]}[>] {colors["yellow"]}Select something:{colors["white"]} '))

        if selected == 1:
            AddDomain(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 2:
            Combiner(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 3:
            ComboExtractor(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 4:
            ComboReverse(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 5:
            Dehash(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 6:
            DuplicateRemover(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 7:
            EmailExtractor(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 8:
            EmailFilter(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 9:
            EmailToUser(self.combos)._start()
            sleep(2)
            self._menu()
        elif selected == 10:
            Watermark(self.combos)._start()
            sleep(2)
            self._menu()
        else:
            Watermark(self.combos)._start()
            sleep(2)
            self._menu()