def contacts():
    with open('templates/contacts.html') as template:
        return template.read()


def about():
    with open('templates/about.html') as template:
        return template.read()
