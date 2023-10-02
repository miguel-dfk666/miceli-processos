import React, { useState, useRef, useEffect } from 'react';
import logoEmpresa from '../components/assets/logo-miceli.png';
import user from '../components/assets/user.png';

const Header: React.FC = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [menuPosition, setMenuPosition] = useState({ top: 0, left: 0 });

  const buttonRef = useRef<HTMLButtonElement>(null);

  const handleMenuToggle = () => {
    setMenuOpen(!menuOpen);
  };

  const handleLogout = () => {
    // Lógica para fazer logout do usuário
    // Implemente a lógica conforme necessário
    console.log('Usuário deslogado!');
  };

  useEffect(() => {
    if (buttonRef.current) {
      const buttonRect = buttonRef.current.getBoundingClientRect();
      const { top, left } = buttonRect;

      // Calcula a posição ideal para o menu com base na posição do botão de usuário
      const menuTop = top + buttonRect.height;
      const menuLeft = left; // Posiciona o menu à esquerda do botão de usuário

      setMenuPosition({ top: menuTop, left: menuLeft });
    }
  }, [menuOpen]);

  return (
    <header className="bg-gray-200 p-4">
      <div className="flex justify-between items-center">
        <img src={logoEmpresa} alt="Logo da Empresa" className="w-20 ml-12" />
        <div className="relative">
          <button ref={buttonRef} className="bg-gray-500 text-white px-3 py-1 rounded" onClick={handleMenuToggle}>
            <img src={user} alt="Usuário" /> <i className={`fas fa-caret-${menuOpen ? 'up' : 'down'}`}></i>
          </button>
          {menuOpen && (
            <div className="absolute mt-2 bg-white border border-gray-300 rounded shadow-lg" style={{ top: menuPosition.top, left: menuPosition.left }}>
              <button className="block px-4 py-2 hover:bg-gray-100 w-full text-left" onClick={handleLogout}>
                Logout
              </button>
              {/* Adicione mais opções de menu conforme necessário */}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
