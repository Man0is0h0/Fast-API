"""create posts table

Revision ID: e921267a9652
Revises: 
Create Date: 2026-09-30 18:36:59.850359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e921267a9652'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer,nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
