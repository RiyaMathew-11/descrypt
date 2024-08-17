import React from "react";
import { Box, Button,Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import logo from "./assets/images/descrypt-white.png";

export default function MainPage() {
  const navigate = useNavigate();
  const handleClick = () => navigate("/chatbot");

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
        alignItems: "center",
        justifyContent: "center",
        background: "linear-gradient(140deg, #202020 30%, #1cb88b 95%)",
        color: "white",
      }}
    >
      <Typography
        variant="h3"
        align="center"
        sx={{ fontSize: 50, mb: 3, fontWeight: "bold" }}
      >
        Descrypt v.0.1
      </Typography>
      <Typography variant="body1" align="center" sx={{ fontSize: 25, mb: 3 }}>
        The language model embedded descriptive answer evaluator.
      </Typography>
      <Button
        variant="contained"
        color="secondary"
        onClick={handleClick}
        sx={{ bgcolor: "#1cb88b", fontWeight: "bold" }} // light purple
      >
        Try Descrypt ↗
      </Button>
      <Box
        sx={{
          position: "fixed",
          top: 0,
          width: "100%",
          height: "10vh",
          backgroundColor: "#000000", // header color
        }}
      >
        <img
          src={logo}
          alt="descrypt logo"
          style={{
            paddingTop: "25px",
            paddingLeft: "25px",
            maxHeight: "25px",
          }}
        />
      </Box>
      <Box
        sx={{
          position: "fixed",
          bottom: 0,
          width: "100%",
          height: "10vh",
          backgroundColor: "#000000", // footer color
        }}
      >
        <Typography
          variant="body1"
          align="center"
          sx={{ paddingTop: "20px", fontSize: 15 }}
        >
        </Typography>
      </Box>
    </Box>
  );
}
