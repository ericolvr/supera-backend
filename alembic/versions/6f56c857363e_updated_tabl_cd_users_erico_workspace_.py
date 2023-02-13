"""updated tabl cd /Users/erico/workspace/supera/backend ; /usr/bin/env /Users/erico/.pyenv/versions/3.8.12/bin/python /Users/erico/.vscode/extensions/ms-python.python-2023.2.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 51007 -- -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload 

Revision ID: 6f56c857363e
Revises: 7d6b97e5d46b
Create Date: 2023-02-12 11:26:17.783234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f56c857363e'
down_revision = '7d6b97e5d46b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('subtotal', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('cart', sa.Column('total', sa.Numeric(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'total')
    op.drop_column('cart', 'subtotal')
    # ### end Alembic commands ###