import React, { useState } from "react";
import axios from "axios";

interface LoginFormData {
  identifier: string;
  password: string;
}

const LoginPage: React.FC = () => {
  const [loginFormData, setLoginFormData] = useState<LoginFormData>({
    identifier: "",
    password: "",
  });

  const handleLoginInputChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, value } = event.target;
    setLoginFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleLoginSubmit = async (event: React.FormEvent): Promise<void> => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/login/", // Endpoint de login na sua API
        loginFormData
      );

      // Lógica de autenticação bem-sucedida
      console.log("Login bem-sucedido:", response.data);

      // Redirecionar ou executar outras ações após o login bem-sucedido
    } catch (error) {
      console.error("Erro ao fazer login:", error);
      // Lógica para tratar erros de login, se necessário
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Faça login na sua conta
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleLoginSubmit}>
          <div>
            <label htmlFor="identifier" className="block text-sm font-medium text-gray-600">
              Email ou Nome de Usuário
            </label>
            <input
              type="text"
              name="identifier"
              id="identifier"
              autoComplete="username"
              required
              className="mt-1 p-2 w-full border rounded-md"
              value={loginFormData.identifier}
              onChange={handleLoginInputChange}
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
              value={loginFormData.password}
              onChange={handleLoginInputChange}
            />
          </div>
          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
            >
              Entrar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
