# DB router for app1

class PollsAppDBRouter(object):
    """
    A router to control pollsapp db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on pollsapp models to 'db_pollsapp'"
        from django.conf import settings
        if not settings.DATABASES.has_key('pollsapp'):
            return None
        if model._meta.app_label == 'pollsapp':
            return 'pollsapp_db'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on pollsapp models to 'pollsapp_db'"
        from django.conf import settings
        if not settings.DATABASES.has_key('pollsapp'):
            return None
        if model._meta.app_label == 'pollsapp':
            return 'pollsapp_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in pollsapp is involved"
        from django.conf import settings
        if not settings.DATABASES.has_key('pollsapp'):
            return None
        if obj1._meta.app_label == 'pollsapp' or obj2._meta.app_label == 'pollsapp':
            return True
        return None
def allow_migrate(self, db, app_label, model_name=None, **hints):
        "Allow any relation if a model in pollsapp is involved"
        from django.conf import settings
        if app_label == 'pollsapp':
            return db == 'pollsapp_db'
        return None
        

    def allow_syncdb(self, db, model):
        "Make sure the pollsapp app only appears on the 'pollsapp' db"
        from django.conf import settings
        if not settings.DATABASES.has_key('pollsapp'):
            return None
        if db == 'pollsapp_db':
            return model._meta.app_label == 'pollsapp'
        elif model._meta.app_label == 'pollsapp':
            return False
        return None
