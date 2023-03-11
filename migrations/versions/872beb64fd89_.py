"""empty message

Revision ID: 872beb64fd89
Revises: 6ecc3b7a0c3d
Create Date: 2023-03-11 23:12:28.254704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872beb64fd89'
down_revision = '6ecc3b7a0c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('uuid', sa.String(length=100), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('administrator')
    op.drop_column('medicalstatus', 'updated')
    op.drop_column('medicalstatus', 'created')
    op.drop_column('students', 'updated')
    op.drop_column('students', 'created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('created', sa.DATETIME(), nullable=True))
    op.add_column('students', sa.Column('updated', sa.DATETIME(), nullable=True))
    op.add_column('medicalstatus', sa.Column('created', sa.DATETIME(), nullable=True))
    op.add_column('medicalstatus', sa.Column('updated', sa.DATETIME(), nullable=True))
    op.create_table('administrator',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('username', sa.VARCHAR(length=15), nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=True),
    sa.Column('updated', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('users')
    # ### end Alembic commands ###