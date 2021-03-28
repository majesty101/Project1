"""empty message

Revision ID: 8e1f9f429342
Revises: 6d908f825a6c
Create Date: 2021-03-23 19:50:42.035468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1f9f429342'
down_revision = '6d908f825a6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('properties_bathroom_key', 'properties', type_='unique')
    op.drop_constraint('properties_descript_key', 'properties', type_='unique')
    op.drop_constraint('properties_filename_key', 'properties', type_='unique')
    op.drop_constraint('properties_location_key', 'properties', type_='unique')
    op.drop_constraint('properties_price_key', 'properties', type_='unique')
    op.drop_constraint('properties_propertyT_key', 'properties', type_='unique')
    op.drop_constraint('properties_room_key', 'properties', type_='unique')
    op.drop_constraint('properties_title_key', 'properties', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('properties_title_key', 'properties', ['title'])
    op.create_unique_constraint('properties_room_key', 'properties', ['room'])
    op.create_unique_constraint('properties_propertyT_key', 'properties', ['propertyT'])
    op.create_unique_constraint('properties_price_key', 'properties', ['price'])
    op.create_unique_constraint('properties_location_key', 'properties', ['location'])
    op.create_unique_constraint('properties_filename_key', 'properties', ['filename'])
    op.create_unique_constraint('properties_descript_key', 'properties', ['descript'])
    op.create_unique_constraint('properties_bathroom_key', 'properties', ['bathroom'])
    # ### end Alembic commands ###
