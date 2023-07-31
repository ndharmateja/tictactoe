import axios from "axios";
import { Board, BoardData } from "./types";

const baseUrl = "http://localhost:3001";

const compute = async (board: Board): Promise<BoardData> => {
  const { data } = await axios.post<BoardData>(`${baseUrl}/compute`, board);
  return data;
};

export default { compute };
