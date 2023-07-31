import React, { useState } from "react";
import { Board, BoardData, Cell, Winner } from "./types";
import { assertNever } from "./utils";
import computeService from "./service";

const INITIAL_BOARD: Board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
];

const INITIAL_BOARD_DATA: BoardData = {
  board: INITIAL_BOARD,
  isComplete: false,
  winner: Winner.Tie,
};

const App = () => {
  const [boardData, setBoardData] = useState<BoardData>(INITIAL_BOARD_DATA);
  const [loading, setLoading] = useState<boolean>(false);
  const { board, isComplete, winner } = boardData;

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

  return (
    <div>
      Board
      {board.map((row, i) => {
        return (
          <>
            <div key={i}>
              <span>
                {row.map((cell, j) => {
                  return (
                    <button
                      disabled={cell !== Cell.Empty || loading}
                      key={i + j}
                      onClick={() => buttonHandler(i, j)}
                    >
                      {getCellSymbol(cell)}
                    </button>
                  );
                })}
              </span>
            </div>
          </>
        );
      })}
      {loading ? <p>Computer is thinking</p> : <></>}
      {isComplete ? (
        <div>
          <p>{getSummaryMessage()}</p>
          <button onClick={() => setBoardData(INITIAL_BOARD_DATA)}>
            Play Again
          </button>
        </div>
      ) : (
        <></>
      )}
    </div>
  );
};

export default App;
