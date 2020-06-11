class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for u in group.get_users():
        if u == user:
            return True
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False

#Test Directory
parent = Group("parent")
child = Group("child")
child_user = "child_user"
parent.add_user(child_user)
child_2 = Group("child_2")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

#Test Case 1
# print(is_user_in_group("child_user", parent))
#expected--> True

#Test Case 2
#print(is_user_in_group("sub_child_user", parent))
#expected--> True

#Test Case 3
#print(is_user_in_group("sub_child_user", sub_child))
#expected--> True

#Test Case 4
# print(is_user_in_group("child_user", sub_child))
#expected--> False

#Test Case 5
#print(is_user_in_group("sub_child_user4", parent))
#expected--> False

#Test Case 6
#print(is_user_in_group("", parent))
#expected--> False

#Test Case 7
# parent2 = Group("parent2")
# print(is_user_in_group("sub_child_user", parent2))
#expected--> False