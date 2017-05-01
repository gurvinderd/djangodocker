# DB router for app1

class BooksDBRouter(object):
    """
    A router to control pollsapp db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on books models to 'db_pollsapp'"
        from django.conf import settings
        if not settings.DATABASES.has_key('books'):
            return None
        if model._meta.app_label == 'books':
            return 'books_db'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on books models to 'pollsapp_db'"
        from django.conf import settings
        if not settings.DATABASES.has_key('books'):
            return None
        if model._meta.app_label == 'books':
            return 'books_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in books is involved"
        from django.conf import settings
        if not settings.DATABASES.has_key('books'):
            return None
        if obj1._meta.app_label == 'books' or obj2._meta.app_label == 'books':
            return True
        return None
def allow_migrate(self, db, app_label, model_name=None, **hints):
        "Allow any relation if a model in books is involved"
        from django.conf import settings
        if app_label == 'books':
            return db == 'books_db'
        return None
        

    def allow_syncdb(self, db, model):
        "Make sure the books app only appears on the 'books' db"
        from django.conf import settings
        if not settings.DATABASES.has_key('books'):
            return None
        if db == 'books_db':
            return model._meta.app_label == 'books'
        elif model._meta.app_label == 'books':
            return False
        return None
