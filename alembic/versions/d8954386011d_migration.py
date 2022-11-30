"""migration

Revision ID: d8954386011d
Revises: 
Create Date: 2022-11-30 06:20:01.837975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8954386011d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('roles',))
    roles_table_tbl = sa.Table('roles', meta)
    op.bulk_insert(roles_table_tbl, [
        {
            'id': 1,
            'name': 'Грузчик'
        },
        {
            'id': 2,
            'name': 'Дворник'
        }
    ])

    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger(), primary_key=True),
        sa.Column('fio', sa.Text()),
        sa.Column('datar', sa.Date()),
        sa.Column('id_role', sa.Integer(), sa.ForeignKey('roles.id'))
    )


def downgrade():
    op.drop_table('roles')
    op.drop_table('users')
