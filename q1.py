"""
In FigJam, you can create tables in your file. These tables can be edited by selecting a subset of cells and setting the color property on the entire selection.

We want to support selections of either:
  (1) the entire table,
  (2) a single row, or
  (3) a single cell.
"""

"""
|------|-----|-----|
| blue | red | red |
|------|-----|-----|
| red  | red | red |
|------|-----|-----|
| red  | red | red |
|------|-----|-----|
"""


class Table:
  def __init__(self, num_rows, num_columns):
    self.num_rows = num_rows
    self.num_columns = num_columns
    # TODO

  def select_table(self):
     # TODO

  def select_row(self, row_index):
    # TODO

  def select_cell(self, row_index, column_index):
     # TODO

  # Returns the color of the cell at (row_index, column_index)
  def get_color(self, row_index, column_index):
     # TODO

  # Sets the given color on every cell in the current selection
  def set_color_on_selection(self, color):
    # TODO

  def __repr__(self):
    column_indices = list(range(self.num_columns))
    row_divider = "".join(map(lambda x: '+---', column_indices)) + "+\n"
    debug_string = row_divider
    for i in range(self.num_rows):
      colors = []
      for j in range(self.num_columns):
        color = self.get_color(i, j)
        colors.append(color[0].upper() if len(color) > 0 else " ")
      debug_string += f"| {' | '.join(colors)} |\n"
      debug_string += row_divider
    return debug_string

def test():
  def assert_table_colors_equal(table, expected):
    for i in range(table.num_rows):
      for j in range(table.num_columns):
        assert table.get_color(i, j) == expected[i][j], f"Expected '{expected[i][j]}' in cell ({i}, {j}); received '{table.get_color(i, j)}'"

  table = Table(2, 3)

  assert_table_colors_equal(table, [
    ['', '', ''],
    ['', '', ''],
  ])

  table.select_table()
  table.set_color_on_selection('red')
  assert_table_colors_equal(table, [
    ['red', 'red', 'red'],
    ['red', 'red', 'red'],
  ])

  table.select_cell(0, 0)
  table.set_color_on_selection('blue')
  assert_table_colors_equal(table, [
    ['blue', 'red', 'red'],
    ['red', 'red', 'red'],
  ])

  table.select_row(0)
  table.set_color_on_selection('blue')
  assert_table_colors_equal(table, [
    ['blue', 'blue', 'blue'],
    ['red', 'red', 'red'],
  ])

  table.select_cell(0, 0)
  table.set_color_on_selection('green')
  assert_table_colors_equal(table, [
    ['green', 'blue', 'blue'],
    ['red', 'red', 'red'],
  ])

  table.select_cell(0, 1)
  table.set_color_on_selection('green')
  table.select_cell(0, 2)
  table.set_color_on_selection('green')
  assert_table_colors_equal(table, [
    ['green', 'green', 'green'],
    ['red', 'red', 'red'],
  ])

  table.select_row(1)
  table.set_color_on_selection('green')
  assert_table_colors_equal(table, [
    ['green', 'green', 'green'],
    ['green', 'green', 'green'],
  ])

  table.select_row(0)
  print("selection_type", table.selection_type)
  print("selection: ", table.selection)
  table.set_color_on_selection('blue')
  print("row_color: ", table._row_color)
  print("cell color: ", table._cell_color)
  assert_table_colors_equal(table, [
    ['blue', 'blue', 'blue'],
    ['green', 'green', 'green'],
  ])

  table.select_cell(0, 2)
  table.set_color_on_selection('red')
  assert_table_colors_equal(table, [
    ['blue', 'blue', 'red'],
    ['green', 'green', 'green'],
  ])

  table.select_row(0)
  table.set_color_on_selection('red')
  assert_table_colors_equal(table, [
    ['red', 'red', 'red'],
    ['green', 'green', 'green'],
  ])

  table.select_row(0)
  table.set_color_on_selection('green')
  assert_table_colors_equal(table, [
    ['green', 'green', 'green'],
    ['green', 'green', 'green'],
  ])


print('Running tests...')
test()
print('Tests complete!')
