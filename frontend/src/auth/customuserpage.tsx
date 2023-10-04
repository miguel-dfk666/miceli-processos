import React, { useState } from "react";
import axios from "axios";
import LoginPage from "./login";

interface FormData {
  username: string;
  email: string;
  password: string;
  confirm_password?: string;
}

const CustomUserPage: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username: "",
    email: "",
    password: "",
    confirm_password: "", // Campo de confirmação de senha
  });

  const [isRegistering, setIsRegistering] = useState(true);

  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (event: React.FormEvent): Promise<void> => {
    event.preventDefault();
    try {
      // Verificar se o registro ou login está sendo realizado
      let apiUrl = "http://127.0.0.1:8000/api/custom-users/";

      if (!isRegistering) {
        // Se não estamos registrando, estamos fazendo login
        apiUrl = "http://127.0.0.1:8000/api/custom-users/";
      }

      const requestBody: FormData = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      };

      if (isRegistering && formData.confirm_password) {
        requestBody.confirm_password = formData.confirm_password;
      }

      const response = await axios.post(apiUrl, requestBody);

      if (isRegistering) {
        // Exibe um alerta para confirmar o registro e redireciona para a página de login na mesma página
        window.alert("Conta criada com sucesso!");

        // Redireciona o usuário para a seção de login na mesma página usando o fragmento de URL
        window.location.href = "#login-section"; // Use o ID da seção de login
      } else {
        // Redireciona ou executa outras ações após o login bem-sucedido
        // window.location.href = "sua_pagina_de_dashboard";
      }
    } catch (error) {
      console.error("Erro ao registrar/fazer login:", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            {isRegistering ? "Cadastre-se na sua conta" : "Faça login na sua conta"}
          </h2>
        </div>
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
          {isRegistering && ( // Somente exiba o campo de confirmação de senha ao registrar
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
          )}
          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
            >
              {isRegistering ? "Registrar" : "Entrar"}
            </button>
          </div>
        </form>
        <div className="text-center">
          <p
            className="cursor-pointer text-sm font-medium text-gray-600 hover:text-gray-800"
            onClick={() => setIsRegistering(!isRegistering)}
          >
            {isRegistering
              ? "Já possui uma conta? Faça login."
              : "Ainda não tem uma conta? Registre-se."}
          </p>
        </div>
      </div>
    </div>
  );
};

export default CustomUserPage;
