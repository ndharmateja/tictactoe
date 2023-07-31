import React from "react";

const App = () => {
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
