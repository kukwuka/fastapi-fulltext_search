"""first

Revision ID: 6d7649736e75
Revises: 
Create Date: 2021-01-22 20:06:25.727909

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import types


# revision identifiers, used by Alembic.
revision = '6d7649736e75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=True),
    sa.Column('content', sa.UnicodeText(), nullable=True),
    sa.Column('search_vector', types.ts_vector.TSVectorType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('text')
    # ### end Alembic commands ###
