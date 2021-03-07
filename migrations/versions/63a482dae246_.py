"""empty message

Revision ID: 63a482dae246
Revises: 
Create Date: 2021-03-07 11:58:37.517913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63a482dae246'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrator',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('admission', sa.String(length=20), nullable=False),
    sa.Column('birthdate', sa.DateTime(), nullable=False),
    sa.Column('zipcode', sa.String(length=10), nullable=False),
    sa.Column('county', sa.String(length=15), nullable=False),
    sa.Column('ward', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('admission')
    )
    op.create_table('medical_status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.Column('diagnosis', sa.String(length=100), nullable=False),
    sa.Column('underlying', sa.String(length=50), nullable=False),
    sa.Column('drug', sa.String(length=50), nullable=False),
    sa.Column('outcome', sa.String(length=50), nullable=False),
    sa.Column('need_referral', sa.Boolean(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical_status')
    op.drop_table('students')
    op.drop_table('administrator')
    # ### end Alembic commands ###