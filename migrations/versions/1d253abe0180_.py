"""empty message

Revision ID: 1d253abe0180
Revises: 46fbcd8a11f6
Create Date: 2020-05-14 14:01:27.136403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d253abe0180'
down_revision = '46fbcd8a11f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('music_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'music_path')
    # ### end Alembic commands ###
