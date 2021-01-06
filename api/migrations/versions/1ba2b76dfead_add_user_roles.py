"""Add user roles

Revision ID: 1ba2b76dfead
Revises: 3d0d38c44cd5
Create Date: 2020-04-27 15:31:46.235979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ba2b76dfead'
down_revision = '3d0d38c44cd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('roles', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'roles')
    # ### end Alembic commands ###