"""Create phone number for user

Revision ID: fc1b0e88b30a
Revises: 
Create Date: 2026-05-29 13:50:24.566031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = 'fc1b0e88b30a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#alembic init alembic
#alembic revision -m " "

#alembic upgrade (revision id)/head
def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))

#alembic downgrade -1
def downgrade() -> None:
    op.drop_column('users','phone_number')
    
#Reverting the
