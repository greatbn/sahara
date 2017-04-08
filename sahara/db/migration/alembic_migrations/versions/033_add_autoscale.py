# Copyright 2017 Sa Pham
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""033_add_autoscale

Revision ID: 033
Revises: 032
Create Date: 2017-03-31 13:33:33.674853

"""

# revision identifiers, used by Alembic.
revision = '033'
down_revision = '032'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('clusters', sa.Column(
        'is_autoscale', sa.Boolean(), nullable=True))
    op.add_column('clusters', sa.Column(
        'max_cpu', sa.Integer(), nullable=True))
    op.add_column('clusters', sa.Column(
        'max_ram', sa.Integer(), nullable=True))
    op.add_column('clusters', sa.Column(
        'min_cpu', sa.Integer(), nullable=True))
    op.add_column('clusters', sa.Column(
        'min_ram', sa.Integer(), nullable=True))
