import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import ImageDiagnosisSection from "../components/ImageDiagnosisSection";
import ChatSection from "../components/ChatSection";

const Chat = () => {
  const location = useLocation();
  const [initialQuery, setInitialQuery] = useState("");

  useEffect(() => {
    const passedInitialQuery = location.state.initialQuery;
    if (passedInitialQuery) {
      setInitialQuery(passedInitialQuery);
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
          <ImageDiagnosisSection />
          <ChatSection
            initialQuery={initialQuery}
          />
        </div>
      </div>
    </>
  )
}

export default Chat;