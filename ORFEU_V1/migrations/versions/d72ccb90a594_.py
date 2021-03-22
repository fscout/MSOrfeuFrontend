"""empty message

Revision ID: d72ccb90a594
Revises: 
Create Date: 2021-03-21 21:50:45.851480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd72ccb90a594'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('categoria_produto', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('categoria_produto')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('marca_produto', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('marca_produto')
    )
    op.create_table('medida',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('medida_produto', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('medida_produto')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_usuario', sa.String(length=20), nullable=False),
    sa.Column('senha_usuario', sa.String(length=128), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('nivel_acesso', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('nome_usuario')
    )
    op.create_table('produto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cod_barras', sa.String(length=13), nullable=False),
    sa.Column('descricao_prod', sa.String(length=40), nullable=False),
    sa.Column('quant_prod', sa.Integer(), nullable=False),
    sa.Column('quant_min', sa.Integer(), nullable=True),
    sa.Column('quant_max', sa.Integer(), nullable=True),
    sa.Column('preco_custo', sa.Float(precision=2), nullable=False),
    sa.Column('preco_venda', sa.Float(precision=2), nullable=False),
    sa.Column('id_categoria_id', sa.Integer(), nullable=True),
    sa.Column('id_marca_id', sa.Integer(), nullable=True),
    sa.Column('id_medida_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_categoria_id'], ['categoria.id'], ),
    sa.ForeignKeyConstraint(['id_marca_id'], ['marca.id'], ),
    sa.ForeignKeyConstraint(['id_medida_id'], ['medida.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cod_barras')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    op.drop_table('usuario')
    op.drop_table('medida')
    op.drop_table('marca')
    op.drop_table('categoria')
    # ### end Alembic commands ###
