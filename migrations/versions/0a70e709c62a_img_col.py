"""img col

Revision ID: 0a70e709c62a
Revises: 82df129621dc
Create Date: 2020-07-18 09:23:07.861098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a70e709c62a'
down_revision = '82df129621dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'image_url')
    # ### end Alembic commands ###
