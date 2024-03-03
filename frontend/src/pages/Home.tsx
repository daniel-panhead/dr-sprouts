import { FormEvent, useState } from "react"
import { useNavigate } from "react-router-dom";
import Logo from "../assets/logo.png";

const Home = () => {
  const navigate = useNavigate();
  const [symptoms, setSymptoms] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    navigate("/chat", {
      state: {
        initialQuery: symptoms
      }
    })
  }

  return (
    <div className="flex flex-col mt-24 items-center gap-y-8">
      <img src={Logo} alt="" className="w-30" />
      <h1 className="-mt-6 text-title font-title text-center">Ask Dr. Sprouts!</h1>
      <h2 className="text-subtitle mb-6">What's wrong with your plant?</h2>
      <form className="flex flex-col items-center gap-y-6 form-control" onSubmit={handleSubmit}>
        <input required type="text" placeholder="Enter the symptoms" className="input" value={symptoms} onChange={(e) => setSymptoms(e.target.value)} />
        <button className="btn btn-primary px-8" type="submit">Submit!</button>
      </form>
    </div>
  )
}

export default Home
