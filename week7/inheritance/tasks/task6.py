# from typing import List
#
#
# class ContactList(list):
#     def search_by_name(self, search_name: str) -> List[str]:
#         found_list = []
#         for name in self:
#             if name.lower().count(search_name.lower()) >= 1:
#                 found_list.append(name)
#         return found_list
#
#
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))


names = ['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']
find = 'ivan'

found_name = []
for name in names:
    if name.lower().count(find.lower()) >= 1:
        found_name.append(name)
print(found_name)
