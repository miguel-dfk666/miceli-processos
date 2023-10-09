  import { useState, useRef, useEffect } from 'react';
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
      if (buttonRef.current && menuOpen) {
        const buttonRect = buttonRef.current.getBoundingClientRect();
        const menuWidth = 100; // largura do menu, ajuste conforme necessário
    
        // Calcula a posição ideal para o menu com base na posição do botão de usuário
        let menuLeft = buttonRect.left + buttonRect.width / 2 - menuWidth / 2; // centraliza o menu em relação ao botão
        const menuTop = buttonRect.bottom + window.scrollY;
    
        // Verifica se o menu está dentro dos limites da tela
        const windowWidth = window.innerWidth;
        if (menuLeft < 0) {
          menuLeft = 0;
        } else if (menuLeft + menuWidth > windowWidth) {
          menuLeft = windowWidth - menuWidth;
        }
    
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
              <div className="fixed mt-1 bg-white border border-gray-300 rounded shadow-lg" style={{ top: menuPosition.top, left: menuPosition.left }}>
                <button className="block px-4 py-2 hover:bg-gray-100 w-30 text-left" onClick={handleLogout}>
                  <a href="/login">Logout</a>
                </button>
              </div>
            )}
          </div>
        </div>
      </header>
    );
  };

  export default Header;
