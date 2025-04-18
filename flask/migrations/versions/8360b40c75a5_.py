"""empty message

Revision ID: 8360b40c75a5
Revises: 5423f85e40c6
Create Date: 2025-03-25 23:08:22.912215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8360b40c75a5'
down_revision = '5423f85e40c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
