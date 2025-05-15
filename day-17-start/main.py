class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def __str__(self):
        return f"{self.user_id}: {self.user_name} {self.following} - {self.followers}"

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001","coreyt")
user_2 = User("002", "jack")

user_2.follow(user_1)

print(user_1)
print(user_2)

