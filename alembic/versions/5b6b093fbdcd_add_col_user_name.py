"""“add_col_user_name”

Revision ID: 5b6b093fbdcd
Revises: 18ef941f29f7
Create Date: 2023-09-19 11:43:33.151537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b6b093fbdcd'
down_revision: Union[str, None] = '18ef941f29f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('user', sa.add_column('username', sa.String()))
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
  op.drop_column('user', 'username')