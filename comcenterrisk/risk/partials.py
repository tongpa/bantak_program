from tg import expose

@expose('risk.templates.little_partial')
def something(name):
    return dict(name=name)