from users.models import User


def __user_level(username, num):
    user = User.objects.get(username=username)
    user.is_level += num
    if user.is_level > user.next_level:
        user.is_level -= user.next_level
        user.next_level = int(user.next_level / 100 * 110)
    user.save()
