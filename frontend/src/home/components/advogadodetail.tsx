import React from 'react';

interface AdvogadoDetailsProps {
  advogado: {
    id: number;
    advogado_oab: string;
    advogado_nome: string;
    total_processos: number;
  };
}

const AdvogadoDetails: React.FC<AdvogadoDetailsProps> = ({ advogado }) => (
  <div className='border border-gray-300 p-2 mb-2 rounded md'>
    <strong>Numero OAB:</strong> {advogado.advogado_oab}<br />
    <strong>Nome Advogado:</strong> {advogado.advogado_nome}<br />
    <strong>Quantidade Processos:</strong> {advogado.total_processos}<br />
  </div>
);

export default AdvogadoDetails;
