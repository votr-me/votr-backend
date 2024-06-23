# # Create the async engine
# engine = create_async_engine(config.DATABASE_URL, echo=config.testing)
# async_session = async_scoped_session(sessionmaker(engine, class_=AsyncSession, expire_on_commit=False), scopefunc=None)

# # Dependency
# async def get_db() -> AsyncGenerator[AsyncSession, None]:
#     """
#     Dependency function that yields db sessions
#     """
#     async with async_session() as session:
#         yield session
