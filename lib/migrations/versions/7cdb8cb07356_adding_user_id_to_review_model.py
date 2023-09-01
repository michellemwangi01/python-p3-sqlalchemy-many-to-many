"""adding user_id to review model

Revision ID: 7cdb8cb07356
Revises: dd26d6f514a2
Create Date: 2023-09-01 12:27:53.810967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cdb8cb07356'
down_revision = 'dd26d6f514a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game_users', schema=None) as batch_op:
        batch_op.alter_column('game_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))

    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))

    with op.batch_alter_table('game_users', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('game_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###