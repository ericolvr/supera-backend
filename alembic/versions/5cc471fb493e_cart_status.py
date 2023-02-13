"""cart status

Revision ID: 5cc471fb493e
Revises: fa0c6adbb0bf
Create Date: 2023-02-10 11:49:32.170188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cc471fb493e'
down_revision = 'fa0c6adbb0bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('status', sa.Enum('UNPROCESSED', 'PROCESSED', name='enumstatus'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'status')
    # ### end Alembic commands ###