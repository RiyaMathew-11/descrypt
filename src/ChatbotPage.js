import React, { useState } from "react";
import {
  Container,
  TextField,
  Typography,
  Box,
  IconButton,
  Avatar,
  Chip,
} from "@mui/material";
import logo from "./assets/images/descrypt-white.png";
import SendIcon from "@mui/icons-material/Send";
import BotAvatar from "./assets/images/bot-avatar-green.png";
import UserAvatar from "./assets/images/user-avatar-green.png";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export default function ChatbotPage() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    {
      from: "bot",
      message:
        "Hello there! I am Descrypt, your self-test bot.\nI will ask you questions based on C programming.\nType start to begin and next to continue.",
    },
  ]);

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleClick = async () => {
    setChat((chat) => [...chat, { from: "user", message }]);
    setMessage("");

    const response = await fetch("http://localhost:5600/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    setChat((chat) => [...chat, { from: "bot", message: data.message }]);
  };

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
        position: "relative",
        zIndex: 1,
        overflow: "hidden",
      }}
    >
      <Container
        sx={{
          display: "flex",
          flexDirection: "column",
          minHeight: "100vh",
          justifyContent: "center",
          alignItems: "center",
          pt: 4,
          pb: 4,
        }}
      >
        <Box
          sx={{
            mt: 1,
            mb: 1,
            width: "100%",
            maxHeight: "calc(60vh - 20px - 30px)",
            p: 2,
            borderRadius: 1,
            position: "relative",
            zIndex: 2,
            overflowY: "auto",
          }}
        >
          <div style={{ width: "100%" }}>
            {chat.map((message, index) => (
              <div
                key={index}
                style={{
                  display: "flex",
                  justifyContent: message.from === "user",
                  alignItems: "right",
                  marginBottom: "10px",
                }}
              >
                {message.from === "user" ? (
                  <Avatar
                    alt="User Avatar"
                    src={UserAvatar}
                    sx={{
                      width: 30,
                      height: 30,
                      marginRight: "10px",
                      multiline: true,
                    }}
                  />
                ) : (
                  <Avatar
                    alt="Bot Avatar"
                    src={BotAvatar}
                    sx={{ width: 30, height: 30, marginRight: "10px" }}
                  />
                )}
                {message.from === "user" ? (
                  <Chip
                    label={message.message.split("\n").map((line, i) => (
                      <p key={i} style={{ margin: 0 }}>
                        {line}
                      </p>
                    ))}
                    variant="outlined"
                    style={{
                      backgroundColor: "#063934",
                      color: "white",
                      fontSize: "1em",
                      padding: `${Math.max(
                        10,
                        message.message.length * 0.25
                      )}px`,
                    }}
                  />
                ) : (
                  <Chip
                    label={message.message.split("\n").map((line, i) => (
                      <p key={i} style={{ margin: 0 }}>
                        {line}
                      </p>
                    ))}
                    variant="outlined"
                    style={{
                      backgroundColor: "green",
                      color: "white",
                      fontSize: "1em",
                      padding: `${Math.max(
                        10,
                        message.message.length * 0.25
                      )}px`,
                    }}
                  />
                )}
              </div>
            ))}
          </div>
        </Box>
        <Box
          sx={{
            mt: 2,
            mb: 2,
            width: "100%",
            maxHeight: "calc(100vh - 20vh - 20px)",
            p: 2,
            borderRadius: 1,
            position: "relative",
            zIndex: 2,
            overflowY: "auto",
            display: "flex",
            alignItems: "flex-end", // Align items at the bottom
          }}
        >
          <div style={{ width: "50%" }}>
            <TextField
              label="Message"
              variant="outlined"
              value={message}
              onChange={handleChange}
              fullWidth
              multiline // Enable multiline input
              rowsMax={4} // Set the maximum number of rows
              sx={{
                color: "white",
                "& .MuiOutlinedInput-root": {
                  "& fieldset": {
                    borderColor: "white",
                  },
                  "&:hover fieldset": {
                    borderColor: "white",
                  },
                  "&.Mui-focused fieldset": {
                    borderColor: "white",
                  },
                },
                "& .MuiInputLabel-outlined": {
                  color: "white",
                },
                "& .MuiInputBase-input": {
                  color: "white",
                },
              }}
            />
          </div>
          <IconButton
            color="primary"
            onClick={handleClick}
            sx={{ mt: 2, color: "#1cb88b" }}
          >
            <SendIcon />
          </IconButton>
        </Box>
      </Container>

      {/* ---------------------------------------------------------------------------------------------------- */}
      <Box
        sx={{
          position: "fixed",
          top: 0,
          width: "100%",
          height: "10vh",
          backgroundColor: "#000000",
          zIndex: 3,
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
        <Box
          sx={{
            position: "fixed",
            top: "10vh",
            width: "100%",
            display: "flex",
            alignItems: "center",
            justifyContent: "flex-start",
            paddingTop: "10px",
            paddingLeft: "15px",
            zIndex: 3,
          }}
        >
          <IconButton
            color="primary"
            onClick={() => (window.location.href = "/")} // Replace "/" with the URL of your main page
            sx={{ color: "#8CE78C" }}
          >
            <ArrowBackIcon />
          </IconButton>
          <Typography
            variant="body1"
            sx={{ marginLeft: "10px", color: "#8CE78C" }}
          >
            Main Page
          </Typography>
        </Box>
      </Box>
      <Box
        sx={{
          position: "fixed",
          bottom: 0,
          width: "100%",
          height: "10vh",
          backgroundColor: "#000000",
          zIndex: 3,
        }}
      >
        <Typography
          variant="body1"
          align="center"
          sx={{ paddingTop: "20px", fontSize: 15 }}
        >
          © 2023 All Rights Reserved
        </Typography>
      </Box>
    </Box>
  );
}
