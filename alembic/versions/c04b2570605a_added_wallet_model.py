"""Added wallet model

Revision ID: c04b2570605a
Revises: 68750c2f0d60
Create Date: 2025-04-04 19:34:39.023846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c04b2570605a'
down_revision: Union[str, None] = '68750c2f0d60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
