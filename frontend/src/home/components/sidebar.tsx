import { FaSearch, FaBook } from 'react-icons/fa';

interface SidebarProps {
  searchQuery: string;
  setSearchQuery: React.Dispatch<React.SetStateAction<string>>;
  sidebarOpen: boolean;
  setSidebarOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

const Sidebar: React.FC<SidebarProps> = ({ searchQuery, setSearchQuery, sidebarOpen, setSidebarOpen }) => {
  return (
    <aside className={`bg-gray-700 p-4 w-64 fixed h-full top-0 left-0 transform transition-transform duration-300 ease-in-out z-10 ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}>
      {/* Conteúdo da Sidebar */}
      <div className="mt-12 mb-4 flex items-center">
        <input
          type="text"
          placeholder="Pesquisar..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="border border-gray-300 p-2 rounded-l w-10/12"
        />
        <button className="bg-gray-600 text-white p-3.5 rounded-r">
          <FaSearch />
        </button>
      </div>
      <button className="bg-gray-600 text-white px-3 py-1 rounded flex items-center">
        <FaBook className="mr-2" />
        Andamentos Processuais
      </button>
    </aside>
  );
};

export default Sidebar;
