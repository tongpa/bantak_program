from tg import expose

@expose('datacenter.templates.little_partial')
def something(name):
    return dict(name=name)