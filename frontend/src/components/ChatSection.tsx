import React, { useEffect, useState } from 'react'
import ChatConversation, { ChatHistory } from './ChatConversation'

const ChatSection = ({ initialQuery }: {initialQuery: string}) => {
  const [chatHistory, setChatHistory] = useState<ChatHistory>([]);
  const [currentQuery, setCurrentQuery] = useState("");

  useEffect(() => {
    setChatHistory((prev) => [
      ...prev,
      {
        message: initialQuery,
        time: new Date(),
        userSent: true
      }
    ])
  }, [initialQuery]);

  const handleSendMessage = async () => {
    if (currentQuery != "") {
      setChatHistory((prev) => [
        ...prev,
        {
          message: currentQuery,
          userSent: true,
          time: new Date()
        }
      ])
      setCurrentQuery("");
    }

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