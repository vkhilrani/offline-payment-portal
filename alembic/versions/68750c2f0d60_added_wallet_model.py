"""Added wallet model

Revision ID: 68750c2f0d60
Revises: 4ff8d47423c0
Create Date: 2025-04-04 11:55:47.168602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68750c2f0d60'
down_revision: Union[str, None] = '4ff8d47423c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
