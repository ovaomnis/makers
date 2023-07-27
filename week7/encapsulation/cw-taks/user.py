class User:
    def _create_user(self, email: str, password: str, is_super=False) -> None:
        self.email = email
        self.__password = password
        self.__is_super = is_super

    def create_user(self, email: str, password: str) -> None:
        self._create_user(email, password)

    def create_superuser(self, email: str, password: str) -> None:
        self._create_user(email, password, is_super=True)

    def admin_login(self, email: str, password: str) -> str:
        if self.__is_super:
            if self.__password == password and self.email == email:
                return 'Successfully logged in'
            return 'Can not authorize with such password and email'
        return 'Forbidden'


simple_user = User()
simple_user.create_user('someemail@gmail.com', 'somepass')
superuser_user = User()
superuser_user.create_superuser('super@gmail.com', 'super1234')
print(simple_user.admin_login('someemail@gmail.com', 'somepass'))
print(superuser_user.admin_login('super@gmail.com', 'super1234'))


