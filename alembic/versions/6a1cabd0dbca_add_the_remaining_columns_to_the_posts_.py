"""add the remaining columns to the posts table

Revision ID: 6a1cabd0dbca
Revises: 55cb45665d37
Create Date: 2026-09-30 22:59:10.663469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a1cabd0dbca'
down_revision: Union[str, Sequence[str], None] = '55cb45665d37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='True'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
