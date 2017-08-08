from tg import expose

@expose('questionaires.templates.little_partial')
def something(name):
    return dict(name=name)