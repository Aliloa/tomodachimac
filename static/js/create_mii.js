"use strict;"

function toggleInput()
{
    const choice = document.getElementsByClassName('user_choice').value;
    const choiceInput = document.getElementsByClassName('choice-input');

    if (choice == 'yes')
    {
        choiceInput.style.display = 'block';
    }
    else
    {
        choiceInput.style.display = 'none';
    }
}