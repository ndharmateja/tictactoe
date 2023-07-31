enum Cell {
  Empty = 0,
  User = 1,
  Computer = 2,
}
type Row = [Cell, Cell, Cell];
enum Winner {
  Tie = 0,
  User = 1,
  Computer = 2,
}

export type Board = [Row, Row, Row];
export interface BoardData {
  board: Board;
  isComplete: boolean;
  winner: Winner;
}
