class PrivateProject:
    __github_link = 'https://github.com/ovaomnis/makers'
    __developers = ['ovaomnis', 'aitenir', 'illiga', 'dinayim', 'jasmin', 'deamon', 'ardager']

    def __init__(self, username):
        self.username = username

    @property
    def github_link(self):
        if self.username.lower() in self.__developers:
            return self.__github_link
        return "Forbidden"


ovaomnis = PrivateProject('ovaomnis')
print(ovaomnis.github_link)
ovamori = PrivateProject('ovaomori')
print(ovamori.github_link)


