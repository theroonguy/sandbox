"""new fields in user model

Revision ID: 499408602dd4
Revises: d80dcc77914b
Create Date: 2019-07-09 10:09:13.147562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '499408602dd4'
down_revision = 'd80dcc77914b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
