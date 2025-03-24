import React, { useState } from 'react';

const FileUploader = ({ onUploadComplete }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setError(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file first.');
      return;
    }

    setUploading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Upload failed. Please try again.');
      }

      const data = await response.json();
      
      console.log('Received summary data:', data); //DEBUG

      onUploadComplete(data.summary);
    } catch (err) {
      setError(err.message);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="flex flex-col items-center p-6 border rounded-2xl shadow-md bg-white w-full max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">Upload Your Academic Paper (PDF)</h2>
      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="mb-4 border border-gray-300 rounded px-3 py-2 w-full"
      />
      <button
        onClick={handleUpload}
        disabled={uploading}
        className="bg-blue-600 text-white py-2 px-6 rounded-xl shadow hover:bg-blue-700 transition"
      >
        {uploading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <p className="text-red-600 mt-3">{error}</p>}
    </div>
  );
};

export default FileUploader;
