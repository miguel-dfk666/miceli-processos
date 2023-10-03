import { useEffect, useState } from 'react';
import './styles/styles.css';
import HomePage from './home/homepage'
import Processo from './libs/processos';

function App() {
  const [processos, setProcessos] = useState<Processo[]>([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}posts`);
        if (!response.ok) {
          throw new Error('Network response was not ok :(');
        }
        const result: Processo[] = await response.json();
        setProcessos(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []); // Note que o array de dependências está vazio, então o useEffect será executado apenas uma vez após o primeiro render

  return (
    <>
      <HomePage data={processos} />
    </>
  );
}

export default App;
