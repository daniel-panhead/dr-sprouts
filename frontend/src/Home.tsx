import { FormEvent, useState } from "react"

const Home = () => {
  const [symptoms, setSymptoms] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
  }

  return (
    <div className="flex flex-col mt-32 items-center gap-y-8">
      <h1 className="text-title font-title text-center">Ask Dr. Sprouts!</h1>
      <h2 className="text-subtitle mb-6">What's wrong with your plant?</h2>
      <form className="flex flex-col items-center gap-y-6 form-control" onSubmit={handleSubmit}>
        <input required type="text" placeholder="Enter the symptoms:" className="input" value={symptoms} onChange={(e) => setSymptoms(e.target.value)} />
        <button className="btn btn-primary px-8" type="submit">Submit!</button>
      </form>
    </div>
  )
}

export default Home
