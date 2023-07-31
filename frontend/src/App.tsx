import React from "react";

const App = () => {
  const getCellSymbol = (cell: Cell): string => {
    switch (cell) {
      case Cell.Empty:
        return "_";
      case Cell.Computer:
        return "X";
      case Cell.User:
        return "O";
      default:
        return assertNever(cell);
    }
  };

  const getSummaryMessage = (): string => {
    let message = "Game Over! ";
    switch (winner) {
      case Winner.Computer:
        message += "You lost, better luck next time!";
        return message;
      case Winner.User:
        message += "You won, congratulations!";
        return message;
      case Winner.Tie:
        message += "It's a tie!";
        return message;
      default:
        return assertNever(winner);
    }
  };

  const buttonHandler = async (i: number, j: number) => {
    // Mark the user clicked cell
    const boardCopy: Board = JSON.parse(JSON.stringify(board));
    boardCopy[i][j] = Cell.User;
    setBoardData({ ...boardData, board: boardCopy });

    // Set loading true
    setLoading(true);

    // Compute the next move
    try {
      const data = await computeService.compute(board);
      setLoading(false);
      setBoardData(data);
    } catch (error) {
      setLoading(false);
    }
  };
};

export default App;
