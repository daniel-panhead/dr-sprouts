import { useEffect } from "react";
import { useLocation } from "react-router-dom";

const Chat = () => {
  const location = useLocation();

  useEffect(() => {
    const initialQuery = location.state.initialQuery;
    console.log(initialQuery);
  }, [location.state.initialQuery]);

  return (
    <div>
      {location.state.initialQuery}
    </div>
  )
}

export default Chat;