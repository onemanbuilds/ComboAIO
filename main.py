from helpers import _clear,_setTitle,_printText,_readFile,_getCurrentTime,_findStringBetween,_getRandomUserAgent,_getRandomProxy,colors
from threading import Thread,active_count
from time import sleep
from os import mkdir,path
import requests

combos = _readFile('combos.txt','r')

class Main:
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
        options = ['AddDomain','Combiner','ComboExtractor','ComboReverse','Dehash','DuplicateRemover','EmailExtractor','EmailFilter','EmailToUser','Watermark']
        counter = 0
        for option in options:
            counter+=1
            _printText(colors['green'],colors['white'],str(counter),option)
        print('')

        selected = int(input(f'{colors["white"]}[>] {colors["yellow"]}Select something:{colors["white"]} '))

        if selected == 1:
            AddDomain()._start()
            sleep(2)
            self._menu()
        elif selected == 2:
            Combiner()._start()
            sleep(2)
            self._menu()
        elif selected == 3:
            ComboExtractor()._start()
            sleep(2)
            self._menu()
        elif selected == 4:
            ComboReverse()._start()
            sleep(2)
            self._menu()
        elif selected == 5:
            Dehash()._start()
            sleep(2)
            self._menu()
        elif selected == 6:
            DuplicateRemover()._start()
            sleep(2)
            self._menu()
        elif selected == 7:
            EmailExtractor()._start()
            sleep(2)
            self._menu()
        elif selected == 8:
            EmailFilter()._start()
            sleep(2)
            self._menu()
        elif selected == 9:
            EmailToUser()._start()
            sleep(2)
            self._menu()
        elif selected == 10:
            Watermark()._start()
            sleep(2)
            self._menu()
        else:
            Watermark()._start()
            sleep(2)
            self._menu()

