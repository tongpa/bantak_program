from tg import expose

@expose('project.templates.little_partial')
def something(name):
    return dict(name=name)