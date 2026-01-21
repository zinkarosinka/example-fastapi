"""add content column to post table

Revision ID: 97ba60236312
Revises: 64cec2bac920
Create Date: 2026-01-19 20:09:27.611571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97ba60236312'
down_revision: Union[str, Sequence[str], None] = '64cec2bac920'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", 'content')
    pass
