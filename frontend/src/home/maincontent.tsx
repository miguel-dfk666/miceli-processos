import React from 'react';
import Dropdown from './components/dropdown';
import Processo from '../libs/processos'; 

interface MainContentProps {
  selectedOption: string;
  subOption: string;
  onOptionChange: (option: string) => void;
  onSubOptionChange: (subOption: string) => void;
  processos: Processo[];
  onConfirmClick: () => void; // Função para lidar com o clique no botão Confirmar
}

const MainContent: React.FC<MainContentProps> = ({
  selectedOption,
  subOption,
  onOptionChange,
  onSubOptionChange,
  processos,
  onConfirmClick,
}) => {
  return (
    <main className="flex-1 p-10 flex flex-col">
      <div className="mb-4 flex items-center">
        <Dropdown
          options={['Selecione uma opção', 'Número do Processo', 'Número OAB', 'Data de Criação']}
          selectedOption={selectedOption}
          onSelect={onOptionChange}
        />
        {selectedOption === 'Número do Processo' && (
          <input
            type="text"
            placeholder="0000000-00.0000.0.00.0000"
            value={subOption}
            onChange={(e) => onSubOptionChange(e.target.value)}
            className="border border-gray-300 p-2 rounded-md ml-5 pr-6"
          />
        )}
        {selectedOption === 'Número OAB' && (
          <input
            type="text"
            placeholder="ABC12345"
            value={subOption}
            onChange={(e) => onSubOptionChange(e.target.value)}
            className="border border-gray-300 p-2 rounded-md ml-2"
          />
        )}
        {selectedOption === 'Data de Criação' && (
          <input
            type="date"
            value={subOption}
            onChange={(e) => onSubOptionChange(e.target.value)}
            className="border border-gray-300 p-2 rounded-md ml-2"
          />
        )}
        <button
          onClick={onConfirmClick}
          className="bg-gray-500 text-white px-4 py-2 rounded-md ml-2 hover:bg-gray-600 transition duration-300"
        >
          Confirmar
        </button>
      </div>
      {/* Renderize os dados dos processos */}
      {processos.map((processo) => (
        <div key={processo.id} className="border border-gray-300 p-2 mb-2 rounded-md">
          <strong>Número do Processo:</strong> {processo.numero_processo}<br />
          <strong>Descrição:</strong> {processo.descricao}
        </div>
      ))}
    </main>
  );
};

export default MainContent;
