"""add coontent column to posts table

Revision ID: 3bc936d77226
Revises: e921267a9652
Create Date: 2026-09-30 20:52:29.391566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bc936d77226'
down_revision: Union[str, Sequence[str], None] = 'e921267a9652'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    """Downgrade schema."""
    pass
