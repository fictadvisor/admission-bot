"""Added study

Revision ID: 022e4ccc401b
Revises: 106ade32a9f4
Create Date: 2023-08-05 21:04:51.255866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '022e4ccc401b'
down_revision = '106ade32a9f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('queue_users', sa.Column('study_form', sa.String(), server_default='Денна', nullable=False))
    op.add_column('queue_users', sa.Column('study_type', sa.String(), server_default='Бюджет', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('queue_users', 'study_type')
    op.drop_column('queue_users', 'study_form')
    # ### end Alembic commands ###
