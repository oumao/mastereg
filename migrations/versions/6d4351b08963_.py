"""empty message

Revision ID: 6d4351b08963
Revises: f3dc9ec7484a
Create Date: 2021-12-01 13:12:09.480497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d4351b08963'
down_revision = 'f3dc9ec7484a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('administrator', sa.Column('created', sa.DateTime(timezone=True), nullable=True))
    op.add_column('administrator', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))
    op.add_column('medicalstatus', sa.Column('created', sa.DateTime(timezone=True), nullable=True))
    op.add_column('medicalstatus', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))
    op.add_column('students', sa.Column('created', sa.DateTime(timezone=True), nullable=True))
    op.add_column('students', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'updated')
    op.drop_column('students', 'created')
    op.drop_column('medicalstatus', 'updated')
    op.drop_column('medicalstatus', 'created')
    op.drop_column('administrator', 'updated')
    op.drop_column('administrator', 'created')
    # ### end Alembic commands ###
