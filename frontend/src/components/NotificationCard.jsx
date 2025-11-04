import React from "react";

export default function NotificationCard({ message }) {
  return (
    <div className="bg-gray-50 border-l-4 border-blue-600 p-3 rounded-md mb-2 shadow-sm">
      <p className="text-gray-700">{message}</p>
    </div>
  );
}
