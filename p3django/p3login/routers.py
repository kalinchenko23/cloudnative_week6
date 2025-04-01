class SimpleRouter:
    """
    A router to control all database operations and ensure read queries go to replicas.
    """
    
    def db_for_read(self, model, **hints):
        """Directs read queries to the replica database."""
        return 'replica' 
        
    def db_for_write(self, model, **hints):
        """Directs write queries to the primary database."""
        return 'default' 

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensures migrations are only applied to the primary database."""
        return db == 'default'