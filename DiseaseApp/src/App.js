import React from "react";
import Chatbot from "react-chatbot-kit";
import "react-chatbot-kit/build/main.css";
import "./App.css";
import ActionProvider from "./compenents/ActionProvider";
import MessageParser from "./compenents/MessageParser";
import config from "./config";
import logo from "./image/ChilVaccSinFondo.png";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <h1>Bienvenidos a DiseaseApp</h1>
          <div className="grid">
            <div className="imageLogo">
              <img src={logo} alt="logo" />
            </div>
            <div>
              <p>
                DiseaseApp es una aplicación web la cual implementa un agente inteligente que ayuda a las personas con posibles 
                enfermedades musculares a detectarlas a tiempo de acuerdo a los síntomas presentados y según el tipo de enfermedad 
                brinda al paciente una serie de recomendaciones para evitar que se siga desarrollando.
              </p>
            </div>
          </div>
        </div>
        <Chatbot
          config={config}
          actionProvider={ActionProvider}
          messageParser={MessageParser}
        />
      </header>
    </div>
  );
}

export default App;
