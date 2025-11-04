import React, { useState } from "react";
import NotificationForm from "./components/NotificationForm";
import ResultBox from "./components/ResultBox";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-10">
      <h1 className="text-4xl font-bold text-indigo-700 mb-8">
        NotiCorp 
      </h1>
      <div className="w-full flex flex-col items-center gap-6">
        <NotificationForm onResult={setResult} />
        {result && <ResultBox result={result} />}
      </div>
    </div>
  );
}
