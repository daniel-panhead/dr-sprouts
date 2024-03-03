import { Link, useLocation } from "react-router-dom";
import ImageDiagnosisSection from "../components/ImageDiagnosisSection";
import ChatSection from "../components/ChatSection";
import Logo from "../assets/logo.png"
import { useEffect, useState } from "react";

const Chat = () => {
  const [initialQuery, setInitialQuery] = useState("");
  const location = useLocation();

  useEffect(() => {
    const passedInitialQuery = location.state ? location.state?.initialQuery : "";
    if (passedInitialQuery != "" && initialQuery == "") {
      setInitialQuery(passedInitialQuery);
    }
  }, [location.state, setInitialQuery, initialQuery]);

  return (
    <>
      <Link to="/" className="flex items-center gap-x-4 p-4 hover:opacity-90 transition-all">
        <img src={Logo} alt="" className="w-16" />
        <span className="font-title text-4xl">Dr. Sprouts</span>
      </Link>
      <div className="flex flex-col items-center p-10 pt-0 flex-grow">
        <h2 className="text-subtitle mb-6">What's wrong with your plant?</h2>
        <div className="flex gap-x-8 w-full h-full">
          <ImageDiagnosisSection />
          <ChatSection initialQuery={initialQuery} />
        </div>
      </div>
    </>
  )
}

export default Chat;