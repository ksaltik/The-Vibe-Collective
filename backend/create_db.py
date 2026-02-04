from app.database import engine, SessionLocal, Base
from app.models import User, VibePack, Rule, Term

def main():
    # Create tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    # Create a session
    db = SessionLocal()

    # Check if data exists
    if db.query(User).count() == 0:
        print("Seeding data...")
        # Create User
        user1 = User(username="KenanDev", reputation_score=100)
        db.add(user1)
        db.commit()
        db.refresh(user1)

        # Create VibePack
        pack1 = VibePack(
            title="Modern FastAPI Production",
            description="Strict rules for building high-performance APIs.",
            is_public=True,
            owner_id=user1.id
        )
        db.add(pack1)
        db.commit()
        db.refresh(pack1)

        # Create Rules
        rule1 = Rule(
            content="Always use typing.Annotated for dependency injection.",
            explanation="Cleaner syntax, better Swagger UI support.",
            rule_type="Constraint",
            pack_id=pack1.id,
            votes=452
        )
        db.add(rule1)

        # Create Term
        term1 = Term(
            name="Lifespan",
            definition_raw="The context manager that handles startup and shutdown logic.",
            definition_personal="Think of this like the __init__ for the whole server.",
            pack_id=pack1.id
        )
        db.add(term1)

        db.commit()

        # Forking test
        print("Testing forking...")
        user2 = User(username="JaneDoe", reputation_score=50)
        db.add(user2)
        db.commit()
        db.refresh(user2)

        forked_pack = VibePack(
            title="Jane's FastAPI",
            description="Forked from KenanDev",
            is_public=False,
            owner_id=user2.id,
            forked_from_id=pack1.id
        )
        db.add(forked_pack)
        db.commit()

        print("Data seeded successfully!")
    else:
        print("Data already exists.")

    # Verification
    print("\n--- Verification ---")
    packs = db.query(VibePack).all()
    for pack in packs:
        print(f"Pack: {pack.title} (Owner: {pack.owner.username})")
        if pack.forked_from:
            print(f"  -> Forked from: {pack.forked_from.title}")
        for rule in pack.rules:
            print(f"  -> Rule: {rule.content[:50]}...")
        for term in pack.terms:
            print(f"  -> Term: {term.name} - {term.definition_personal}")

    db.close()

if __name__ == "__main__":
    main()
