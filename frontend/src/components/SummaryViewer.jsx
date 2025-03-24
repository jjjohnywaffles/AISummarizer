import React from 'react';

const SummaryViewer = ({ summaryData, onReset }) => {
  if (!summaryData) return null;

  return (
    <div className="bg-white p-8 rounded-2xl shadow mt-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-4 text-center">{summaryData.title || 'Paper Summary'}</h1>
      {summaryData.authors && (
        <p className="text-md mb-6 text-center font-medium">
            By: {summaryData.authors.join(', ')}
        </p>
        )}

        {['introduction', 'methods', 'results', 'discussion', 'conclusion'].map((section) => (
        summaryData[section] && (
            <div key={section} className="mb-8">
            <h2 className="text-2xl font-semibold mb-2 capitalize">{section}</h2>
            <ul className="list-disc pl-6 space-y-1">
                {summaryData[section].map((sentence, idx) => (
                <li key={idx}>{sentence}</li>
                ))}
            </ul>
            </div>
            )
        ))}

      {summaryData.statistics && (
        <div className="mb-8">
          <h2 className="text-2xl font-semibold mb-2">Notable Statistics</h2>
          <ul className="list-disc pl-6 space-y-1">
            {summaryData.statistics.map((stat, idx) => <li key={idx}>{stat}</li>)}
          </ul>
        </div>
      )}

      {summaryData.citations && (
        <div className="mb-8">
          <h2 className="text-2xl font-semibold mb-2">Citations</h2>
          <ul className="list-disc pl-6 space-y-1">
            {summaryData.citations.map((citation, index) => (
              <li key={index}>{citation}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="text-center">
        <button
          onClick={onReset}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700 transition"
        >
          Upload Another Paper
        </button>
      </div>
    </div>
  );
};

export default SummaryViewer;
