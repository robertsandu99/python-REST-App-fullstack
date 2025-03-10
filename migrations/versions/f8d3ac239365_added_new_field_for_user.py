"""added new field for user

Revision ID: f8d3ac239365
Revises: 28b5ee1a6f28
Create Date: 2025-02-11 21:35:29.628224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8d3ac239365'
down_revision: Union[str, None] = '28b5ee1a6f28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('teams_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'teams', ['teams_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'teams_id')
    # ### end Alembic commands ###
