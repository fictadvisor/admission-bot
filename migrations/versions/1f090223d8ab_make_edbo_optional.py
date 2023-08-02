"""Make edbo optional

Revision ID: 1f090223d8ab
Revises: ebb2adfc3c0b
Create Date: 2023-08-02 01:12:08.100020

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1f090223d8ab'
down_revision = 'ebb2adfc3c0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'printed_edbo',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'printed_edbo',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    # ### end Alembic commands ###