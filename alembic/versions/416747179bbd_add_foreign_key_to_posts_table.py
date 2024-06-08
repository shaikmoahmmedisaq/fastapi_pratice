"""add foreign-key to posts table

Revision ID: 416747179bbd
Revises: f76222f523c2
Create Date: 2024-06-07 15:51:02.854402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '416747179bbd'
down_revision: Union[str, None] = 'f76222f523c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='posts',referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCAdE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts")
    op.add_column('posts','owner_id')
    pass
