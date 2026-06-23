"use strict";


async function calltrying() {
 const userschoice = document.getElementById('userschoice');
 const response = await fetch("/trying",
      { method: 'POST',
        headers: {'Accept': 'application/json, text/plain, */*',
                  'Content-Type': 'application/json'
          },
        body: JSON.stringify({'number':userschoice.value})
      });
  userschoice.value='';
  const data = await response.json();
  display(data);
}

function display(data) {
    const mylist = document.getElementById('answers');
    const text = document.createElement("p");
    text.innerHTML = data.message; 
    mylist.append(text);
};
