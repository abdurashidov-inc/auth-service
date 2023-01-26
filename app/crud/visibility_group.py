# # Native # #

# # Installed # #
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload

# # Package # #
from app.schemas.visibility_group import IVisibilityGroupCreate, IVisibilityGroupUpdate
from app.crud.base_sqlmodel import CRUDBase
from app.models.visibility_group import Visibility_Group


class CRUDVisibilityGroup(CRUDBase[Visibility_Group, IVisibilityGroupCreate, IVisibilityGroupUpdate]):
    async def get_visibility_group_by_prefix(self, db_session: AsyncSession, *, prefix: str) -> Visibility_Group:
        visibility_group = await db_session.exec(select(Visibility_Group).where(Visibility_Group.prefix == prefix))
        return visibility_group.first()

    async def get_visibility_group_and_users(self, db_session: AsyncSession) -> Visibility_Group:
        visibility_group = await db_session.exec(select(Visibility_Group).options(selectinload(Visibility_Group.user)))
        return visibility_group.all()


visibility_group = CRUDVisibilityGroup(Visibility_Group)