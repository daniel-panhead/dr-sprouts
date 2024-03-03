import { useEffect, useRef } from "react";
import ChatBubble, { ChatMessage } from "./ChatBubble";
import ChatLoading from "./ChatLoading";

export type ChatHistory = ChatMessage[];

const ChatConversation = ({ chatHistory, submitted }: {chatHistory: ChatHistory, submitted: Date}) => {
  const scrollWindowRef = useRef(null);

  useEffect(() => {
    if(scrollWindowRef.current) {
      scrollWindowRef.current.scrollTop = scrollWindowRef.current.scrollHeight;
    }
  }, [submitted])
  return (
    <div ref={scrollWindowRef} className="flex flex-col w-full max-h-[60dvh] flex-grow p-6 gap-y-2 bg-light rounded-[1.5em] overflow-y-scroll">
      {chatHistory && chatHistory.map((chat, i) => {
        return (
          <ChatBubble message={chat.message} userSent={chat.userSent} time={chat.time} key={i} />
        );
      })}
      {chatHistory && chatHistory.slice(-1)[0]?.userSent && 
        <ChatLoading />
      }
    </div>
  );
};

export default ChatConversation;