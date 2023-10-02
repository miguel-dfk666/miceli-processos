import React, { useState } from 'react';
import Header from './components/header';
import Sidebar from './components/sidebar';
import { FaBars } from 'react-icons/fa';
import Processo from '../libs/processos';
import MainContent from './maincontent';

interface HomePageProps {
  data: Processo[];
}

const HomePage: React.FC<HomePageProps> = ({ data }) => {
  const [selectedOption, setSelectedOption] = useState<string>('Selecionar Opção');
  const [subOption, setSubOption] = useState<string>('');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(false);

  const handleOptionChange = (option: string) => {
    setSelectedOption(option);
    setSubOption('');
  };

  const handleConfirmClick = () => {
    // Lógica para lidar com o clique no botão "Confirmar"
    // Implemente a lógica conforme necessário
    console.log('Botão Confirmar clicado!');
  };

  return (
    <div className="bg-zinc-300 min-h-screen flex flex-col relative">
      <Header />
      <button
        className="fixed top-0 left-0 w-16 h-16 bg-gray-700 flex items-center justify-center text-white z-50 rounded-r"
        onClick={() => setSidebarOpen(!sidebarOpen)}
      >
        <FaBars />
      </button>
      <div className="flex flex-1">
        <Sidebar searchQuery={searchQuery} setSearchQuery={setSearchQuery} sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
        <MainContent
          selectedOption={selectedOption}
          subOption={subOption}
          onOptionChange={handleOptionChange}
          onSubOptionChange={setSubOption}
          onConfirmClick={handleConfirmClick}
          processos={data}
        />
      </div>
    </div>
  );
};

export default HomePage;