class AddDomain:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [AddDomain]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                ╔═╗╔╦╗╔╦╗╔╦╗╔═╗╔╦╗╔═╗╦╔╗╔
                                                ╠═╣ ║║ ║║ ║║║ ║║║║╠═╣║║║║
                                                ╩ ╩═╩╝═╩╝═╩╝╚═╝╩ ╩╩ ╩╩╝╚╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False
        self.added = 0
        
    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [AddDomain] ^| ADDED: {self.added}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _domain(self):
        domain = str(input(f'{colors["white"]}[>] {colors["yellow"]}Domain:{colors["white"]} '))

        if '@' in domain:
            domain = domain
        else:
            domain = '@'+domain

        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            elif '@' in line.split(':')[0]:
                _printText(colors['red'],colors['white'],'ERROR','Please use user combo instead of email!')
                break
            else:
                new_line = line.split(':')[0]+domain+':'+line.split(':')[1]
                with open(f'[AddDomain]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.added += 1
                _printText(colors['green'],colors['white'],'AddDomain',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._domain()

class Combiner:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [Combiner]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                  ╔═╗╔═╗╔╦╗╔╗ ╦╔╗╔╔═╗╦═╗
                                                  ║  ║ ║║║║╠╩╗║║║║║╣ ╠╦╝
                                                  ╚═╝╚═╝╩ ╩╚═╝╩╝╚╝╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False
        self.combined = 0
        
    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Combiner] ^| COMBINED: {self.combined}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _combine(self):
        user_email_path = str(input(f'{colors["white"]}[>] {colors["yellow"]}User/email list path:{colors["white"]} '))
        password_path = str(input(f'{colors["white"]}[>] {colors["yellow"]}Password list path:{colors["white"]} '))
        print('')

        user_email_list = _readFile(user_email_path,'r')
        password_list = _readFile(password_path,'r')

        for i in range(len(user_email_list)):
            for j in range(len(password_list)):
                if len(user_email_list[i]) == 0 or len(password_list[j]) == 0:
                    _printText(colors['red'],colors['white'],'ERROR','User/email list or password list empty!')
                    break
                else:
                    new_line = f'{user_email_list[i]}:{password_list[j]}'
                    with open(f'[Combiner]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                        f.write(f'{new_line}\n')
                    self.combined += 1
                    _printText(colors['green'],colors['white'],'Combine',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._combine()

class Dehash:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [Dehash]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                                    ╔╦╗╔═╗╦ ╦╔═╗╔═╗╦ ╦
                                                     ║║║╣ ╠═╣╠═╣╚═╗╠═╣
                                                    ═╩╝╚═╝╩ ╩╩ ╩╚═╝╩ ╩
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False

        self.dehashed = 0
        self.bads = 0
        self.retries = 0

        self.use_proxy = int(input(f'{colors["white"]}[>] {colors["yellow"]}Proxy -> [1]Proxy/[2]Proxyless:{colors["white"]} '))
        self.proxy_type = int(input(f'{colors["white"]}[>] {colors["yellow"]}ProxyType -> [1]Https/[2]Socks4/[3]Socks5:{colors["white"]} '))
        self.threads = int(input(f'{colors["white"]}[>] {colors["yellow"]}Threads:{colors["white"]} '))
        self.session = requests.session()
        print('')

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Dehash] ^| DEHASHED: {self.dehashed} ^| BAD: {self.bads} ^| RETRIES: {self.retries}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _dehash(self,user,hash):
        useragent = _getRandomUserAgent('[Dehash]/useragents.txt')

        headers = {'User-Agent':useragent}

        proxy = _getRandomProxy(self.use_proxy,self.proxy_type,'[Dehash]/proxies.txt')

        try:
            response = self.session.get(f'https://hashtoolkit.com/decrypt-hash/?hash={hash}',headers=headers,proxies=proxy)

            result = _findStringBetween(response.text,'<h1 class="res-header">Hashes for: <code>','</code></h1>')

            if result != None and '<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="' not in result:
                self.dehashed += 1
                _printText(colors['green'],colors['white'],'HIT',f'{user}:{result}')
                with open('[Dehash]/hits.txt','a',encoding='utf8') as f:
                    f.write(f'{user}:{result}\n')
            else:
                self.bads += 1
                _printText(colors['green'],colors['white'],'BAD',f'{user}:{hash}')
                with open('[Dehash]/bads.txt','a',encoding='utf8') as f:
                    f.write(f'{user}:{result}\n')
        except Exception:
            self.retries += 1
            self._dehash(user,hash)

    def _start(self):
        t = Thread(target=self._titleUpdate)
        threads = []
        for combo in combos:
            Run = True
            
            user = combo.split(':')[0]
            hash = combo.split(':')[1]

            while Run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._dehash,args=(user,hash))
                    threads.append(thread)
                    thread.start()
                    Run = False

        for x in threads:
            x.join()

        t.start()
        self.stop_thread = True
        t.join()

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

class DuplicateRemover:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [DuplicateRemover]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                           ╔╦╗╦ ╦╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╦  ╦╔═╗╦═╗
                                            ║║║ ║╠═╝║╣ ╠╦╝║╣ ║║║║ ║╚╗╔╝║╣ ╠╦╝
                                           ═╩╝╚═╝╩  ╚═╝╩╚═╚═╝╩ ╩╚═╝ ╚╝ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

    def _duplicateRemove(self):
        cleaned_file = set(combos)
        for line in cleaned_file:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                with open(f'[DuplicateRemover]/cleaned_{_getCurrentTime()}.txt','w',encoding='utf8') as f:
                    f.write(f'{line}\n')
        
        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        self._duplicateRemove()

class EmailExtractor:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [EmailExtractor]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                        ╔═╗╔╦╗╔═╗╦╦  ╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                                        ║╣ ║║║╠═╣║║  ║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
                                        ╚═╝╩ ╩╩ ╩╩╩═╝╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False

        self.extracted = 0

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [EmailExtractor] ^| EXTRACTED: {self.extracted}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _emailExtract(self):
        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            elif '@' not in line.split(':')[0]:
                _printText(colors['red'],colors['white'],'ERROR','Please use email combo instead of user!')
                break
            else:
                new_line = line.split(':')[0]
                with open(f'[EmailExtractor]/email_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.extracted += 1
                _printText(colors['green'],colors['white'],'EmailExtractor',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._emailExtract()

class EmailFilter:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [EmailFilter]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                               ╔═╗╔╦╗╔═╗╦╦  ╔═╗╦╦ ╔╦╗╔═╗╦═╗
                                               ║╣ ║║║╠═╣║║  ╠╣ ║║  ║ ║╣ ╠╦╝
                                               ╚═╝╩ ╩╩ ╩╩╩═╝╚  ╩╩═╝╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)
        self.stop_thread = False

        self.filtered = 0

        self.providers = _readFile('[EmailFilter]/providers.txt','r')
        self.threads = int(input(f'{colors["white"]}[>] {colors["yellow"]}Threads:{colors["white"]} '))
        print('')

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [EmailFilter] ^| FILTERED: {self.filtered}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _createFolder(self,foldername):
        if not path.exists(foldername):
            mkdir(foldername)
        else:    
            _printText(colors['red'],colors['white'],'ERROR',f'{foldername} already exists!')

    def _emailFilter(self,combo:str):
        email = combo.split(':')[0]
        if '@' in email:
            for provider in self.providers:
                if provider in email:
                    self._createFolder(f'[EmailFilter]/[{provider}]')
                    with open(f'[EmailFilter]/[{provider}]/{provider}.txt','a',encoding='utf8') as f:
                        f.write(f'{combo}\n')
        else:
            _printText(colors['red'],colors['white'],'ERROR',f'Invalid format {email}!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        threads = []
        for combo in combos:
            Run = True
            while Run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._emailFilter,args=(combo,))
                    threads.append(thread)
                    thread.start()
                    Run = False

        for x in threads:
            x.join()

        t.start()
        self.stop_thread = True
        t.join()

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

class EmailToUser:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [EmailToUser]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                              ╔═╗╔╦╗╔═╗╦╦ ╔╦╗╔═╗╦ ╦╔═╗╔═╗╦═╗
                                              ║╣ ║║║╠═╣║║  ║ ║ ║║ ║╚═╗║╣ ╠╦╝
                                              ╚═╝╩ ╩╩ ╩╩╩═╝╩ ╚═╝╚═╝╚═╝╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False

        self.converted = 0

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [EmailToUser] ^| CONVERTED: {self.converted}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _emailToUser(self):
        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            elif '@' not in line.split(':')[0]:
                _printText(colors['red'],colors['white'],'ERROR','Please use email combo instead of user!')
                break
            else:
                new_line = line.split(':')[0].split('@')[0]+':'+line.split(':')[1]
                with open(f'[EmailToUser]/user_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.converted += 1
                _printText(colors['green'],colors['white'],'EmailToUser',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._emailToUser()

class ComboExtractor:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [ComboExtractor]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                      ╔═╗╔═╗╔╦╗╔╗ ╔═╗╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                                      ║  ║ ║║║║╠╩╗║ ║║╣ ╔╩╦╝ ║ ╠╦╝╠═╣║   ║ ║ ║╠╦╝
                                      ╚═╝╚═╝╩ ╩╚═╝╚═╝╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.stop_thread = False

        self.extracted = 0

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Extractor] ^| EXTRACTED: {self.extracted}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _extract(self):
        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                new_line = line.split(':')[0]+':'+line.split(':')[1].split()[0]
                with open(f'[ComboExtractor]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.extracted += 1
                _printText(colors['green'],colors['white'],'ComboExtractor',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._extract()

class ComboReverse:
    def __init__(self) -> None:
        _setTitle('[ComboAIO] ^| [ComboReverse]')
        _clear()
        title = colors['white']+"""
                                   ╔════════════════════════════════════════════════╗
                                          ╔═╗╔═╗╔╦╗╔╗ ╔═╗╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗
                                          ║  ║ ║║║║╠╩╗║ ║╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣ 
                                          ╚═╝╚═╝╩ ╩╚═╝╚═╝╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)
        self.stop_thread = False

        self.reversed = 0

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Reversed] ^| REVERSED: {self.reversed}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _reverse(self):
        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                new_line = line.split(':')[1]+':'+line.split(':')[0]
                with open(f'[ComboReverse]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.reversed += 1
                _printText(colors['green'],colors['white'],'ComboExtractor',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._reverse()

class Watermark:
    def __init__(self) -> None:
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
        self.stop_thread = False

        self.added = 0
        
    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Watermark] ^| ADDED: {self.added}')
            sleep(0.4)
            if self.stop_thread == True:
                break

    def _watermark(self):
        separator = str(input(f'{colors["white"]}[>] {colors["yellow"]}Enter the custom separator:{colors["white"]} '))
        author = str(input(f'{colors["white"]}[>] {colors["yellow"]}Author:{colors["white"]} '))
        print('')

        for line in combos:
            if len(line.split(':')) != 2:
                _printText(colors['red'],colors['white'],'ERROR','Invalid format!')
                break
            else:
                new_line = f'{line} {separator} Author: {author}'
                with open(f'[Watermark]/combo_{_getCurrentTime()}.txt','a',encoding='utf8') as f:
                    f.write(f'{new_line}\n')
                self.added += 1
                _printText(colors['green'],colors['white'],'ADDED',new_line)

        print('')
        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')

    def _start(self):
        t = Thread(target=self._titleUpdate)
        t.start()
        self.stop_thread = True
        t.join()
        self._watermark()

if __name__ == '__main__':
    Main()._menu()