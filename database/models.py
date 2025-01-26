from sqlalchemy import String, ForeignKey, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, create_async_engine


engine = create_async_engine(url="sqlite+aiosqlite:///db_user.sqlite3")
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25))
    balance: Mapped[int] = mapped_column()

class Transaction(Base):
    __tablename__ = 'transaction'

    id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    add: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(String(25))
    time: Mapped[int] = mapped_column()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)