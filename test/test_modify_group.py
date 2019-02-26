from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Second", header="AAAAA", footer="BBBBB"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
