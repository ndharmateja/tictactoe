import * as React from "react";
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";

const CircularIndeterminate = () => {
  return (
    <Box sx={{ display: "inline" }}>
      <CircularProgress size={10} />
    </Box>
  );
};

export default CircularIndeterminate;
