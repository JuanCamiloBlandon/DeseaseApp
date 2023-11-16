import React from 'react';

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const getMessageFromApi = (userMessage) => {

    fetch('http://127.0.0.1:8000/', {
      method: 'POST',
      body: JSON.stringify({
        mensaje: userMessage,
      }),
      headers: {
         'Content-type': 'application/json; charset=UTF-8',
      },
      })
   .then(response => response.json())
   .then(data => { 
    console.log(data);
    const botMessage = createChatBotMessage(data
      );

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
   });
   
  };
  
  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: { getMessageFromApi},
        });
      })}
    </div>
  );
};

export default ActionProvider;