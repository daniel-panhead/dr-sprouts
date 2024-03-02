import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import ChatConversation, { ChatHistory } from "../components/ChatConversation";

const Chat = () => {
  const location = useLocation();
  const [chatHistory, setChatHistory] = useState<ChatHistory>([]);

  useEffect(() => {
    setChatHistory([
      {  
        message: "My plant's leaves turned brown and fell off. What happened??",
        userSent: true,
        time: new Date(Date.now() - 1498)
      },
      {  
        message: "Water your plant and expose it to sunlight n stuff",
        userSent: false,
        time: new Date()
      }
    ]);

    const initialQuery = location.state.initialQuery;
    if (initialQuery) {
      setChatHistory((prev) => [
        ...prev,
        {
          message: initialQuery,
          userSent: true,
          time: new Date()
        }
      ])
    }
  }, [location.state.initialQuery]);

  return (
    <>
      <Link to="/" className="flex items-center gap-x-4 hover:opacity-90 transition-all">
        <div className="m-4 w-16 h-14 bg-white"></div>
        <span className="font-title text-4xl">Dr. Sprouts</span>
      </Link>
      <div className="flex flex-col items-center p-10 pt-0 h-full">
        <h2 className="text-subtitle mb-6">What's wrong with your plant?</h2>
        <div className="flex gap-x-8 w-full h-full">
          <div className="flex flex-col basis-1/4 items-center gap-y-5">
            <h3 className="text-4xl">Image Diagnosis</h3>
            <div className="w-52 h-52 bg-white"></div>
            <button className="btn btn-primary">Upload Image</button>
          </div>
          <div className="flex flex-col basis-3/4 gap-y-6 h-full items-center">
            <ChatConversation chatHistory={chatHistory} />
            <div className="flex w-full">
              <input type="text" placeholder="Enter your query:" className="input flex-grow rounded-r-none" />
              <button className="btn btn-secondary px-6 rounded-l-none">Enter</button>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Chat;