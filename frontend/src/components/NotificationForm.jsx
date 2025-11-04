import React, { useState } from "react";

export default function NotificationForm({ onResult }) {
  const [title, setTitle] = useState("");
  const [message, setMessage] = useState("");
  const [type, setType] = useState("alert");
  const [primaryChannel, setPrimaryChannel] = useState("sms");
  const [fallbackChannel, setFallbackChannel] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      type,
      primary: primaryChannel,
      fallback: fallbackChannel || null,
      title,
      message,
    };

    try {
      const res = await fetch("http://127.0.0.1:8000/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      onResult(data);
    } catch (error) {
      onResult({ success: false, log: ["Error de conexión con el backend."] });
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-lg"
    >
      <h2 className="text-2xl font-bold mb-5 text-center text-indigo-700">
        Enviar Notificación
      </h2>

      <div className="mb-4">
        <label className="block font-semibold mb-1">Título</label>
        <input
          className="border w-full p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>

      <div className="mb-4">
        <label className="block font-semibold mb-1">Mensaje</label>
        <textarea
          className="border w-full p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          rows={3}
          required
        />
      </div>

      <div className="mb-4 flex gap-4">
        <div className="flex-1">
          <label className="block font-semibold mb-1">Tipo</label>
          <select
            className="border w-full p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
            value={type}
            onChange={(e) => setType(e.target.value)}
          >
            <option value="alert">Alerta</option>
            <option value="reminder">Recordatorio</option>
            <option value="newsletter">Boletín</option>
          </select>
        </div>

        <div className="flex-1">
          <label className="block font-semibold mb-1">Canal principal</label>
          <select
            className="border w-full p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
            value={primaryChannel}
            onChange={(e) => setPrimaryChannel(e.target.value)}
          >
            <option value="email">Email</option>
            <option value="sms">SMS</option>
            <option value="push">Push</option>
            <option value="whatsapp">WhatsApp</option>
          </select>
        </div>
      </div>

      <div className="mb-5">
        <label className="block font-semibold mb-1">
          Canal de respaldo (opcional)
        </label>
        <select
          className="border w-full p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          value={fallbackChannel}
          onChange={(e) => setFallbackChannel(e.target.value)}
        >
          <option value="">Ninguno</option>
          <option value="email">Email</option>
          <option value="sms">SMS</option>
          <option value="push">Push</option>
          <option value="whatsapp">WhatsApp</option>
        </select>
      </div>

      <button
        type="submit"
        className="bg-indigo-600 text-white font-bold px-6 py-3 rounded-lg hover:bg-indigo-700 w-full transition-colors"
      >
        Enviar Notificación
      </button>
    </form>
  );
}
