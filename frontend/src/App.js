import React, { useState } from 'react';
import FileUploader from './components/FileUploader';
import SummaryViewer from './components/SummaryViewer';
import './App.css';

function App() {
  const [summaryData, setSummaryData] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      {!summaryData ? (
        <FileUploader onUploadComplete={(data) => setSummaryData(data)} />
      ) : (
        <SummaryViewer summaryData={summaryData} onReset={() => setSummaryData(null)} />
      )}
    </div>
  );
}

export default App;