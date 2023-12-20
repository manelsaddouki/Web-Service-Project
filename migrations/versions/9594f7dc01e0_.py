"""empty message

Revision ID: 9594f7dc01e0
Revises: 713952635bec
Create Date: 2023-12-20 13:08:59.663429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9594f7dc01e0'
down_revision = '713952635bec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('funds', schema=None) as batch_op:
        batch_op.alter_column('donation',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    with op.batch_alter_table('funds', schema=None) as batch_op:
        batch_op.alter_column('donation',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###