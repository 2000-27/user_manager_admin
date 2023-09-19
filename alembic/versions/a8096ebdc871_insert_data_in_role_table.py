"""insert data in role table

Revision ID: a8096ebdc871
Revises: 5b6b093fbdcd
Create Date: 2023-09-19 16:43:58.545542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8096ebdc871'
down_revision: Union[str, None] = '5b6b093fbdcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.bulk_insert(
    'role',
    [
        {
           "role_name": "Admin",
        },
        {
           "role_name": "Manager",
        },
        {
           "role_name": "User",
        },
    ],  
)
  


def downgrade() -> None:
    op.drop_table('role')
