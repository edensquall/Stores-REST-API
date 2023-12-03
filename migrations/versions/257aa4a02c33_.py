"""empty message

Revision ID: 257aa4a02c33
Revises: 265687c01f43
Create Date: 2023-12-03 17:25:11.755040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '257aa4a02c33'
down_revision = '265687c01f43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('email', type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
