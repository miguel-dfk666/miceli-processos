import React, { useState } from 'react';
// import { Chart } from "react-google-charts";
import Dropdown from './components/dropdown';
import ProcessoDetails from './components/processdetail'; // Importe o componente ProcessoDetails
import AdvogadoDetails from './components/advogadodetail'; // Importe o componente AdvogadoDetails

interface MainContentProps {
  selectedOption: string;
  subOption: string;
  onOptionChange: (option: string) => void;
  onSubOptionChange: (subOption: string) => void;
  onConfirmClick: () => void;
  processoInfo: {
    id: number;
    numero_processo: string;
    data_processo: string;
    assunto_principal: string;
  };
  advogadoInfo: {
    id: number;
    advogado_oab: string;
    advogado_nome: string;
    total_processos: number;
  };
}

const MainContent: React.FC<MainContentProps> = ({
  selectedOption,
  subOption,
  onOptionChange,
  onSubOptionChange,
}) => {
  const [processoInfo, setProcessoInfo] = useState<any>(null); // Estado para armazenar informações do processo
  const [advogadoInfo, setAdvogadoInfo] = useState<any>(null); // Estado para armazenar informações do advogado

  const handleConfirmClick = () => {
    // Simulando uma chamada à API com um atraso de 1 segundo
    setTimeout(() => {
      if (selectedOption === 'Número do Processo') {
        // Simulando uma resposta da API para um número de processo específico (subOption)
        const resultadoDaBusca = {
          id: 1,
          numero_processo: subOption,
          data_processo: '2023-11-01',
          assunto_principal: 'Assunto do Processo',
        };
        setProcessoInfo(resultadoDaBusca); // Atualizando o estado com as informações do processo
        setAdvogadoInfo(null); // Resetando as informações do advogado
      } else if (selectedOption === 'Número OAB') {
        // Simulando uma resposta da API para um número de OAB específico (subOption)
        const resultadoDaBusca = {
          id: 1,
          advogado_oab: subOption,
          advogado_nome: 'Rafael de Oliveira de Santos',
          total_processos: 10,
        };
        setAdvogadoInfo(resultadoDaBusca); // Atualizando o estado com as informações do advogado
        setProcessoInfo(null); // Resetando as informações do processo
      }
    }, 1000); // Atraso de 1 segundo para simular a chamada à API
  };

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
          onClick={() => {
            // Quando o botão "Confirmar" é clicado, chama a função handleConfirmClick
            handleConfirmClick();
          }}
          className="bg-gray-500 text-white px-4 py-2 rounded-md ml-2 hover:bg-gray-600 transition duration-300"
        >
          Confirmar
        </button>
      </div>

      {/* Exibe detalhes do processo se processoInfo estiver definido */}
      {processoInfo && <ProcessoDetails processo={processoInfo} />}

      {/* Exibe detalhes do advogado se advogadoInfo estiver definido */}
      {advogadoInfo && <AdvogadoDetails advogado={advogadoInfo} />}
    </main>
  );
};

export default MainContent;
