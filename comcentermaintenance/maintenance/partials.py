from tg import expose

@expose('maintenance.templates.little_partial')
def something(name):
    return dict(name=name)