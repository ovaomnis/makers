class UserInitial:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def check_pass(self, username: str, password: str):
        return self.username == username and self.password == password


class SocialMedia(UserInitial):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.posts = 0

    def post(self, username: str, password: str):
        if self.check_pass(username, password):
            self.posts += 1
            return 'Successfully created'
        return 'You have no permission'


class TikTok(SocialMedia):
    def post_post(self, username: str, password: str):
        super().post(username, password)


class Instagram(SocialMedia):
    def post_post(self, username: str, password: str):
        super().post(username, password)

