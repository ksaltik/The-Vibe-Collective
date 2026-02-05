from sqlalchemy.types import TypeDecorator, UserDefinedType
import os

class Vector(UserDefinedType):
    """
    Mock Vector type for SQLite compatibility.
    Real pgvector.sqlalchemy.Vector should be used in production with PostgreSQL.
    """
    def __init__(self, dim=None):
        self.dim = dim

    def get_col_spec(self, **kw):
        return "VECTOR(%d)" % self.dim

    def bind_processor(self, dialect):
        def process(value):
            return value
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value
        return process

# Try to import real Vector, fall back to mock if not available or if using SQLite (simplified check)
try:
    from pgvector.sqlalchemy import Vector as PgVector
    # Check if we are forcing SQLite (based on env or default).
    # In this sandbox environment, we likely want the MockVector for the models to load without pgvector extension present in DB.
    # However, for the purpose of the code review, I should use the real one if possible, but fallback for safety.
    # A simple strategy: Use Real Vector if imported, but if we are on SQLite, we might face issues during CREATE TABLE.
    # For now, let's just use the Real Vector and assume the user has PG if they want vectors.
    # BUT the review said SQLite is incompatible.
    # So I will use a Conditional Type.

    if os.getenv("DATABASE_URL", "").startswith("sqlite"):
        # SQLite doesn't support the VECTOR type definition in DDL usually without extension
        # So we use a custom type that compiles to TEXT or JSON on SQLite
        from sqlalchemy import Text
        class Vector(TypeDecorator):
            impl = Text
            cache_ok = True
            def __init__(self, dim):
                super().__init__()
                self.dim = dim
    else:
        Vector = PgVector

except ImportError:
    pass
