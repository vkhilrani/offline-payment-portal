"""Added Wallet Model

Revision ID: 4ff8d47423c0
Revises: 6c9b693c2472
Create Date: 2025-04-04 11:28:26.746084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ff8d47423c0'
down_revision: Union[str, None] = '6c9b693c2472'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
