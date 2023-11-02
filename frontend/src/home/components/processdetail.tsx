import React from 'react';

interface ProcessoDetailsProps {
  processo: {
    id: number;
    numero_processo: string;
    data_processo: string;
    assunto_principal: string;
  };
}

const ProcessoDetails: React.FC<ProcessoDetailsProps> = ({ processo }) => (
  <div className="border border-gray-300 p-2 mb-2 rounded-md">
    <strong>Número do Processo:</strong> {processo.numero_processo}<br />
    <strong>Data do processo:</strong> {processo.data_processo}<br />
    <strong>Descrição:</strong> {processo.assunto_principal} <br />
  </div>
);

export default ProcessoDetails;
