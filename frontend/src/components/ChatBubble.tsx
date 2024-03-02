import { useState } from "react";

export type ChatMessage = {
  message: string,
  time: Date,
  userSent: boolean
};

const ChatBubble = ({message, time, userSent}: ChatMessage) => {
  const [showTimestamp, setShowTimestamp] = useState(false);

  return (
    <div
      className={`chat ${userSent ? "chat-end" : "chat-start"}`}
      onClick={() => setShowTimestamp(!showTimestamp)}
    >
      {showTimestamp &&
        <span className="chat-header opacity-50">{time.toLocaleTimeString()}</span>
      }
      <div className={`chat-bubble hover:brightness-95 active:brightness-90 transition-all ${userSent ? "chat-bubble-secondary" : "chat-bubble-primary"}`}>
        {message}
      </div>
    </div>
  );
};

export default ChatBubble