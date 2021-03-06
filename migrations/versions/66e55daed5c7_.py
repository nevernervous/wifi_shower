"""empty message

Revision ID: 66e55daed5c7
Revises: 
Create Date: 2018-11-03 06:28:56.532913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66e55daed5c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mac_id', sa.String(length=255), nullable=False),
    sa.Column('secret_key', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('sold_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mac_id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(length=255), nullable=False),
    sa.Column('preheat_cycle', sa.Float(), nullable=True),
    sa.Column('shower_cycle', sa.Float(), nullable=True),
    sa.Column('shower_temp', sa.Float(), nullable=True),
    sa.Column('old_shower_habits', sa.Float(), nullable=True),
    sa.Column('water_used', sa.Float(), nullable=True),
    sa.Column('water_saved', sa.Float(), nullable=True),
    sa.Column('challenge_level', sa.Float(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('last_shower_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('showering_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('shower_mode', sa.Integer(), nullable=True),
    sa.Column('preheat_cycle', sa.Float(), nullable=True),
    sa.Column('shower_cycle', sa.Float(), nullable=True),
    sa.Column('old_shower_habits', sa.Float(), nullable=True),
    sa.Column('water_used', sa.Float(), nullable=True),
    sa.Column('water_saved', sa.Float(), nullable=True),
    sa.Column('shower_temp', sa.Float(), nullable=True),
    sa.Column('mixing_temp', sa.Float(), nullable=True),
    sa.Column('challenge_level', sa.Float(), nullable=True),
    sa.Column('aggregate_water_used', sa.Float(), nullable=True),
    sa.Column('average_water_used', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('showering_data')
    op.drop_table('profile')
    op.drop_table('device')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
