"""add content column to post table

Revision ID: 772b01cea083
Revises: d8ca685889a5
Create Date: 2024-06-07 14:41:26.454508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '772b01cea083'
down_revision: Union[str, None] = 'd8ca685889a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
