"""added user_email as a foreign key in order table

Revision ID: ac637b9b8ae7
Revises: 348c39df6119
Create Date: 2024-05-30 13:15:11.065325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac637b9b8ae7'
down_revision = '348c39df6119'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_email', sa.String(), nullable=True))
        batch_op.drop_constraint('fk_existing_constraint_name', type_='foreignkey')  # Replace 'fk_existing_constraint_name' with the actual constraint name
        batch_op.create_foreign_key('fk_order_user_email', 'user', ['user_email'], ['email'])
        batch_op.drop_column('user_id')

def downgrade():
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint('fk_existing_constraint_name', type_='foreignkey')  # Replace 'fk_existing_constraint_name' with the actual constraint name
        batch_op.create_foreign_key('fk_order_user_id', 'user', ['user_id'], ['id'])
        batch_op.drop_column('user_email')

    # ### end Alembic commands ###
