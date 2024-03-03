import ChatBubble, { ChatMessage } from "./ChatBubble";
import ChatLoading from "./ChatLoading";

export type ChatHistory = ChatMessage[];

const ChatConversation = ({ chatHistory }: {chatHistory: ChatHistory}) => {
  return (
    <div className="flex flex-col w-full h-full p-6 gap-y-2 bg-light rounded-[1.5em] overflow-y-scroll">
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