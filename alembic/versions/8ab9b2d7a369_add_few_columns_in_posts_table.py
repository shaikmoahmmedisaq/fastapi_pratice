"""add few_columns in posts table

Revision ID: 8ab9b2d7a369
Revises: 73ea8947484e
Create Date: 2024-06-11 14:06:29.195002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ab9b2d7a369'
down_revision: Union[str, None] = '73ea8947484e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
