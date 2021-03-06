# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2012>  Gabriel Falc達o <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from os.path import dirname, abspath, join
from nose.tools import with_setup
from tests.asserts import prepare_stdout
from tests.asserts import assert_stdout_lines

from lettuce import Runner

current_dir = abspath(dirname(__file__))
join_path = lambda *x: join(current_dir, *x)

@with_setup(prepare_stdout)
def test_output_with_success_colorless():
    "Language: ja -> sucess colorless"

    runner = Runner(join_path('ja', 'success', 'dumb.feature'), verbosity=3)
    runner.run()

    assert_stdout_lines(
        "\n"
        "フィーチャ: ダムフィーチャ           # tests/functional/language_specific_features/ja/success/dumb.feature:3\n"
        "  テストをグリーンになればテスト成功 # tests/functional/language_specific_features/ja/success/dumb.feature:4\n"
        "\n"
        "  シナリオ: 何もしない               # tests/functional/language_specific_features/ja/success/dumb.feature:6\n"
        "    前提 何もしない                  # tests/functional/language_specific_features/ja/success/dumb_steps.py:6\n"
        "\n"
        "1 feature (1 passed)\n"
        "1 scenario (1 passed)\n"
        "1 step (1 passed)\n"
    )

@with_setup(prepare_stdout)
def test_output_of_table_with_success_colorless():
    "Language: ja -> sucess table colorless"

    runner = Runner(join_path('ja', 'success', 'table.feature'), verbosity=3)
    runner.run()

    assert_stdout_lines(
        "\n"
        "フィーチャ: テーブル記法                     # tests/functional/language_specific_features/ja/success/table.feature:3\n"
        "  日本語でのテーブル記法がパスするかのテスト # tests/functional/language_specific_features/ja/success/table.feature:4\n"
        "\n"
        "  シナリオ: 何もしないテーブル               # tests/functional/language_specific_features/ja/success/table.feature:6\n"
        "    前提 データは以下:                       # tests/functional/language_specific_features/ja/success/table_steps.py:6\n"
        "      | id | 定義       |\n"
        "      | 12 | 何かの定義 |\n"
        "      | 64 | 別の定義   |\n"
        "\n"
        "1 feature (1 passed)\n"
        "1 scenario (1 passed)\n"
        "1 step (1 passed)\n"
    )

@with_setup(prepare_stdout)
def test_output_outlines_success_colorless():
    "Language: ja -> sucess outlines colorless"

    runner = Runner(join_path('ja', 'success', 'outlines.feature'), verbosity=3)
    runner.run()

    assert_stdout_lines(
        "\n"
        "フィーチャ: アウトラインを日本語で書く           # tests/functional/language_specific_features/ja/success/outlines.feature:3\n"
        "  図表のテストをパスすること                     # tests/functional/language_specific_features/ja/success/outlines.feature:4\n"
        "\n"
        "  シナリオアウトライン: 全てのテストで何もしない # tests/functional/language_specific_features/ja/success/outlines.feature:6\n"
        "    前提 入力値を <データ1> とし                 # tests/functional/language_specific_features/ja/success/outlines_steps.py:13\n"
        "    もし 処理 <方法> を使って                    # tests/functional/language_specific_features/ja/success/outlines_steps.py:22\n"
        "    ならば 表示は <結果> である                  # tests/functional/language_specific_features/ja/success/outlines_steps.py:31\n"
        "\n"
        "  例:\n"
        "    | データ1 | 方法 | 結果       |\n"
        "    | 何か    | これ | 機能       |\n"
        "    | その他  | ここ | 同じ       |\n"
        "    | データ  | 動く | unicodeで! |\n"
        "\n"
        "1 feature (1 passed)\n"
        "3 scenarios (3 passed)\n"
        "9 steps (9 passed)\n"
    )

@with_setup(prepare_stdout)
def test_output_outlines_success_colorful():
    "Language: ja -> sucess outlines colorful"

    runner = Runner(join_path('ja', 'success', 'outlines.feature'), verbosity=4)
    runner.run()

    assert_stdout_lines(
        '\n'
        "\033[1;37mフィーチャ: アウトラインを日本語で書く           \033[1;30m# tests/functional/language_specific_features/ja/success/outlines.feature:3\033[0m\n"
        "\033[1;37m  図表のテストをパスすること                     \033[1;30m# tests/functional/language_specific_features/ja/success/outlines.feature:4\033[0m\n"
        '\n'
        "\033[1;37m  シナリオアウトライン: 全てのテストで何もしない \033[1;30m# tests/functional/language_specific_features/ja/success/outlines.feature:6\033[0m\n"
        "\033[0;36m    前提 入力値を <データ1> とし                 \033[1;30m# tests/functional/language_specific_features/ja/success/outlines_steps.py:13\033[0m\n"
        "\033[0;36m    もし 処理 <方法> を使って                    \033[1;30m# tests/functional/language_specific_features/ja/success/outlines_steps.py:22\033[0m\n"
        "\033[0;36m    ならば 表示は <結果> である                  \033[1;30m# tests/functional/language_specific_features/ja/success/outlines_steps.py:31\033[0m\n"
        '\n'
        "\033[1;37m  例:\033[0m\n"
        "\033[0;36m   \033[1;37m |\033[0;36m データ1\033[1;37m |\033[0;36m 方法\033[1;37m |\033[0;36m 結果      \033[1;37m |\033[0;36m\033[0m\n"
        "\033[1;32m   \033[1;37m |\033[1;32m 何か   \033[1;37m |\033[1;32m これ\033[1;37m |\033[1;32m 機能      \033[1;37m |\033[1;32m\033[0m\n"
        "\033[1;32m   \033[1;37m |\033[1;32m その他 \033[1;37m |\033[1;32m ここ\033[1;37m |\033[1;32m 同じ      \033[1;37m |\033[1;32m\033[0m\n"
        "\033[1;32m   \033[1;37m |\033[1;32m データ \033[1;37m |\033[1;32m 動く\033[1;37m |\033[1;32m unicodeで!\033[1;37m |\033[1;32m\033[0m\n"
        '\n'
        "\033[1;37m1 feature (\033[1;32m1 passed\033[1;37m)\033[0m\n"
        "\033[1;37m3 scenarios (\033[1;32m3 passed\033[1;37m)\033[0m\n"
        "\033[1;37m9 steps (\033[1;32m9 passed\033[1;37m)\033[0m\n"
    )

