import ChatBubble, { ChatMessage } from "./ChatBubble";

export type ChatHistory = ChatMessage[];

const ChatConversation = ({ chatHistory }: {chatHistory: ChatHistory}) => {
  return (
    <div className="flex flex-col w-full h-full p-6 gap-y-2 bg-light rounded-[1.5em] overflow-y-scroll">
      {chatHistory && chatHistory.map((chat) => {
        return (
          <ChatBubble message={chat.message} userSent={chat.userSent} time={chat.time} />
        );
      })}
      {chatHistory && chatHistory.slice(-1)[0]?.userSent && 
        <div className="chat chat-start">
          <div className="chat-bubble chat-bubble-primary">
            <span className="loading loading-dots loading-sm"></span>
          </div>
        </div>
      }
    </div>
  );
};

export default ChatConversation;