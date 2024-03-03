import React, { useCallback, useEffect, useState } from 'react'
import ChatConversation, { ChatHistory } from './ChatConversation'
import { useLocation } from 'react-router-dom';

const ChatSection = ({ initialQuery }: {initialQuery: string}) => {
  const [chatHistory, setChatHistory] = useState<ChatHistory>([]);
  const [currentQuery, setCurrentQuery] = useState("");

  const addMessageToHistory = (
    newMessage: string,
    userSent: boolean
  ) => {
    setChatHistory((prev) => [
      ...prev,
      {
        message: newMessage,
        time: new Date(),
        userSent
      }
    ])
  }

  const handleSendMessage = async () => {
    if (currentQuery != "") {
      addMessageToHistory(currentQuery, true);
      const currentQueryCopy = (' ' + currentQuery).slice(1);
      
      setCurrentQuery("");
      await sendQuery(currentQueryCopy);
    }
  }

  const sendQuery = useCallback(async (currentQuery: string) => {
    const result = await fetch("http://127.0.0.1:8000/input", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({response: currentQuery})
    })
    const response = await result.json();
    
    addMessageToHistory(response.message, false);
  }, []);

  useEffect(() => {
    if (initialQuery != "") {
      addMessageToHistory(initialQuery, true);
      sendQuery(initialQuery);
    }
  }, [initialQuery, sendQuery]);

  return (
    <div className="flex flex-col basis-3/4 gap-y-6 flex-grow items-center">
      <ChatConversation chatHistory={chatHistory} />
      <form className="flex w-full" onSubmit={handleSendMessage}>
        <input
          type="text"
          placeholder="Enter your query"
          className="input flex-grow rounded-r-none"
          value={currentQuery}
          onChange={(e) => setCurrentQuery(e.target.value)}
        />
        <button className="btn btn-secondary px-6 rounded-l-none" type="submit">Enter</button>
      </form>
    </div>
  )
}

export default ChatSection