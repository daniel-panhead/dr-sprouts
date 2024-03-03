import React, { useEffect, useState } from 'react'
import ChatConversation, { ChatHistory } from './ChatConversation'

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

  useEffect(() => {
    if (initialQuery != "") addMessageToHistory(initialQuery, true);
  }, [initialQuery]);

  const handleSendMessage = async () => {
    if (currentQuery != "") {
      addMessageToHistory(currentQuery, true);
      const currentQueryCopy = (' ' + currentQuery).slice(1);
      
      setCurrentQuery("");
      await sendQuery(currentQueryCopy);
    }
  }

  const sendQuery = async (currentQuery: string) => {
    const result = await fetch("http://127.0.0.1:8000", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({response: currentQuery})
    })
    const response = await result.text();
    
    addMessageToHistory(response, false);
  }

  return (
    <div className="flex flex-col basis-3/4 gap-y-6 h-full items-center">
      <ChatConversation chatHistory={chatHistory} />
      <div className="flex w-full">
        <input
          type="text"
          placeholder="Enter your query"
          className="input flex-grow rounded-r-none"
          value={currentQuery}
          onChange={(e) => setCurrentQuery(e.target.value)}
        />
        <button className="btn btn-secondary px-6 rounded-l-none" onClick={handleSendMessage}>Enter</button>
      </div>
    </div>
  )
}

export default ChatSection