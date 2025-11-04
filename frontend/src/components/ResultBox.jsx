export default function ResultBox({ result }) {
  if (!result) return null;

  const { success, log } = result;

  const statusText = success
    ? "✅ Notificación enviada correctamente"
    : "❌ No se pudo enviar la notificación";

  const statusColor = success ? "text-green-700" : "text-red-700";

  return (
    <div className="mt-6 bg-white shadow-md p-5 rounded-xl w-full max-w-md border border-gray-200">
      <h2 className={`font-bold text-lg mb-3 ${statusColor}`}>{statusText}</h2>

      <div className="bg-gray-50 p-3 rounded-lg">
        <p className="font-semibold mb-2 text-gray-700">Detalles del proceso:</p>
        <ul className="list-disc list-inside text-gray-600 text-sm space-y-1">
          {log && log.length > 0 ? (
            log.map((line, index) => <li key={index}>{line}</li>)
          ) : (
            <li>No hay detalles disponibles.</li>
          )}
        </ul>
      </div>
    </div>
  );
}
