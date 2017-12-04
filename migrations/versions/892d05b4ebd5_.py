"""empty message

Revision ID: 892d05b4ebd5
Revises: 782188237051
Create Date: 2017-12-04 15:38:42.107105

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '892d05b4ebd5'
down_revision = '782188237051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('done_status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('done_status', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tasks_pkey')
    )
    op.drop_table('todos')
    # ### end Alembic commands ###
