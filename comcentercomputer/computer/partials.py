from tg import expose

@expose('computer.templates.little_partial')
def something(name):
    return dict(name=name)