"use strict";
// document ready in ES6
Document.prototype.ready = callback => {
	if(callback && typeof callback === 'function') {
		document.addEventListener("DOMContentLoaded", () =>  {
			if(document.readyState === "interactive" || document.readyState === "complete") {
				return callback();
			}
		});
	}
};


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
