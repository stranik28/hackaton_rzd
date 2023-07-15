from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from sqlalchemy.sql import Select

class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_all(self, query: Select) -> list[Any]:
        result = await self._session.execute(query)
        return result.scalars().all()
    
    async def first(self, query: Select) -> Any:
        result = await self._session.execute(query)
        return result.first()