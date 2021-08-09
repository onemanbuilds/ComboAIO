from helpers import _clear,_setTitle,_printText,_findStringBetween,_getRandomUserAgent,_getRandomProxy,colors
from threading import Thread,active_count
from time import sleep
import requests

class Dehash:
    def __init__(self,combos) -> None:
        _setTitle('[ComboAIO] ^| [Dehash]')
        _clear()
        title = colors['lpurple']+"""
                                   ╔════════════════════════════════════════════════╗
                                                    ╔╦╗╔═╗╦ ╦╔═╗╔═╗╦ ╦
                                                     ║║║╣ ╠═╣╠═╣╚═╗╠═╣
                                                    ═╩╝╚═╝╩ ╩╩ ╩╚═╝╩ ╩
                                   ╚════════════════════════════════════════════════╝
        """
        print(title)

        self.dehashed = 0
        self.bads = 0
        self.retries = 0

        self.combos = combos

        self.use_proxy = int(input(f'{colors["lpurple"]}[>] {colors["yellow"]}[1]Proxy [2]Proxyless:{colors["lpurple"]} '))
        self.proxy_type = None
        if self.use_proxy == 1:
            self.proxy_type = int(input(f'{colors["lpurple"]}[>] {colors["yellow"]}[1]Https [2]Socks4 [3]Socks5:{colors["lpurple"]} '))
        self.threads = int(input(f'{colors["lpurple"]}[>] {colors["yellow"]}Threads:{colors["lpurple"]} '))
        self.session = requests.session()
        print('')

    def _titleUpdate(self):
        while True:
            _setTitle(f'[ComboAIO] ^| [Dehash] ^| DEHASHED: {self.dehashed} ^| BAD: {self.bads} ^| RETRIES: {self.retries}')
            sleep(0.4)

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
        t.start()
        threads = []
        for combo in self.combos:
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

        _printText(colors['yellow'],colors['white'],'FINISHED','Process done!')