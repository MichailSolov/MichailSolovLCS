import pprint
import vk_api


class VkUser:
    def __init__(self):
        self.session = vk_api.vk_api.VkApi(
            token=input("enter your token: "))

    def user(self):
        return vk_api.vk_api.VkApi.method(self.session, 'users.get', {'user_ids': self.user})[0]["first_name"]

    def mutual_friends(self):
        try:
            users = input("enter users(expm: user1 & user2): ")
            user1 = users.split(' & ')[0]
            user2 = users.split(' & ')[1]
            vk_id_a = vk_api.vk_api.VkApi.method(self.session, 'friends.getMutual',
                                                 {'source_uid': user1, 'target_uid': user2})
            return [str(vk_api.vk_api.VkApi.method(self.session, 'users.get',
                                                   {'user_ids': a})[0]["first_name"])
                    + ' ' +
                    str(vk_api.vk_api.VkApi.method(self.session, 'users.get',
                                                   {'user_ids': a})[0]["last_name"])

                    for a in vk_id_a
                    ]
        except:
            print("please, try to enter data again")


p = VkUser()
pprint.pprint(p.mutual_friends())

