from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create hotels table
    op.create_table(
        'hotels',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('location', sa.String(), nullable=False)
    )

    # Create bookings table
    op.create_table(
        'bookings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('guest_name', sa.String(), nullable=False),
        sa.Column('hotel_id', sa.Integer(), sa.ForeignKey('hotels.id'))
    )

def downgrade():
    # Drop bookings table
    op.drop_table('bookings')

    # Drop hotels table
    op.drop_table('hotels')
