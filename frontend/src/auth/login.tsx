import { useState } from "react";
import axios from "axios";

interface FormData {
  username_or_email: string;
  password: string;
}

const LoginPage: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username_or_email: "",
    password: "",
  });

  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (
    event: React.FormEvent<HTMLFormElement>
  ): Promise<void> => {
    event.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/api/login/", formData);
      console.log(response.data);
    } catch (error) {
      // Tratar os erros da requisição
      console.error("Erro ao fazer login:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded shadow-lg">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center">Faça login na sua conta</h2>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username_or_email" className="block text-sm font-medium text-gray-600">
              Nome de Usuário ou Email
            </label>
            <input
              type="text"
              name="username_or_email"
              id="username_or_email"
              autoComplete="username"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.username_or_email}
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
              autoComplete="current-password"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={formData.password}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <button
              type="submit"
              className="w-full bg-gray-600 text-white p-2 rounded-md hover:bg-gray-700 focus:outline-none focus:ring focus:ring-indigo-200"
            >
              Entrar
            </button>
          </div>
        </form>
        <div className="text-center mt-4">
          <p className="text-sm text-gray-600 hover:text-gray-800 cursor-pointer">
            Ainda não tem uma conta? <a href="/signup">Registre-se</a>.
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
