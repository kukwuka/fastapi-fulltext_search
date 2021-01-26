"""Timezone

Revision ID: b1e980e011a5
Revises: 
Create Date: 2021-01-26 14:56:56.223122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_searchable import sync_trigger
from sqlalchemy_utils import types

# revision identifiers, used by Alembic.
revision = 'b1e980e011a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('text',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('rubrics', sa.UnicodeText(), nullable=True),
                    sa.Column('text', sa.UnicodeText(), nullable=True),
                    sa.Column('search_vector', types.ts_vector.TSVectorType(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    conn = op.get_bind()
    sync_trigger(
        conn,
        'text',
        'search_vector',
        ['text']
    )


def downgrade():
    op.drop_table('text')
