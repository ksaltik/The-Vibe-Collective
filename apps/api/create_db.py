import sys
import os

# Fix import path: Add apps/api to sys.path, not apps/api/app
sys.path.append(os.path.join(os.path.dirname(__file__)))

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
        # Create Users
        user1 = User(username="KenanDev", reputation_score=100)
        user2 = User(username="JaneDoe", reputation_score=50)
        user3 = User(username="Pythonista", reputation_score=80)
        db.add_all([user1, user2, user3])
        db.commit()
        db.refresh(user1)
        db.refresh(user2)
        db.refresh(user3)

        # 1. Kenan's FastAPI Rules
        pack1 = VibePack(
            title="FastAPI Production Vibes",
            description="Strict rules for building high-performance APIs.",
            is_public=True,
            owner_id=user1.id
        )
        db.add(pack1)
        db.commit()
        db.refresh(pack1)

        db.add(Rule(
            content="Use Pydantic V2",
            explanation="V1 is deprecated and slower.",
            rule_type="Instruction",
            tags="Syntax,Performance",
            pack_id=pack1.id,
            votes=452
        ))
        db.add(Rule(
            content="Do NOT use generic try/except",
            explanation="It hides critical DB connection errors.",
            rule_type="Anti-Pattern",
            pack_id=pack1.id
        ))
        db.add(Term(
            name="Lifespan",
            definition_raw="Context manager for startup/shutdown events.",
            definition_personal="Use this instead of on_event startup.",
            pack_id=pack1.id
        ))

        # 2. Modern React Anti-Patterns
        pack2 = VibePack(
            title="Modern React Anti-Patterns",
            description="Common mistakes in Next.js 14 and React 18.",
            is_public=True,
            owner_id=user2.id
        )
        db.add(pack2)
        db.commit()
        db.refresh(pack2)

        db.add(Rule(
            content="Do not use useEffect for data fetching",
            explanation="Use Server Components or React Query instead.",
            rule_type="Anti-Pattern",
            pack_id=pack2.id,
            votes=320
        ))
        db.add(Rule(
            content="Use clsx and tailwind-merge",
            explanation="For conditional classes in Shadcn components.",
            rule_type="Instruction",
            tags="CSS,UI",
            pack_id=pack2.id
        ))
        db.add(Term(
            name="Hydration Error",
            definition_raw="Mismatch between server-rendered HTML and client-side DOM.",
            definition_personal="Usually caused by random numbers or dates generated during render.",
            pack_id=pack2.id
        ))

        # 3. Generic Python Data Science
        pack3 = VibePack(
            title="Generic Python Data Science",
            description="Standard practices for Pandas and NumPy.",
            is_public=True,
            owner_id=user3.id
        )
        db.add(pack3)
        db.commit()
        db.refresh(pack3)

        db.add(Rule(
            content="Use vectorized operations",
            explanation="Avoid loops in Pandas for better performance.",
            rule_type="Instruction",
            tags="Performance,Pandas",
            pack_id=pack3.id,
            votes=150
        ))
        db.add(Term(
            name="Broadcasting",
            definition_raw="How NumPy treats arrays with different shapes during arithmetic operations.",
            definition_personal="Magic way to multiply big arrays without loops.",
            pack_id=pack3.id
        ))

        db.commit()

        # Forking test
        print("Testing forking...")
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
            type_label = "[VIBE]" if rule.rule_type == "Instruction" else "[ANTI]"
            print(f"  -> {type_label} {rule.content} ({rule.explanation})")

    db.close()

if __name__ == "__main__":
    main()
