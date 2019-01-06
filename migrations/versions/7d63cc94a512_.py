"""empty message

Revision ID: 7d63cc94a512
Revises: 1bee119f3d48
Create Date: 2018-09-03 10:39:30.888312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d63cc94a512'
down_revision = '1bee119f3d48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('my_web', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'my_web')
    # ### end Alembic commands ###