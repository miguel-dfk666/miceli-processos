import { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";

const CustomUserPage: React.FC = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirm_password: "",
  });

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>): void => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/custom-users/", formData);
      console.log(response.data);
    } catch (error) {
      console.error("Erro ao registrar:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded shadow-lg">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center">
          Cadastre-se na sua conta
        </h2>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username" className="block text-sm font-medium text-gray-600">
              Nome de Usuário
            </label>
            <input
              type="text"
              name="username"
              id="username"
              autoComplete="username"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.username}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-600">
              Endereço de Email
            </label>
            <input
              type="email"
              name="email"
              id="email"
              autoComplete="email"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.email}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-600">
              Senha
            </label>
            <input
              type="password"
              name="password"
              id="password"
              autoComplete="new-password"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.password}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="confirm_password" className="block text-sm font-medium text-gray-600">
              Confirme a Senha
            </label>
            <input
              type="password"
              name="confirm_password"
              id="confirm_password"
              autoComplete="new-password"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.confirm_password}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <button
              type="submit"
              className="w-full bg-gray-600 text-white p-2 rounded-md hover:bg-gray-700 focus:outline-none focus:ring focus:ring-indigo-200"
            >
              Registrar
            </button>
          </div>
        </form>
        <div className="text-center mt-4">
          <p className="text-sm text-gray-600 hover:text-gray-800 cursor-pointer">
            Já possui uma conta? <a href="/login">Faça login</a>.
          </p>
        </div>
      </div>
    </div>
  );
};

export default CustomUserPage;
