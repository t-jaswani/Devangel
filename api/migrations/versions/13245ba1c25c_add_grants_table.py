"""Add Grants table

Revision ID: 13245ba1c25c
Revises: 5a212ad480c5
Create Date: 2020-04-17 17:49:40.976216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13245ba1c25c'
down_revision = '5a212ad480c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('deadline', sa.Date(), nullable=False),
    sa.Column('application_link', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grant')
    # ### end Alembic commands ###
